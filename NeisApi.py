import requests

class NeisApi:
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def get_data(self):
        response = requests.get(self.url, params=self.params)
        return response.text