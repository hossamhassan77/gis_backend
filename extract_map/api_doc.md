## POST /extract-map

Extract and download data from OpenStreetMap attributes as a various file formats.

#### Parameters:

| Parameter           | Type       | Required  | Description  |
| ------------------- | ---------- | --------  |-----------
| file_format         | str        |    Yes    | Input your file format from (html, excel, csv).|
| selected_properties | list       |    Yes    | Choose more than one property that you want to extract from ("highway" ,"building", "natural" , "waterway", "railway", "amenity" ,"shop" ,"Emergency" ,"Healthcare" ,"Man made", "Military", "Office" ,"Public transport", "Telecom", "Tourism" ,"Sport").|
| bounds              | dict       |    No     | Map bound for user map view, the parameter format should be like: {"south":34.29218201355655,"west":-94.2624602013088,"north":50.389969655785514,"east":-77.1237883263088}.|
| custom_area         | list       |    No     | A list of dict contains lat, lng format for each vertex of drown polygon, alt least 3 dicts, and the format should be like: [{"lat":30.06095999755898,"lng":31.20790958404541},{"lat":30.059288551718552,"lng": 31.190614700317383},{"lat": 30.06095999755898,"lng":31.20790958404541}].|
| email               | str        |    Yes    | User email.        |
| username            | str        |    Yes    | User username.     |

**Note: Send one between "bound" and "custom_area" and the other must be `null`**

#### `Example`

`Request:`

```json
{
    "file_format": "csv",
    "selected_properties": ["Building", "Highway"],
    "bounds" : null,
    "custom_area": [{"lat":30.06095999755898,"lng":31.20790958404541},{"lat":30.059288551718552,"lng": 31.190614700317383},{"lat":30.04491295269813,"lng": 31.19353294372559},{"lat":30.060439995210462,"lng": 31.20829582214355},{"lat": 30.06095999755898,"lng":31.20790958404541}],
    "email": "wakeb.d@wakeb.tech",
    "username": "wakeb_data"
}
```

Response :
1. how much data that download.
2. user email.
3. user username.
4. file downloaded path in server.

```json
{
    "data": "963 row saved",
    "email": "wakeb.d@wakeb.tech",
    "username": "wakeb_data",
    "downloading_path": "http://20.46.50.48:8090/wakeb_mapdata/a1XI8sjziAYixyk55JCrLccVp.csv"
}
```