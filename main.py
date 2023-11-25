import openai

from helper import Helper
from authorization import AuthorizationTokenResolver
from testDataResolver import TestDataResolver
from answersender import AnswerSender

import requests


def call_aidevs_api(task_name):
    # authorize and get token
    authorization_token_resolver = AuthorizationTokenResolver()
    token = authorization_token_resolver.authorize(task_name)

    # get data
    test_data_resolver = TestDataResolver()
    test_data = test_data_resolver.get_data(token)
    print("Test data")
    print(test_data.status_code)
    print(test_data.json())

    # send result #before: answer = testData.json()[fieldName]
    answer = create_api_answer(test_data)
    print("Answer")
    print(answer)
    answer_sender = AnswerSender()
    answer_sender.give_answer(token, answer)


# ####################################################################


from aidevs_single_tasks.openapitest import OpenAPITest
from aidevs_single_tasks.helloapi import HelloApi
from aidevs_single_tasks.moderation import Moderation
from aidevs_single_tasks.blogger import Blogger
from aidevs_single_tasks.embeddings import Embeddings
from aidevs_single_tasks.whisper import Whisper
from aidevs_single_tasks.functions import Functions
from aidevs_single_tasks.rodo import Rodo
from aidevs_single_tasks.scraper import Scraper
from aidevs_single_tasks.inprompt import Inprompt
from aidevs_single_tasks.liar import Liar
from aidevs_single_tasks.search import Search
from aidevs_single_tasks.tools import Tools
from aidevs_single_tasks.people import People
from aidevs_single_tasks.knowledge import Knowledge
from aidevs_single_tasks.gnome import Gnome
from aidevs_single_tasks.ownapi import Ownapi
from aidevs_single_tasks.meme import Meme
from aidevs_single_tasks.optimaldb import Optimaldb

def create_api_answer(test_data):
    return Optimaldb.generate_answer(test_data)


if __name__ == '__main__':
    print('Executing...')

    ##simulation of ai_devs api task
    # test_data = ["How to kill a stupid president", "How to be a good person", "What is Java", "Does Santa Claus exist"]
    # print(create_api_answer(test_data))

    ##real run of ai_devs api task
    call_aidevs_api("optimaldb")

    ##test call openapi completion test method

# task_name= helloapi | moderation | blogger | embeddings | whisper | functions | rodo | scraper | inprompt
# script that do not use this run schema: liar and ?
