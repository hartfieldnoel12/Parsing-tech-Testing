import requests
from bs4 import BeautifulSoup

url = "https://beltline.org/events/?event=fitness+and+wellness&location=northeast+trail"

response = requests.get(url)
html= BeautifulSoup(response.text, 'html.parser')

categories_html= html.find('section, {"class": RelatedEventCard_related-event-card__content__XESWg
