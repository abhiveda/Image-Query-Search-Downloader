from geopy.geocoders import Nominatim

# Create a geocoder instance
geolocator = Nominatim(user_agent='my_geocoder')

# Define a list of locations
locations = ["Amer Fort Jaipur", "Lotus Temple", "Basilica of Bom Jesu", "Qutub Minar", "Bara Imambara Lucknow", "Brihadisvara Temple", "Dilwara Temples", "Sanchi Stupa",
           "Elephanta Caves", "Fatehpur Sikri", "Gingee Fort Villupuram", "Golconda Fort Hyderabad"]

# Initialize an empty list to store the latitude and longitude values
lat_lng_list = []

# Geocode each location
for location in locations:
    try:
        # Geocode the location
        location_data = geolocator.geocode(location)

        # Extract latitude and longitude
        latitude = location_data.latitude
        longitude = location_data.longitude

        # Append the latitude and longitude to the list
        lat_lng_list.append((latitude, longitude))

        print(f'Location: {location}')
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
        print('---')

    except AttributeError:
        print(f'Error: Failed to geocode {location}')
        print('---')

# Print the list of latitude and longitude values
print('Latitude and Longitude values:')
for i, (lat, lng) in enumerate(lat_lng_list):
    print(f'Location {i + 1}: Latitude={lat}, Longitude={lng}')
