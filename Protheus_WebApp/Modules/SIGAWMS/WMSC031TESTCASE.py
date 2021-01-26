from tir import Webapp
import unittest

class WMSC031(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAWMS", "10/12/2020", "T1", "M SP 01", "42")
        inst.oHelper.Program("WMSC031")

    def test_WMSC031_CT001(self):
        
        self.oHelper.SetValue('Recurso Humano de ?', '')
        self.oHelper.SetValue('Recurso Humano ate ?', 'ZZZZZZ')
        self.oHelper.SetValue('Recurso Fisico de ?', '')
        self.oHelper.SetValue('Recurso Fisico ate ?', 'ZZZZZZ')
        self.oHelper.SetValue('Cliente de ?', '')
        self.oHelper.SetValue('Cliente ate ?', 'ZZZZZZ')
        self.oHelper.SetValue('Serviço de ?', '')
        self.oHelper.SetValue('Servico ate ?', 'ZZZ')
        self.oHelper.SetValue('Período de ?', '01/01/2000')
        self.oHelper.SetValue('Período até ?', '12/12/2030')
        self.oHelper.SetValue('Consolidar ?', 'Sim')
        self.oHelper.SetValue('Agrupar por ?', 'Rec.Humano')
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickBox('Funcionario','000260')
        
        self.oHelper.SetButton('Sair')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()

