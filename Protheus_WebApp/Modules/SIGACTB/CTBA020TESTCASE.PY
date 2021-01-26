from tir import Webapp
import unittest

class CTBA020(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "08/07/2019", "T1", "D MG 01 ", "34")

        inst.oHelper.Program("CTBA020")

    def test_CTBA020_047(self):

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("CT1_CONTA","INCLUIRTIR",name_attr=True) 

        self.oHelper.SetValue("CT1_DESC01","INCLUIRTIR",name_attr=True)

        self.oHelper.SetValue("CT1_CLASSE","2 - Analitica",name_attr=True)

        self.oHelper.SetValue("CT1_NORMAL","1 - Devedora",name_attr=True)

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG    INCLUIRTIR", "Filial+cod Conta")

        self.oHelper.SetButton("Outras Ações", "Visualizar")
        
        self.oHelper.CheckResult("CT1_CONTA", "INCLUIRTIR",name_attr=True)
        self.oHelper.CheckResult("CT1_DESC01", "INCLUIRTIR",name_attr=True)
        self.oHelper.CheckResult("CT1_CLASSE", "2 - Analitica",name_attr=True)
        self.oHelper.CheckResult("CT1_NORMAL", "1 - Devedora",name_attr=True)
        

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_CTBA020_048(self):
        self.oHelper.SearchBrowse(f"D MG    EXCLUIRTIR", "Filial+cod Conta")

        self.oHelper.SetButton("Outras Ações", "Excluir")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG    EXCLUIRTIR", "Filial+cod Conta")
        
        self.oHelper.SetButton("Outras Ações", "Visualizar")

        self.oHelper.CheckResult("CT1_CONTA", "EXCLUIRTIR",name_attr=True)
        self.oHelper.CheckResult("CT1_DESC01", "EXCLUIRTIR",name_attr=True)

        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertFalse()
       
    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()