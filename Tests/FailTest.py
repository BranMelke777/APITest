import unittest
from Jsons import sendRequest


class FailTest(unittest.TestCase):

    def test1_send_non_exist_IP(self):
        res = sendRequest("https://ipinfo.io/89.138.45.989")
        self.assertEqual(res['status'], 404, "Fail: Returns Data")

    def test2_send_request_with_parametr_x(self):
        res = sendRequest("https://ipinfo.io/x")
        self.assertEqual(res['status'], 404, "Fail: Returns Data")

    def test3_Send_request_with_special_carecters(self):
        res = sendRequest("https://ipinfo.io/89.138.45.989/#&*")
        self.assertEqual(res['status'], 404, "Fail: Returns Data")
