from apptweak import apptweak
import unittest
from unittest.mock import patch

class TestRessource(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    @patch("apptweak.ressource.urllib.request.Request", return_value='True')
    @patch("apptweak.Ressource.reader", return_value=True)
    def test_http_request(self,mock_check,mock_load):

        with self.assertRaises(Exception):
            apptweak.Ressource.http_request('a', {'b':'c'})

        apptweak.API_KEY = "validkey"
        self.assertTrue(apptweak.Ressource.http_request('a', {'b':'c'}))

if __name__ == '__main__':
    unittest.main()
