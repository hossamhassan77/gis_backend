from osgeo import gdal

def dem_to_hillshade(input_dem: str, output_hillshade: str):
    """Converts DEM to hillshade using GDAL Python API."""
    # Open the DEM file
    dem_dataset = gdal.Open(input_dem)
    if not dem_dataset:
        raise FileNotFoundError(f"Unable to open DEM file: {input_dem}")
    # Generate hillshade
    gdal.DEMProcessing(output_hillshade, dem_dataset, 'hillshade')
    print(f"Hillshade saved to {output_hillshade}")

if __name__ == "__main__":
    input_dem = r"D:\Data\DEM\GMTED2010N10E030_075\South_Sinai.tif"
    output_hillshade = r"D:\Data\DEM\GMTED2010N10E030_075\South_Sinai_hillshade.tif"

    dem_to_hillshade(input_dem, output_hillshade)
