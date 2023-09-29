# static-google-map-and-similarity
This is a python web API project for **Comparing images captured with drones to static Google satellite maps**, the project provides endpoints to collect data from Google maps with variance methods and end point to respond with the most similar google satellite to drone image.
 
## Folders:
#### 1. GoogleMaps_API:
This folder contains various types of documents such as markdown file, Python file, and folder for some images, this contains web API endpoints that downloads static Google satellite maps for a specific geographic point [Latitude, Longitude], or a number of static snaps of the map previously mentioned in map bound.

#### 2. Similarity_of_images:
Contains web API endpoints that compares images captured with drones and the produced images of `GoogleMaps_API` endpoints.
## Other Files:
#### 1. Postman collection for all branch endpoints with example for each of them.
#### 2. Retirements.txt: contains all required python packages to be install before running main.py.
- _Import the JSON file in postman platform._ 

## Getting started:
#### Perquisites:
* `Python 3.6+`
* The endpoints in folder **Similarity_of_images** is depend on **GoogleMaps_API**.

#### Installing:
1. Clone the repository.
2. Install dependencies using pip: `pip install -r requirement.txt.
3. Start the server `main.py`.

#### Running tests: 
* Run `python test.py` to execute the test suite.