#  Celem zadania jest nauczenie Cię pracy z generatorami grafik i dokumentów. Zadanie polega na wygenerowaniu mema z podanego obrazka i podanego tekstu.
#  Mem ma być obrazkiem JPG o wymiarach 1080x1080. Powinien posiadać czarne tło, dostarczoną grafikę na środku i podpis zawierający dostarczony tekst.
#  Grafikę możesz wygenerować za pomocą darmowych tokenów dostępnych w usłudze RenderForm (50 pierwszych grafik jest darmowych).
#  URL do wygenerowanej grafiki spełniającej wymagania wyślij do endpointa /answer/.
#  W razie jakichkolwiek problemów możesz sprawdzić hinty https://zadania.aidevs.pl/hint/meme
import os

import requests

from helper import Helper
from dotenv import load_dotenv # pip install python-dotenv

TEMPLATE_URL = 'https://renderform.io/console/template/canvas-editor/?templateId=skinny-newts-wave-weakly-1386'
TEMPLATE_ID = 'skinny-newts-wave-weakly-1386'
RENDER_URL = 'https://get.renderform.io/api/v2/render'

class Meme:

    def generate_answer(test_data):
        load_dotenv()
        RENDERFORM_API_KEY = os.getenv("RENDERFORM_API_KEY")
        test_data_json = test_data.json()
        meme_text = str(test_data_json["text"])
        meme_img = test_data_json["image"]

        req_headers = {
            "x-api-key": RENDERFORM_API_KEY,
        }

        req_body = {
            "template": TEMPLATE_ID,
            "data": {
                "text_input.text": meme_text,
                "image_input.src": meme_img
            }
        }
        print(RENDER_URL, RENDERFORM_API_KEY)
        response = requests.post(RENDER_URL, headers=req_headers, json=req_body)
        print(response.content, response.status_code)
        meme_url = response.json()["href"]
        print("Answered with", meme_url)
        return meme_url


if __name__ == '__main__':
    test_data = Helper.create_simulated_response(
        b'{"text":"Dlaczego chaos wygrywa z porzadkiem? Bo jest lepiej zorganizowany.", "image":"https://s.lubimyczytac.pl/upload/authors/3221/874253-140x200.jpg"}')
    Meme.generate_answer(test_data)

def save_to_file(response):
    if response.status_code == 200:
        with open("meme_image.jpg", "wb") as file:
            file.write(response.content)

