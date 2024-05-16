from gradio_client import Client, file

client = Client("Ghana-NLP/khaya-image-caption")
result = client.predict(
    # file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),  # filepath in 'parameter_5' Image component
    file('https://miro.medium.com/v2/resize:fit:460/0*yuztX2tq7yF4m3WB.jpg'),  # filepath in 'parameter_5' Image component
    "Twi",  
    api_name="/generate"  # Use the correct endpoint name here
)
# Literal['Twi', 'Amharic', 'Dagbani', 'Ewe', 'Ga', 'Gurene', 'Fante', 'Hausa', 'Kikuyu', 'Kimeru', 'Luo', 'Shona', 'Swahili', 'Tigrinya', 'Yoruba'] in 'Choose Language! (default is Twi)' Dropdown component

print(result)


'''
Loaded as API: https://ghana-nlp-khaya-image-caption.hf.space ✔
('a close up of a red bus on a white background', 'bɔs kɔkɔɔ bi a wɔabɛn ho a ɛwɔ akyi fitaa', 'C:\\Users\\Atharva Pawar\\AppData\\Local\\Temp\\gradio\\a8fbe02ca229ebd73542611c1142b16d150a528c\\image.PNG')
'''