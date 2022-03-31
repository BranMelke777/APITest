import unittest
from Jsons import Jsons, sendRequest


class APIGeoTest(unittest.TestCase):
    def test1_checkNewYorkIP(self):
        res = sendRequest("https://ipinfo.io/161.185.160.93/geo/")
        self.assertEqual(res, Jsons.NewYork, "Fail: Return Data not equal to expected newYork data")

    def test2_checkJerusalemIP(self):
        res = sendRequest("http://ipinfo.io/89.138.45.91/geo")
        self.assertEqual(res, Jsons.Jerusalem, "Fail: Return Data not equal to expected Jerusalem data")

    def test3_checkBlairgowrieIP(self):
        res = sendRequest("https://ipinfo.io/86.138.45.91/geo")
        self.assertEqual(res, Jsons.Blairgowrie, "Fail: Return Data not equal to expected Blairgowrie data")
