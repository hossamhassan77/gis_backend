# 3D-map visualization
The Drone Image Data Processing for processing aerial drone imagery. ODM turns simple 2D images into:
* Classified Point Clouds
* 3D Textured Models
* Georeferenced Orthophotos 
* Georeferenced Digital Elevation Models

## Requirements
* Python 3.7+
* FastAPI
* Uvicorn
* Docker

## Installation
1. Install the required dependencies:
```bash
pip install -r requirements.txt
```
2. After installing Docker:
Run this command in cmd prompt `docker pull opendronemap/odm` to 

## Folders:
#### 1. src: 
Contains API documentation, `main.py` file to run the server, and `open_drone_map.py` contains utils functions.
#### 2. wakeb_mapdata: 
Contains the schema of file directory to drones images 'wakeb_mapdata/dataset/project/images'.
## Other Files:
1. Postman collection for all endpoints with example for each of them. _Import the JSON file in postman platform._ 
2. requirements.txt: contains all required python packages to be install before running `main.py`.

The `/drones-products` endpoint processes the drone image data by calling the `produced_from_odm` method of the `ODM` class. It takes the `image_folder_dir` as a query parameter and produces various data formats from the drone images using the Open Drone Map container.
