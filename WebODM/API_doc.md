# DRONE IMAGE TO 3D MODEL

#### Base URL:
https://127.0.0.1

##### EndPoint:
`GET /from_images_to_pointCloud`
get a json contain lat, lng, alt, R,G, and for an area captured with drone.

##### Response:
+ Response 200 (JSON)


##### Parameters:
1. photos_folder(required, str): Folder path to drones' images.
```json
{
    "photos_folder": "D:/Drones & Mapping/Datasets/Ortho mapping tutorial_Drone data/images"
}
```