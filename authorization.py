import requests
from helper import Helper


class AuthorizationTokenResolver:
  def authorize(self, taskName):
    url = Helper.BASE_URL + "token/" + taskName
    data = {'apikey': Helper.AIDEVS_API_KEY} # klucz do AIDEVS
    response = requests.post(url, json=data)
    return response.json()["token"]

