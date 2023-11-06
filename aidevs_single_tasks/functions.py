import openai
from helper import Helper

functions_list = [
        {
            "name": "addUser",
            "description": "New user",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Imie"},
                    "surname": {"type": "string", "description": "Nazwisko"},
                    "year": {"type": "integer", "description": "Rok urodzenia"}
                }
            },
            "required": [
                "name", "surname", "year"
            ]
        }
    ]


# C0205.functions - define a function list for a function call
# additionalyi the code really calls the openai model for verification
# Wykonaj zadanie o nazwie functions zgodnie ze standardem zgłaszania odpowiedzi opisanym na zadania.aidevs.pl.
# Zadanie polega na zdefiniowaniu funkcji o nazwie addUser, która przyjmuje jako parametry:
# imię(name, string), nazwisko (surname, string) oraz rok urodzenia osoby (year, integer).
# Jako odpowiedź musisz wysłać jedynie ciało funkcji w postaci JSON-a.
class Functions:
    @staticmethod
    def generate_answer(test_data):
        print(test_data.json())

        user_message = str(test_data.json()["msg"])

        openai.api_key = Helper().get_openapi_key()
        ai_resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613", # snapshot version for function calling
            function_call={"name": "addUser"},
            messages=[
                {"role": "user",
                 "content": user_message
                 }
            ],
            functions=functions_list)

        json_result = ai_resp.choices[0].message.function_call

        print(functions_list[0])
        return functions_list[0]


if __name__ == '__main__':
    #sim_content = b'{"msg": "Ala ma kota"}'

    sim_content = b'{"msg": "add user Adam Kowalski 1990"}'
    sim_response = Helper().create_simulated_response(sim_content)
    Functions().generate_answer(sim_response)
