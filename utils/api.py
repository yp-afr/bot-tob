import json

import requests

from data.config import API_TOKEN, API_URL


class Api:

    @staticmethod
    async def sendRequestApi(data):
        headers = {"Token": API_TOKEN}
        response = requests.request("POST", API_URL, headers=headers, data=json.dumps(data))
        return json.loads(response.text)
