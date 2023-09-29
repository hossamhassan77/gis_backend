# Endpoint(1): GET /mapBound-hillshade
### Description:
Generate a shaded relief map from JSON format for map bound.

## Parameters:
| Parameter | Type   | Required  | Description                           |
| ----------| -------| ----------|---------------------------------------|
| west      | float  |    Yes    |Geographical map bound direction West. |
| east      | float  |    Yes    |Geographical map bound direction East. |
| north     | float  |    Yes    |Geographical map bound direction North.|
| south     | float  |    Yes    |Geographical map bound direction South.|

## Example:
Request:
```
GET /mapBound-hillshade?west=32.13973602505795&south=29.88397934934521&east=32.956926480302506&north=30.22656908627855
```
## Responses:
#### Status Code: 200 Success
* Format: JSON
* Example:
```Json
{
    "status": "Success",
    "file_path": "D:\\Github\\GIS\\wakeb_mapdata\\CdGCBh0a6shjKMduukOMXXoMj.tif"
}
```
### Status Code: 400 Bad Request
```Json
{
    "detail": "Entity not processable"
}
```


# Endpoint(2): GET /dem-hillshade
### Description:
Generate a shaded relief map from any Digital Elevation Model raster.

## Parameters:
| Parameter | Type   | Required  | Description                           |
| ----------| -------| ----------|---------------------------------------|
| input_dem | str    | Yes       |The digital elevation model file path. |

## Example:
Request:
```
GET /dem-hillshade?input_dem=D:\Github\GIS\wakeb_mapdata\ALPSMLC30_N021E039_DSM.tif
```
## Responses:
#### Status Code: 200 Success
* Format: JSON
* Example:
```Json
{
    "Status": "Hillshade produced",
    "file_path": "D:\\Github\\GIS\\wakeb_mapdata\\FhglxCD2Gt.tif"
}
```
### Status Code: 400 Unprocessable Entity
```Json
{
    "detail": "Entity not processable"
}
```