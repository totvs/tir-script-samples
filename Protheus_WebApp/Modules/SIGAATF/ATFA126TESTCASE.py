from tir import Webapp
import unittest

class ATFA126(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "01/06/2015", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA126")

        inst.oHelper.AddParameter("D MG 02 MV_ULTDEPR","","20150531")
        inst.oHelper.AddParameter("MV_ULTDEPR", "D MG 01 ", "20150531")
        inst.oHelper.AddParameter("MV_ALTLCTO", "", "N")
        inst.oHelper.AddParameter("MV_ATFSOLD", "", "1")
        inst.oHelper.AddParameter("MV_PRELAN", "", "S")
        inst.oHelper.SetParameters()

    #######################################################
    # Caso de teste 001 - Solicitação de baixa            #
    #######################################################
    def test_ATFA126_010(self):

        codigoATF = 'D MG 01 000002ATFA126   000101'

        self.oHelper.SearchBrowse(codigoATF,key=1,index=1)

        self.oHelper.SetButton("Aprovar")
        self.oHelper.WaitShow("Análise das solicitações de baixa e transferência de Ativo - APROVAR")
        self.oHelper.CheckResult("Cód. Solic.","000002")

        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()
        

    #######################################################
    # Caso de teste 002 - Solicitação de transferencia    #
    #######################################################
    def test_ATFA126_011(self):

        codigoATF = 'D MG 01 000004ATFA125   000101'
        

        self.oHelper.SearchBrowse(codigoATF,key=1,index=1)

        self.oHelper.SetButton("Aprovar")
        self.oHelper.WaitShow("Análise das solicitações de baixa e transferência de Ativo - APROVAR")
        

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("X")
        self.oHelper.Program("ATFA012")
        codigo = "ATFA125   0001   "
        self.oHelper.SearchBrowse(f"D MG 02 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATFA125   0001    "
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N3_CUSTBEM", "CC126ALT", grid=True, line=2,name_attr=True)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")
        self.oHelper.Program("ATFA126")
        

        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

        
