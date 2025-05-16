import requests
import json
from bs4 import BeautifulSoup

#example 1

# url = "https://example.com/"
# response = requests.get(url)
# html_content = response.text

# soup = BeautifulSoup(html_content, "html.parser")

# heading = soup.find_all("a")
# for h in heading:
#     print(h.text.strip())

# links = soup.find_all("a")

# for link in links:
#     print(link.get("href"))

#example 2

# url = "https://www.python.org/"
# response = requests.get(url)
# html_content = response.text

# soup = BeautifulSoup(html_content, "html.parser")
# news = soup.find("div", class_="medium-widget event-widget last")
# headlines = news.find_all("li")
# # print(headlines)

# for item in headlines:
#     title = item.find("a").text.strip()
#     time = item.find("time").text.strip()
#     print(f"title: {title} time: {time}")



#example 3

url = "https://quotes.toscrape.com/"
response = requests.get(url)
html_content = response.text
# print(html_content)

soup = BeautifulSoup(html_content, "html.parser")
quotes = soup.find("div", class_="quote")

append_quotes = []
for quote in quotes:
    text = soup.find("span", class_="text").text.strip()
    author = soup.find("small", class_="author").text.strip()
    append_quotes.append({
        "Text": text,
        "author": author
    })

#quotes save in json file
with open("quotes_json.json", 'w') as json_file:
     save_quotes_in_json_file = json.dump(append_quotes, json_file)
     print("quotes save in custom json")



