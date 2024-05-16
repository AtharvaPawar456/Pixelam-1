# pip install markdown
import markdown

data = markdown.markdown('''
# To Do
## At Home
* Wash dishes
## At Work
* Finish Report
''')

# print(markdown.markdown('## Work Tasks'))
print(data)

