from tir import Webapp
import unittest

class GFEA094(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA094")

    def test_GFEA094_CT001(self):
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial até ?',filial_ate)
        self.oHelper.SetValue('Período de ?',data_ini)
        self.oHelper.SetValue('Período até ?',data_fim)
        self.oHelper.SetValue('Situação Cálculo ?','Todos')
        self.oHelper.SetValue('Situação Lanctos ?','Todos')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Outras Ações','Dados Provisão')

        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
