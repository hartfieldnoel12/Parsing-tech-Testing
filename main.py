import requests
from bs4 import BeautifulSoup
import re

base = "https://beltline.org"
url = base + "/events/?event=fitness+and+wellness&location=northeast+trail"

response = requests.get(url)
html= BeautifulSoup(response.text, 'html.parser')

categories_html= html.find('section', {"class": "Container_container__ozJnP Container_md__TAxhg Container_center__kUR9j"})
courses_html = categories_html.findChildren("div", class=re.compile('^"RelatedEventCard_related-event-card__CLrCv"'))

courses_mardown = "# BeltLine Courses"
for c in courses_html:
  text = c.find('p').text
  url = base + c.find('a', href = True)['href']

  print(text)
  text_stripped = re.sub(' +', ' ', text).strip()

  
  courses_markdown += ""
  ## {}
  [{}]({})
  "".format(text_stripped, url)

with open("courses.md", "w") as courses_file:
  courses_file.write(courses_markdown)
