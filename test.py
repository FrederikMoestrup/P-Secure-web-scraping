import requests
from bs4 import BeautifulSoup

#Hvis der var med end en liste af items på siden
#items = soup.find("div", class_="table module operating-status").find_all("div", class_="item")

#print(items[2].find("a").get("title"))

#for item in items:
#    print(item)

url = "https://digitaliser.dk/driftsstatus"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
items = soup.find_all("div", class_="item")

#print(items[0].find("a").get("title"))

#print(items[0].find("span").get_text().split(": ")[1])

#print(items[0].find("div", class_="last-updated").find_all("span")[1].get_text())

print(items[0].find("a", class_="btn-outline").get("href"))