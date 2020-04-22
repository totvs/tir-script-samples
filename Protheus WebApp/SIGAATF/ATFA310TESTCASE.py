from tir import Webapp
import unittest

class ATFA310(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "16/06/2015", "T1", "M SP 01 ", "01")
        inst.oHelper.Program("ATFA310")

        inst.oHelper.AddParameter("MV_ULTDEPR", "M SP 01", "31/05/2015")
        inst.oHelper.AddParameter("MV_ULTDEPR", "D RJ 02", "31/05/2015")
        inst.oHelper.SetParameters()
    
    ##############################################################################
    # test_ATFA310_001 - Caso de teste 001                            
    # Inclusão de Planejamento de Aquisição                                                   
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44233
    # 19/09/2019                                                      
    ##############################################################################

    def test_ATFA310_001(self):

        #Inicio
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetValue("NN_CODIGO", "ATF310T_01")
        self.oHelper.SetValue("NN_ITEM", "0001")
        self.oHelper.SetValue("NN_DESCRIC", "PLANEJAMENTO AUTOMACAO CTRL")
        self.oHelper.SetValue("NN_QUANTD", "1,000")
        self.oHelper.SetValue("NN_GRUPO", "ATSP")
        self.oHelper.SetValue("NN_DTPREVI", "16/06/2015")
        self.oHelper.SetValue("NN_VORIG1", "1.000.000,00", grid=True, row=1)
        self.oHelper.SetValue("NN_TXDEPR1", "100,0000", grid=True, row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        #Ao salvar, a rotina abre novamente a tela de inclusão
        self.oHelper.SetButton("Cancelar")

        #Conferencia de planejamento de aquisições
        self.oHelper.SearchBrowse("M SP 01 ATF310T_010001")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("NN_CODIGO", "ATF310T_01")
        self.oHelper.CheckResult("NN_ITEM", "0001")
        self.oHelper.CheckResult("NN_DESCRIC", "PLANEJAMENTO AUTOMACAO CTRL")
        self.oHelper.CheckResult("NN_QUANTD", "1,000")
        self.oHelper.CheckResult("NN_GRUPO", "ATSP ")
        self.oHelper.CheckResult("NN_DTPREVI", "16/06/2015")
        self.oHelper.CheckResult("NN_VORIG1", "1.000.000,00", grid=True, line=1)
        self.oHelper.CheckResult("NN_TXDEPR1", "100,0000", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    ##############################################################################
    # test_ATFA310_002 - Caso de teste 002                            
    # Efetivação de planejamento de aquisição                                                   
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44234
    # 19/09/2019                                                      
    ##############################################################################

    def test_ATFA310_002(self):
        
        self.oHelper.SearchBrowse("D RJ 02 ATF310T_01EF02")
        self.oHelper.SetButton("Outras Ações", "Efetivar")
        
        self.oHelper.SetValue("Por item", True)
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitProcessing("Processando...")

        self.oHelper.SearchBrowse("D RJ 02 ATF310T_01EF02")
        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult("NN_CODIGO", "ATF310T_01")
        self.oHelper.CheckResult("NN_ITEM", "EF02")
        self.oHelper.CheckResult("NN_DESCRIC", "PLANEJAMENTO AUTOMACAO CTRL EFETIVAC")
        self.oHelper.CheckResult("NN_QUANTD", "1,000")
        self.oHelper.CheckResult("NN_GRUPO", "EFRJ ")
        self.oHelper.CheckResult("NN_DTPREVI", "30/06/2016")
        self.oHelper.CheckResult("NN_ITMEFTV", "EF02")
        self.oHelper.CheckResult("NN_VORIG1", "2.000.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
