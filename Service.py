class Service:

    def __init__(self, name, status, lastUpdated, operatingTime, link):
        self.name = name
        self.status = status
        self.lastUpdated = lastUpdated
        self.operatingTime = operatingTime
        self.link = link

    def to_dict(self):  # Convert object to dictionary
        return {"name": self.name, "status": self.status, "last updated": self.lastUpdated, "operatingTime": self.operatingTime, "link": self.link}