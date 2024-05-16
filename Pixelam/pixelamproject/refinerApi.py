import requests
import base64

domain = "https://fd28-34-69-150-193.ngrok-free.app/"

def call_flask_api(image_path, text_prompt):
    # API endpoint URL
    api_url = f'{domain}imgpromptupload'

    # Read the image file and convert it to base64
    with open(image_path, "rb") as img_file:
        base64_img = base64.b64encode(img_file.read()).decode("utf-8")

    # Payload data
    payload = {'image_base64': base64_img, 'text_prompt': text_prompt}

    # Send POST request to the API endpoint
    response = requests.post(api_url, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the returned image
        with open('upscaled_image.jpg', 'wb') as f:
            f.write(response.content)
        # print("Image saved successfully.")
        return image_path
    else:
        print("Failed to retrieve the upscaled image.")

# Example usage
image_path = 'cat.png'
text_prompt = 'a white cat'
call_flask_api(image_path, text_prompt)
