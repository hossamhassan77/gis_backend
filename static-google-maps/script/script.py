from database_collector import StaticMaps
bound = [{"lat": 29.958648180974592, "lng": 32.56177935865722},  {"lat": 29.96423081250812, "lng": 32.55209629511779}, {"lat": 29.96027773825908, "lng": 32.54304019252879}, {"lat": 29.95475524155053, "lng": 32.53889528403536}, {"lat": 29.958648180974592, "lng": 32.56177935865722}]
imgs_number = 2
altitude = 150
c = StaticMaps(bound, imgs_number, altitude)
zoom = c.calculate_zoom_level()
polygon = c.generate_polygon_from_listOf_points()
points = c.random_points_in_polygon(polygon.iloc[0].geometry)
c.save_static_imgs(points, zoom)