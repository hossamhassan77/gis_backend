"""
Modules providing FastAPI framework, and uvicorn ready for production,
and ODM class from open_drone_map.py
"""
import subprocess
import uvicorn
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/drones-products")
async def produced_from_odm(image_folder_dir: str):
    """
    Function take parameters from request query string that produces many 
    types of data formats from drones images by using Docker from opendronemap/odm container
    """
    try:
        command = f'docker run -ti --rm -v {image_folder_dir}:/datasets opendronemap/odm --project-path /datasets project'
        process = subprocess.run(command, shell=True, check=False)
        if process.returncode != 0:
            raise subprocess.CalledProcessError(returncode=process.returncode, cmd=command)
        return {"Status": "All file formats produced",
                "file_path": "./wakeb_mapdata/datasets/project/*"}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
