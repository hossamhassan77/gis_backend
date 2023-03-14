import requests
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
directions = {"north": 0, "east": 90, "south": 180, "west": 270}
@app.get("/googleMaps")
def zoom(request: item):
    pixel_distance = (request.alt * 2 * math.pi * 1000) / (640 * 256 * 2 ** 20)
    zoom_level = int(math.log((2 * math.pi * 1000 * math.cos(math.radians(37.7749))) / (pixel_distance * 640), 2))
    response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={request.lat},{request.lng}&zoom={zoom_level}&size=640x640&key=AIzaSyCIog63DvS6W2p-fhSWYFzNvDvqYFvUBPg')
    new_point = distance(meters=request.distance).destination(Point(request.lat, request.lng), bearing=directions[request.direction])
    new_point_lat = round(new_point.latitude, 6)
    new_point_lng = round(new_point.longitude, 6)
    
    if response.status_code == 200:
        with open(f"high_resolution_api/high_resolution_image.png", 'wb') as f:
            for chunk in response:
                f.write(chunk)
        return(zoom_level, response.status_code, "photo_saved")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)