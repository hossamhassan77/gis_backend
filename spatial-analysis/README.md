# Spatial-analysis
### Introduction
This API provides a range of spatial analysis capabilities for geographical datasets, allowing you to perform various operations and obtain useful insights from your spatial data.
### Installation 
- install `python 3.6+`.
- Install dependencies using pip: `pip install -r requirements.txt`.
### Endpoints
- `/spatial-analysis/read-file`:
Read and convert a geographic file (e.g., csv, geojson, shapefile) to a GeoDataFrame.
- `/spatial-analysis/save-to-db`:
Save spatial data to a database table.
- `/spatial-analysis/buffer`:
Calculate a buffer zone around a geographical point.
- `/spatial-analysis/centroid`:
Calculate the centroid of spatial data.
- `/spatial-analysis/data-type`:
Get unique values for object data types and (min, max) for numeric data types in the spatial data.
- `/spatial-analysis/overlay`:
Perform spatial overlay operations between two GeoDataFrames.
- `/spatial-analysis/shape-length`:
Calculate the shape length of geometries in a spatial data file.
- `/spatial-analysis/shape-area`:
Calculate the shape area of geometries in a spatial data file.
- `/spatial-analysis/detect-crs`:
Detect the coordinate reference system (CRS) of a spatial data file.
- `/spatial-analysis/data-frame-description`:
Generate a descriptive summary of a GeoDataFrame from a given file.
- `/spatial-analysis/aggregate-columns:
Aggregate and summarize specified columns of a GeoDataFrame from a given file.
- `/spatial-analysis/spatial-join`:
Perform a spatial join operation between two geographical datasets.

### Folders
1. src:
 - `util.py` python file contains utils functions.
 - `main.py` python file contains fastapi endpoints and to run server.
2. wakeb_mapdata:
Contains all data to be tested in endpoints.
3. And docs files [README.md, API_DOCS.md, requirements.txt].