import re

def extract_lat_long(text):
    # Define the regex pattern to match latitude and longitude
    pattern = r'Latitude:\s*(-?\d+\.\d+),\s*Longitude:\s*(-?\d+\.\d+)'

    # Search for the pattern in the text
    match = re.search(pattern, text)

    # If the pattern is found, extract latitude and longitude
    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return latitude, longitude
    else:
        return None, None  # Return None for latitude and longitude if pattern not found

# Example text
text = "Latitude: 19.0014635, Longitude: 72.8375045"

# Extract latitude and longitude
latitude, longitude = extract_lat_long(text)
print("Latitude:", latitude)
print("Longitude:", longitude)
