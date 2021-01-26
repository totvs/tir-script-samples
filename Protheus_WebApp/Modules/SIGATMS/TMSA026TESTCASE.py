from tir import Webapp
import unittest
import datetime

class TMSA026(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 03 ','43')
        inst.oHelper.Program("TMSA026")

    def test_TMSA026_CT001(self):
        
        self.oHelper.SetButton('Incluir')

        self.oHelper.SetBranch("M SP 03")

        self.oHelper.SetValue("DDY_USUARI", "000000")

        self.oHelper.SetValue("DDY_ROTINA", "TMSA040",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DDY_STATUS", "1",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DDY_TPBLQ", "CR",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA026_CT002(self): 

        self.oHelper.SearchBrowse("M SP 03 000000TMSA040")
        
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
