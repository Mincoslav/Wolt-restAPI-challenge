import flask
from flask import request, json
from Model.JsonToPython import JsonToPython

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/restaurants/search', methods=['GET'])
def api_id():
    # Check if a query and location was provided as part of the URL.
    # If they are provided, assign them to variables.
    # If no parameters are provided, display an error in the browser.
    if ('q' and 'lat' and 'lon') in request.args:
        query = str(request.args['q'])
        user_lat = float(request.args['lat'])
        user_lon = float(request.args['lon'])
        user_location = [user_lat, user_lon]
    else:
        return "Error: No query field provided. Please specify a query."

    # Create an empty list for results
    results = []
    restaurants = JsonToPython.loadfile()

    for restaurant in restaurants:
        if query in restaurant.tags:
            results.append(restaurant)
            print(type(restaurant.location))

    close_results = []

    for result in results:

        if result.distance(user_location, result.location) <= 3:
            close_results.append(result)
            print(result)
        else:
            print("fucked")

    json_string = json.dumps(close_results, default=lambda x: x.__dict__, indent = 4)
    return json_string


if __name__ == "__main__":
    app.run()
