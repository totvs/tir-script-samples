from tir import Webapp
import unittest

class GTPA284(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', "01/03/2020", 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA284')

    def test_GTPA284_CT001(self):
        self.oHelper.SetButton('Outras Ações','Gerar Massa de Lotes')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
