from tir import Webapp
import unittest

class PCOA105(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "01/06/2017", "T1", "M PR 01 ", "57")
        inst.oHelper.Program("PCOA105")

    ##############################################################################
    # test_PCOA105_001 - Caso de teste 001                                                
    # Inclusão de totais da planilha orçamentária por conta 
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44139          
    # 17/09/2019                                                      
    ##############################################################################       
    def test_PCOA105_001(self):
        
        self.oHelper.SetValue("Totais da Planilha Orçamentária", True)
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Classe Orçamentária", True)
        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Total Por  ? ", "Total por Classe")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado por Classe")
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Entidade Origem  ? ", "AK6")
        self.oHelper.SetButton("Finalizar")
        
        self.oHelper.SearchBrowse("M PR 01 001")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "001")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por Classe")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse("M PR 01 002")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "002")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado por Classe")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    #############################################################################
    # test_PCOA105_002 - Caso de teste 002                            
    # Inclusão de totais da planilha orçamentária por CC              
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44140
    # 17/09/2019                                                      
    #############################################################################
    def test_PCOA105_002(self):
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Centro de Custo", True)
        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Total Por  ? ", "Total por C.C.")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado por C.C.")
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Entidade Origem  ? ", "CTT")
        self.oHelper.SetButton("Finalizar")
        
        self.oHelper.SearchBrowse("M PR 01 003")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "003")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por C.C.")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse("M PR 01 004")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "004")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado por C.C.")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()
    
    #############################################################################
    # test_PCOA105_003 - Caso de teste 003                            
    # Inclusão de totais da planilha orçamentária por Item contábil   
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44142
    # 17/09/2019                                                      
    #############################################################################
    def test_PCOA105_003(self):
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Item Contábil", True)
        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Total Por  ? ", "Total por Item")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado por Item")
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Entidade Origem  ? ", "CTD")
        self.oHelper.SetButton("Finalizar")
        
        self.oHelper.SearchBrowse("M PR 01 005")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "005")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por Item")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse("M PR 01 006")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "006")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado por Item")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    #############################################################################
    # test_PCOA105_004 - Caso de teste 004                            
    # Inclusão de totais da planilha orçamentária por Classe de valor 
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44143
    # 17/09/2019                                                      
    #############################################################################

    def test_PCOA105_004(self):
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Classe de Valor", True)
        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Total Por  ? ", "Total por Cl. Valor")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado Cl. Valor")
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Entidade Origem  ? ", "CTH")
        self.oHelper.SetButton("Finalizar")
        
        self.oHelper.SearchBrowse("M PR 01 007")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "007")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por Cl. Valor")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse("M PR 01 008")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "008")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado Cl. Valor")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    ###############################################################################
    # test_PCOA105_005 - Caso de teste 005                            
    # Inclusão de totais da planilha orçamentária por operação        
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44147
    # 17/09/2019                                                      
    ###############################################################################

    def test_PCOA105_005(self):
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Operação", True)
        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Total Por  ? ", "Total por Oper.")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado Oper.")
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Entidade Origem  ? ", "AKF")
        self.oHelper.SetButton("Finalizar")
        
        self.oHelper.SearchBrowse("M PR 01 009")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "009")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por Oper.")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse("M PR 01 010")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "010")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado Oper.")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    ##############################################################################
    # test_PCOA105_006 - Caso de teste 006                            
    # Inclusão de totais da planilha orçamentária por unidade         
    #  orçamentaria                                                   
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44145
    # 17/09/2019                                                      
    ##############################################################################

    def test_PCOA105_006(self):
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Unidade Orçamentária", True)
        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Total Por  ? ", "Total por Unidade Or")
        self.oHelper.SetValue("Acumulado Por  ? ", "Acumulado Unidade Or")
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Entidade Origem  ? ", "AMF")
        self.oHelper.SetButton("Finalizar")
        
        self.oHelper.SearchBrowse("M PR 01 011")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "011")
        self.oHelper.CheckResult("AKK_DESCRI", "Total por Unidade Or")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse("M PR 01 012")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("AKK_COD", "012")
        self.oHelper.CheckResult("AKK_DESCRI", "Acumulado Unidade Or")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
