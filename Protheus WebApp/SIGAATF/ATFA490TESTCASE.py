from tir import Webapp
import unittest


class ATFA490(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "01/03/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA490")

        # Para que o Tipo de Saldo seja considerado nas pesquisas e validações relacionados

        #inst.oHelper.AddParameter("MV_CTBCTG ","", ".T.")
        # inst.oHelper.SetParameters()

# ==================================================================================
#                 Copiar Provisão
# Kanoah "https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T532"
# ==================================================================================
    def test_ATFA490_001(self):
            ##COPIA
        self.oHelper.SearchBrowse("D MG 01 00000000060001")
        self.oHelper.SetButton("Outras Ações", "Copiar")
        self.oHelper.SetValue("FNU_COD","TIR01")
        self.oHelper.SetValue("FNU_DESCR","Copia TIR")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()


# ==================================================================================
#                 Revisar Provisão
# Kanoah "https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T551"
# ==================================================================================
    def test_ATFA490_002(self):
        self.oHelper.SearchBrowse("D MG 01 00000000070001")

        self.oHelper.SetButton("Outras Ações", "Revisar")

        self.oHelper.SetValue("Mostra Lanc. Contabeis ?","Não")
        self.oHelper.SetValue("Aglut Lançamentos ?","Não")
        self.oHelper.SetValue("Contabiliza Online ?","Não")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckHelp("Deseja gravar a operação, bloqueando a revisão anterior ?","Sim")

        self.oHelper.AssertTrue()    

# ==================================================================================
#                 Desbloqueio de Provisão
# Kanoah "https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T537"
# ==================================================================================
    def test_ATFA490_003(self):
        self.oHelper.SearchBrowse("D MG 01 00000000080001")
        self.oHelper.SetButton("Outras Ações", "Bloqueio/Desbloq")
        self.oHelper.SetValue("FNU_MSBLQL","2 - Não")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckHelp("Deseja Realizar o bloqueio/desbloqueio do controle de provisão ?","Sim")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("FNU_MSBLQL","2 - Não")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()    
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
