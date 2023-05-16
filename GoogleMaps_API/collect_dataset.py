import string, os, json
import geopandas as gpd
from PIL import Image
import random
from shapely.geometry import Point
from PIL.ExifTags import TAGS, GPSTAGS
import requests

# folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
# def get_geographic_coord_from_img(photo: str): 
#     image = Image.open(photo)
#     exif_data = image._getexif()
#     # Define a dictionary to map GPS tags to their human-readable names
#     gps_tags = {}
#     for key, value in GPSTAGS.items():
#         gps_tags[key] = value
#     # Loop over the EXIF data and print any GPS properties
#     for tag_id, value in exif_data.items():
#         tag_name = TAGS.get(tag_id, tag_id)
#         if tag_name == 'GPSInfo':
#                 for gps_tag_id in value:
#                     gps_tag_name = gps_tags.get(gps_tag_id, gps_tag_id)
#                     if gps_tag_name == 'GPSLongitude':
#                         lng = float(round(value[gps_tag_id][0] + value[gps_tag_id][1]/60 + value[gps_tag_id][2]/3600, 15))
#                         if value[3] == 'W':
#                             lng = -lng
#                     elif gps_tag_name == 'GPSLatitude' :
#                         lat = float(value[gps_tag_id][0] + value[gps_tag_id][1]/60 + value[gps_tag_id][2]/3600)
#                         if value[1] == 'S':
#                             lat = -lat
#     return lng, lat

# lng, lat = get_geographic_coord_from_img(r'D:\Drones & Mapping\Datasets\Ortho mapping tutorial_Drone data\images\YUN_0042.JPG')

# def make_polygon_from_center_point(lng, lat):
#     coord_list = []
#     coords= {}
#     if lng < 0:
#         lng -= 0.0004
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}
#         lng += 0.0008
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}
#     else :
#         lng += 0.0004
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}
#         lng -= 0.0008
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}

#     if lat < 0:
#         lat -= 0.0004
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}
#         lat += 0.0008
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}
#     else :
#         lat += 0.0004
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)
#         coords= {}
#         lat -= 0.0008
#         coords["lat"] = lat
#         coords["lng"] = lng
#         coord_list.append(coords)

#     return coords

# generated_polygon = item.generate_polygon_from_listof_points(make_polygon_from_center_point(lng,lat))
# list_of_random_points = item.random_points_in_polygon(2, generated_polygon.iloc[0].geometry)
# for i, point in enumerate(list_of_random_points):
#         response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={point.y},{point.x}&zoom={19}&size=640x640&key=AIzaSyCIog63DvS6W2p-fhSWYFzNvDvqYFvUBPg')
#         if not os.path.exists(f"{folder_name}"):
#                     os.makedirs(f"{folder_name}")
#         with open(f"{folder_name}\{i}_{point.y},{point.x}.png", 'wb') as f:
#                     for chunk in response:
#                         f.write(chunk)
# print ({"Result": f"Images saved in \{folder_name}"})


def areaOfInterestPath(path:list):
        """Input polygon path as a google objects to return polygon geoDataFrame.
        For example : areaOfInterestPath([{"lat":30.06095999755898,"lng":31.20790958404541},{"lat":30.059288551718552,"lng": 31.190614700317383},{"lat":30.04491295269813,"lng": 31.19353294372559}])
        """
        outer_coords = []
        for xy in path :
            inner_coordinates = []
            inner_coordinates.append(xy['lng'])
            inner_coordinates.append(xy['lat'])
            outer_coords.append(inner_coordinates)
        polygon = {
                "type": "FeatureCollection",
                "features": [
                    { 
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [outer_coords]
                            }
                            }
                        ]
                        }
        polygon2json = json.dumps(polygon)
        processed_area = gpd.read_file(polygon2json)
        return (processed_area)

def random_points_in_polygon(number, polygon):
        points = []
        min_x, min_y, max_x, max_y = polygon.bounds
        i = 0
        while i < number:
            point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
            if polygon.contains(point):
                points.append(point)
                i += 1
        return (points)


def get_geographic_coord_from_img(photo: str):
    image = Image.open(photo)

    exif_data = image._getexif()
    name, file_extension = os.path.splitext(photo)
    # Define a dictionary to map GPS tags to their human-readable names
    gps_tags = {}
    for key, value in GPSTAGS.items():
        gps_tags[key] = value
    # Loop over the EXIF data and print any GPS properties
    for tag_id, value in exif_data.items():
        tag_name = TAGS.get(tag_id, tag_id)
        if tag_name == 'GPSInfo':
                for gps_tag_id in value:
                    gps_tag_name = gps_tags.get(gps_tag_id, gps_tag_id)
                    if gps_tag_name == 'GPSLongitude':
                        lng = float(round(value[gps_tag_id][0] + value[gps_tag_id][1]/60 + value[gps_tag_id][2]/3600, 15))
                        if value[3] == 'W':
                            lng = -lng
                    elif gps_tag_name == 'GPSLatitude' :
                        lat = float(value[gps_tag_id][0] + value[gps_tag_id][1]/60 + value[gps_tag_id][2]/3600)
                        if value[1] == 'S':
                            lat = -lat
    coord_list = []
    coords= {}
    if lng < 0:
        lng -= 0.0004
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}
        lng += 0.0008
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}
    else :
        lng += 0.0004
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}
        lng -= 0.0008
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}

    if lat < 0:
        lat -= 0.0004
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}
        lat += 0.0008
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}
    else :
        lat += 0.0004
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}
        lat -= 0.0008
        coords["lat"] = lat
        coords["lng"] = lng
        coord_list.append(coords)
        coords= {}

    polygon = areaOfInterestPath(coord_list)
    list_of_random_points = random_points_in_polygon(20, polygon.iloc[0].geometry)
    for i, point in enumerate(list_of_random_points):
            response = requests.get(f'https://maps.googleapis.com/maps/api/staticmap?maptype=satellite&center={point.y},{point.x}&zoom={20}&size=640x640&key=AIzaSyCIog63DvS6W2p-fhSWYFzNvDvqYFvUBPg')
            if not os.path.exists(f"{name}"):
                        os.makedirs(f"{name}")
            with open(f"{name}\{i}_{point.y},{point.x}.png", 'wb') as f:
                        for chunk in response:
                            f.write(chunk)
    print ({"Result": f"Images saved in \{name}"})

folders_path = [r'D:\Drones & Mapping\drones15Feb2023\Data for GIS\DJI_202302141624_001_Zenmuse-L1-mission', r'D:\Drones & Mapping\drones15Feb2023\Data for GIS\DJI_202302141657_003_Zenmuse-L1-mission', r'D:\Drones & Mapping\Raw_Images12Apr23\DCIM\DJI_202304121320_003', r'D:\Drones & Mapping\Raw_Images12Apr23\DCIM\DJI_202304121305_001']
for i in folders_path:
    files_list = []
    for root, dirs, files in os.walk(i):
        for file in files:
            file_path = os.path.join(root, file) 
            _, file_extension = os.path.splitext(file_path)
            if file_extension == ".JPG":
                files_list.append(file_path)


    for i in files_list:
        get_geographic_coord_from_img(i)