from area_of_interest import AOI
from fastapi import FastAPI
import uvicorn
import json

app = FastAPI()

@app.post("/area-of-interest/polygon")
async def polygon(request: AOI):
    point_to_polygon = AOI.points_to_polygon(request.list_of_points)
    return json.loads(point_to_polygon.to_json())

@app.post("/area-of-interest/rectangle")
async def rectangle(request: AOI) -> dict:
    mapBound_to_polygon = AOI.boundsBox(request.boundBox)
    return json.loads(mapBound_to_polygon.to_json())

@app.post("/area-of-interest/circle")
async def circle(request: AOI):
    circle_to_point = AOI.circle_to_point(request.point, request.radius)
    return json.loads(circle_to_point.to_json())

@app.post("/area-of-interest/clip")
async def return_clip(request: AOI):
    clipped_data = AOI.clip_data(request.gdf, request.aoi)
    return json.loads(clipped_data.to_json())

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)