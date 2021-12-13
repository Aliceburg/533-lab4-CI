import unittest
from test_compare import TestCompare
from test_shape import TestShape
from test_size import TestSize
from testrectangle_cal import TestRectangleCal
from testgraphic import TestGraphic
from testround_cal import TestRoundCal

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCompare))
    suite.addTest(unittest.makeSuite(TestShape))
    suite.addTest(unittest.makeSuite(TestSize))
    suite.addTest(unittest.makeSuite(TestRectangleCal))
    suite.addTest(unittest.makeSuite(TestGraphic))
    suite.addTest(unittest.makeSuite(TestRoundCal))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
