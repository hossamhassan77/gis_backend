"""
os to use operating system-dependent functionality
Pandas for data manipulation and analysis,
Geopandas to handle spatial data.
! pip install pandas geopandas
"""
import os
import json
from typing import Optional

import pandas
import geopandas

class SplitView:
    """
    Class have constructors, like: espg(used coords if it global or local coord), latitude and  longitude
    and all utils functions that is important to complete all features in split view section.
    """
    def __init__(self, espg: int, long: str, lat: str) -> None:
        self.espg = espg
        self.long = long
        self.lat = lat
    def read_file_without_map_bound(self, file_path: str) -> geopandas.GeoDataFrame:
        """Function takes file path, longitude, and latitude from class constructor function\
        then returns geopandas.GeoDataFrame
        """
        extension = os.path.splitext(file_path)[1]
        if extension == ".csv":
            data_frame = pandas.read_csv(file_path)
            geo_data_frame = geopandas.GeoDataFrame(data_frame,\
                            geometry=geopandas.points_from_xy(data_frame[self.long], data_frame[self.lat]),\
                            crs=self.espg).dropna(subset=[self.long, self.lat])
        else:
            geo_data_frame =  geopandas.read_file(file_path).dropna(subset=[self.long, self.lat])
        return geo_data_frame
    def read_file(self, file_path: str, map_bound: dict) -> geopandas.GeoDataFrame:
        """Function takes file path, longitude, and latitude from class constructor function\
        and map bound to intersect the map view with the dataset,\
        then returns intersected  geopandas.GeoDataFrame
        """
        extension = os.path.splitext(file_path)[1]
        if extension == ".csv":
            data_frame = pandas.read_csv(file_path)
            geo_data_frame = geopandas.GeoDataFrame(data_frame,\
                            geometry=geopandas.points_from_xy(data_frame[self.long], data_frame[self.lat]),\
                            crs=self.espg).dropna(subset=[self.long, self.lat])
        else:
            geo_data_frame =  geopandas.read_file(file_path).dropna(subset=[self.long, self.lat])
        map_view = self.map_bound_to_polygon(map_bound)
        geo_data_frame = geo_data_frame.overlay(map_view, how='intersection', keep_geom_type=False)
        return geo_data_frame
    def get_datatype(self, file_path: str, time: Optional[str] = None) -> list:
        """
        Function returns each datatype for every column,
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
        geo_data_frame = self.read_file_without_map_bound(file_path)
        values = []
        if time:
            geo_data_frame[time] = pandas.to_datetime(geo_data_frame[time])
        for i in (geo_data_frame.columns):
            uniques = []
            if geo_data_frame.dtypes[i] in ['float', 'int64', 'datetime64[ns]', 'geometry']:
                if i in (self.long, self.lat, time, 'geometry'):
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
    def map_bound_to_polygon(self, bound: dict) -> geopandas.GeoDataFrame:
        """
        The bound box of map view, Needs bounds dict, returns polygon that will be overlayed with the GeoDataFrame.
        >>> boundsBox({"south": 39.331, "west": -105.170, "north": 40.386, "east": -102.91})`
        """
        lat_lng = []
        coords = []
        bounds = bound
        lat_lng.append(bounds['west'])
        lat_lng.append(bounds['north'])
        coords.append(lat_lng)
        lat_lng = []
        lat_lng.append(bounds['east'])
        lat_lng.append(bounds['north'])
        coords.append(lat_lng)
        lat_lng = []
        lat_lng.append(bounds['east'])
        lat_lng.append(bounds['south'])
        coords.append(lat_lng)
        lat_lng = []
        lat_lng.append(bounds['west'])
        lat_lng.append(bounds['south'])
        coords.append(lat_lng)
        coords.append(lat_lng)
        json_polygon = {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [coords]}}]}
        json_string = json.dumps(json_polygon)
        gdf_polygon= geopandas.read_file(json_string)
        return gdf_polygon
    def filter_data_frame(self, file_path: str, map_bound: dict, filter_query: list, filter_option: str) -> geopandas.GeoDataFrame:
        """
        Filter a GeoDataFrame based on specified filter conditions.
        """
        data_frame = self.read_file(file_path, map_bound)
        if filter_option == "clear_all":
            return data_frame
        for i in filter_query:
            if data_frame.dtypes[i['column']] in ('float64', 'int64'):
                query = (data_frame[i['column']] >= i['value'][0]) & (data_frame[i['column']] <= i['value'][1])
                if filter_option == 'include':
                    data_frame = data_frame[query]
                else:
                    data_frame = data_frame[~query]
            elif data_frame.dtypes[i['column']] in ('geometry', 'datetime64[ns]'):
                continue
            else:
                query = data_frame[i['column']] == i['value']
                if filter_option == 'include':
                    data_frame = data_frame[query]
                else:
                    data_frame = data_frame[~query]
        return data_frame
    def get_data_distribution(self, file_path: str, map_bound: dict, time: Optional[dict] = None) -> dict:
        """
        Generate data distribution information and charts.

        This method reads data from a specified file path, processes it, and generates distribution
        information and charts for each column. It provides insights into the distribution of data values
        within each column, including frequency counts for categorical data.
        """
        original_data = self.read_file(file_path, map_bound)
        if time:
            original_data[time] = pandas.to_datetime(original_data[time])
        distribution = {"distribution":{"filtered_column":{"original":{}}},"charts": []}
        distribution["distribution"]['filtered_column']['original'] = len(original_data)
        for original_data_columns in original_data.columns:
            chart = {}
            if original_data_columns in (self.long, self.lat, time, "geometry"):
                pass
            else:
                chart['title'] = original_data_columns
                if original_data[original_data_columns].dtypes == "object":
                    chart['horizontal'] = True
                else :
                    chart['horizontal'] = False
                original_data[original_data_columns] = original_data[original_data_columns].astype(str)
                unique_values = original_data[original_data_columns].unique()
                values = []
                for value in unique_values :
                    values.append(value)
                    chart['original'] = {"x_axe": values}
                chart['original']['y_axe'] =  original_data[original_data_columns].value_counts().to_list()
                distribution['charts'].append(chart)
        return json.dumps(distribution)
    def split_view_distribution(self, file_path: Optional[str] = None, map_bound_one: Optional[dict] = None, map_bound_two: Optional[dict] = None, time: Optional[dict] = None) -> dict:
        """
        Generate data distribution comparison between original and splitted views.

        This method reads data from a specified file path and creates two views of the data based on provided
        map bounds. It then compares the distribution of data between the original view and the second view,
        which is obtained by overlaying the second map bound on the data. The comparison includes distribution
        information and charts for each column
        """
        original_data = self.read_file(file_path,map_bound_one)
        second_view   = self.read_file_without_map_bound(file_path)
        if time:
            original_data[time] = pandas.to_datetime(original_data[time])
            second_view[time]   = pandas.to_datetime(second_view[time])
        second_map_view = self.map_bound_to_polygon(map_bound_two)
        splitted_data = second_view.overlay(second_map_view, how='intersection', keep_geom_type=False)
        distribution = {"distribution":{"difference": {"diff": {}, "diff_percentage":{}}, "filtered_column":{"original":{}, "splitted":{}}}, "charts":[]}
        distribution["distribution"]['filtered_column']['original'] = len(original_data)
        distribution["distribution"]['filtered_column']['splitted'] = len(splitted_data)
        distribution["distribution"]['difference']['diff'] = len(splitted_data) - len(original_data)
        distribution["distribution"]['difference']['diff_percentage'] = round(((len(splitted_data) - len(original_data)) / abs(len(original_data)))*100)
        for (original_data_columns, splitted_data_columns) in  zip(original_data.columns,  splitted_data.columns):
            chart = {}
            if original_data_columns in (self.long, self.lat, time, "geometry"):
                pass
            else:
                chart['title'] = original_data_columns
                if original_data[original_data_columns].dtypes == "object":
                    chart['horizontal'] = True
                else :
                    chart['horizontal'] = False
                original_data[original_data_columns] = original_data[original_data_columns].astype(str)
                unique_values = original_data[original_data_columns].unique()
                values = []
                for value in unique_values :
                    values.append(value)
                    chart['original'] = {"x_axe": values}
                chart['original']['y_axe'] =  original_data[original_data_columns].value_counts().to_list()

            if splitted_data_columns in (self.long, self.lat, time, "geometry"):
                pass
            else:
                chart['title'] = splitted_data_columns
                if splitted_data[splitted_data_columns].dtypes == "object":
                    chart['horizontal'] = True
                else :
                    chart['horizontal'] = False
                splitted_data[splitted_data_columns] = splitted_data[splitted_data_columns].astype(str)
                unique_values = splitted_data[splitted_data_columns].unique()
                values = []
                for value in unique_values :
                    values.append(value)
                    chart['splitted'] = {"x_axe": values}
                chart['splitted']['y_axe'] =  splitted_data[original_data_columns].value_counts().to_list()
                distribution['charts'].append(chart)
        return json.dumps(distribution)
