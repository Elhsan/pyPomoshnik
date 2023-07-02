import requests
from bs4 import BeautifulSoup

def get_news():
  response = requests.get("https://kun.uz/ru/news/2023/05/22/zelenskiy-putin-i-prigojin-vyskazalis-o-situatsii-v-baxmute")
  soup = BeautifulSoup(response.content, "html.parser")


  paragraphs = soup.find_all("div", class_="single-layout__center slc")
  for paragraph in paragraphs:
    print(paragraph.text)
  return
