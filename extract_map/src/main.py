from extract_map_OSM import Extract_map
from fastapi import FastAPI, HTTPException, status
import  random, string
import osmnx as ox
import uvicorn

app = FastAPI()

@app.post('/extract-map')
async def extract_map_data(request: Extract_map):
    file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    tags = {}
    try:
        if request.bounds:
            directions = request.bounds
            for property in request.selected_properties: 
                tags[property.lower()] = True
            shipped_data = ox.geometries_from_bbox(directions['north'], directions['south'], directions['east'], directions['west'], tags)

        elif request.custom_area:
            for property in request.selected_properties: 
                tags[property.lower()] = True
            processed_area = Extract_map.areaOfInterestPath(request.custom_area)
            geometry_values = processed_area._get_value(0, 'geometry')
            shipped_data = ox.geometries_from_polygon(geometry_values, tags)

    except Exception as e: 
        raise  HTTPException(status_code=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED, detail=str(e))
    
    shipped_data = shipped_data.reset_index()

    try:
        Extract_map.to_extension(shipped_data, file_name , request.file_format)
    except IOError as e:
        raise HTTPException(status_code=status.HTTP_301_MOVED_PERMANENTLY, detail=str(e))
    
    return  ({"data": f"{len(shipped_data)} row saved",
                "email": request.email,
                "username": request.username,
                "downloading_path": f"http://192.168.150.195:8080/wakeb_mapdata/{file_name}.{request.file_format.lower()}"
                })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)