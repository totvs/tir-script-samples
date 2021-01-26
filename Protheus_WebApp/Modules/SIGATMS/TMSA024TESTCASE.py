from tir import Webapp
import unittest
import datetime

class TMSA024(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 03 ','43')
        inst.oHelper.Program("TMSA024")

    def test_TMSA024_CT001(self):
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        self.oHelper.SetButton('Incluir')

        self.oHelper.SetBranch("M SP 03")

        self.oHelper.SetValue("DIU_TIPRES", "1")
        self.oHelper.SetValue("DIU_CODCLI", "000001")
        self.oHelper.SetValue("DIU_LOJCLI", "01")
        self.oHelper.SetValue("DIU_INIVIG", "01/01/2020")
        self.oHelper.SetValue("DIU_FIMVIG", dataAtual)

        self.oHelper.SetValue("DIV_DESCRI", "TESTE TMS",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DIV_DIASEM", "1",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DIV_SERTMS", "1",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DIV_TIPVEI", "01",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA024_CT002(self): 

        self.oHelper.SearchBrowse("M       000001")
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Outras Ações","Copiar")        
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")

        self.oHelper.SetButton("Outras Ações","Excluir")        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
