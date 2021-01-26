from tir import Webapp
import unittest
import time

class GFEC010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "25/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC010")

    def test_GFEC010_CT001(self):   
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'      
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial até ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data até ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        time.sleep(20)
                  
        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
