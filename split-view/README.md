# Split view
### Introduction
The SplitView class is designed to handle various aspects of spatial data manipulation, filtering, and visualization. It provides a range of methods that enable data reading, filtering, distribution analysis, and comparison between original and split views. This class is particularly useful for applications that involve geographic data and require insights into data distribution within specific map bounds.
### Installation 
- install `python 3.7+`.
- Install dependencies using pip: `pip install -r requirements.txt`.
## Endpoints

This README also provides documentation for FastAPI endpoints that utilize the SplitView class.

- `data_types`: Endpoint that returns unique values and numeric range for columns.
- `original_data_vis`: Endpoint for visualizing original dataset within map bounds.
- `filter_original_data`: Endpoint for filtering original data.
- `get_original_distribution`: Endpoint for generating data distribution information for the original view.
- `visualize_splitted_data`: Endpoint for visualizing original and splitted data within map bounds.
- `filter_split`: Endpoint for filtering and splitting data distributions.
- `distribute_splitted_data`: Endpoint for generating data distribution comparison between original and splitted views.
### Folders
1. src:
    - `split.py` python file contains utils functions.
    - `main.py` python file contains fastapi endpoints and to run server.
2. wakeb_mapdata:
Contains all data to be tested in endpoints.
3. And docs files [README.md, api_doc.md, requirements.txt].
4. postman collection for all endpoints.