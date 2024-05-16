import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

import os 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "application_default_credentials.json"

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

# # Sample function call for textGen function
generated_texts = textGen("what is the famous local items in africa list them")
print("Generated Texts:", generated_texts)