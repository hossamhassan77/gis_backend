## DEM Contour
Generates contour lines from a Digital Elevation Model (DEM) file.

**Endpoint:** `/dem-contour`

**Method:** GET

### Parameters

- `input_dem` (str): The path to the input DEM file.
- `elevation_interval` (float): The contour elevation interval.
### Request:
```
/dem-contour?input_dem=D:\Github\GIS\Land_use\wakeb_mapdata\ALPSMLC30_N021E039_DSM.tif&elevation_interval=100
```
### Response:

- `Status` (str): The status of the contour generation process. Possible values: "Contour produced" or error message.
- `file_path` (str): The absolute file path of the generated contour file (GeoJSON format).

#### Example:
```JSON
{
    "Status": "Contour produced",
    "file_path": "D:\\Github\\GIS\\Land_use\\wakeb_mapdata\\a89evnU5A4.geojson"
}
```
---

## Map Bound Contour

Generates contour lines from a specified map boundary.

**Endpoint:** `/mapBound-contour`

**Method:** GET

### Parameters

- `north` (float): The northern latitude coordinate of the map boundary.
- `south` (float): The southern latitude coordinate of the map boundary.
- `west` (float): The western longitude coordinate of the map boundary.
- `east` (float): The eastern longitude coordinate of the map boundary.
- `elevation_interval` (float): The contour elevation interval.
### Request:
```
/mapBound-contour?west=32.13973602505795&south=29.88397934934521&east=32.956926480302506&north=30.22656908627855&elevation_interval=100
```
### Response

Returns a GeoJSON representation of the contour lines.

#### Example:
```JSON
    {
    "type": "FeatureCollection",
    "features": [
        {
            "id": "0",
            "type": "Feature",
            "properties": {
                "ID": 0,
                "elev": 0.0
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        32.562500000305874,
                        30.22680555555147
                    ],
                    [
                        32.562500000305874,
                        30.22666666666258
                    ],
                    [
                        32.56277777780587,
                        30.22638888916258
                    ],
                    [
                        32.56305555558365,
                        30.226388889023692
                    ],
                    [
                        32.56324074076883,
                        30.22666666666258
                    ],
                    [
                        32.56324074076883,
                        30.22680555555147
                    ]
                ]
            }
        },
        {
            "id": "1",
            "type": "Feature",
            "properties": {
                "ID": 1,
                "elev": 100.0
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        32.34930555572251,
                        30.22680555555147
                    ],
                    [
                        32.34930555572251,
                        30.22666666666258
                    ],
                    [
                        32.34944444447251,
                        30.22638888916258
                    ],
                    [
                        32.349722222250286,
                        30.22638888916258
                    ],
                    [
                        32.35000000002807,
                        30.22652777791258
                    ],
                    [
                        32.35027777752807,
                        30.22666666666258
                    ],
                    [
                        32.35027777752807,
                        30.22680555555147
                    ]
                ]
            }
        },
        {
            "id": "2",
            "type": "Feature",
            "properties": {
                "ID": 2,
                "elev": 100.0
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        32.35027777808362,
                        30.22680555555147
                    ],
                    [
                        32.35027777808362,
                        30.22666666666258
                    ],
                    [
                        32.350555555583625,
                        30.22652777791258
                    ],
                    [
                        32.35083333308362,
                        30.22666666666258
                    ],
                    [
                        32.35083333308362,
                        30.22680555555147
                    ]
                ]   
            }
        }
    }
```


