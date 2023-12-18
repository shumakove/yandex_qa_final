import requests

import configuration


def create_new_order(body, debug=False):
    response = requests.post(configuration.URL_SERVICE + configuration.ORDER_PATH, json=body)
    if debug:
        print(response)
    return response


def get_information_by_order_track(track_number, debug=False):
    params = {'t': str(track_number)}
    response = requests.get(configuration.URL_SERVICE + configuration.TRACK_PATH, params=params)
    if debug:
        print(response.json())
    return response.json()
