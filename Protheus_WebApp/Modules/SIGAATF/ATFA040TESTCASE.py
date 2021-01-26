from tir import Webapp
import unittest


class ATFA040(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "17/12/2019", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA040")

# ==================================================================================
#                 Cancelamento de baixa 
# Kanoah "https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T46678"
# ==================================================================================
    def test_ATFA040_001(self):
        ##cancelamento de baixa
        self.oHelper.AddParameter("MV_ULTDEPR", "D MG 01", "20191211")
        self.oHelper.SetParameters()
        self.oHelper.WaitShow("Baixa de Adiantamentos de Ativos Imobilizados")
        self.oHelper.SetKey("F12")
        # self.oHelper.SetButton("Param")
        # --
        self.oHelper.SetValue("Mostra Lanc.Contab ?","Nao")  
        self.oHelper.SetValue("Aglut Lancamentos ?","Nao")  
        self.oHelper.SetValue("Contabiliza Online ?","Não")  
        self.oHelper.SetButton("OK")
                

        self.oHelper.SearchBrowse("D MG 01 000100")
              
        self.oHelper.SetButton("Canc. Baixa")
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()


        self.oHelper.SearchBrowse("D MG 01 000100")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.ClickFolder("Valores")
        self.oHelper.CheckResult("N3_VORIG1","100,22")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("D MG 01 000030")
        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult("N1_CBASE","000030")
        # self.oHelper.RestoreParameters() ##Comentado devido ao proximo testcase ajustar o parametro
        self.oHelper.AssertFalse()

    def test_ATFA040_002(self):
        #BAIXA DE ADIANTAMENTO
        self.oHelper.AddParameter("MV_ULTDEPR", "D MG 01", "20200731")
        self.oHelper.SetParameters()
        self.oHelper.WaitShow("Baixa de Adiantamentos de Ativos Imobilizados")
        self.oHelper.SetButton("x")
        self.oHelper.ChangeEnvironment(date="17/08/2020",group="T1", branch="D MG 01 ")
        self.oHelper.Program("ATFA040")

        self.oHelper.WaitShow("Baixa de Adiantamentos de Ativos Imobilizados")

        self.oHelper.SearchBrowse("D MG 01 ATFA040_AD")

        self.oHelper.SetButton("Baixa Adiant")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("Código","NOVO_AD")
        self.oHelper.SetValue("Item","0001")
        self.oHelper.SetValue("Descrição","NOVO_AD")
        self.oHelper.SetValue("cBaseAdt","ATFA040_AD",name_attr=True)
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickBox("Codigo Item", "0001")
        self.oHelper.ClickBox("Codigo Item", "0002")
        self.oHelper.ClickBox("Codigo Item", "0003")

        self.oHelper.SetButton("Salvar")

        self.oHelper.WaitShow("Ativo Imobilizado - Ativo")

        self.oHelper.SetValue("Num.Plaqueta","NOVO_AD 0001")

        self.oHelper.CheckResult("Cod. Fornec.","")
        self.oHelper.CheckResult("Loja Fornec.","")
        self.oHelper.CheckResult("Serie N.F.","")
        self.oHelper.CheckResult("Nota Fiscal","")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Baixa de Adiantamentos de Ativos Imobilizados - BAIXA ADIANT")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()
                
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
