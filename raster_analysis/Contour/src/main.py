import requests
from fastapi import FastAPI, HTTPException
import subprocess
import uvicorn
from osgeo import gdal
import json
import geopandas as gpd
import os, random, string

app = FastAPI()

@app.get("/dem-contour")
async def dem_contour(input_dem: str, elevation_interval:float) -> dict:
    if not os.path.exists('wakeb_mapdata'):
        os.mkdir('wakeb_mapdata')
    absolute_path = os.path.abspath("wakeb_mapdata")
    file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    try:
        command = f'gdal_contour -a elev {input_dem} {absolute_path}/{file_name}.geojson -i {elevation_interval}'
        subprocess.run(command, shell=True)
        return {"Status": "Contour produced",
                "file_path": f"{absolute_path}\\{file_name}.geojson"}
    except:
        raise HTTPException(status_code=400, detail= "Entity not processable")
@app.get("/mapBound-contour")
async def mapBound_contour(north: float, south: float, west: float, east: float, elevation_interval:float) -> dict:
    dem_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    contour_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    absolute_path = os.path.abspath("wakeb_mapdata")
    request_url = f'https://portal.opentopography.org/API/globaldem?demtype=NASADEM&west={west}&south={south}&east={east}&north={north}&outputFormat=GTiff&API_Key=9365153072b4cdc3a56597c1b492cde3'
    response = requests.get(request_url)
    if response.status_code == 200:
        with open(f'wakeb_mapdata/{dem_name}.tif', 'wb') as file:
            file.write(response.content)
            
        command = f'gdal_contour -a elev wakeb_mapdata/{dem_name}.tif {absolute_path}/{contour_name}.geojson -i {elevation_interval}'
        subprocess.run(command, shell=True)
        df = gpd.read_file(rf'wakeb_mapdata/{contour_name}.geojson')
        return json.loads(df.to_json())
    else:
        raise HTTPException(status_code=400, detail= "Entity not processable")
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)