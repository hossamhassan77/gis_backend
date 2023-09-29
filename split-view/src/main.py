"""
FastAPI is a modern web framework for building APIs 
BaseModel is used to define data models with validation and serialization capabilities.
SplitView is a class defined in a module named "split.py".
"""
from typing import Optional
import json
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from split import SplitView

app = FastAPI()

@app.get("/split-view/data-type")
def data_types(espg: int, file_path: str, long: str, lat: str, time_column: Optional[str]= None) -> dict:
    """Endpoint that returns unique values for object dtypes and (min,max) for numeric dtypes."""
    split = SplitView(espg, long, lat)
    return {"dataTypes": split.get_datatype(file_path, time_column)}

class OriginalViewParams(BaseModel):
    """
    Represents parameters for just visualizing original dataset in any map bound .
    ### Attributes:
        espg (int): The EPSG code for the coordinate system.
        long (str): The column name for longitude data.
        lat (str): The column name for latitude data.
        file_path (str): The path to the input data file.
        map_bound (dict): Dictionary representing the map bounds.
    """
    espg: int
    long: str
    lat: str
    file_path: str
    map_bound: dict
@app.post("/split-view/original-data")
async def original_data_vis(request: OriginalViewParams):
    """Dataset intersection woth map bound to visualize in spilt view section """
    split = SplitView(request.espg, request.long, request.lat)
    geo_data_frame = split.read_file(request.file_path, request.bound)
    return json.loads(geo_data_frame.to_json())

class FilterOriginalData(BaseModel):
    """
    Represents parameters for filtering data for visualization.
    ### Attributes:
        espg (int): The EPSG code for the coordinate system.
        long (str): The column name for longitude data.
        lat (str): The column name for latitude data.
        file_path (str): The path to the input data file.
        filter_query (Optional[list]): Optional list of dictionaries specifying filter conditions for the splitted view.
        filter_option (str): Filter option for the original view, either "include" or "exclude" or "clear_all".
    """
    espg: int
    long: str
    lat: str
    file_path: str
    map_bound: dict
    filter_query: Optional[list]
    filter_option: str
@app.post("/split-view/filter-original-data")
async def filter_original_data(request: FilterOriginalData):
    """Filters data for visualization"""
    split = SplitView(request.espg, request.long, request.lat)
    filtered_data = split.filter_data_frame(request.file_path, request.map_bound, request.filter_query, request.filter_option)
    return json.loads(filtered_data.to_json())

class OriginalDataDistribution(BaseModel):
    """
    Represents parameters for data distribution.
    ### Attributes:
        espg (int): The EPSG code for the coordinate system.
        long (str): The column name for longitude data.
        lat (str): The column name for latitude data.
        file_path (str): The path to the input data file.
        map_bound (dict): Dictionary representing the map bounds.
        time_column (Optional[str]): Optional column name for time-related data.
        """
    espg: int
    long: str
    lat: str
    file_path: str
    map_bound: dict
    time_column: Optional[str]
@app.post("/split-view/original-data-distribution")
async def get_original_distribution(request: OriginalDataDistribution):
    """Generate data distribution information and charts."""
    split = SplitView(request.espg, request.long, request.lat)
    original_distribution = split.get_data_distribution(request.file_path, request.map_bound, request.time_column)
    return json.loads(original_distribution)

class SplitViewVisualization(BaseModel):
    """
    Represents parameters for visualizing splitted data.

    ### Attributes:
        espg (int): The EPSG code for the coordinate system.
        long (str): The column name for longitude data.
        lat (str): The column name for latitude data.
        file_path (str): The path to the input data file.
        original_map_bound (dict): Dictionary representing the original map bounds.
        splitted_map_bound (dict): Dictionary representing the splitted map bounds.
    """
    espg: int
    long: str
    lat: str
    file_path: str
    original_map_bound: dict
    splitted_map_bound: dict
@app.post("/split-view/split-view-visualization")
async def visualize_splitted_data(request: SplitViewVisualization):
    """Returns original data and splitted data in json format to be visualize in spilt view section."""
    split = SplitView(request.espg, request.long, request.lat)
    original_data_frame = split.read_file(request.file_path, request.original_map_bound)
    splitted_data_frame = split.read_file(request.file_path, request.splitted_map_bound)
    return {"Original_data": json.loads(original_data_frame.to_json()),
            "Splitted_data": json.loads(splitted_data_frame.to_json())
            }

class FilterOriginalSplit(BaseModel):
    """
    Represents parameters for filtering and splitting data distributions.

    ### Attributes:
        espg (int): The EPSG code for the coordinate system.
        long (str): The column name for longitude data.
        lat (str): The column name for latitude data.
        file_path (str): The path to the input data file.
        original_map_bound (dict): Dictionary representing the original map bounds.
        splitted_map_bound (dict): Dictionary representing the splitted map bounds.
        original_filter_query (Optional[list]): Optional list of dictionaries specifying filter conditions for the original view.
        splitted_filter_query (Optional[list]): Optional list of dictionaries specifying filter conditions for the splitted view.
        original_filter_option (str): Filter option for the original view, either "include" or "exclude" or "clear_all".
        splitted_filter_option (str): Filter option for the splitted view, either "include" or "exclude" or "clear_all".
    """
    espg: int
    long: str
    lat: str
    file_path: str
    original_map_bound: dict
    splitted_map_bound: dict
    original_filter_query: Optional[list]
    splitted_filter_query: Optional[list]
    original_filter_option: str
    splitted_filter_option: str
@app.post("/split-view/split-view-filter")
async def filter_split(request: FilterOriginalSplit):
    """
    Filtering and splitting data distributions
    """
    split = SplitView(request.espg, request.long, request.lat)
    original_filtered_data = split.filter_data_frame(request.file_path, request.original_map_bound, request.original_filter_query, request.original_filter_option)
    splitted_filtered_data = split.filter_data_frame(request.file_path, request.splitted_map_bound, request.splitted_filter_query, request.splitted_filter_option)
    return {
        "Original": json.loads(original_filtered_data.to_json()),
        "Splitted": json.loads(splitted_filtered_data.to_json())
    }

class SplitDataDistribution(BaseModel):
    """
        Represents parameters for splitting and comparing data distribution.

      ### Attributes:
        espg (int): The EPSG code for the coordinate system.
        long (str): The column name for longitude data.
        lat (str): The column name for latitude data.
        file_path (str): The path to the input data file.
        original_map_bound (dict): Dictionary representing the original map bounds.
        splitted_map_bound (dict): Dictionary representing the splitted map bounds.
        time_column (Optional[str]): Optional column name for time-related data.
    """
    espg: int
    long: str
    lat: str
    file_path: str
    original_map_bound: dict
    splitted_map_bound: dict
    time_column: Optional[str]
@app.post("/split-view/split-view-distribution")
async def distribute_splitted_data(request: SplitDataDistribution):
    """
    Generate data distribution comparison between original and splitted views as json formate.
    """
    split = SplitView(request.espg, request.long, request.lat)
    original_splitted_data = split.split_view_distribution(request.file_path, request.original_map_bound, request.splitted_map_bound, request.time_column)
    return json.loads(original_splitted_data)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
