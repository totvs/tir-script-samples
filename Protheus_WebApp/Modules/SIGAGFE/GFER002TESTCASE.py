from tir import Webapp
import unittest

class GFER002(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "29/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFER002")
           
    def test_GFER002_CT001(self):
               
        self.oHelper.SetValue('Data Impl Inicial ?','01/01/2018')
        self.oHelper.SetValue('Data Impl Final ?','31/12/2020')
        self.oHelper.SetValue('Data Emis Inicial ?','01/01/2018')
        self.oHelper.SetValue('Data Emis Final ?','31/12/2020')
        self.oHelper.SetValue('Movimentos a Exibir ?','Todos')
        self.oHelper.SetValue('Formato de Extração ?','Relatório')
        self.oHelper.SetValue('Diretório de Arquivo ?','spool')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Arquivo')
        self.oHelper.SetButton('Imprimir')
        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()