
import unittest

from PPLCHAPRE02TESTCASE import PPLCHAPRE02TESTCASE

def PPLCHAPRE02TESTSUITE():

    suite = unittest.TestSuite()
    suite.addTest(PPLCHAPRE02TESTCASE("test_PPLCHAPRE02_CT001"))
    suite.addTest(PPLCHAPRE02TESTCASE("test_PPLCHAPRE02_CT002"))
    suite.addTest(PPLCHAPRE02TESTCASE("test_PPLCHAPRE02_CT003"))
    suite.addTest(PPLCHAPRE02TESTCASE("test_PPLCHAPRE02_CT004"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(PPLCHAPRE02TESTSUITE())
