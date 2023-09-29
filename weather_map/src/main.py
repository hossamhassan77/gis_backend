from weather_mapExtraction import weather_map
from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/weather-map/current-weather/random-points-in-bound")
async def main(request: weather_map):
    points = weather_map.random_points_in_polygon(request.points_number, weather_map.generate_polygon_from_listof_points(request.bound).iloc[0].geometry)
    current_weather_list = []
    for i, point in enumerate(points):
        i += 1
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lon={point.x}&lat={point.y}&units=metric&appid=7dd4268263c638c054a45d4565f7d5fb")
        current_weather_list.append({f"Point({i}): 'lng':{point.x}, 'lat': {point.y}": response.json()})
    return (current_weather_list)

@app.get("/weather-map/current-weather/specific-point")
async def main(lat: float, lng:float):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lon={lng}&lat={lat}&units=metric&appid=7dd4268263c638c054a45d4565f7d5fb")
    return(response.json())

@app.get("/weather-map/forecast/specific-point")
async def main(lat: float, lng:float):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lng}&appid=7dd4268263c638c054a45d4565f7d5fb&units=metric")
    return(response.json())

@app.post("/weather-map/forecast/random-points-in-bound")
async def main(request: weather_map):
    points = weather_map.random_points_in_polygon(request.points_number, weather_map.generate_polygon_from_listof_points(request.bound).iloc[0].geometry)
    current_weather_list = []
    for i, point in enumerate(points):
        i += 1
        response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={point.y}&lon={point.x}&appid=7dd4268263c638c054a45d4565f7d5fb&units=metric")
        current_weather_list.append({f"Point({i}): 'lng':{point.x}, 'lat': {point.y}": response.json()})
    return(current_weather_list)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
