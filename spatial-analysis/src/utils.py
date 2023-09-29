"""
os to use operating system-dependent functionality
pandas for data manipulation and analysis,
geopandas to handle spatial data,
upload GeoDataFrame into PostGIS database.
"""
import os
import json
from typing import Optional
import pandas
import geopandas
from sqlalchemy import create_engine
from pyproj import CRS
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info

class SpatialAnalysis:
    """A class contains all utils functions for spatial analysis."""
    def __init__(self, long: str, lat: str) -> None:
        self.long = long
        self.lat = lat
        self.engine = create_engine('postgresql://postgres:123456@localhost/hosam_db')
    def convert_to_df(self, file_path: str) -> geopandas.GeoDataFrame:
        """
        Function takes file path(csv, GeoJSON, shapefile(zip)), longitude, and latitude from class\
        constructor function then returns geopandas.GeoDataFrame
        """
        extension = os.path.splitext(file_path)[1]
        if extension == ".csv":
            data_frame = pandas.read_csv(file_path)
            geo_data_frame = geopandas.GeoDataFrame(data_frame,\
                            geometry=geopandas.points_from_xy(data_frame[self.long],\
                                        data_frame[self.lat])).dropna(subset=[self.long, self.lat])
            utm_crs_list = query_utm_crs_info(
                datum_name="WGS 84",
                area_of_interest=AreaOfInterest(
                    west_lon_degree = data_frame[self.long].min(),
                    south_lat_degree = data_frame[self.lat].min(),
                    east_lon_degree = data_frame[self.long].max(),
                    north_lat_degree = data_frame[self.lat].max()))
            utm_crs = CRS.from_epsg(utm_crs_list[0].code)
            if geo_data_frame.crs is None:
                geo_data_frame = geo_data_frame.set_crs(utm_crs)
            geo_data_frame = geo_data_frame.to_crs(utm_crs)
        else:
            geo_data_frame =  geopandas.read_file(file_path)
        return geo_data_frame
    def buffer_df(self, file_path, buffer_size):
        """Calculate a buffer around a geographical point."""
        geo_data_frame = self.convert_to_df(file_path)
        projected_geo_data_frame = geo_data_frame.to_crs(epsg=6933)
        projected_geo_data_frame['buffer'] = projected_geo_data_frame["geometry"].buffer(buffer_size)
        projected_geo_data_frame = projected_geo_data_frame.set_geometry('buffer').drop("geometry", axis=1)
        geo_data_frame = projected_geo_data_frame.to_crs('wgs84')
        return geo_data_frame
    def centroid_df(self, file_path):
        """Calculate the centroid of spatial data."""
        geo_data_frame = self.convert_to_df(file_path)
        projected_geo_data_frame = geo_data_frame.to_crs(epsg=6933)
        projected_geo_data_frame['centroid'] = projected_geo_data_frame.centroid
        projected_geo_data_frame = projected_geo_data_frame.set_geometry("centroid").drop('geometry', axis=1)
        geo_data_frame = projected_geo_data_frame.to_crs('wgs84')
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
        geo_data_frame = self.convert_to_df(file_path)
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
    def area_of_interest(self, path:list):
        """Receive a list of objects of polygon's points to convert it into a geographic polygon could be intersected for area of interest feature.
        >>> area_of_interest(AreaOfInterestPath)
        return geopandas.GeoDataFrame
        """
        outer_coords = []
        for coord_dict in path :
            inner_coords = []
            inner_coords.append(coord_dict['lng'])
            inner_coords.append(coord_dict['lat'])
            outer_coords.append(inner_coords)
        polygon = {
                "type": "FeatureCollection",
                "features": [
                    {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [outer_coords]   
                                }
                        }
                            ]
                }
        polygon2json = json.dumps(polygon)
        processed_area = geopandas.read_file(polygon2json)
        return (processed_area)
    def detect_crs(self, file_path: str):
        """Detect what is the coordinate reference system from one (lat, lng) point."""
        geo_data_frame = self.convert_to_df(file_path)
        utm_crs_list = query_utm_crs_info(
        datum_name="WGS 84",
        area_of_interest=AreaOfInterest(
            west_lon_degree = geo_data_frame[self.long].min(),
            south_lat_degree = geo_data_frame[self.lat].min(),
            east_lon_degree = geo_data_frame[self.long].max(),
            north_lat_degree = geo_data_frame[self.lat].max()
            )
        )
        utm_crs = CRS.from_epsg(utm_crs_list[0].code)
        return str(utm_crs)
    def data_frame_description(self, file_path)-> pandas.DataFrame:
        """Generate a descriptive summary of a GeoDataFrame after converting it from a given file.
        
        Parameters:
        file_path (str): The file path to the data file (e.g., shapefile, GeoJSON, csv)."""
        geo_data_frame = self.convert_to_df(file_path)
        for coords in geo_data_frame.columns:
            if coords in (self.lat, self.long):
                geo_data_frame = geo_data_frame.drop([coords], axis=1)
        return geo_data_frame.describe()
    def aggregate_columns(self, file_path, describe_options: list[str], columns: Optional[list[str]] = None)-> pandas.DataFrame:
        """Aggregate and summarize specified columns of a GeoDataFrame from a given file.
        
        Parameters:
        file_path (str): The file path to the data file (e.g., shapefile, GeoJSON, csv).
        describe_options (list): A list of aggregation functions to apply to the specified columns.
        columns (list, optional): A list of column names in the GeoDataFrame to be summarized.\
                                  If None, all columns are considered.
        """
        geo_data_frame = self.convert_to_df(file_path)
        columns_dictionary = {}
        for column in columns:
            columns_dictionary[column] = describe_options
        return geo_data_frame.agg(columns_dictionary)
    def spatial_join(self, file_path_one, file_path_two, join_direction) -> geopandas.GeoDataFrame:
        """
        Perform a spatial join operation between two geographical datasets.

        Parameters:
        - file_path_one (str): The file path to the first geographical dataset.
        - file_path_two (str): The file path to the second geographical dataset.
        - join_direction (str): The type of spatial join to perform. It can be one of the following values:
            - 'inner': Keep only the intersecting geometries.
            - 'left': Keep all geometries from the first dataset and add attributes from the second dataset where they intersect.
            - 'right': Keep all geometries from the second dataset and add attributes from the first dataset where they intersect.
            - 'outer': Keep all geometries from both datasets and add attributes where they intersect.
        """
        geo_data_frame_one = self.convert_to_df(file_path_one)
        geo_data_frame_one = geo_data_frame_one.to_crs('wgs84')
        geo_data_frame_two = self.convert_to_df(file_path_two)
        geo_data_frame_two = geo_data_frame_two.to_crs('wgs84')
        joined_data_frames = geo_data_frame_one.sjoin(geo_data_frame_two, how=join_direction)
        return (joined_data_frames)
