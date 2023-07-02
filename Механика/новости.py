import requests
from bs4 import BeautifulSoup

def свежие_ноавости():
  response = requests.get("https://kun.uz")
  soup = BeautifulSoup(response.content, "html.parser")


  paragraphs = soup.find_all("main")
  for paragraph in paragraphs:
    print(paragraph.text)
  return
свежие_ноавости()