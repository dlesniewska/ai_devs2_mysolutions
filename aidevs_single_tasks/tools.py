from authorization import AuthorizationTokenResolver
from helper import Helper
import openai
from helper import Helper
import requests
import json

from testDataResolver import TestDataResolver

functions_list = [
    {
        "name": "ToDo",
        "description": "Add a task to the ToDo list",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Task name"}
            }
        },
        "required": [
            "name"
        ]
    },
    {
        "name": "Calendar",
        "description": "Add an event to the calendar",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Event name"},
                "date": {"type": "string", "description": "Event date"}
            }
        },
        "required": [
            "name","date"
        ]
    }
]


# c0402.tools - function calling
# Celem zadania jest zdecydowanie, czy podane przez API zadanie powinno zostać dodane do listy zadań (ToDo),
#  czy do kalendarza (jeśli ma ustaloną datę). Oba narzędzia mają lekko definicje struktury JSON-a (różnią się jednym polem).
#  Spraw, aby Twoja aplikacja działała poprawnie na każdym zestawie danych testowych.
class Tools:
    @staticmethod
    def generate_answer(test_data):
        # authorize and get token
        authorization_token_resolver = AuthorizationTokenResolver()
        token = authorization_token_resolver.authorize("tools")

        # get data
        test_data_resolver = TestDataResolver()
        test_data = test_data_resolver.get_data(token)
        print("Test data")
        print(test_data.json())

        user_message = str(test_data.json()["question"])
        print(user_message)


        openai.api_key = Helper().get_openapi_key()
        ai_resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # tool_call=[{"name": "ToDo"}],
            messages=[
                {"role": "system",
                 "content": """
                 ###Facts:###
                 - today is 2023-11-17
                 - jutro is 2023-11-18
                 - pojutrze is 2023-11-19
                 - if date is specified, the task should be added to the Calendar 
                 ###Examples###
                 user: Przypomnij mi, ze mam kupic mleko 
                 assistant: {"tool":"ToDo","desc":"Kup mleko"} 
                 user: Jutro mam spotkanie z Marianem
                 assistant: {"tool":"Calendar","desc":"Spotkanie z Marianem","date":"2023-11-18"}
                 """
                 },
                {"role": "user",
                 "content": f"{user_message}"
                 }
            ],
            # tools=functions_list
        )

        json_result = ai_resp.choices[0].message.content

        print(json_result)
        # return f"{json_result}"
        #wysyłka
        url = Helper.BASE_URL + "/answer/" + token
        data = {'answer': json.loads(json_result)}
        response = requests.post(url, json=data)
        print('Result: ' + json.dumps(response.json()))
        return response.json()["code"] == "0"


if __name__ == '__main__':
    test_data = Helper.create_simulated_response(
        b'{"code": 0, "question": "Pojutrze mam kupic 1kg ziemniakow"}')

    ans = Tools().generate_answer(test_data)
    print(ans)
