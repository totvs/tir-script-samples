import unittest

from PPLCHAPRE02ODTESTCASE import PPLCHAPRE02ODTESTCASE


def PPLCHAPRE02ODTESTSUITE():

    suite = unittest.TestSuite()
    suite.addTest(PPLCHAPRE02ODTESTCASE('test_PPLCHAPRE02OD_CT001'))
    suite.addTest(PPLCHAPRE02ODTESTCASE('test_PPLCHAPRE02OD_CT002'))
    suite.addTest(PPLCHAPRE02ODTESTCASE('test_PPLCHAPRE02OD_CT003'))
    suite.addTest(PPLCHAPRE02ODTESTCASE('test_PPLCHAPRE02OD_CT004'))
    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(PPLCHAPRE02ODTESTSUITE())
