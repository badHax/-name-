import folium

SF_COORDINATES = (18.1096, -76.2975)
"""
crimedata = pd.read_csv('SFPD_Incidents_-_Current_Year__2015_.csv')

# for speed purposes
MAX_RECORDS = 1000
"""
def make_map():
    map = folium.Map(location=SF_COORDINATES, zoom_start=8)
    
    try:
        map.create_map(path='templates/mapping.html')
        return True
    except Exception as ex:
        return False
    
"""
# add a marker for every record in the filtered data, use a clustered view
for each in crimedata[0:MAX_RECORDS].iterrows():
    map.simple_marker(
        location = [each[1]['Y'],each[1]['X']],
	    clustered_marker = True)
"""
