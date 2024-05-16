import requests, re, json, time, random, os, base64, io
from geopy.geocoders import Nominatim


from PIL import Image

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models
import os 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "application_default_credentials.json"
def textSummary(text):
    # Initialize the parser with your text
    text = text.replace('*', '').replace('$', '').replace('#', '')

    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Initialize the LexRank summarizer
    summarizer_lex = LexRankSummarizer()

    # Summarize using LexRank
    summary = summarizer_lex(parser.document, 6)

    # Concatenate the summary sentences into a string
    lex_summary = ""
    for sentence in summary:
        lex_summary += str(sentence) + " "
    
    return lex_summary


from PIL import Image
import io
import base64

def create_2x2_grid_from_base64(image_data_list):
    # Open images from base64 data
    images = [Image.open(io.BytesIO(base64.b64decode(img_data))) for img_data in image_data_list]

    # Calculate the dimensions of the grid
    max_width = max(img.size[0] for img in images)
    max_height = max(img.size[1] for img in images)
    grid_width = 2 * max_width
    grid_height = 2 * max_height

    # Create a blank image for the grid
    grid = Image.new('RGB', (grid_width, grid_height), color=(255, 255, 255))

    # Paste images onto the grid
    for i in range(2):
        for j in range(2):
            idx = i * 2 + j
            if idx < len(images):
                img = images[idx]
                img_width, img_height = img.size

                # Calculate maximum scale factor to fit the image within the grid cell
                scale_factor = min(max_width / img_width, max_height / img_height)

                # Resize the image
                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)
                resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

                # Calculate offsets to center the image
                x_offset = max_width * j + (max_width - new_width) // 2
                y_offset = max_height * i + (max_height - new_height) // 2

                grid.paste(resized_img, (x_offset, y_offset))

    return grid





def translate(text, source, target):
    url = "https://translation-backend-nlpghana-staging.azurewebsites.net/v1/translate"

    # Language codes
    languages = {
        'English': 'en',
        'Yoruba': 'yo',
        'Fante': 'fat',
        'Kimeru': 'mer',
        'Twi': 'tw',
        'Kikuyu': 'ki',

        'Ewe': 'ee',
        'Ga': 'gaa',
        'Dagbani': 'dag',
        'Gurene': 'gur',
        'Luo': 'luo',
    }

    def translate_chunk(chunk):
        data = {
            "source_language": languages[source],
            "target_language": languages[target],
            "text": chunk
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data, headers=headers)
        print("------")

        if response.status_code == 200:
            return response.json().get('message', 'Failed to get message from response')
        else:
            return "Failed to translate ..."

    # Split text into chunks of 20 words
    words = text.split()
    if len(words) > 20:
        chunks = [' '.join(words[i:i + 20]) for i in range(0, len(words), 20)]
    else:
        chunks = [text]

    translated_chunks = [translate_chunk(chunk) for chunk in chunks]
    translated_text = ' '.join(translated_chunks)

    return translated_text


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
    






