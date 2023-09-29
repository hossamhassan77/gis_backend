""" 
Modules for geographic functions and fastapi requests 
!pip install geopandas pydantic typing json
"""
import json
import geopandas
from pydantic import BaseModel
from typing import Optional
class AOI(BaseModel):
    list_of_points: Optional[list]
    boundBox      : Optional[dict]
    point         : Optional[dict]
    radius        : Optional[int]
    gdf           : Optional[str]
    aoi           : Optional[str]
    def points_to_polygon(points: list) -> geopandas.GeoDataFrame:
        """Receive a list of objects of polygon's points to convert it into
           a geographic polygon could be intersected for area of interest feature.
        >>> Area_of_interest.points_to_polygon([{"lat":0.38427119123016,"lng":-5.18831674093013},{"lat":10.35078901802308,"lng":-4.38631478780513},{"lat":19.84234491122627,"lng":-4.50167123311763}])
        return geopandas.GeoDataFrame
        """
        outer_coords = []
        for xy in points :
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
        processed_area = geopandas.read_file(polygon2json)
        return processed_area
    
    def boundsBox(bound:dict) -> geopandas.GeoDataFrame:
        """The bound box of map view, Needs bounds dict, returns polygon that will be overlayed with the GeoDataFrame.
        >>> Area_of_interest.boundsBox({"south": 39.331, "west": -105.170, "north": 40.386, "east": -102.91})
        return GeoDataFrame
        """
        lat_lng = []
        coords = []
        bounds = bound
        lat_lng.append(bounds['west'])
        lat_lng.append(bounds['north'])
        coords.append(lat_lng)
        lat_lng = []
        lat_lng.append(bounds['east'])
        lat_lng.append(bounds['north'])
        coords.append(lat_lng)
        lat_lng = []
        lat_lng.append(bounds['east'])
        lat_lng.append(bounds['south'])
        coords.append(lat_lng)
        lat_lng = []
        lat_lng.append(bounds['west'])
        lat_lng.append(bounds['south'])
        coords.append(lat_lng)
        coords.append(lat_lng)
        json_polygon = {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [coords]}}]}
        json_string = json.dumps(json_polygon)
        gdf_polygon= geopandas.read_file(json_string)
        return gdf_polygon
    
    def circle_to_point(point:dict, radius) -> geopandas.GeoDataFrame:
        coords = [point["lng"], point["lat"]]
        json_polygon = {
            "type": "FeatureCollection",
            "features": [
                {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": coords}}]}
        json_string = json.dumps(json_polygon)
        gdf_polygon= geopandas.read_file(json_string, crs="EPSG:4326")
        gdf_polygon_utm = gdf_polygon.to_crs(gdf_polygon.estimate_utm_crs())
        gdf_polygon_utm["buffered"] = gdf_polygon_utm.buffer(radius)
        gdf_buffer_geometry = gdf_polygon_utm.set_geometry('buffered').drop("geometry", axis=1)
        gdf_polygon = gdf_buffer_geometry.to_crs(crs='wgs84')
        return gdf_polygon
    
    def clip_data(gdf, aoi):
        geo_df = geopandas.read_file(gdf)
        aoi_df = geopandas.read_file(aoi)
        clipped_gdf = geo_df.clip(aoi_df, keep_geom_type=False)
        return clipped_gdf
