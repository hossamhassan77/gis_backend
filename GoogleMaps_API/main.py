from google_map_api import item
import uvicorn
from fastapi import FastAPI
from geopy.distance import distance
from geopy.point import Point

app = FastAPI()
@app.get("/googleMaps")
def main(request: item):
    zoom_level = item.calculate_zoom_level(request.alt)
    new_point = distance(meters=request.distance).destination(Point(request.lat, request.lng), bearing=request.direction_to_degree[request.direction])
    new_point_lat, new_point_lng = round(new_point.latitude, 3), round(new_point.longitude, 3)
    respond = item.save_googleMaps_imgs(request.lat, request.lng, new_point_lat, new_point_lng, request.direction, zoom_level)
   
    return(respond)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)