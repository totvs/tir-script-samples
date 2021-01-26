from tir import Webapp
import unittest
import time
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')


class GTPA315(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', "01/03/2020", 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA315')

    def test_GTPA315_CT001(self):
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
