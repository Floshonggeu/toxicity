
import warnings

from requests import api
warnings.filterwarnings("ignore")

# from api import app

import unittest
import requests

class TestApi(unittest.TestCase):

    URL = "http://host.docker.internal:4000"

    def test_website_is_up(self):
        r = requests.get(TestApi.URL)
        self.assertTrue(r.status_code == 200)

if __name__ == '__main__':
    unittest.main()