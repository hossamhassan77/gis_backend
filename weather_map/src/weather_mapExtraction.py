from pydantic import BaseModel
import geopandas
import json
import random
from shapely.geometry import  Point
from typing import Optional

class weather_map(BaseModel):
    points_number : Optional[int]
    bound: Optional[list]
    lat: Optional[float]
    lng: Optional[float]

    def generate_polygon_from_listof_points(bound: list):
        """Receive a list of objects of polygon's points to convert it into a geographic polygon could be intersected for area of interest feature.
            >>> item.generate_polygon_from_listof_points(bound)
            return geopandas.GeoDataFrame
            """
        outer_coords = []
        for xy in bound :
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
        processed_area = geopandas.read_file(polygon2json)
        return (processed_area)
    
    def random_points_in_polygon(number, polygon):
        points = []
        min_x, min_y, max_x, max_y = polygon.bounds
        i = 0
        while i < number:
            point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            if polygon.contains(point):
                points.append(point)
                i += 1
        return (points)