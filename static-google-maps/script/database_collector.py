import time
import math
import json
import geopandas
import random
from shapely.geometry import Point
import requests
import os
import string
class StaticMaps:
    def __init__(self, map_bound, img_num, altitude):
        self.map_bound = map_bound
        self.img_num = img_num
        self.altitude = altitude
    
    def calculate_zoom_level(self):
        """
            Return Google Maps zoom level from altitude in meter.
            >>> generate_polygon_from_listOf_points()
            return int
        """
        pixel_distance = (self.altitude * 2 * math.pi * 1000) / (640 * 256 * 2 ** 20)
        zoom_level = int(math.log((2 * math.pi * 1000 * math.cos(math.radians(37.7749))) / (pixel_distance * 640), 2))
        return zoom_level
    
    def generate_polygon_from_listOf_points(self) -> geopandas.GeoDataFrame:
        """
            Receive a list of objects of polygon's points to convert it into a geographic polygon could be intersected for area of interest feature.
            >>> generate_polygon_from_listOf_points()
            return GeoDataFrame
        """
        outer_coords = []
        for xy in self.map_bound :
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
        return processed_area
    

    def random_points_in_polygon(self, polygon) -> list:
        """
            By giving this function a polygon data frame, it will generate a number of random points in this polygon.
            >>> random_points_in_polygon(geopandas.GeoDataFrame)
            return list
        """
        points = []
        min_x, min_y, max_x, max_y = polygon.bounds
        i = 0
        while i < self.img_num:
            point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            if polygon.contains(point):
                points.append(point)
                i += 1
        return points

    def save_static_imgs(self, points, zoom_level) -> dict:
        """
            Saving a number of static Google Maps images inside custom area.
            >>> save_static_images(random_points_in_polygon, 19)
            return {"Result": "Images saved in /folder_name"}
        """
        folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        for i, point in enumerate(points):
            i+=1
            response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={point.y},{point.x}&zoom={zoom_level}&size=640x640&key=AIzaSyCU-JhfQHGclz6vgGXSk8D_18kem-RKOUk&signature=wGNz-TSklvSpfuP8cvEWjAapEQc=')
            
            if not os.path.exists(f"{folder_name}"):
                os.makedirs(f"{folder_name}")
            with open(f"{folder_name}\{point.y},{point.x}.png", 'wb') as f:
                for chunk in response:
                    f.write(chunk)
        print({"Result": f"Images saved in {os.path.abspath(folder_name)}"})
