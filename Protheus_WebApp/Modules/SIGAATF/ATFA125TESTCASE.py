from tir import Webapp
import unittest

class ATFA125(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA125")
        inst.oHelper.AddParameter("MV_ULTDEPR", "", "20160331")
        inst.oHelper.AddParameter("MV_ALTLCTO", "", "N")
        inst.oHelper.AddParameter("MV_ATFSOLD", "", "1")
        inst.oHelper.AddParameter("MV_PRELAN", "", "S")
        inst.oHelper.SetParameters()

    def test_ATFA125_001(self):

        codigoATF = 'AF125_AT01'
        codigoItem = '0001'

        self.oHelper.SetButton("Solic. Baixa")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("cCBASE", codigoATF, name_attr=True)
        self.oHelper.SetValue("cITEM", codigoItem, name_attr=True)
        self.oHelper.SetValue("nQTDBX", "1,000", name_attr=True)
        self.oHelper.SetValue("cCONDPG", "100", name_attr=True)
        self.oHelper.SetValue("nVlVenda", "16.000,00", name_attr=True)
        self.oHelper.ClickFolder("Dados da Solicitacao")
        self.oHelper.SetValue("Hist. Solic.", "TESTCASE TIR 001")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetValue("cOrd", "Filial+cod. do Bem + Código Item + Tipo Ativo + Situação", name_attr=True)
        self.oHelper.SetValue("cCampo", "D MG 01 AF125_AT01 0001", name_attr=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("cCBASE", codigoATF, name_attr=True)
        self.oHelper.CheckResult("cITEM", codigoItem, name_attr=True)
        self.oHelper.CheckResult("nQTDBX", "1,000", name_attr=True)
        self.oHelper.CheckResult("cCONDPG", "100", name_attr=True)
        self.oHelper.CheckResult("nVlVenda", "16.000,00", name_attr=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

        
