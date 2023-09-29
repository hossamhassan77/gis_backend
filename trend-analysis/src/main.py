"""
fastAPI and uvicorn for production,
TrendAnalysis is a class contains all constructor and utils functions that is required.
"""
from fastapi import FastAPI
import uvicorn
from trend import TrendAnalysis

app = FastAPI()
@app.get("/trend-analysis/dataType-validGrouping")
async def data_types(espg: int, file_path: str, long: str, lat : str, time: str):
    """Endpoint that insure what property should appears to user in trend analysis section."""
    trend = TrendAnalysis(espg, file_path,long, lat, time)
    return  {"dataTypes": trend.get_datatype(), "valid_grouping": trend.valid_group()}
@app.get("/trend-analysis/grouping-property-bydate")
async def grouping_property(espg: int, file_path: str, long: str, lat : str, time:str, grouping: str, property_column: str):
    """
    Returns json contains values on x axe and y axe to visualize as graph,
    and the average number of the numeric property column.
    """
    trend = TrendAnalysis(espg, file_path, long, lat, time)
    return trend.convert_grouped_df_to_list(grouping, property_column)
@app.get("/trend-analysis/time-range")
async def get_time_range(espg: int, file_path: str, long: str, lat : str, time:str, grouping: str, property_column: str, time_range: str, number_of_ranges: int):
    """
    Returns one or two of dicts depends on number of range(1, or 2) \
    as json contains values on x axe and y axe to visualize as graph.
    """
    trend = TrendAnalysis(espg, file_path, long, lat, time)
    return trend.create_time_range(grouping, property_column, time_range, number_of_ranges)
@app.get("/trend-analysis/local-trend")
async def local_trend(espg: int, file_path: str, long: str, lat : str, time: str, area: str):
    """
    Local trend is when you interested in specific area of your all data frame area. 
    """
    trend = TrendAnalysis(espg, file_path, long, lat, time)
    return trend.local_trend(area)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
