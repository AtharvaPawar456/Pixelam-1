import requests

# Define the API endpoint
url = "https://translation-api.ghananlp.org/v1/translate"

# Define the request payload
payload = {
    "in": "Translation text",
    "lang": "en-tw"
}

# Make the POST request
response = requests.post(url, json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print("Response:", response.json())
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
