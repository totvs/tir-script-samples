import unittest

from PPLCHAPRE03TESTCASE import PPLCHAPRE03TESTCASE


def PPLCHAPRE03TESTSUITE():

    suite = unittest.TestSuite()
    suite.addTest(PPLCHAPRE03TESTCASE('test_PPLCHAPRE03_CT001'))
    suite.addTest(PPLCHAPRE03TESTCASE('test_PPLCHAPRE03_CT002'))
    suite.addTest(PPLCHAPRE03TESTCASE('test_PPLCHAPRE03_CT003'))
    suite.addTest(PPLCHAPRE03TESTCASE('test_PPLCHAPRE03_CT004'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(PPLCHAPRE03TESTSUITE())
