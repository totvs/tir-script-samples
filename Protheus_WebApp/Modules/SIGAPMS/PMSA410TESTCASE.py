from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSA410(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS",DateSystem,"T1","D MG 01 ","44")
        self.oHelper.Program("PMSA410")

    def test_PMSA410_066(self):
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSU000001", "Filial+projeto")
        self.oHelper.SetButton("Alt.Cadastro")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Gerenciamento de Projetos")
        self.oHelper.SetValue("Tipo Proj","0001")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSU000001", "Filial+projeto")
        self.oHelper.SetButton("Alt.Cadastro")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Gerenciamento de Projetos")
        self.oHelper.CheckResult("Tipo Proj","0001")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
