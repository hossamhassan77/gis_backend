### we want to get :
- hillshade.
- landcover.
- contour lines.

### Hillshade: 
Hillshade is a representation of the three-dimensional terrain using shadows to simulate the effect of light falling on the landscape. It is typically derived from digital elevation models (DEMs) or digital terrain models (DTMs).
### Landcover data:
refers to the physical coverage and distribution of different types of land surfaces or features on the Earth's surface. It is often obtained through remote sensing techniques, such as satellite imagery or aerial photography.
### Contour lines:
Represent lines of equal elevation on a map, connecting points of the same elevation. Contour lines represent lines of equal elevation on a map, connecting points of the same elevation. 

### Hillshade refs:
- [What to concern](https://pro.arcgis.com/en/pro-app/3.0/help/analysis/raster-functions/hillshade-function.htm)
- [GDAL: Tools to analyze and visualize DEMs.](https://gdal.org/programs/gdaldem.html)
- [Azimuth & Elevation](https://observablehq.com/@sahilchinoy/hillshader)
### Scenarios:
1. User upload the DEM then we return hillshade.
2. From given one geographic point (lat,lng), We download Digital Elevation Model then return hillshade.
3. Draw a polygon, download DEM, make hillshade, then clip hillshade as user's polygon.

### Solution:
- For the first scenario it's done with GDAL package with minimum time(0.5 sec) for each DEM 3600x3600 pixels.
- For the second and third scenarios, we need to search for DEMs providers such as 'USGS', 'Landsat', and 'Sentinel'.
    - We found [EODAG - Earth Observation Data Access Gateway](https://eodag.readthedocs.io/en/latest/getting_started_guide/overview.html), This library allows to search, aggregate results, and download data not only from USGS, but also from many other data providers.
