## GET URL: /drones-products
### Query Parameters:

- image_folder_dir(required: str): Path to the folder containing drone image data.

#### Example:
`http://127.0.0.1:8000/drones-products?image_folder_dir=your/image/folder/path`
##### Important note:
Image dataset must be in this directory `.../wakeb_mapdata/datasets/project/images`, but when you send the request send the path to `\wakeb_mapdata\datasets`

#### Response:
- Status Code: 200 OK - When the process finishes, the results will be organized as follows:
```
|-- images/
    |-- img-1234.jpg
    |-- ...
|-- opensfm/
    |-- see mapillary/opensfm repository for more info
|-- odm_meshing/
    |-- odm_mesh.ply                    # A 3D mesh
|-- odm_texturing/
    |-- odm_textured_model.obj          # Textured mesh
    |-- odm_textured_model_geo.obj      # Georeferenced textured mesh
|-- odm_georeferencing/
    |-- odm_georeferenced_model.laz     # LAZ format point cloud
|-- odm_orthophoto/
    |-- odm_orthophoto.tif              # Orthophoto GeoTiff
```

- Status Code: 204 No Content - If the operation is successful, the server responds with an empty response.
- Status Code: 400 Bad Request - If an error occurs during the operation.