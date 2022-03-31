import unittest
from Jsons import Jsons, sendRequest


class APITest(unittest.TestCase):

    def test1_send_IP_addres_without_slash(self):
        res = sendRequest("https://ipinfo.io/161.185.160.93")
        self.assertEqual(res, Jsons.NewYork, "Fail: Return Data not equal to expected newYork data")

    def test2_send_IP_of_a_city_inside_region(self):
        res = sendRequest("https://ipinfo.io/89.138.45.9")
        city = "H̱olon"
        self.assertEqual(res['city'], city, "Fail: Return Data not equal to expected Jerusalem data")

    def test3_send_Geo_without_IP_addraes(self):
        res = sendRequest("https://ipinfo.io/geo")
        self.assertEqual(res, Jsons.Jerusalem, "Fail: Return Data not equal to expected Blairgowrie data")
