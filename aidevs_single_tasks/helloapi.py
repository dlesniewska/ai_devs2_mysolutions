from helper import Helper
from authorization import AuthorizationTokenResolver
from testDataResolver import TestDataResolver
from answersender import AnswerSender


class HelloApi:
    @staticmethod
    def generate_answer(test_data):
        return test_data.json()["cookie"]
