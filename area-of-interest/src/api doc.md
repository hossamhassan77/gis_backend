# Area of Interest API

This API allows you to perform various area of interest operations, such as creating polygons, rectangles, and circles.

## Endpoints

#### Create Polygon

- **URL:** `/area-of-interest/polygon`
- **Method:** POST
- **Description:** Creates a polygon from a list of points.
- **Request Body:**
    - `list_of_points` (list of dictionary): An list of points that define the polygon.
        - `lat` (float): The lat coordinate of the point.
        - `lng` (float): The lng coordinate of the point.
- **Response:**
    - The response contains the created polygon in GeoJSON format.
    
#### Create Rectangle

- **URL:** `/area-of-interest/rectangle`
- **Method:** POST
- **Description:** Creates a rectangle from a bounding box.
- **Request Body:**
    - `boundBox` (dictionary): An dictionary representing the bounding box of the rectangle.
        - `north` (float): The northern lat coordinate of the bounding box.
        - `south` (float): The southern lat coordinate of the bounding box.
        - `west` (float): The western lng coordinate of the bounding box.
        - `east` (float): The eastern lng coordinate of the bounding box.
- **Response:**
    - The response contains the created rectangle in GeoJSON format.
    
#### Create Circle

- **URL:** `/area-of-interest/circle`
- **Method:** POST
- **Description:** Creates a circle from a center point and radius.
- **Request Body:**
    - `point` (dictionary): An dictionary representing the center point of the circle.
        - `lat` (float): The lat coordinate of the center point.
        - `lng` (float): The lng coordinate of the center point.
    - `radius` (int): The radius of the circle in meters.
- **Response:**
    - The response contains the created circle in GeoJSON format.

#### Clip

- **URL:** `/area-of-interest/clip`
- **Method:** POST
- **Description:** Clips data based on the provided Area of Interest (AOI).
- **Request Body:**
    - `gdf` (str): the file path to GeoDataFrame containing the data to be clipped.
    - `aoi` (str): the file path to GeoDataFrame representing the Area of Interest (AOI) to clip the data with.
- **Response:**
    - The response contains the clipped data as a GeoJSON object.

## Example Usage

#### Create Polygon

```
POST /area-of-interest/polygon
```
Request Body:
```
{
  "list_of_points": [
    {"lat": 40.1234, "lng": -74.5678},
    {"lat": 40.2345, "lng": -74.6789},
    {"lat": 40.3456, "lng": -74.7890},
    ...
  ]
}
```
Response Body:
```
{
  "type": "Polygon",
  "coordinates": [
    [
      [-74.5678, 40.1234],
      [-74.6789, 40.2345],
      [-74.7890, 40.3456],
      ...
    ]
  ]
}
```

#### Create Rectangle

```
POST /area-of-interest/rectangle
```
Request Body:
```
{
  "boundBox": {
    "north": 40.1234,
    "south": 40.5678,
    "west": -74.6789,
    "east": -74.2345
  }
}
```
Response Body:
```
{
  "type": "Polygon",
  "coordinates": [
    [
      [-74.6789, 40.1234],
      [-74.2345, 40.1234],
      [-74.2345, 40.5678],
      [-74.6789, 40.5678],
      [-74.6789, 40.1234]
    ]
  ]
}
```

#### Create circle

```
POST /area-of-interest/clip
```
Request Body:
```
{
    "gdf": "http:/localhost:8000/wakeb_mapdata/raptor_nest.geojson",
    "aoi": "http:/localhost:8000/wakeb_mapdata/counties.geojson"
}
```
Response Body:
```
{
  "type": "Polygon",
  "coordinates": [
    [
      [-74.5678, 40.1243],
      [-74.5692, 40.1238],
      [-74.5714, 40.1225],
      ...
    ]
  ]
}
```

#### Clip

```
POST /area-of-interest/circle
```
Request Body:
```
{
  "point": {
    "lat": 40.1234,
    "lng": -74.5678
  },
  "radius": 1000
}
```
Response Body:
```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {...},
      "geometry": {
        "coordinates": [
          32.60774035671716,
          29.483196142025164
        ],
        "type": "Point"
      }
    }
  ],
  ...
}
```