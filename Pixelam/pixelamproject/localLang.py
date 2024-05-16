import requests

def translate(text, source, target):
    url = "https://translation-backend-nlpghana-staging.azurewebsites.net/v1/translate"

    # Language codes
    languages = {
        'English': 'en',
        'Twi': 'tw',
        'Ewe': 'ee',
        'Ga': 'gaa',
        'Fante': 'fat',
        'Yoruba': 'yo',
        'Dagbani': 'dag',
        'Kikuyu': 'ki',
        'Gurene': 'gur',
        'Luo': 'luo',
        'Kimeru': 'mer'
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

# Example usage
text = """
## A Brief Overview of Indian History

Indian history is a tapestry of diverse cultures, traditions, and empires. The ancient Indus Valley Civilization (c. 3300–1300 BCE) marked the subcontinent's early urban development. Vedic traditions followed, laying the foundation for Hinduism. The Maurya Empire (c. 322–185 BCE) unified much of India under Ashoka's rule, promoting Buddhism. The Gupta Empire (c. 320–550 CE) is considered a golden age of art, science, and literature. Later, the Mughal Empire (1526–1857) brought architectural marvels and cultural fusion. British colonial rule (1858–1947) led to significant socio-political changes, culminating in India's independence in 1947.
"""

trans = translate(text, 'English', 'Yoruba')  # Translating from English to Yoruba
print(trans)
print(translate(trans, 'Yoruba', 'English'))  # Translating from Yoruba to English





'''
200
{'type': 'Success', 'message': 'Ẹ ǹlẹ́, báwo lẹ ṣe'}
Ẹ ǹlẹ́, báwo lẹ ṣe

200
{'type': 'Success', 'message': 'Hello, how are you?'}
Hello, how are you?
'''