analysis = SpatialAnalysis('long_x_dd', 'lat_y_dd')
# print(analysis.convert_to_df(r'D:\Github\GIS\wakeb_mapdata\Raptor_Nests.zip'))
# print(analysis.buffer_df(r'D:\Github\GIS\wakeb_mapdata\raptor_nest.csv',200))
# print(analysis.centroid_df(r'D:\Github\GIS\wakeb_mapdata\raptor_nest.csv'))
# print(analysis.get_datatype(r'D:\Github\GIS\wakeb_mapdata\raptor_nest.csv', 'lastsurvey'))
# print(analysis.area_of_interest([{"lat":0.38427119123016,"lng":-5.18831674093013},{"lat":10.35078901802308,"lng":-4.38631478780513},{"lat":19.84234491122627,"lng":-4.50167123311763}]))
# print(analysis.detect_crs(r'D:\Github\GIS\wakeb_mapdata\SCHUYLKILL.csv'))
# print(analysis.data_frame_description(r'D:\Github\GIS\wakeb_mapdata\raptor_nest.csv'))
# print(analysis.aggregate_columns(r"D:\Github\GIS\wakeb_mapdata\SCHUYLKILL.csv", ['sum', 'min', 'mean', 'max'], ['SOG', 'COG']))
print(analysis.spatial_join(r'D:\Github\GIS\wakeb_mapdata\raptor_nest.csv', r'D:\Github\GIS\wakeb_mapdata\counties.geojson', 'inner'))
