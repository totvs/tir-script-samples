
import unittest
import sys

from PPLPRORINTTESTCASE import PPLPRORINTTESTCASE

def PPLPRORINTTESTSUITE():

    suite = unittest.TestSuite()
    suite.addTest(PPLPRORINTTESTCASE("test_PPLPRORINT_CT001"))
    suite.addTest(PPLPRORINTTESTCASE("test_PPLPRORINT_CT002"))
    suite.addTest(PPLPRORINTTESTCASE("test_PPLPRORINT_CT003"))
    suite.addTest(PPLPRORINTTESTCASE("test_PPLPRORINT_CT004"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    ret = not runner.run(PPLPRORINTTESTSUITE()).wasSuccessful()
    sys.exit(ret)
