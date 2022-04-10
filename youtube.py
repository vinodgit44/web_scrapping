from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.youtube.com/").text
soup = BeautifulSoup(html_text, "lxml")


title= soup.findAll("id" , id="video-title-link")
print(title)
