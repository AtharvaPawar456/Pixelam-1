import pandas as pd

# Load the CSV file
df = pd.read_csv('final_tour_places.csv')

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Save the JSON data to a file
with open('data.json', 'w') as json_file:
    json_file.write(json_data)
