# Images Folder contains images of the downloaded images from GoogleMaps with schema shown at the last of this page.

## Python file download number of static shots from Google Maps for a specific cases:

1. Geographic point (latitude, longitude, altitude).
2. Fixed distance.
3. A known direction.

##### Import libraries :
```python
import requests
from fastapi import FastAPI
import uvicorn
import math
from pydantic import BaseModel
from geopy.distance import distance
from geopy.point import Point 
```

```python  
app = FastAPI() 
```

#### Initialize request body

```python
class item(BaseModel):
    lat: float
    lng: float
    alt: float
    distance: int
    direction: str
```

#### Every direction pointed to a specific degree 
##### 0 degree is the North
```python
direction_to_degree = {"north": 0, "east": 90, "south": 180, "west": 270}
```

#### Define get root & function returns images count and status code
```python 
@app.get("/googleMaps")
def zoom(request: item):
```

#### Calculate Google Maps zoom level
```python 
pixel_distance = (request.alt * 2 * math.pi * 1000) / (640 * 256 * 2 ** 20)
zoom_level = int(math.log((2 * math.pi * 1000 * math.cos(math.radians(37.7749))) / (pixel_distance * 640), 2))
```

#### Calculate the new geographic positioning depending on explicit direction and distance 
```python 
new_point = distance(meters=request.distance).destination(Point(request.lat, request.lng),\
    bearing=direction_to_degree[request.direction])
new_point_lat, new_point_lng = round(new_point.latitude, 3), round(new_point.longitude, 3)
```

#### Define a counting variable, the make a "while loop" looping till Latitude and Longitude be the same and this mean it reach the explicit directed distance contained:
1. Adding 1 to the counter.
2. Get a static shot from Google map with a initialized (lat,lng, and zoom level).
3. Checking moving direction then detecting which earth quarter you are?
4. Move position center a little bit forward the destination.
5. Save shot to local file.
6. Go back to the request with the new (lat, lng), and do it until center reach destination. 
```python
img_count = 0
    while new_point_lat != request.lat and new_point_lng != request.lng:
        img_count += 1
        response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={request.lat},{request.lng}&zoom={zoom_level}&size=640x640&key=AIzaSyCIog63DvS6W2p-fhSWYFzNvDvqYFvUBPg')
        if request.direction in ("north", "south") :
            if new_point_lat > request.lat:
                request.lat += 0.001
                request.lat = round(request.lat, 3)
            elif new_point_lat < request.lat:
                request.lat -= 0.001
                request.lat = round(request.lat, 3)
        elif request.direction in ("west", "east") :
            if new_point_lng > request.lng:
                request.lng += 0.001
                request.lng = round(request.lng, 3)
            elif new_point_lng < request.lng:
                request.lng -= 0.001
                request.lng = round(request.lng, 3)
        with open(f"high_resolution_api/Image_{img_count}.png", 'wb') as f:
            for chunk in response:
                f.write(chunk)
    return json.dumps({"img_count": img_count}, "images_saved")
```
``` python 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
```

##### Example for request body :
```json
{
    "lat": 30.058152,
    "lng": 31.197144,
    "alt": 200,
    "direction": "east",
    "distance": 700
}
```