from tir import Webapp
import unittest

class GTPA285(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', "01/03/2020", 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA285')

    def test_GTPA285_CT001(self):
        self.oHelper.SetValue('Cliente de: ?', '')
        self.oHelper.SetValue('Loja de: ?', '')
        self.oHelper.SetValue('Cliente até: ?', 'ZZZZZZ')
        self.oHelper.SetValue('Loja até: ?', 'ZZ')
        self.oHelper.SetValue('Requisição de: ?', '')
        self.oHelper.SetValue('Requisição até: ?', 'ZZZZZZ')
        self.oHelper.SetValue('Data de Emissão de: ?', '01/01/2020')
        self.oHelper.SetValue('Data de Emissão até: ?', '31/12/2020')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
