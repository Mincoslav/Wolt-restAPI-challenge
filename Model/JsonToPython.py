import json

from Model.Restaurant import Restaurant


class JsonToPython:

    filename = ''

    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def loadfile():

        with open('Model/restaurants.json') as json_file:

            data = json.load(json_file)
            restaurants = []

            for p in data['restaurants']:

                blurhash = p['blurhash']
                city = p['city']
                currency = p['currency']
                delivery_price = p['delivery_price']
                description = p['description']
                image = p['image']
                location = p['location']
                name = p['name']
                online = p['online']
                tags = p['tags']

                restaurant = Restaurant(blurhash, city, currency, delivery_price,
                                        description, image, location, name, online, tags)

                restaurants.append(restaurant)

        return restaurants
