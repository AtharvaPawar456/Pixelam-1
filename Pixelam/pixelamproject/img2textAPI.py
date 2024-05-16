import requests
import base64

import markdown


domain = "https://aa54-34-125-88-132.ngrok-free.app/"

def send_image_and_prompt_to_api(image_path, text_prompt, domain):
    # Define the API endpoint
    url = f'{domain}upload'

    # Read the image file and convert it to base64
    with open(image_path, "rb") as img_file:
        base64_img = base64.b64encode(img_file.read()).decode("utf-8")

    # Make the POST request
    response = requests.post(url, data={'image_base64': base64_img, 'text_prompt': text_prompt})

    # Return the response
    return response.json()

# Example usage:
# image_path = "hmp----.jpeg"
# image_path = "data.jpeg"
image_path = "C:/Users/Atharva Pawar/Documents/GitHub/Pixelam/pixelamproject/pixelapp/static/pixelapp/uploaded_files/11_05_24_02_18_25_sampledata.jpeg"

# with open(image_path, "rb") as img_file:
#     base64_img = base64.b64encode(img_file.read()).decode("utf-8")
# print("base64_img: ", base64_img)
# text_prompt = "read all the text from this image"
text_prompt = "count people in this image, only retun count"
api_response = send_image_and_prompt_to_api(image_path, text_prompt, domain)
print(api_response)
print(markdown.markdown(api_response['llm_resp']))



'''

doctordataset = {
"dadar" : [
    "Dr. Saidu Mukesh Kota" : {
        "phone" : "09004461881"
        "link" : "https://www.google.com/maps/place/Dr.+Saidu+Mukesh+Kota/@19.0180404,72.8476603,17z/data=!3m1!4b1!4m6!3m5!1s0x3be7cff322a04b67:0x764cc3bc6e424361!8m2!3d19.0180404!4d72.8476603!16s%2Fg%2F11t3g_y8mn?authuser=0&hl=en&entry=ttu"
    }
]
}


Dr J K Mandot
02224113094
https://maps.app.goo.gl/Yu2C1b3eAcTftH3B9
5/A, Vissanji Park, Naigaum Cross Road, Near Dadar C Railway Station, Dadar, Dadar, Mumbai, Maharashtra 400014

------------------------------

Dr Kulkarni Ulhas Yashwant
02224143865
https://maps.app.goo.gl/1XeKxsGLdyEdck8L9
173, Hindu Colony, Sir Bhalchandra Road, Dadar East, Mumbai, Maharashtra 400014

------------------------------

Doctor Mankar
Civic Centre, opposite to Rastriya hotel, Dadar East, Dadar, Mumbai, Maharashtra 400014
https://maps.app.goo.gl/Z9XZV4yFrHvoBr9XA
------------------------------
------------------------------














'''