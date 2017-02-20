import folium

#Kingston
SF_COORDINATES = (18.0179, -76.8099)

def make_normal_map():
    map = folium.Map(location=SF_COORDINATES, zoom_start=13)
    try:
        map.create_map(path='templates/mapping.html')
        return True
    except Exception as ex:
        return False


if __name__ == "__main__":
    make_normal_map()

