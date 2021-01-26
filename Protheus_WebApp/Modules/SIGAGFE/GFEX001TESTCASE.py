from tir import Webapp
import unittest
import time

class GFEX001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "28/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEX001")

    def test_GFEX001_CT001(self):         
        data_ini = '01/01/2000'
        data_fim = '31/12/2049'
        
        self.oHelper.SetValue('Log Cálculo ?','Sim')
        self.oHelper.SetValue('Tipo Cálculo ?','Ambos')
        self.oHelper.SetValue('Agrupador ?','')
        self.oHelper.SetValue('Nr Docto Carga ?','')
        self.oHelper.SetValue('Período De ?',data_ini)
        self.oHelper.SetValue('Período Até ?',data_fim)
        self.oHelper.SetValue('Log Rateio Contabil ?','Sim')
        self.oHelper.SetValue('Nr Cálculo ?','')
        self.oHelper.SetValue('Nr Docto Frete ?','')
              
        self.oHelper.SetButton('Ok')

        time.sleep(5)

        self.oHelper.SetButton('x')

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
