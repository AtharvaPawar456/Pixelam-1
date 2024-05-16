def textGen(text):
    import vertexai
    from vertexai.generative_models import GenerativeModel, Part, FinishReason
    import vertexai.preview.generative_models as generative_models

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

    return generated_texts


# Sample function call for textGen function
generated_texts = textGen("This is a sample text for generation.")
print("Generated Texts:")
for text in generated_texts:
    print(text)


'''

Sign in to the gcloud CLI
You are seeing this page because you ran the following command in the gcloud CLI from this or another machine. If this is not the case, close this tab.


gcloud auth application-default login --no-launch-browser



Enter the following authorization code in gcloud CLI on the machine you want to log into. This is a credential similar to your password and should not be shared with others.

4/0AdLIrYfmc8ku2MoGuKakuJAEgkYK-XFDpYzu-5b4DVUJpKWR1lAKBGIEkYlx76fNFmM4LQ

4/0AdLIrYfmc8ku2MoGuKakuJAEgkYK-XFDpYzu-5b4DVUJpKWR1lAKBGIEkYlx76fNFmM4LQ

4/0AdLIrYdx8QY2e9zEroWH3gb-vvkeuUy2FeA6ilc-_4s3kXFoj1n3jwNuTm0ftjBW1pAMdg
'''