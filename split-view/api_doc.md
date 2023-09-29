# Split view API Documentation
## Endpoint: /split-view/data-type
### Method: `GET`
#### Description: Endpoint that returns unique values for object dtypes and (min,max) for numeric dtypes.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - file_path (str): The path to the input data file.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - time_column (Optional[str]): Optional column name for time-related data.
Response: A JSON representation of unique values for object dtypes and (min,max) for numeric dtypes.
## Endpoint: /split-view/original-data
### Method: `POST`
#### Description: Dataset intersection with map bound to visualize in the split view section.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - file_path (str): The path to the input data file.
  - map_bound (dict): A dictionary representing the map bounds with keys "south", "west", "north", and "east".
Response: A JSON representation of the GeoDataFrame containing the original data.

## Endpoint: /split-view/filter-original-data
### Method: `POST`
#### Description: Filters data for visualization.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - file_path (str): The path to the input data file.
  - map_bound (dict): A dictionary representing the map bounds with keys "south", "west", "north", and "east".
  - filter_query (Optional[list]): An optional list of dictionaries specifying filter conditions for the splitted view.
  - filter_option (str): Filter option for the original view, either "include", "exclude", or "clear_all".
Response: A JSON representation of the filtered GeoDataFrame.

## Endpoint: /split-view/original-data-distribution
### Method: `POST`
#### Description: Generate data distribution information and charts.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - file_path (str): The path to the input data file.
  - map_bound (dict): A dictionary representing the map bounds with keys "south", "west", "north", and "east".
  - time_column (Optional[str]): Optional column name for time-related data.
Response: A JSON representation of data distribution information and charts.

## Endpoint: /split-view/split-view-visualization
### Method: `POST`
#### Description: Returns original data and splitted data in JSON format to be visualized in the split view section.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - file_path (str): The path to the input data file.
  - original_map_bound (dict): A dictionary representing the original map bounds with keys "south", "west", "north", and "east".
  - splitted_map_bound (dict): A dictionary representing the splitted map bounds with keys "south", "west", "north", and "east".
Response: A JSON representation containing Original_data and Splitted_data.

## Endpoint: /split-view/split-view-filter
### Method: `POST`
#### Description: Filtering and splitting data distributions.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - file_path (str): The path to the input data file.
  - original_map_bound (dict): A dictionary representing the original map bounds with keys "south", "west", "north", and "east".
  - splitted_map_bound (dict): A dictionary representing the splitted map bounds with keys "south", "west", "north", and "east".
  - original_filter_query (Optional[list]): An optional list of dictionaries specifying filter conditions for the original view.
  - splitted_filter_query (Optional[list]): An optional list of dictionaries specifying filter conditions for the splitted view.
  - original_filter_option (str): Filter option for the original view, either "include", "exclude", or "clear_all".
  - splitted_filter_option (str): Filter option for the splitted view, either "include", "exclude", or "clear_all".
Response: A JSON representation containing Original and Splitted filtered data.

## Endpoint: /split-view/split-view-distribution
### Method: `POST`
#### Description: Generate data distribution comparison between original and splitted views in JSON format.
### Request Body:
- JSON object with the following attributes:
  - espg (int): The EPSG code for the coordinate system.
  - long (str): The column name for longitude data.
  - lat (str): The column name for latitude data.
  - file_path (str): The path to the input data file.
  - original_map_bound (dict): A dictionary representing the original map bounds with keys "south", "west", "north", and "east".
  - splitted_map_bound (dict): A dictionary representing the splitted map bounds with keys "south", "west", "north", and "east".
  - time_column (Optional[str]): Optional column name for time-related data.
Response: A JSON representation of data distribution comparison between original and splitted views.
