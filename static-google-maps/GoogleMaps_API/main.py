from google_map_api import item
import uvicorn
from fastapi import FastAPI, HTTPException
from geopy.distance import distance
from geopy.point import Point
import requests
import random, string, os

app = FastAPI()
@app.get("/googleMaps/point-to-point")
def main(alt:int, flight_distance:int, lat:float, lng:float, direction: str):
    direction_to_degree = {"north": 0, "east": 90, "south": 180, "west": 270}
    try:
        zoom_level = item.calculate_zoom_level(alt)
        new_point = distance(meters= flight_distance).destination(Point(lat, lng), bearing=direction_to_degree[direction])
        new_point_lat, new_point_lng = round(new_point.latitude, 3), round(new_point.longitude, 3)
        respond = item.save_googleMaps_imgs(lat, lng, new_point_lat, new_point_lng, direction, zoom_level)
        return(respond)
    except:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.post("/googleMaps/random-imgs-in-mapBound")
def get_imgs_in_map_bound(request: item):
    try:
        folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        zoom_level = item.calculate_zoom_level(request.alt)
        generate_polygon = item.generate_polygon_from_listof_points(request.map_bound)
        list_of_random_points = item.random_points_in_polygon(request.imgs_numbers, generate_polygon.iloc[0].geometry)
        for i, point in enumerate(list_of_random_points):
            i+=1
            response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={point.y},{point.x}&zoom={zoom_level}&size=640x640&key=AIzaSyCU-JhfQHGclz6vgGXSk8D_18kem-RKOUk&signature=wGNz-TSklvSpfuP8cvEWjAapEQc=')
            if not os.path.exists(f"{folder_name}"):
                        os.makedirs(f"{folder_name}")
            with open(f"{folder_name}\{i}_{point.y},{point.x}.jpg", 'wb') as f:
                        for chunk in response:
                            f.write(chunk)
        return ({"Result": f"Images saved in \{folder_name}"})
    except:
          raise HTTPException(status_code=404, detail="Item not found")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)