from tir import Webapp
import unittest

class GFEC022(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "23/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC022")

    def test_GFEC022_CT001(self):
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'
        corte_a = '80'
        corte_b = '90'
        series = '10'

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        self.oHelper.SetValue('% de Corte A ?',corte_a)
        self.oHelper.SetValue('% de Corte B ?',corte_b)
        self.oHelper.SetValue('Qtde séries ?',series)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('X')
    
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
