import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class HTBClient:
    def __init__(self, app_token):
        self._app_token = app_token
        self._base_url = "https://www.hackthebox.com/api/v4"
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": "Bearer " + app_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": os.environ.get('USER_AGENT')
        })

    def do_request(self, method, endpoint, **kwargs):
        url = self._base_url + endpoint
        res_raw = self._session.request(method, url, **kwargs)
        res = res_raw.json()
        return res['info']
