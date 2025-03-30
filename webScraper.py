import requests
from bs4 import BeautifulSoup
import Service

def scrapAllServices():
    url = "https://digitaliser.dk/driftsstatus"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    items = soup.find_all("div", class_="item")
    services = []

    for item in items:
        services.append(scrapService(item))

    return services


def scrapService(item):
    name = item.find("a").get("title")
    status = item.find("span").get_text().split(": ")[1]
    lastUpdated = item.find("div", class_="last-updated").find_all("span")[1].get_text()
    operatingTime = item.find("div", class_="operating-time").find_all("span")[1].get_text()
    link = item.find("a", class_="btn-outline").get("href")

    service = Service.Service(name, status, lastUpdated, operatingTime, link)
    return service