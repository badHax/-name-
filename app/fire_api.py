import folium


class Mapping(object):
    #Kingston
    SF_COORDINATES = (18.0179, -76.8099)
    
    def make_general_map(self):
        map = folium.Map(location= self.SF_COORDINATES, zoom_start=13)
        try:
            map.save(path='maps/map.html')
            return True
        except Exception as ex:
            return False
    
    def make_path_map(self):
        pass
    
    def make_shaped_overlay(self):
        pass
