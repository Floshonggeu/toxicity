
import warnings

from requests import api
warnings.filterwarnings("ignore")
import unittest
import requests
import time 
class TestApi(unittest.TestCase):

    URL = "http://host.docker.internal:4000"

    def test_website_is_up(self):
        r = requests.get(TestApi.URL)
        self.assertTrue(r.status_code == 200)


    def test_stress(self):

        self.startTime= time.time()
        for i in range (100):
            doc=requests.get(TestApi.URL)
        t=time.time()-self.startTime
        self.assertTrue(t<60)

#    def test_output(self):
#        r=[]
#        r1=requests.get(TestApi.URL)
#        r2=requests.get(TestApi.URL)
#        r.append(r1)
#        r.append(r2)
#        self.assertEqual(r,["toxic","neutral"])
if __name__ == '__main__':
    unittest.main()