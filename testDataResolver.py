import requests
from helper import Helper


class TestDataResolver:
    @staticmethod
    def get_data(token):
        url = Helper.BASE_URL + "/task/" + token
        response = requests.get(url)
        return response
