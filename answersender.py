from helper import Helper
import requests
import json


class AnswerSender:
    @staticmethod
    def give_answer(token, answer):
        url = Helper.BASE_URL + "/answer/" + token
        data = {'answer': answer}
        response = requests.post(url, json=data)
        print('Result: ' + json.dumps(response.json()))
        return response.json()["code"] == "0"
