import requests

MAKE_OWNAPI_WH = "https://hook.eu2.make.com/ifc8p9fztmkpf47mxo4w883f1bnkisl0"


class Ownapi:
    @staticmethod
    def generate_answer(test_data):
        print(test_data)
        return MAKE_OWNAPI_WH


if __name__ == '__main__':
    api_resp = requests.post(MAKE_OWNAPI_WH, json={"question": "whats the meaning of life? - answer extra short"})
    print("Response", api_resp.content)