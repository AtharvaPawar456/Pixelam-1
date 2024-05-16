# pip install geopy

from geopy.geocoders import Nominatim

def get_location_details(latitude, longitude):
    # Initialize Nominatim geocoder
    geolocator = Nominatim(user_agent="location-details")

    # Combine latitude and longitude into a single string
    location_str = f"{latitude}, {longitude}"

    # Try to reverse geocode the coordinates
    try:
        location = geolocator.reverse(location_str)

        # Extract location details from the result
        address = location.address if location else "Location details not found"
        return address
    except Exception as e:
        return f"Error: {str(e)}"

# Example coordinates
latitude = 19.0014635
longitude = 72.8375045

# Get location details
location_details = get_location_details(latitude, longitude)
print(location_details)


# Railway Colony Road, Railway Colony, F/S Ward, Zone 2, Mumbai, Mumbai City District, Maharashtra, 400013, India