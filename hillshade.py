import os
import subprocess
import random
import string

def dem_hillshade(input_dem: str) -> dict:
    """Converts DEM to hillshade using GDAL cmd."""
    if not os.path.exists('raster_analysis_output'):
        os.mkdir('raster_analysis_output')
    file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    try:
        command = f'gdaldem hillshade {input_dem} raster_analysis_output/{file_name}.tif'
        subprocess.run(command, shell=True, check=False)
        return {"status": f"Output saved in Raster_analysis_output\\{file_name}.tif"}
    except Exception as e:
        raise ValueError("Entity not processable.") from e

if __name__ == "__main__":
    print(dem_hillshade(r"D:\Data\DEM\GMTED2010N10E030_075\South_Sinai.tif"))