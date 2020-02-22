import math


class Restaurant:

    def __init__(self, blurhash, city, currency, delivery_price, description, image, location, name, online, tags):

        self.blurhash = blurhash
        self.city = city
        self.currency = currency
        self.delivery_price = delivery_price
        self.description = description
        self.image = image
        self.location = location
        self.name = name
        self.online = online
        self.tags = tags

    def get_location(self):
        print("getter method called")
        return self.location

    @staticmethod
    def distance(origin, destination):
        lat1 = origin[0]
        lon1 = origin[1]

        lat2 = destination[1]
        lon2 = destination[0]
        #lat1, lon1 = origin
        #lat2, lon2 = destination
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d


