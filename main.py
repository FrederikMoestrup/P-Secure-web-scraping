import webScraper
import json

services = webScraper.scrapAllServices()
services_json = json.dumps([service.to_dict() for service in services], indent=4)
print(services_json)