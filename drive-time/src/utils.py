"""

"""
from datetime import datetime, timedelta
from typing import Union
import googlemaps
import json
import geopandas

class DriveTime:
    """"""
    def __init__(self, api_key) -> None:
        self.api_key = api_key
    def get_drive_time_geocoded(self, lat:Union[int, float], long:Union[int, float], max_travel_time:int) -> list:
        """
        Calculate valid destinations within a specified maximum drive time from\
        a given latitude and longitude and return it as geocoded locations.
        
        Parameters:
        lat (float): Latitude of the starting location.
        long (float): Longitude of the starting location.
        max_travel_time (int): Maximum travel time in minutes.
        """
        google_maps = googlemaps.Client(key=self.api_key)
        origin_coordinates = (lat, long)
        target_time = datetime.now() + timedelta(seconds=max_travel_time * 60)
        places_result = google_maps.places_nearby(location=origin_coordinates,
                                                    radius=max_travel_time * 60)
        valid_destinations = []
        for place in places_result['results']:
            destination_location = (place['geometry']['location']['lat'],\
                                    place['geometry']['location']['lng'])
            directions = google_maps.directions(
                origin=origin_coordinates,
                destination=destination_location,
                mode="driving",
                departure_time=target_time)
            if directions and 'legs' in directions[0]:
                total_duration = directions[0]['legs'][0]['duration']['value']
                if total_duration <= (max_travel_time * 60):
                    valid_destinations.append(place)
        geocoded_locations = []
        for destination in valid_destinations:
            geocoded_locations.append(destination['vicinity'])
        return geocoded_locations
    def get_drive_time_locations(self, lat:Union[int, float], long:Union[int, float], max_travel_time:int) -> list:
        """
        Calculate valid destinations within a specified maximum drive time from\
        a given latitude and longitude and return it as (latitude and longitude).
        
        Parameters:
        lat (float): Latitude of the starting location.
        long (float): Longitude of the starting location.
        max_travel_time (int): Maximum travel time in minutes.
        """
        google_maps = googlemaps.Client(key=self.api_key)
        origin_coordinates = (lat, long)
        places_result = google_maps.places_nearby(location=origin_coordinates,
                                                    radius=max_travel_time * 60)
        points = {"type": "FeatureCollection", "features": []}
        for place in places_result['results']:
            destination_lng, destination_lat = place['geometry']['location']['lat'],\
                                    place['geometry']['location']['lng']
            point_feature = {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [destination_lng, destination_lat]}}
        points['features'].append(point_feature)
        geojson_format = json.dumps(points)
        processed_area = geopandas.read_file(geojson_format)
        return processed_area
    def convert_geocode(self, geocode_list: list) -> geopandas.GeoDataFrame:
        """
        Convert a list of addresses to a GeoDataFrame containing point geometries.
        
        Parameters:
        geocode_list (list): A list of addresses to be geocoded.
        """
        points = {"type": "FeatureCollection", "features": []}
        google_maps = googlemaps.Client(key=self.api_key)
        for address in geocode_list:
            geocode_result = google_maps.geocode(address)
            if geocode_result:
                location = geocode_result[0]['geometry']['location']
                latitude = location['lat']
                longitude = location['lng']
                point_feature = {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [longitude, latitude]}}
                points['features'].append(point_feature)
        geojson_format = json.dumps(points)
        processed_area = geopandas.read_file(geojson_format)
        return processed_area

drive_time = DriveTime("AIzaSyCIog63DvS6W2p-fhSWYFzNvDvqYFvUBPg")
print(drive_time.get_drive_time_geocoded(30.058204316571594, 31.196944960430784, 20))
print(drive_time.convert_geocode(drive_time.get_drive_time_geocoded(30.058056251123933, 31.19751463041555, 20)))
