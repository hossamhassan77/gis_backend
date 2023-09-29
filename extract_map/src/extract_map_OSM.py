try:
    import json
    # import string
    # import osmnx as ox
    # import random
    from fastapi import FastAPI
    from typing import Optional
    from pydantic import BaseModel
    # import os
    import geopandas as gpd
except ImportError:
    raise ("Couldn't import module")

app = FastAPI()

class Extract_map(BaseModel):
    file_format: str
    selected_properties: list
    bounds: Optional[dict]
    custom_area: Optional[list]
    email: str
    username: str

    def to_extension(dataFrame, file_name, file_format):

            if file_format.lower() == "geojson":
                dataFrame.to_file(rf"wakeb_mapdata/{file_name}.{file_format}", encoding='utf-8')
            
            elif file_format.lower() == "csv":
                dataFrame.to_csv(rf"wakeb_mapdata/{file_name}.{file_format}")

            elif file_format.lower() == "html":
                dataFrame.to_html(rf"wakeb_mapdata/{file_name}.{file_format}")

            elif file_format.lower() == "excel":
                dataFrame.to_excel(rf"wakeb_mapdata/{file_name}.xlsx")
            # else :
            #     return(json.dumps("Not supported format."))
            
    def areaOfInterestPath(path:list):
        """Input polygon path as a google objects to return polygon geoDataFrame.
        For example : areaOfInterestPath([{"lat":30.06095999755898,"lng":31.20790958404541},{"lat":30.059288551718552,"lng": 31.190614700317383},{"lat":30.04491295269813,"lng": 31.19353294372559}])
        """
        outer_coords = []
        for xy in path :
            inner_coordinates = []
            inner_coordinates.append(xy['lng'])
            inner_coordinates.append(xy['lat'])
            outer_coords.append(inner_coordinates)
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
        processed_area = gpd.read_file(polygon2json)
        return (processed_area)
