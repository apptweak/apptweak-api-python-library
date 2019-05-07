from apptweak import apptweak
import unittest
from unittest.mock import patch

class TestApptweak(unittest.TestCase):

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

    def test_urljoir(self):
        self.assertEqual(apptweak.urljoin('a','b'),'a/b')
        self.assertEqual(apptweak.urljoin('','b'),'/b')
        self.assertEqual(apptweak.urljoin('a',''),'a/')
        self.assertEqual(apptweak.urljoin('',''),'/')

    def test_list_to_string(self):
        self.assertEqual(apptweak.list_to_string(['a','b']),'a,b')
        self.assertEqual(apptweak.list_to_string(['a']),'a')
        self.assertEqual(apptweak.list_to_string(['a',]),'a')
        self.assertEqual(apptweak.list_to_string(['a',123,'v']),'a,123,v')
        self.assertEqual(apptweak.list_to_string([12,22]),'12,22')

if __name__ == '__main__':
    unittest.main()
