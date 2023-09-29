## Trend Analysis API Documentation

This API provides endpoints for trend analysis using the `TrendAnalysis` class.

### `GET /trend-analysis/dataType-validGrouping`
Endpoint that ensures which property should appear to the user in the trend analysis section.

#### Parameters
| Parameter        | Type | Description                                        |
|------------------|------|----------------------------------------------------|
| `espg`           | int  | The EPSG code for the coordinate system.           |
| `file_path`      | str  | Path to the data file.                             |
| `long`           | str  | Longitude information.                             |
| `lat`            | str  | Latitude information.                              |
| `time`           | str  | Time information.                                  |

#### Response

- **200 OK**: Successful response containing a JSON object with two fields:
  - `dataTypes` (list): List of data types.
  - `valid_grouping` (list): List of valid grouping options.

### `GET /trend-analysis/grouping-property-bydate`

Returns JSON containing values on the x-axis and y-axis to visualize as a graph, along with the average value of the specified numeric property column.

#### Parameters

| Parameter        | Type | Description                                        |
|------------------|------|----------------------------------------------------|
| `espg`           | int  | The EPSG code for the coordinate system.           |
| `file_path`      | str  | Path to the data file.                             |
| `long`           | str  | Longitude information.                             |
| `lat`            | str  | Latitude information.                              |
| `time`           | str  | Time information.                                  |
| `grouping`       | str  | Grouping parameter.                                |
| `property_column`| str  | Numeric property column.                           |

#### Response

- **200 OK**: Successful response containing a JSON object with the data for graph visualization.

### `GET /trend-analysis/time-range`
Returns one or two JSON objects depending on the number of ranges (1 or 2). Each object contains values on the x-axis and y-axis to visualize as graphs.

#### Parameters
| Parameter        | Type | Description                                        |
|------------------|------|----------------------------------------------------|
| `espg`           | int  | The EPSG code for the coordinate system.           |
| `file_path`      | str  | Path to the data file.                             |
| `long`           | str  | Longitude information.                             |
| `lat`            | str  | Latitude information.                              |
| `time`           | str  | Time information.                                  |
| `grouping`       | str  | Grouping parameter.                                |
| `property_column`| str  | Numeric property column.                           |
| `time_range`     | str  | Time range parameter.                              |
| `number_of_ranges`| int | Number of ranges (1 or 2).                         |

#### Response

- **200 OK**: Successful response containing one or two JSON objects with data for graph visualization.