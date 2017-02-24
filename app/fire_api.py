import folium

# contains methods for generating maps in a web view (iframe)
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
    
    # for shading a general area
    def make_shaped_overlay(self):
        pass
    
    def make_path(self):
        pass

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

