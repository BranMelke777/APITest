import os
from unittest import TestLoader, TestSuite
from Tests.APITest import APITest
from Tests.CityAPIGeoTest import APIGeoTest
from Tests.FailTest import FailTest
from pyunitreport import HTMLTestRunner
from datetime import datetime

if __name__ == "__main__":

    test_loader = TestLoader()

    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(APITest),
        test_loader.loadTestsFromTestCase(APIGeoTest),
        test_loader.loadTestsFromTestCase(FailTest)


    ))

    # Creating output directory if not exists
    reports = '{}\\reports'.format(os.path.dirname(os.path.abspath(__file__)))
    try:
        if not os.path.exists(reports):
            os.makedirs(reports)
    except OSError as e:
        print("Couldn't create output directory, Error: {}".format(e))

    # Creating a html results file
    kwargs = {
        "output": reports,
        "report_name": "report_{}.html".format(datetime.now().strftime("%d-%m-%Y-%H-%M-%S")),
        "failfast": True
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(test_suite)
