# Spatial Analysis API

These APIs provide a range of spatial analysis capabilities for geographical datasets, allowing you to perform various operations and obtain useful insights from your spatial data.

#### 1. Read Geographic File
- **Endpoint:** `/spatial-analysis/read-file`
- **Description:** Read and convert a geographic file (e.g., csv, geojson, shapefile) to a GeoDataFrame.
- **Parameters:**
  - `long` (float): The longitude of the location.
  - `lat` (float): The latitude of the location.
  - `file_path` (str): The path to the geographic file.
- **HTTP Method:** GET
- **Response:** A JSON representation of the GeoDataFrame.

#### 2. Save to Database
- **Endpoint:** `/spatial-analysis/save-to-db`
- **Description:** Save spatial data to a database table.
- **Parameters:**
  - `long` (float): The longitude of the location.
  - `lat` (float): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
  - `table_name` (str): The name of the database table to save the data to.
- **HTTP Method:** GET
- **Response:** A JSON representation of the saved spatial data.

#### 3. Buffer
- **Endpoint:** `/spatial-analysis/buffer`
- **Description:** Calculate a buffer zone around a geographical point.
- **Parameters:**
  - `long` (float): The longitude of the location.
  - `lat` (float): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
  - `buffer_size` (Union[int, float]): The size of the buffer zone in the same units as the spatial data file's coordinate system.
- **HTTP Method:** GET
- **Response:** A JSON object containing the buffered geometries.

#### 4. Centroid
- **Endpoint:** `/spatial-analysis/centroid`
- **Description:** Calculate the centroid of spatial data.
- **Parameters:**
  - `long` (float): The longitude of the location.
  - `lat` (float): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
- **HTTP Method:** GET
- **Response:** A JSON object containing the centroid coordinates.

#### 5. Data Types
- **Endpoint:** `/spatial-analysis/data-type`
- **Description:** Get unique values for object data types and (min, max) for numeric data types in the spatial data.
- **Parameters:**
  - `file_path` (str): The path to the spatial data file.
  - `long` (str): The EPSG code specifying the coordinate system.
  - `lat` (str): The latitude of the location.
  - `time_column` (Optional[str]): The name of the time column (if applicable).
- **HTTP Method:** GET
- **Response:** JSON containing data type information.

#### 6. Overlay
- **Endpoint:** `/spatial-analysis/overlay`
- **Description:** Perform spatial overlay operations between two GeoDataFrames.
- **Parameters:**
  - `long` (str): The longitude of the location.
  - `lat` (str): The latitude of the location.
  - `file_path` (str): The path to the first spatial data file.
  - `overlay_method` (str): The overlay operation to perform ('intersection', 'union', 'identity', 'symmetric_difference', or 'difference').
  - `file_path_two` (Optional[str]): The path to the second spatial data file (optional).
  - `aoi_path` (Optional[list]): A list of AOI (Area of Interest) coordinates (optional).
- **HTTP Method:** GET
- **Response:** A JSON representation of the result of the overlay operation.

#### 7. Shape Length
- **Endpoint:** `/spatial-analysis/shape-length`
- **Description:** Calculate the shape length of geometries in a spatial data file.
- **Parameters:**
  - `long` (str): The longitude of the location.
  - `lat` (str): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
- **HTTP Method:** GET
- **Response:** A JSON representation of the calculated shape lengths.

#### 8. Shape Area
- **Endpoint:** `/spatial-analysis/shape-area`
- **Description:** Calculate the shape area of geometries in a spatial data file.
- **Parameters:**
  - `long` (str): The longitude of the location.
  - `lat` (str): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
- **HTTP Method:** GET
- **Response:** A JSON representation of the calculated shape areas.

#### 9. Detect CRS (Coordinate Reference System)
- **Endpoint:** `/spatial-analysis/detect-crs`
- **Description:** Detect the coordinate reference system (CRS) of a spatial data file.
- **Parameters:**
  - `long` (float): The longitude of the location.
  - `lat` (float): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
- **HTTP Method:** GET
- **Response:** The EPSG code specifying the CRS.

#### 10. DataFrame Description
- **Endpoint:** `/spatial-analysis/data-frame-description`
- **Description:** Generate a descriptive summary of a GeoDataFrame from a given file.
- **Parameters:**
  - `long` (float): The longitude of the location.
  - `lat` (float): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
- **HTTP Method:** GET
- **Response:** A JSON representation of the data frame description.

#### 11. Aggregate Columns
- **Endpoint:** `/spatial-analysis/aggregate-columns`
- **Description:** Aggregate and summarize specified columns of a GeoDataFrame from a given file.
- **Parameters:** A JSON request body with the following attributes:
  - `long` (str): The longitude of the location.
  - `lat` (str): The latitude of the location.
  - `file_path` (str): The path to the spatial data file.
  - `describe_options` (list[str]): List of description options (e.g., ['mean', 'max']).
  - `columns` (Optional[list[str]]): List of columns to aggregate (optional).
- **HTTP Method:** POST
- **Response:** A JSON representation of the aggregated data.

#### 12. Spatial Join
- **Endpoint:** `/spatial-analysis/spatial-join`
- **Description:** Perform a spatial join operation between two geographical datasets.
- **Parameters:**
  - `long` (str): The longitude of the location.
  - `lat` (str): The latitude of the location.
  - `file_path_one` (str): The path to the first spatial data file.
  - `file_path_two` (str): The path to the second spatial data file.
  - `join_direction` (str): The type of spatial join to perform ('inner', 'left', 'right', 'outer').
- **HTTP Method:** GET


- **Response:** A JSON representation of the result of the spatial join.

#### Running the API
- To run the API, execute the script with `uvicorn` on `http://127.0.0.1:8000`.