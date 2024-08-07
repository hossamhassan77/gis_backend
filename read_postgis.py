"""

"""
import json
import os
import geopandas
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

class ReadDB:
    """Dealing with postgis tables."""

    def __init__(self) -> None:
        self.engine = create_engine(
            f"""
            postgresql://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}
            @{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}
            """
        )

    def read_postgis_table(self, table_name):
        """
        Reads data from a PostGIS table and returns it as a GeoJSON format.

        Returns:
            dict: A dictionary containing the data from the PostGIS table in GeoJSON format.

        Raises:
            ConnectionRefusedError: If there's an issue reading the data from the database.
        """
        try:
            geo_data_frame = geopandas.read_postgis(
                f"SELECT * FROM {table_name}",
                self.engine,
                geom_col="geometry",
            )
        except Exception as err:
            raise ConnectionRefusedError("Cant't read table from database.") from err
        return json.loads(geo_data_frame.to_json())
