from tir import Webapp
import unittest

class ATFA110(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "30/03/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA110")

        inst.oHelper.AddParameter("MV_ULTDEPR", "", "20160229")
        inst.oHelper.AddParameter("MV_ATFCTAP", "", "1")
        inst.oHelper.SetParameters()

    ##############################################################################
    # test_ATFA110_001 - Caso de teste 001                       
    # Estorno de revisão de estimativa de produção por meio de Apt. Multiplos                
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44421
    # 24/09/2019
    ##############################################################################

    def test_ATFA110_001(self):

        codigoATF   = 'ATF_APT001'
        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0001")
        self.oHelper.SetButton("Outras Ações", "Apt. multiplos")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("FNA_DATA", "25/03/2016")
        self.oHelper.SetValue("FNA_OCORR", "P8 - Estorno de revisão de estim. de produção")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetValue("Filial       ?", "D MG 01")
        self.oHelper.SetValue("ID Movto.    ?", "0000000016")

        self.oHelper.SetButton("OK")

        self.oHelper.ClickBox("Cod Base Bem", grid_number=1, select_all=True)
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0001")
        self.oHelper.SetButton("Apontamento")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("FNA_DATA", "26/03/2016")
        self.oHelper.SetValue("FNA_OCORR", "P1 - Revisão de estimativa de produção")
        self.oHelper.SetValue("FNA_QUANTD", "2,00")
        
        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

    ##############################################################################
    # test_ATFA110_002 - Caso de teste 002                        
    # Apontamento de Produção por Revisão de estimativa de produção                           
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44419
    # 24/09/2019
    ##############################################################################
    def test_ATFA110_002(self):
        
        codigoATF   = 'ATF_APT001'
        itemATF     = '0003'

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}{itemATF}")
        
        self.oHelper.SetButton("Apontamento")
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("FNA_DATA", "27/03/2016")
        self.oHelper.SetValue("FNA_OCORR", "P1 - Revisão de estimativa de produção")
        self.oHelper.SetValue("FNA_QUANTD", "2,00")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}{itemATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N3_CBASE", codigoATF)
        self.oHelper.CheckResult("N3_ITEM", itemATF)
        self.oHelper.ClickFolder("Depreciação")
        self.oHelper.CheckResult("N3_PRODANO", "2,000")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    ##############################################################################
    # test_ATFA110_003 - Caso de teste 003                        
    # Apontamento de Produção Multiplos por revisão de estimativa de produção                
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44420
    # 24/09/2019
    ##############################################################################

    def test_ATFA110_003(self):

        codigoATF = 'ATF_APT001'

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0007")
        self.oHelper.SetButton("Outras Ações", "Apt. multiplos")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("FNA_DATA", "28/03/2016")
        self.oHelper.SetValue("FNA_OCORR", "P1 - Revisão de estimativa de produção")
        self.oHelper.SetValue("FNA_QUANTD", "1,00")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetValue("Filial de referência ?", "D MG 01")
        self.oHelper.SetValue("Código base inicial ?", "ATF_APT001")
        self.oHelper.SetValue("Código base final ?", "ATF_APT001")
        self.oHelper.SetValue("Item inicial ?", "0007")
        self.oHelper.SetValue("Item final ?", "0009")
        self.oHelper.SetValue("Conta contábil final ?", "ZZZZZZZZZZZZZZZZZZZZ")
        self.oHelper.SetValue("Grupo final ?", "ZZZZ")
        self.oHelper.SetButton("OK")

        self.oHelper.ClickBox("Cod Base Bem", grid_number=1, select_all=True)
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0007")
        self.oHelper.SetButton("Visualizar")

        #Item 4

        self.oHelper.CheckResult("N3_CBASE", codigoATF)
        self.oHelper.CheckResult("N3_ITEM", "0007")
        self.oHelper.ClickFolder("Depreciação")
        self.oHelper.CheckResult("N3_PRODANO", "1,000")
        self.oHelper.SetButton("Confirmar")

        #Item 5

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0008")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N3_CBASE", codigoATF)
        self.oHelper.CheckResult("N3_ITEM", "0008")
        self.oHelper.ClickFolder("Depreciação")
        self.oHelper.CheckResult("N3_PRODANO", "1,000")
        self.oHelper.SetButton("Confirmar")

        #Item 6

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}0009")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N3_CBASE", codigoATF)
        self.oHelper.CheckResult("N3_ITEM", "0009")
        self.oHelper.ClickFolder("Depreciação")
        self.oHelper.CheckResult("N3_PRODANO", "1,000")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

        
