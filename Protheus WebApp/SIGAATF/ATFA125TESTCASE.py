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

    #######################################################
    # Caso de teste 001 - Solicitação de baixa            #
    #######################################################
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

    #######################################################
    # Caso de teste 002 - Solicitação de transferencia    #
    #######################################################
    def test_ATFA125_002(self):

        codigoATF = 'AT125_AT2'
        codigoItem = '0001'

        self.oHelper.SetButton("Outras Ações", "Solic. Transf.")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("cCBASE", "AT125_AT2", name_attr=True)
        self.oHelper.SetValue("cITEM", "0001", name_attr=True)
        
        self.oHelper.SetValue("cFilDest", "D MG 02", name_attr=True)
        self.oHelper.SetValue("cGeraNF", "2 - Não", name_attr=True)

        self.oHelper.ClickFolder("Dados da Solicitacao")
        self.oHelper.SetValue("Hist. Solic.", "TESTCASE TIR 002")
        self.oHelper.SetButton("Ok")

        #Conferencia
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetValue("cOrd", "Filial+cod. do Bem + Código Item + Tipo Ativo + Situação", name_attr=True)
        self.oHelper.SetValue("cCampo", "D MG 01 AT125_AT2 0001", name_attr=True)
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("cCBASE", codigoATF, name_attr=True)
        self.oHelper.CheckResult("cITEM", codigoItem, name_attr=True)
        self.oHelper.CheckResult("cFilDest", "D MG 02", name_attr=True)

        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()
    #######################################################
    # Caso de teste 002 - Solicitação de transferencia em #
    # Lote - sem marcar checkbox                          #
    #######################################################

    def test_ATFA125_003(self):

        codigoATF = 'AF125_AT3'

        self.oHelper.SetButton("Outras Ações", "Solic. Transf. Lote")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("cBasei", codigoATF, name_attr=True)
        self.oHelper.SetValue("cBasef", codigoATF, name_attr=True)
        self.oHelper.SetValue("cItemi", "0001", name_attr=True)
        self.oHelper.SetValue("cItemf", "0003", name_attr=True)
        
        self.oHelper.SetValue("cFilDest", "D MG 02", name_attr=True)
        
        self.oHelper.SetValue("_cGERANF", "2 - Não", name_attr=True)
        self.oHelper.SetValue("Hist. Solic.", "TIR TEST CASE 003")

        self.oHelper.SetButton("Ok")
        
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        #Conferencia item 1
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetValue("cOrd", "Filial+cod. do Bem + Código Item + Tipo Ativo + Situação", name_attr=True)
        self.oHelper.SetValue("cCampo", "D MG 01 AF125_AT3 0001", name_attr=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("cCBASE", codigoATF, name_attr=True)
        self.oHelper.CheckResult("cITEM", "0001", name_attr=True)
        self.oHelper.CheckResult("cFilDest", "D MG 02", name_attr=True)

        self.oHelper.SetButton("Ok")

        #Conferencia item 2
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetValue("cOrd", "Filial+cod. do Bem + Código Item + Tipo Ativo + Situação", name_attr=True)
        self.oHelper.SetValue("cCampo", "D MG 01 AF125_AT3 0002", name_attr=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("cCBASE", codigoATF, name_attr=True)
        self.oHelper.CheckResult("cITEM", "0002", name_attr=True)
        self.oHelper.CheckResult("cFilDest", "D MG 02", name_attr=True)

        self.oHelper.SetButton("Ok")

        #Conferencia item 3
        self.oHelper.SetButton("Outras Ações", "Pesquisar")
        self.oHelper.SetValue("cOrd", "Filial+cod. do Bem + Código Item + Tipo Ativo + Situação", name_attr=True)
        self.oHelper.SetValue("cCampo", "D MG 01 AF125_AT3 0003", name_attr=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("cCBASE", codigoATF, name_attr=True)
        self.oHelper.CheckResult("cITEM", "0003", name_attr=True)
        self.oHelper.CheckResult("cFilDest", "D MG 02", name_attr=True)

        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

        
