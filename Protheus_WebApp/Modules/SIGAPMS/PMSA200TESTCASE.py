from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSA200(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS", DateSystem, "T1", "D MG 01 ", "44")
        self.oHelper.Program("PMSA200") 

    def test_PMSA200_CT060(self):
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.SearchBrowse("D MG 01 PMSRTIR001", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações", "Alt.Estrutura")
        self.AjustaAtalho()
        self.oHelper.SetFocus("AF8_PROJET")
        self.oHelper.SetKey(key="CTRL", additional_key="M") 
        self.oHelper.SetValue("Procurar por:", "ALTERACAO DO PROJETO POR TIR")
        self.oHelper.SetButton("Procurar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetFocus("AF8_PROJET")
        self.oHelper.SetKey(key="CTRL", additional_key="B") 
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetFocus("AF8_PROJET")
        self.oHelper.SetKey(key="CTRL", additional_key="Y") 
        self.oHelper.WaitShow("Tarefas do Projeto")
        self.oHelper.SetValue("Descricao*", "Tarefa TIR")
        self.oHelper.ClickFolder("Cronograma") 
        self.oHelper.SetValue("Dt.Ini. Prv.*", DateSystem)
        self.oHelper.SetValue("Dt.Fin. Prv.*", DateSystem)
        self.oHelper.SetButton("Data Inicial")
        self.oHelper.WaitShow("Tarefas do Projeto")
        self.oHelper.ClickFolder("Produtos")
        self.oHelper.SetValue("Cod.Produto" , "PMS000000000000000000000000001"  , grid=True)
        self.oHelper.SetValue("Quantidade"  , "1,0000"                          , grid=True)
        self.oHelper.SetValue("Dt. Necess." , DateSystem                        , grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Gerenciamento de Projetos - Alterar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Gerenciamento de Projetos")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown() 

if __name__ == "__main__":
    unittest.main()