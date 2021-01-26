from tir import Webapp
import unittest

class GFER001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "22/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFER001")
           
    def test_GFER001_CT001(self):
               
        self.oHelper.SetButton('Outras Ações','Parâmetros')
        
        self.oHelper.SetValue('Filiais ?','D MG 01;')
        self.oHelper.SetValue('Período ?','2018/05')
        self.oHelper.SetValue('Dia inicial ?','01')
        self.oHelper.SetValue('Dia final ?','31')
        self.oHelper.SetValue('Exibir Provisão ?','Sim')
        self.oHelper.SetValue('Exibir Estorno ?','Sim')
        self.oHelper.SetValue('Exibir Realizado ?','Sim')
        self.oHelper.SetValue('Formato de Extração ?','Relatório')
        self.oHelper.SetValue('Diretório de Arquivo ?','spool')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Imprimir')
        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()