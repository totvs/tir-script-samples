from tir import Webapp
import unittest


class CTBA270(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "29/06/2015", "T1", "M SP 02 ", "34")

        inst.oHelper.Program("CTBA270")

        

        
     ###########################################################################################
    # Caso de teste 001 - Incluir Rateio                                                       #
    # 29/08/2019                                                                               #
    ###########################################################################################

    def test_CTBA270_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 02")
        self.oHelper.SetValue("Codigo Rateio", "CTLR02")
        self.oHelper.SetValue("Descricao", "Rateio Incluido")
        self.oHelper.SetValue("Tipo", "1 - Movimento Mes")
        #self.oHelper.SetValue("Perc. Base","100,00")

        self.oHelper.SetValue("Ctq_CtOri", "11101001", name_attr=True)
        self.oHelper.SetValue("cCtq_CtPar", "11101001", name_attr=True)

        self.oHelper.SetValue("cCtq_CCOri", "01101", name_attr=True)
        self.oHelper.SetValue("cCtq_CCPar", "01101", name_attr=True)

        self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "1110100101", grid=True, row=1)
        self.oHelper.SetValue("CTQ_CCCPAR", "0110101", grid=True, row=1)
        self.oHelper.SetValue("CTQ_VALOR", "80,00", grid=True, row=1)

        self.oHelper.LoadGrid()
        self.oHelper.SetKey("Down", grid=True)
        #self.oHelper.SetFocus("CTQ_CTCPAR", grid_cell=True,row_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "1110100102", grid=True, row=2)
        self.oHelper.SetValue("CTQ_CCCPAR", "0110102", grid=True, row=2)
        self.oHelper.SetValue("CTQ_VALOR", "20,00", grid=True, row=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    ###########################################################################################
    # Caso de teste 002 - Alteração de centro de custo                                        #
    # 29/08/2019                                                                              #
    ###########################################################################################

    def test_CTBA270_002(self):
        self.oHelper.SetButton("Outras Ações", "Legenda")

        self.oHelper.WaitShow("Desbloqueado e Indice atualizado")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Outras Ações", "Log Proc")
        self.oHelper.SetButton("Detalhes")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sair")
        self.oHelper.AssertTrue()

    ###########################################################################################
    # Caso de teste 003 - Alteração de centro de custo                                        #
    # 29/08/2019                                                                              #
    ###########################################################################################
    def test_CTBA270_003(self):

        self.oHelper.AddParameter("MV_CTBHRAT","","1")
        self.oHelper.SetParameters()
        self.oHelper.SearchBrowse("D MG 01 TR0003")
        self.oHelper.SetButton("Alterar")

        self.oHelper.WaitShow("Rateios Off-Line - ALTERAR")
        self.oHelper.SetValue("CTQ_CCCPAR", "CCCTB270A", grid=True, row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("cCtq_Rateio", "TR0003", name_attr=True)
        self.oHelper.CheckResult("cCtq_Tipo", "1 - Movimento Mes", name_attr=True)
        self.oHelper.CheckResult("cCtq_CtOri", "OCTBA27001", name_attr=True)
        self.oHelper.CheckResult("cCtq_CtPar", "PCTBA27001", name_attr=True)

        self.oHelper.CheckResult("CTQ_CCCPAR", "CCCTB270A", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue()



     ###########################################################################################
    # Caso de teste 004 - #Inclusão de rateio com parametro MV_REDUZID = 1 passando no         #
    #    campo CTQ_CCPAR ( 2 VEZES)Alteração de centro de custo                                #
    #    https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T43763            #
    #                                                                                          #
    ###########################################################################################

    def test_CTBA270_004(self):
        self.oHelper.AddParameter("MV_REDUZID","","S")
        self.oHelper.AddParameter("MV_CTBCACH","","1")
        
        self.oHelper.SetParameters()

        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 02")
        self.oHelper.SetValue("Codigo Rateio", "CTB279")
        self.oHelper.SetValue("Descricao", "CTB270_REDUZIDO")
        self.oHelper.SetValue("Tipo", "1 - Movimento Mes")
        self.oHelper.SetValue("Perc. Base","100,00")

        self.oHelper.SetValue("Ctq_CtOri", "203010100", name_attr=True)
        

        #self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "203010100", grid=True, row=1)
        self.oHelper.SetValue("CTQ_VALOR", "101,34", grid=True, row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "203010100", grid=True, row=1)
        
        
        self.oHelper.LoadGrid()
              
                
       
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()


    ###############################################################################################
    # Caso de teste 005 - #Inclusão de rateio com parametro MV_REDUZID = 1 MV_CTBCASH = 1         #
    #                         Digitando o código reduzido                                         #
    #     https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T43827              #
    #                                                                                             # 
    #                                                                                             #
    ###############################################################################################

    def test_CTBA270_005(self):
        self.oHelper.AddParameter("MV_REDUZID","","S")
        self.oHelper.AddParameter("MV_CTBCACH","","1")
        self.oHelper.SetParameters()
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 02")
        self.oHelper.SetValue("Codigo Rateio", "CTB271")
        self.oHelper.SetValue("Descricao", "CTB271_REDUZIDO")
        self.oHelper.SetValue("Tipo", "1 - Movimento Mes")
        self.oHelper.SetValue("Perc. Base","100,00")

        self.oHelper.SetValue("Ctq_CtOri", "203010100", name_attr=True)
        

        self.oHelper.LoadGrid()
        self.oHelper.SetValue("CTQ_CTCPAR", "203010100", grid=True, row=1)
        self.oHelper.SetValue("CTQ_VALOR", "200,34", grid=True, row=1)
        
        self.oHelper.LoadGrid()
        #self.oHelper.SetKey("Down", grid=True)
        
            
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue()

    ###############################################################################################
    # Caso de teste 006 - #Inclusão de rateio com centro de custo obrigatório                     #
    #                      Não inserindo o Centro de custo antes do alerta                        #
    #     https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/171512                    #
    #                                                                                             # 
    ###############################################################################################

    def test_CTBA270_006(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        #Cabeçalho
        self.oHelper.SetValue("Codigo Rateio", "R23883")
        self.oHelper.SetValue("Descricao", "CTA CC OBRIGAT")
        self.oHelper.SetValue("Tipo", "1 - Movimento Mes")
        self.oHelper.SetValue("Perc. Base","100,00")

        #Origem
        self.oHelper.SetValue("Ctq_CtOri", "CTBA28150002", name_attr=True)
        
        #Partida
        self.oHelper.SetValue("cCtq_CtPar", "CTBA28130002", name_attr=True)

        #Contra partida
        self.oHelper.SetValue("CTQ_CTCPAR", "CTBA28130001", grid=True, row=1)
        self.oHelper.SetValue("CTQ_VALOR", "100,00", grid=True, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        #Tela de alerta
        self.oHelper.SetButton("Não")

        #Correção dos campos não preenchidos
        #Origem
        self.oHelper.SetValue("cCtq_CCOri", "CTB270501", name_attr=True)

        #Partida
        self.oHelper.SetValue("cCtq_CCPar", "CTB270302", name_attr=True)

        #Contra partida
        self.oHelper.SetValue("CTQ_CCCPAR", "CTB270301", grid=True, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        #Ao salvar, a rotina abre novamente a tela de inclusão
        self.oHelper.SetButton("Cancelar")

        #Conferencia de resultados

        #Posicionar no rateio incluído
        #Filial+Cod Rateio
        self.oHelper.SearchBrowse("D MG 01 R23883")
        self.oHelper.SetButton("Visualizar")
        
        #Cabeçalho
        self.oHelper.CheckResult("Codigo Rateio", "R23883")

        #Origem
        self.oHelper.CheckResult("Ctq_CtOri", "CTBA28150002", name_attr=True)
        self.oHelper.CheckResult("cCtq_CCOri", "CTB270501", name_attr=True)

        #Partida
        self.oHelper.CheckResult("cCtq_CtPar", "CTBA28130002", name_attr=True)
        self.oHelper.CheckResult("cCtq_CCPar", "CTB270302", name_attr=True)

        #Contra partida
        self.oHelper.CheckResult("CTQ_CTCPAR", "CTBA28130001", grid=True, line=1)
        self.oHelper.CheckResult("CTQ_CCCPAR", "CTB270301", grid=True, line=1)
        self.oHelper.CheckResult("CTQ_VALOR", "100,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