def textGen(text):

    vertexai.init(project="glassy-chalice-421910-c8", location="us-central1")
    model = GenerativeModel("gemini-1.5-pro-preview-0409")

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    responses = model.generate_content(
        [text],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    generated_texts = []
    for response in responses:
        generated_texts.append(response.text)
    joined_text = "\n".join(generated_texts)

    return joined_text

def vertexAIGen(prompt):
    try:
        llmresp_text = textGen(prompt)

    except requests.RequestException as e:
        llmresp_text = f"Error: A problem occurred with the request - {e}"
    except json.decoder.JSONDecodeError:
        llmresp_text = "Error: Unable to parse response JSON"
    except Exception as e:
        llmresp_text = f"An unexpected error occurred: {e}"

    return llmresp_text


# Colab API Code
# old
# def vertexAIGen(prompt, VertexAIdomainUrl):
#     try:
#         # URL of the Flask API endpoint
#         url = f"{VertexAIdomainUrl}api/text"

#         # Make a POST request to the API endpoint
#         response = requests.post(url, data=prompt)

#         # Raise an exception if the request was unsuccessful
#         response.raise_for_status()

#         # Parse the response
#         llmresp_text = response.json().get('text', "Error: 'text' key not found in the response")

#     except requests.RequestException as e:
#         llmresp_text = f"Error: A problem occurred with the request - {e}"
#     except json.decoder.JSONDecodeError:
#         llmresp_text = "Error: Unable to parse response JSON"
#     except Exception as e:
#         llmresp_text = f"An unexpected error occurred: {e}"

#     return llmresp_text


# --------------------------------------------------------------------------------------

def generate_text_from_image_and_prompt(base64_encoded, prompt):
    # Convert image to base64
    # with open(image_path, "rb") as img_file:
        # img_binary = img_file.read()
        # base64_encoded = base64.b64encode(img_binary).decode("utf-8")

    # Initialize Vertex AI
    vertexai.init(project="glassy-chalice-421910-c8", location="us-central1")

    # Initialize the generative model
    model = GenerativeModel("gemini-1.5-pro-preview-0409")

    # Create Part object from base64 image data
    image_part = Part.from_data(
        mime_type="image/jpeg",
        data=base64.b64decode(base64_encoded)
    )

    # Define generation configuration
    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    # Define safety settings
    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    # Generate content
    responses = model.generate_content(
        [image_part, prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    # Accumulate the generated text
    generated_text = ""
    for response in responses:
        generated_text += response.text

    return generated_text


def Vertex_Img_text_2_text(userimage_base64, text_prompt):
    try:
        responText = generate_text_from_image_and_prompt(userimage_base64, text_prompt)
        return responText

    except FileNotFoundError:
        return "Error: The specified image file was not found."
    except requests.RequestException as e:
        return f"Error: A problem occurred with the request - {e}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# old
# def Vertex_Img_text_2_text(userimage_base64, text_prompt, VertexAIdomainUrl):
#     try:
#         # Define the API endpoint
#         url = f'{VertexAIdomainUrl}upload'

#         # Read the image file and convert it to base64
#         # with open(image_path, "rb") as img_file:
#         #     base64_img = base64.b64encode(img_file.read()).decode("utf-8")

#         # Prepare the data payload
#         payload = {'image_base64': userimage_base64, 'text_prompt': text_prompt}

#         # Make the POST request
#         response = requests.post(url, data=payload)
        
#         # Raise an exception if the request was unsuccessful
#         response.raise_for_status()

#         # Parse the response
#         response_data = response.json()

#         # Check if the response contains the expected key
#         if 'llm_resp' in response_data:
#             return response_data['llm_resp']
#         else:
#             raise ValueError("Response JSON does not contain 'llm_resp' key")

#     except FileNotFoundError:
#         return "Error: The specified image file was not found."
#     except requests.RequestException as e:
#         return f"Error: A problem occurred with the request - {e}"
#     except ValueError as e:
#         return f"Error: {e}"
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

def upScaleAPI(userimage_base64, text_prompt, VertexAIdomainUrl):
    # API endpoint URL
    api_url = f'{VertexAIdomainUrl}imgpromptupload'

    # Read the image file and convert it to base64
    # with open(image_path, "rb") as img_file:
    #     base64_img = base64.b64encode(img_file.read()).decode("utf-8")

    # Payload data
    payload = {'image_base64': userimage_base64, 'text_prompt': text_prompt}

    # Send POST request to the API endpoint
    response = requests.post(api_url, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the returned image
        # with open('upscaled_image.jpg', 'wb') as f:
        #     f.write(response.content)
        # print("Image saved successfully.")
        return response
    else:
        print("Failed to retrieve the upscaled image.")


# def imgGen(text_prompt, VertexAIdomainUrl):
def imgGen(prompt, VertexAIdomainUrl):
    try:
        # URL of the Flask API endpoint
        url = f"{VertexAIdomainUrl}imggen"

        # Make a POST request to the API endpoint
        response = requests.post(url, data=prompt)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the response
        llmresp_text = response.json().get('imgbase64', "Error: 'text' key not found in the response")

    except requests.RequestException as e:
        llmresp_text = f"Error: A problem occurred with the request - {e}"
    except json.decoder.JSONDecodeError:
        llmresp_text = "Error: Unable to parse response JSON"
    except Exception as e:
        llmresp_text = f"An unexpected error occurred: {e}"

    return llmresp_text








'''
Old code:


# def vertexAIGen(prompt):
#     # URL of the Flask API endpoint
#     url = f"{VertexAIdomainUrl}api/text"

#     # Make a POST request to the API endpoint
#     response = requests.post(url, data=prompt)

#     # Print the response from the API
#     # print(f"Response from the API: \n {response.json()}", )

#     try:
#         llmresp_text = response.json()['text']
#     except json.decoder.JSONDecodeError:
#         llmresp_text = "Error: Unable to parse response JSON"
#     return llmresp_text



# def Vertex_Img_text_2_text(image_path, text_prompt):
#     # Define the API endpoint
#     url = f'{VertexAIdomainUrl}upload'

#     # Read the image file and convert it to base64
#     with open(image_path, "rb") as img_file:
#         base64_img = base64.b64encode(img_file.read()).decode("utf-8")

#     # Make the POST request
#     response = requests.post(url, data={'image_base64': base64_img, 'text_prompt': text_prompt})

#     # Return the response
#     return response.json()['llm_resp']

'''