"""
OS and datetime for operations and time process,
Pandas for data manipulation,
Geopandas for geospatial capabilities.
"""
import os
from datetime import timedelta
import pandas
import geopandas

class TrendAnalysis():
    """
    class contains constructor __init__ that initialize espg code for\
    coordinates and dataset file path,\
    and group of functions that helps trend analysis.
    """
    def __init__(self, espg: int, file_path: str, long: str, lat: str, time: str) -> None:
        self.espg = espg
        self.file_path = file_path
        self.long = long
        self.lat = lat
        self.time = time

    def read_file(self) -> geopandas.GeoDataFrame:
        """Function takes file path, longitude, and latitude from class constructor function\
        then returns geopandas.GeoDataFrame
        """
        extension = os.path.splitext(self.file_path)[1]
        if extension == ".csv":
            data_frame = pandas.read_csv(self.file_path)
            geo_data_frame = geopandas.GeoDataFrame(data_frame,\
                            geometry=geopandas.points_from_xy(data_frame[self.long], data_frame[self.lat]),\
                            crs=self.espg).dropna(subset=[self.long, self.lat, self.time])
        else:
            geo_data_frame =  geopandas.read_file(self.file_path).dropna(subset=[self.long, self.lat, self.time])
        geo_data_frame[self.time] = pandas.to_datetime(geo_data_frame[self.time])
        geo_data_frame = geo_data_frame.sort_values(by=self.time)
        geo_data_frame = geo_data_frame.reset_index()
        return geo_data_frame
    def get_datatype(self) -> list:
        """Function returns each datatype for every column,
        and if the datatype is numeric, return min and max range,
        and if the datatype is objects, return all unique values too.
        >>> get_datatype(time_column, longitude_column, latitude_column)
        >>> returns [
                {"column": "Column or property_column name",
                "is_numeric": false,
                "values": [List of unique values]},
                {"column": "Column or property_column name",
                "is_numeric": true,
                "minimum": "1",
                "maximum": "9999"}
                    ]
        """
        geo_data_frame = self.read_file()
        values = []
        for i in (geo_data_frame.columns):
            uniques = []
            if geo_data_frame.dtypes[i] in ['float', 'int64', 'datetime64[ns]', 'geometry']:
                if i in (self.long, self.lat, self.time, 'geometry'):
                    continue
                maximum = str(geo_data_frame[i].max())
                minimum = str(geo_data_frame[i].min())
                column_report = ({
                                "column": i,
                                "is_numeric": True,
                                "minimum": minimum,
                                "maximum": maximum
                                })
                values.append(column_report)
            else:
                for unique_values in geo_data_frame[i].unique():
                    uniques.append(unique_values)
                    column_report =  {"column": i, "is_numeric": False, "values": uniques}
                values.append(column_report)
        return values
    def valid_group(self) -> dict:
        """
        Function check what is the valid time group for any time series dataset,\
        to improve user experience to not choose a not valid time grouping.
        """
        geo_data_frame = self.read_file()
        time_delta = geo_data_frame[self.time][len(geo_data_frame)-1] - geo_data_frame[self.time][0]
        valid_grouping = ["none"]
        if time_delta.seconds > 0:
            valid_grouping.extend(("hour", "minute"))
        if time_delta.days > 0 :
            valid_grouping.extend(("year", "month", "day"))
        return {'grouping_options': valid_grouping}
    def create_grouping(self, grouping: str, property_column: str) -> dict:
        """
        Takes grouping time and the numeric column as property column,\
        then return grouped DF with just 3 column [index, timestamp, selected property]
        """
        geo_data_frame = self.read_file()
        group = {'minute': 'T', 'hour': 'H', 'day':'D', 'week': 'W', 'month': 'M', 'year': 'Y'}
        if grouping == "none":
            keep_important_gdf_column = geo_data_frame[[self.time, property_column]]
        else:
            keep_important_gdf_column = geo_data_frame[[self.time, property_column]]
            geo_data_frame = keep_important_gdf_column.groupby(pandas.Grouper(key=self.time, freq=group[grouping])).mean()
        geo_data_frame = geo_data_frame.reset_index().dropna(subset=[property_column])
        return keep_important_gdf_column, geo_data_frame
    def convert_grouped_df_to_list(self, grouping: str, property_column: str):
        """
        Converting the DataFrame that comes from create_grouping function to JSON format.
        """
        graph_values = {}
        geo_data_frame = self.create_grouping(grouping, property_column)[1]
        x_axe = geo_data_frame[self.time].to_list()
        graph_values['x_axe']= [str(time_obj) for time_obj in x_axe]
        y_axe = geo_data_frame[property_column].to_list()
        graph_values['y_axe']= [round(num, 2) for num in y_axe]
        return graph_values, {"Avg":round(geo_data_frame[property_column].mean(), 2)}
    def create_time_range(self, grouping: str, property_column: str, time_range: str, number_of_ranges: int):
        """
        Function takes grouping time, numeric property column, time range, and number of ranges (1, or 2)
        and returns json for the last time range and the before the last time. 
        """
        time_range_group = {'minute': 'minutes', 'hour': 'hours', 'day':'days', 'week': 'weeks'}
        geo_data_frame = self.create_grouping(grouping, property_column)[0]
        max_timestamp = geo_data_frame[self.time].max()
        one_time_range = max_timestamp - timedelta(**{time_range_group[time_range]: 1})
        last_time_range = geo_data_frame[(geo_data_frame[self.time] >= one_time_range) &\
                                            (geo_data_frame[self.time] <= max_timestamp)]
        if number_of_ranges == 1:
            return {"last": {
                            "x_axe":[str(time_obj) for time_obj in last_time_range[self.time].to_list()],
                            "y_axe": last_time_range[property_column].to_list()
                            }}
        else:
            start_time_last_hour = max_timestamp - timedelta(**{time_range_group[time_range]: 2})
            last_hour_data = geo_data_frame[(geo_data_frame[self.time] >= start_time_last_hour) &\
                                            (geo_data_frame[self.time] <= max_timestamp)]
            first_timestamp = last_hour_data[self.time].min()
            end_time_first_hour = first_timestamp + timedelta(hours=1)
            first_hour_data = geo_data_frame[(geo_data_frame[self.time] >= first_timestamp) &\
                                              (geo_data_frame[self.time] <= end_time_first_hour)]
            return {
                "last": {
                        "x_axe":[str(time_obj) for time_obj in last_time_range[self.time].to_list()],
                        "y_axe": last_time_range[property_column].to_list()
                        },
                "before":
                        {
                        "x_axe":[str(time_obj) for time_obj in first_hour_data[self.time].to_list()],
                        "y_axe": first_hour_data[property_column].to_list()
                        }
                    }
    def local_trend(self, area: str):
        data_frame = self.read_file()
        area_of_interest = geopandas.read_file(area)
        overlayed = data_frame.overlay(area_of_interest, how= 'intersection', keep_geom_type=False)
        return overlayed.to_json()
