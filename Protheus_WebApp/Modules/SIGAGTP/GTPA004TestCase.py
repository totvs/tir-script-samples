from tir import Webapp
import unittest

class GTPA004(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '15/04/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA004')

    def test_GTPA004_CT001(self):
        self.oHelper.SearchBrowse('D MG    00000000009', key=1, index=True)
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
