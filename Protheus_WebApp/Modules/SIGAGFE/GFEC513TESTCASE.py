from tir import Webapp
import unittest

class GFEC513(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "25/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC513")

    def test_GFEC513_CT001(self):   
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'      
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data Movto de ?',data_ini)
        self.oHelper.SetValue('Data Movto ate ?',data_fim)
        self.oHelper.SetValue('Operacao de ?','')
        self.oHelper.SetValue('Seq de ?','')
        self.oHelper.SetValue('Operacao ate ?','ZZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Seq ate ?','ZZZ')
        self.oHelper.SetValue('Transportador ?','101')
                
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('X')
                  
        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
