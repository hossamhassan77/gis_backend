# Trend-analysis
### Introduction
The Trend Analysis API is designed to provide endpoints for conducting trend analysis using the TrendAnalysis class. This API allows users to analyze trends based on different data types, groupings, and time ranges.
### Installation 
- install `python 3.7+`.
- Install dependencies using pip: `pip install -r requirements.txt`.
### Endpoints
- `/dataType-validGrouping`
Endpoint that ensures which property should appear to the user in the trend analysis section.
- `/grouping-property-bydate`
Returns JSON containing values on the x-axis and y-axis to visualize as a graph, along with the average value of the specified numeric property column.
- `/time-range`
Returns one or two JSON objects depending on the number of ranges (1 or 2). Each object contains values on the x-axis and y-axis to visualize as graphs.
### Folders
1. src:
 - `trend.py` python file contains utils functions.
 - `main.py` python file contains fastapi endpoints and to run server.
2. wakeb_mapdata:
Contains all data to be tested in endpoints.
3. And docs files [README.md, API_DOCS.md, requirements.txt].