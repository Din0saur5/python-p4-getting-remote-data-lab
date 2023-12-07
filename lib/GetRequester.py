import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
    def get_response_body(self):
        return self.response.content
    
    def load_json(self):
        package = json.loads(self.response.content)
        return package

