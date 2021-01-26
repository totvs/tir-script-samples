from tir import Webapp
import unittest
import time


class GTPA801B(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '07/10/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA421')

    def test_GTPA801B_CT001(self):
        print("test_GTPA801B_CT001 - Visualizar")
        self.oHelper.SearchBrowse('D MG    00000920200201', key=1, index=True)
        self.oHelper.SetButton("Outras Ações", "Conferência de Conhecimento")
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
