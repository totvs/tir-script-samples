from tir import Webapp
import unittest

class TMSA021(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGATMS", "02/06/2020", "T1", "M SP 03", "43")
        inst.oHelper.Program("TMSA021")

    def test_TMSA021_CT001(self):
        self.oHelper.WaitShow("Classificacao ONU")

        self.oHelper.SetButton('Incluir')

        self.oHelper.SetBranch("M SP 03")

        self.oHelper.SetValue("DY3_ONU", "4444")
        self.oHelper.SetValue("DY3_DESCRI", "TESTE COVID PARA CAVALARIA MARITIMA")
        self.oHelper.SetValue("DY3_CLASSE", "4",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_NRISCO", "4.1",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_LIMVEI", "12.000,00",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_LIMEMB", "1.000,00",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_UN", "CX",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("M SP    444401")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("DY3_ONU", "4444")
        self.oHelper.CheckResult("DY3_DESCRI", "TESTE COVID PARA CAVALARIA MARITIMA")
        self.oHelper.CheckResult("DY3_CLASSE", "4",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_NRISCO", "4.1",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_LIMVEI", "12.000,00",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_LIMEMB", "1.000,00",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_UN", "CX",grid=True,grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_TMSA021_CT002(self):

        self.oHelper.SearchBrowse("M SP    444401")

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("DY3_ONU", "4444")
        self.oHelper.SetValue("DY3_DESCRI", "TESTE COVID PARA CAVALARIA MARITIMA")
        self.oHelper.SetValue("DY3_CLASSE", "4",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_NRISCO", "4.1",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_LIMVEI", "15.000,00",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_LIMEMB", "1.500,00",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DY3_UN", "CX",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("M SP    444401")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("DY3_ONU", "4444")
        self.oHelper.CheckResult("DY3_DESCRI", "TESTE COVID PARA CAVALARIA MARITIMA")
        self.oHelper.CheckResult("DY3_CLASSE", "4",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_NRISCO", "4.1",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_LIMVEI", "15.000,00",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_LIMEMB", "1.500,00",grid=True,grid_number=1)
        self.oHelper.CheckResult("DY3_UN", "CX",grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()


    def test_TMSA021_CT003(self):

        self.oHelper.SearchBrowse("M SP    444401")
        self.oHelper.SetButton("Outras Ações", "Excluir")

        #self.oHelper.SetValue("DY3_ONU", "4444")
        #self.oHelper.SetValue("DY3_DESCRI", "TESTE COVID PARA CAVALARIA MARITIMA")
        #self.oHelper.SetValue("DY3_CLASSE", "4",grid=True,grid_number=1,row=1)
        #self.oHelper.SetValue("DY3_NRISCO", "4.1",grid=True,grid_number=1,row=1)
        #self.oHelper.SetValue("DY3_LIMVEI", "15.000,00",grid=True,grid_number=1,row=1)
        #self.oHelper.SetValue("DY3_LIMEMB", "1.500,00",grid=True,grid_number=1,row=1)
        #self.oHelper.SetValue("DY3_UN", "CX",grid=True,grid_number=1,row=1)
        #self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
