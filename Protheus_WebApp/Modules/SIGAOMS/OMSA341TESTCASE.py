from tir import Webapp
import unittest
import datetime

class OMSA341(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGAOMS',dataAtual,'T1','D MG 01 ','39')
        inst.oHelper.Program("OMSA341")

    #Conferir
    def test_OMSA341_CT001(self): 

        self.oHelper.SearchBrowse("D MG 01 000007")

        self.oHelper.SetButton("Conferir")

        self.oHelper.SetValue("DAP_CODGRU", "BOL", grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DAP_REALIZ", "10,00", grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        
        self.oHelper.ClickFolder("Veiculo")
        self.oHelper.ClickFolder("Carga")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()  

    #Estornar a Conferencia
    def test_OMSA341_CT002(self): 

        self.oHelper.SearchBrowse("D MG 01 000007")

        self.oHelper.SetButton("Outras Ações", "Estornar Conf.")
        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.AssertTrue()  

    #Prestar Titulos
    def test_OMSA341_CT003(self): 

        self.oHelper.SearchBrowse("D MG 01 000007")

        self.oHelper.SetButton("Conferir")

        self.oHelper.SetValue("DAP_CODGRU", "BOL", grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DAP_REALIZ", "10,00", grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse("D MG 01 000007")

        self.oHelper.SetButton("Outras Ações", "Prestar Títulos")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.WaitShow('Prestacao de Contas - PRESTAR TÍTULOS')
        self.oHelper.ClickFolder("Titulos")
        self.oHelper.ClickBox('Prefixo', '07', grid_number = 1)

        self.oHelper.ClickFolder("Baixa")
        self.oHelper.SetValue("cMotBx", "NORMAL", name_attr=True)
        self.oHelper.SetValue("cBanco", "470", name_attr=True)
        self.oHelper.SetValue("cAgencia", "00001", name_attr=True)
        self.oHelper.SetValue("cConta", "456123001", name_attr=True)
        self.oHelper.SetValue("nValRec", "10,00", name_attr=True) 

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()  
    
    #Cancelar Baixas
    def test_OMSA341_CT004(self):

        self.oHelper.SearchBrowse("D MG 01 000007")
        self.oHelper.SetButton("Outras Ações", "Prestar Títulos")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetButton("Outras Ações", "Cancelar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()

    #Funçoes Gerais
    def test_OMSA341_CT005(self):
        
        self.oHelper.SearchBrowse("D MG 01 000007")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações", "Status Financeiro")
        self.oHelper.SetButton("Ok")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()