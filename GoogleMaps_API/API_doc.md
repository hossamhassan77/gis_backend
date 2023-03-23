# Google Maps API

#### Base URL:
https://127.0.0.1

##### EndPoint:
`GET /googleMaps`
get an image screen shoot from Google Maps.

##### Response:
+ Response 200 (Image)
<img data-canonical-src="https://raw.githubusercontent.com/Wakeb-Tech/GIS/main/Google_maps_API/Images/6hfednZsQz8CYpd3TFpWl7pHg.png?token=GHSAT0AAAAAACAAJPERSU26T7RI3PHCC2RSZA4GSIQ" width="400" height="400"/>

##### Parameters:
1. lat(required, float): Geographical latitude center.
2. lng(required, float): Geographical longitude center.
3. lat(required, float): The height of drone's hover in meters.
4. direction(required, string): Drone's moving Direction, it should be between(north, south, west, east).
5. distance(required, string): The distance that drone moved in meters.
```json
{
    "lat": 30.058152,
    "lng": 31.197144,
    "alt": 200,
    "direction": "east",
    "distance": 700
}
```
##### Error Response:
+ 404 Not Found: Their is a wrong parameter in the body request.
+ 403 Forbidden: Google blocked you IP.
+ 422 Unprocessable entity: Their is a wrong parameter in the body request.
