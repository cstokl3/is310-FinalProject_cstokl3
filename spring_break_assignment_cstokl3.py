import bs4
from bs4 import BeautifulSoup
import requests

#I saved the raw_script_urls.txt file directly into the same folder and directory as this python script
urls = open('C:/Users/bake9/Desktop/is310/cstokl3/is310-FinalProject_cstokl3/is310-assignments/raw_script_urls.txt', 'r', encoding='ISO-8859-1')

#Create empty dictionaries to later add the scraped links and text to.
link = []
dictionary_text = {}
dictionary_text['Text'] = []

#Use the ' +++$++ ' visible in the text file as the marker to split the rows into three different columns, the last 'split' would contain the links. Use strip to clean the links up and remove any spaces/addtional characters. 
for text in urls:
    fixed = text.split(' +++$+++ ')
    link.append((fixed[2].strip()))
    print(link)
    
#The function used to get the text inside the links.
def Url(text):
    response = requests.get(text)
    soup = BeautifulSoup(response.text, features='html.parser')
    lines = soup.find_all('pre')

    for line in lines:
        line = lines.get_text()
        dictionary_text[line[0]] = lines
# Check to make sure that there are no errors occuring during the scrape, these lines of code in the function will make sure we only get 200 response codes, ensuring that is it okay. 
    if response.status_code == requests.codes.ok: 
      return response.text

#I used 50 in the loop, since any higher took quite long in my terminal.
for add in text[0:50]:
    Url(add)

print(dictionary_text)

#From add, the new file should now contain the text we were looking for in the links.
new_file = open('new_raw_scripts_urls.txt', 'w+')
new_file.writelines(str(dictionary_text))
new_file.close()


