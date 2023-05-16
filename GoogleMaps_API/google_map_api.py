import requests
import random
import string
import math
import json
from pydantic import BaseModel
from shapely.geometry import Point
import geopandas


class item(BaseModel):
    map_bound: list
    imgs_numbers: int
    alt: int

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
    
    def calculate_zoom_level(altitude):
        pixel_distance = (altitude * 2 * math.pi * 1000) / (640 * 256 * 2 ** 20)
        zoom_level = int(math.log((2 * math.pi * 1000 * math.cos(math.radians(37.7749))) / (pixel_distance * 640), 2))
        return(zoom_level)
        
    def save_googleMaps_imgs(latitude, longitude, new_lat, new_lng, direction, zoom):
        img_count = 0
        folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        while new_lat != latitude and new_lng != longitude:
            img_count += 1
            
            response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={latitude},{longitude}&zoom={zoom}&size=640x640&key=AIzaSyCIog63DvS6W2p-fhSWYFzNvDvqYFvUBPg')
            if direction in ("north", "south") :
                if new_lat > latitude:
                    latitude += 0.001
                    latitude = round(latitude, 3)
                elif new_lat < latitude:
                    latitude -= 0.001
                    latitude = round(latitude, 3)
            elif direction in ("west", "east") :
                if new_lng > longitude:
                    longitude += 0.001
                    longitude = round(longitude, 3)
                elif new_lng < longitude:
                    longitude -= 0.001
                    longitude = round(longitude, 3)
            with open(f"\{folder_name}\{img_count}-{latitude},{longitude}.png", 'wb') as f:
                for chunk in response:
                    f.write(chunk)
        return ({"img_count": img_count, "directory": f"\{folder_name}"})

    def random_points_in_polygon(number, polygon):
        points = []
        min_x, min_y, max_x, max_y = polygon.bounds
        i = 0
        while i < number:
            point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            if polygon.contains(point):
                points.append(point)
                i += 1
        print (points)


# item.random_points_in_polygon(10, item.generate_polygon_from_listof_points([{'lat': 34.0068887, 'lng': -117.0926903}, {'lat': 34.0068887, 'lng': -117.0926903}, {'lat': 34.0068887, 'lng': -117.0926903}, {'lat': 34.0068887, 'lng': -117.0926903}]).iloc[0].geometry)