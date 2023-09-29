from fastapi import FastAPI, HTTPException
import uvicorn
from osgeo import gdal
import subprocess
import os, random, string
import requests

app = FastAPI()

@app.get("/dem-hillshade")
async def dem_hillshade(input_dem: str) -> dict:
    if not os.path.exists('wakeb_mapdata'):
        os.mkdir('wakeb_mapdata')
    absolute_path = os.path.abspath("wakeb_mapdata")
    file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    try:
        command = f'gdaldem hillshade {input_dem} {absolute_path}/{file_name}.tif'
        subprocess.run(command, shell=True)
        return {"Status": "Hillshade produced",
                "file_path": f"{absolute_path}\\{file_name}.tif"}
    except:
        raise HTTPException(status_code=400, detail= "Entity not processable")

@app.get("/mapBound-hillshade")
async def mapBound_hillshade(north: float, south: float, west: float, east: float) -> dict:
    dem_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    hillshade_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))
    absolute_path = os.path.abspath("wakeb_mapdata")
    request_url = f'https://portal.opentopography.org/API/globaldem?demtype=NASADEM&west={west}&south={south}&east={east}&north={north}&outputFormat=GTiff&API_Key=9365153072b4cdc3a56597c1b492cde3'
    response = requests.get(request_url)
    if response.status_code == 200:
        with open(f'wakeb_mapdata/{dem_name}.tif', 'wb') as file:
            file.write(response.content)
        command = f'gdaldem hillshade wakeb_mapdata/{dem_name}.tif wakeb_mapdata/{hillshade_name}.tif'
        subprocess.run(command, shell=True)
        return({"status": "Success", 
                "file_path": f"{absolute_path}\\{hillshade_name}.tif"})
    else:
        raise HTTPException(status_code=400, detail= "Entity not processable")
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)