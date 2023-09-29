from google_map_api import item
import pandas 
import unittest

class TestMyFunction(unittest.TestCase):
    def test_returns_generate_polygon_from_listof_points(self):
        result = item.generate_polygon_from_listof_points([{"lat":40.38427119123016,"lng":-105.18831674093013},{"lat":40.35078901802308,"lng":-104.38631478780513},{"lat":39.84234491122627,"lng":-104.50167123311763},{"lat":39.93507177126157,"lng":-105.61129037374263},{"lat":40.44700542822942,"lng":-105.52889291280513}])
        self.assertIsInstance(result, pandas.DataFrame)

    def test_returns_calculate_zoom_level(self):
        result = item.calculate_zoom_level(200)
        self.assertEqual(result, 20)

    def test_returns_save_googleMaps_imgs(self):
        result = item.save_googleMaps_imgs(23.3333, 25.669, 23.3343, 25.663, 'east', 20)
        self.assertTrue(result)
    
    def test_returns_random_points_in_polygon(self):
        result = item.random_points_in_polygon(5, item.generate_polygon_from_listof_points([{"lat":40.38427119123016,"lng":-105.18831674093013},{"lat":40.35078901802308,"lng":-104.38631478780513},{"lat":39.84234491122627,"lng":-104.50167123311763},{"lat":39.93507177126157,"lng":-105.61129037374263},{"lat":40.44700542822942,"lng":-105.52889291280513}]).iloc[0].geometry)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()

""" To run specific function
python GIS\GoogleMaps_API\test.py TestMyFunction.{function name}
"""