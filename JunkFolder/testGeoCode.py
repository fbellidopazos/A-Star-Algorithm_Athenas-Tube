from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="AStar-Athens")
location = geolocator.geocode("KAT Metro")
print(location)
print(location.address)
print((location.latitude, location.longitude))