"""
uvicorn for running applications,
json for working and converting JSON data in Python,
FastAPI framework for building web APIs,
SpatialAnalysis module contains utility functions and classes for spatial analysis.
"""
import json
from typing import Union, Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from utils import SpatialAnalysis

app = FastAPI()
@app.get("/spatial-analysis/read-file")
async def read_file(long, lat, file_path):
    """Dataset intersection with map bound to visualize in spilt view section."""
    analysis = SpatialAnalysis(long, lat)
    geo_data_frame = analysis.convert_to_df(file_path)
    return json.loads(geo_data_frame.to_json())
@app.get("/spatial-analysis/save-to-db")
async def save_to_db(long, lat, file_path, table_name):
    """
    Save spatial data to a database table.

    This asynchronous function takes geographic coordinates (longitude and latitude),
    an EPSG code, a file path to spatial data, and a table name as input. It converts
    the spatial data to a DataFrame and saves it to the specified database table.

    Parameters:
    - espg (str): The EPSG code specifying the coordinate system.
    - long (float): The longitude of the location.
    - lat (float): The latitude of the location.
    - file_path (str): The path to the spatial data file.
    - table_name (str): The name of the database table to save the data to.

    Returns:
    - JSON: A JSON representation of the saved spatial data in the DataFrame.
    """
    analysis = SpatialAnalysis(long, lat)
    geo_data_frame = analysis.convert_to_df(file_path)
    geo_data_frame.to_postgis(table_name, analysis.engine, index=True, index_label="Index", if_exists="replace")
    return json.loads(geo_data_frame.to_json())

@app.get('/spatial-analysis/buffer')
async def buffer(long, lat, file_path: str, buffer_size: Union[int, float]):
    """
    Calculate a buffer around a geographical point.
    
    Parameters:
    - espg (str): The EPSG code specifying the coordinate system.
    - long (float): The longitude of the location.
    - lat (float): The latitude of the location.
    - file_path (str): The path to the spatial data file.
    - buffer_size (Union[int, float]): The size of the buffer zone in the same units as
      the spatial data file's coordinate system. It can be an integer or a floating-point number.

    Returns:
    - JSON: A JSON object containing the buffered geometries.
    """
    analysis = SpatialAnalysis(long, lat)
    geo_data_frame = analysis.buffer_df(file_path, buffer_size)
    return json.loads(geo_data_frame.to_json())

@app.get("/spatial-analysis/centroid")
async def centroid(long, lat, file_path: str):
    """
    Calculate the centroid of spatial data.
    
    Parameters:
    - espg (str): The EPSG code specifying the coordinate system.
    - long (float): The longitude of the location.
    - lat (float): The latitude of the location.
    - file_path (str): The path to the spatial data file.

    Returns:
    - JSON: A JSON object containing the centroid coordinates."""
    analysis = SpatialAnalysis(long, lat)
    centroid_data_frame = analysis.centroid_df(file_path)
    return json.loads(centroid_data_frame.to_json())

@app.get("/spatial-analysis/data-type")
async def data_types(file_path: str, long: str, lat: str, time_column: Optional[str]=None):
    """Endpoint that returns unique values for object dtypes and (min,max) for numeric dtypes."""
    analysis = SpatialAnalysis(long, lat)
    return {"dataTypes": analysis.get_datatype(file_path, time_column)}

@app.get("/spatial-analysis/overlay")
async def make_overlay(file_path: str, long: str, lat: str, overlay_method:str, file_path_two: Optional[str]=None, aoi_path: Optional[list]=None):
    """
    Perform spatial overlay between GeoDataFrames,\
    Implements several methods that are all effectively subsets of the union.
    operation ('intersection', 'union', 'identity', 'symmetric_difference' or 'difference')
    """
    analysis = SpatialAnalysis(long, lat)
    geo_data_frame = analysis.convert_to_df(file_path)
    if file_path_two:
        second_geo_data_frame = analysis.convert_to_df(file_path)
    else:
        second_geo_data_frame = analysis.area_of_interest(aoi_path)
    overlay_result = geo_data_frame.overlay(second_geo_data_frame, how= overlay_method, keep_geom_type=False)
    return json.loads(overlay_result.to_json())

@app.get("/spatial-analysis/shape-length")
async def calculate_shape_length(long: str, lat: str, file_path: str):
    """Calculate the shape length of geometries in a spatial data file."""
    analysis = SpatialAnalysis(long, lat)
    geo_data_frame = analysis.convert_to_df(file_path)
    projected_geo_data_frame = geo_data_frame.to_crs('EPSG:32636')
    projected_geo_data_frame['shape_length'] = projected_geo_data_frame['geometry'].length
    geo_data_frame = projected_geo_data_frame.to_crs('wgs84')
    return json.loads(geo_data_frame.to_json())

@app.get("/spatial-analysis/shape-area")
async def calculate_shape_are(long: str, lat: str, file_path: str):
    """Calculate the shape area of geometries in a spatial data file."""
    analysis = SpatialAnalysis(long, lat)
    geo_data_frame = analysis.convert_to_df(file_path)
    projected_geo_data_frame = geo_data_frame.to_crs(epsg=6933)
    projected_geo_data_frame['shape_area'] = projected_geo_data_frame["geometry"].area
    geo_data_frame = projected_geo_data_frame.to_crs('wgs84')
    return json.loads(geo_data_frame.to_json())
@app.get("/spatial-analysis/detect-crs")
async def detect_crs(long, lat, file_path):
    """Detect what is the coordinate reference system from one (lat, lng) point."""
    analysis = SpatialAnalysis(long, lat)
    espg_code = analysis.detect_crs(file_path)
    return espg_code
@app.get("/spatial-analysis/data-frame-description")
async def df_description(long, lat, file_path):
    """Generate a descriptive summary of a GeoDataFrame after converting it from a given file."""
    analysis = SpatialAnalysis(long, lat)
    describe = analysis.data_frame_description(file_path)
    return json.loads(describe.to_json())
class Aggregate(BaseModel):
    long: str
    lat: str
    file_path: str
    describe_options: list[str]
    columns: Optional[list[str]]
@app.post("/spatial-analysis/aggregate-columns")
async def aggregate_columns(request: Aggregate):
    """Aggregate and summarize specified columns of a GeoDataFrame from a given file."""
    analysis = SpatialAnalysis(request.long, request.lat)
    aggregate = analysis.aggregate_columns(request.file_path, request.describe_options, request.columns)
    return json.loads(aggregate.to_json())
@app.get("/spatial-analysis/spatial-join")
async def spatial_join(long, lat, file_path_one, file_path_two, join_direction):
    """Perform a spatial join operation between two geographical datasets."""
    analysis = SpatialAnalysis(long, lat)
    spatial_join_df = analysis.spatial_join(file_path_one, file_path_two, join_direction)
    return json.loads(spatial_join_df.to_json())
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
