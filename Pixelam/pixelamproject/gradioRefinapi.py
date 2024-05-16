from gradio_client import Client
import base64

client = Client("atharvapawar/imgRefine")

# Function to convert image to base64
def image_to_base64(filepath):
    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

image_path = 'cat.png'
base64_image = image_to_base64(image_path)

result = client.predict(
    base64_image,  # Upload the base64 encoded image text
    "a white cat",  # Prompt
    api_name="/handle_upload"
)

print(result)
