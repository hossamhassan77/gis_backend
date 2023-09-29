# Endpoint(1): GET /googleMaps/point-to-point
## Description:
Downloads number of static Google satellite map form geographic point to another with a specific zoom level.

## Parameters:

| Parameter      | Type       | Required  | Description|
| -------------  | ---------- | --------  |-----------
| lat            | int        |    Yes    |Geographical latitude center.|
| lng            | int        |    Yes    |Geographical longitude center.|
| alt            | int        |    Yes    |The height of drone's hover in meters.|
| direction      | str        |    Yes    |Drone's moving Direction, it should be between(north, south, west, east).|
| flight_distance| int        |    Yes    |The distance that drone moved in meters|

## Example:
Request:
```
GET /googleMaps/point-to-point?lat=30.058152&lng=31.197144&alt=200&direction=east&flight_distance=700
```
### Success Response:

### Status Code: 200
* Format: JSON
* Example:
```Json
{
    "img_count": 20,
    "directory": ".\\7UFQN"
}
```
### Status Code: 404
* Format: JSON
* Example:
```Json
{
  "detail": "Item not found"
}
```


# Endpoint(2): POST /googleMaps/random-imgs-in-mapBound
## Description:
Downloads number of static Google satellite map in a given map bound.

## Parameters:

| Parameter      | Type       | Required  | Description|
| -------------  | ---------- | --------  |-----------
| map_bound      | list       |    Yes    |A list of (lat, lng) of the bound vertex.|
| imgs_numbers   | int        |    Yes    |How many image you want to download.|
| alt            | int        |    Yes    |The height of drone's hover in meters.|

## Example:
Request:
```
POST /googleMaps/random-imgs-in-mapBound
```
```JSON
{
    "map_bound": [{"lat":40.38427,"lng":-105.18831},{"lat":40.35078,"lng":-104.38631},{"lat":39.84234,"lng":-104.50167}],
    "imgs_numbers": 2,
    "alt": 200
}
```
### Success Response:

### Status Code: 200
* Format: JSON
* Example:
```Json
{
    "Result": "Images saved in .\\7JQQ6f"
}
```
### Status Code: 404
* Format: JSON
* Example:
```Json
{
  "detail": "Item not found"
}
```