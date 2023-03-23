import requests
import random
import string
from fastapi import FastAPI
import uvicorn
import math
from pydantic import BaseModel
from geopy.distance import distance
from geopy.point import Point

app = FastAPI()

class item(BaseModel):
    lat: float
    lng: float
    alt: float
    distance: int
    direction: str
    direction_to_degree = {"north": 0, "east": 90, "south": 180, "west": 270}

    def calculate_zoom_level(altitude):
        pixel_distance = (altitude * 2 * math.pi * 1000) / (640 * 256 * 2 ** 20)
        zoom_level = int(math.log((2 * math.pi * 1000 * math.cos(math.radians(37.7749))) / (pixel_distance * 640), 2))
        return(zoom_level)
        
    def save_googleMaps_imgs(latitude, longitude, new_lat, new_lng, direction, zoom):
        img_count = 0
        while new_lat != latitude and new_lng != longitude:
            img_count += 1
            Image_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
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
            with open(f"personal_github\gis_backend\GoogleMaps_API\Images\{Image_name}.png", 'wb') as f:
                for chunk in response:
                    f.write(chunk)
        return ({"img_count": img_count, "Status": response.status_code})

@app.get("/googleMaps")
def zoom(request: item):
    zoom_level = item.calculate_zoom_level(request.alt)

    new_point = distance(meters=request.distance).destination(Point(request.lat, request.lng), bearing=request.direction_to_degree[request.direction])
    new_point_lat, new_point_lng = round(new_point.latitude, 3), round(new_point.longitude, 3)

    respond = item.save_googleMaps_imgs(request.lat, request.lng, new_point_lat, new_point_lng, request.direction, zoom_level)
    return(respond)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)