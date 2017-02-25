import folium       #leaflet mapping library
import pyperclip    #copying and pasting to clipboard
import io           #io
import database     #db interface

db = database.Database()

"""
# contains methods for generating maps in a web view (iframe)
#
#
# Dependencies
#
# Jinja2
#
# Pandas (Map Data Binding only)
#
# Numpy (Map Data Binding only)
#
# Vincent (Map Data Binding only)
#
#
"""
class Mapping(object):
    
    #Kingston
    SF_COORDINATES = (18.0179, -76.8099)
    
    #area is a list with two elements - lat and lng
    def make_general_map(self, name_of_map, coordinates=SF_COORDINATES, tiles='Stamen Toner'):
        mp = folium.Map(location = coordinates, zoom_start=14, tiles=tiles)
        try:
            mp.save('app/maps/'+name_of_map +'.html')
            return True
        except Exception as ex:
            print ex
            return False
            
    def show_stations(self, map):
        stations = db.get_stations()
    
    def map_to_iframe(self, map_file):
        return "<iframe src='app/maps/"+ map_file +".html'></iframe>"
        
    def make_point_on_map(self, map, lat, lng):
        folium.Marker(location=[lat, lng], popup='Fire Hydrant').add_to(map)
        
    def make_path_map(self):
        pass
    
    # for shading a general area
    # *** area is a list with latitude and logitude
    def make_shaped_overlay(self, area, map, name = 'place title'):
        folium.CircleMarker(location=area, radius=50,
                    popup=name, color='#ff0000',
                    fill_color='#ff0000').add_to(map)
    
    def make_path(self):
        pass

"""
# contains method for alerting the best possible station
# reroutes if criteria is not met
# criteria may include:
#
#   +   truck may not have water(due to a drought or something) but may still be able to
#       to respond due to a water source (hydrant) being close.
#
#   +   Elevation of of the fire may require trucks  with more suitable pumps
#
#   +   Depending on what is burning there would be an escalation of the fire:
#           -- May require deploying trucks from multiple stations
#           -- irrespective of certain criteria that would otherwise cause the issue to be
#               passed to another station
"""
class Deploy(object):
    #best available
    def dispatch_from_best_station(self):
        pass
    
    def dispatch_next_best(self):
        pass


#  a map as an object
class Mapof():
    pass


# a hydrant as an object
class Hydrant(object):
    pass


# a truck as an object
class Truck(object):
    pass


# an alert as an object
#
# based on what is burning there is a code for the weight of the alert
#
class Alert(object):
    pass


# an incident report as an object
class IncidentReport(object):
    pass

"""
class handles data that from reports from previous reports (mainly analytical purposes)

*   make predictive reports
*   custom graphical reports
"""
class Analytics():
    pass
