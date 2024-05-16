import re

data = "sudehfbseb edfsjuehjbrf drsjrubesjnw ff drsubdf v https://miro.medium.com/v2/resize:fit:460/0*yuztX2tq7yF4m3WB.jpg "

# Extract URLs ending with .jpg, .png, or .jpeg
urls = re.findall(r'\bhttps?://\S+?\.(?:jpg|png|jpeg)\b', data)

print(urls)
