from tir import Webapp 
import unittest
from datetime import datetime 
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA530(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")
        self.oHelper.Program("FATA300") 

    def test_FATA530_CT002(self):
        Opportunity = '000287'
        Proposal = '000285'

        self.oHelper.SearchBrowse(f"D MG 01 {Opportunity}", "Filial+oportunidade + Revisao")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Oportunidade de Venda - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Proposta Comercial')
        self.oHelper.WaitShow('Proposta Comercial')
        self.oHelper.SearchBrowse(f"{Proposal}", "Proposta No.")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow('Proposta Comercial Cabeçalho - ALTERAR')
        self.oHelper.SetButton('Outras Ações','Serviços (PMS)')
        self.oHelper.ClickGridCell("No.Projeto", row=2, grid_number=1)
        self.oHelper.ClickBox("Versão", "002")
        self.oHelper.ClickTree("EDT 02 - FATA530", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.ClickFolder("Edt")
        self.oHelper.SetValue("AF5_DESCRI","EDT 02 - FATA530 - ALTERADO")
        self.oHelper.SetButton("Salvar")
        self.oHelper.ClickTree("EDT 02 - FATA530 - ALTERADO", right_click = True)
        self.oHelper.ClickMenuPopUpItem("Visualizar")        
        self.oHelper.ClickFolder("Edt")
        self.oHelper.CheckResult("AF5_DESCRI","EDT 02 - FATA530 - ALTERADO")        
        self.oHelper.SetButton("Cancelar")        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página") 
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()