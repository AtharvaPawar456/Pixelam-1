import markdown
import requests

VertexAIdomainUrl = "https://b2ca-34-125-88-132.ngrok-free.app/"

def vertexAIGen(prompt):
    # URL of the Flask API endpoint
    url = f"{VertexAIdomainUrl}api/text"

    # Make a POST request to the API endpoint
    response = requests.post(url, data=prompt)

    # Print the response from the API
    print(f"Response from the API: \n {response.json()}", )
    return response.json()['text']

prompt = "what is the famous local items in africa list them"
resp = vertexAIGen(prompt)
print("prompt:", prompt)
print("resp: ", markdown.markdown(resp))
