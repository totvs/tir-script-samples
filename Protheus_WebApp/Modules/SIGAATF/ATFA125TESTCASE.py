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

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SetButton("Solic. Baixa")
        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetFocus('Código',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse(codigoATF)
        self.oHelper.SetButton('OK')
        # self.oHelper.SetValue("cCBASE", codigoATF, name_attr=True)
        self.oHelper.SetFocus('Item',grid_cell=False)
        # self.oHelper.SetValue("cITEM", codigoItem, name_attr=True)
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

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SetButton("Outras Ações", "Solic. Transf.")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetFocus('Código',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse("AT125_AT2")
        self.oHelper.SetButton('OK')
        # self.oHelper.SetValue("cCBASE", "AT125_AT2", name_attr=True) ##alterado para melhora na cobertura de linhas de codigo

        self.oHelper.SetFocus('Item',grid_cell=False)
        # self.oHelper.SetValue("cITEM", "0001", name_attr=True) ##alterado para melhora na cobertura de linhas de codigo

        self.oHelper.SetFocus('Filial Dest.',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SetBranch("D MG 02")
        
        # self.oHelper.SetValue("cFilDest", "D MG 02", name_attr=True) ##alterado para melhora na cobertura de linhas de codigo
        
        

        self.oHelper.ClickFolder("Dados da Solicitacao")
        self.oHelper.SetValue("Hist. Solic.", "TESTCASE TIR 002")
        

        self.oHelper.ClickFolder("Dados do Bem")
        self.oHelper.SetValue("cGeraNF", "2 - Não", name_attr=True)
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
    # Caso de teste 006 - Solicitação de transferencia em #
    # Lote                      #
    #######################################################

    def test_ATFA125_006(self):
        codigoATF = 'TB00000001'

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SetButton("Outras Ações", "Solic. Transf. Lote")
        
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("cBasei", codigoATF, name_attr=True)
        self.oHelper.SetValue("cBasef", codigoATF, name_attr=True)
        self.oHelper.SetValue("cItemi", "0001", name_attr=True)
        self.oHelper.SetValue("cItemf", "0003", name_attr=True)
        
        # self.oHelper.SetValue("cFilDest", "D MG 02", name_attr=True)
        self.oHelper.SetFocus('Filial destino',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SetBranch("D MG 02")

        self.oHelper.SetFocus('Até Item:',grid_cell=False) ##somente para atualizar a grid e liberar campo nota
        
        self.oHelper.SetValue("_cGERANF", "1 - Sim", name_attr=True)
        self.oHelper.SetValue("_cClasNF", "2 - Classificada", name_attr=True)
        self.oHelper.SetValue("_cTesS", "939", name_attr=True)
        self.oHelper.SetValue("_cSerie", "NF1", name_attr=True)
        self.oHelper.SetValue("_cTesE", "339", name_attr=True)
        self.oHelper.SetValue("_cCONDPAG", "000", name_attr=True)
        self.oHelper.SetValue("_cArmaz", "02", name_attr=True)
        self.oHelper.SetValue("Hist. Solic.", "TRANSFERÊNCIA EM PENDENCIA")

        self.oHelper.SetButton("Ok")

        self.oHelper.ClickBox("Item        ",contents_list='0002', grid_number=1,select_all=False)
        self.oHelper.ClickBox("Item        ",contents_list='0003', grid_number=1,select_all=False)
        
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_ATFA125_007(self):

        codigoSol = '000003' 
        codigoATF = 'EXCBAIXA'

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SearchBrowse(f"D MG 01 {codigoSol}{codigoATF}", " Filial+cód. Solic. + Cod. do Bem ...")  

        self.oHelper.SetButton("Outras Ações", "Excluir")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton('Sim')


        self.oHelper.AssertTrue()
    
    def test_ATFA125_003(self):
        self.oHelper.AddParameter("MV_ATFWFM", "", ".T.")
        self.oHelper.SetParameters()

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')
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

        self.oHelper.ClickBox("", grid_number=1,select_all=True)
        
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton('Não')
        self.oHelper.CheckHelp(text='AF125MAIL',button='Fechar')

        self.oHelper.SetButton('Não')
        self.oHelper.CheckHelp(text='AF125MAIL',button='Fechar')
        self.oHelper.SetButton('Não')
        self.oHelper.CheckHelp(text='AF125MAIL',button='Fechar')

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

    def test_ATFA125_004(self):
        codigoSol = '000002'
        codigoATF = 'ATFA126 '

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SearchBrowse(f"D MG 01 {codigoSol}{codigoATF}", " Filial+cód. Solic. + Cod. do Bem ...")  

        self.oHelper.SetButton("Outras Ações", "Excluir")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton('Sim')


        self.oHelper.AssertTrue()


        ##BAIXA EM LOTE
    def test_ATFA125_005(self):

        codigoATF = 'AF125_LOTE'

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SetButton("Outras Ações", "Solic. Baixa Lote")
        self.oHelper.SetBranch("D MG 01")
        
        self.oHelper.SetFocus('Do código',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse(f"{ codigoATF }")
        self.oHelper.SetButton('OK')

        self.oHelper.SetValue('Até',f'{codigoATF}')

        self.oHelper.SetValue('Do item','0001')
        self.oHelper.SetValue('cItemF','0003',name_attr=True)

        self.oHelper.SetButton('Ok')
        self.oHelper.CheckHelp(text='AF125OBG',button='Fechar')

        self.oHelper.SetValue('Hist. Solic.','BAIXA EM LOTE TIR')
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickBox("Item        ",contents_list='0001', grid_number=1,select_all=False)
        # self.oHelper.ClickBox("Item        ",contents_list='0003', grid_number=1,select_all=False)
        

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 008 - Solicitação de baixa com nota   #
    #######################################################
    def test_ATFA125_008(self):

        codigoATF = 'BXMESMANT '
        codigoItem = '0001'

        self.oHelper.WaitShow('Solicitações de baixa e transferência de Ativo')

        self.oHelper.SetButton("Solic. Baixa")
        self.oHelper.SetBranch("D MG 01 ")
        
        self.oHelper.SetFocus('Código',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse(codigoATF)
        self.oHelper.SetButton('OK')
        # self.oHelper.SetValue("cCBASE", codigoATF, name_attr=True)
        self.oHelper.SetFocus('Item',grid_cell=False)
        # self.oHelper.SetValue("cITEM", codigoItem, name_attr=True)
        self.oHelper.SetValue("nQTDBX", "1,000", name_attr=True)
        self.oHelper.SetValue("cCONDPG", "100", name_attr=True)
        self.oHelper.SetValue("nVlVenda", "792,00", name_attr=True)


        self.oHelper.ClickFolder("Dados da Solicitacao")
        self.oHelper.SetValue("Hist. Solic.", "TESTCASE TIR 008")
        self.oHelper.ClickFolder("Dados do Bem")

        self.oHelper.SetValue("Gera NFS", "1 - Sim")
        self.oHelper.SetValue("Cliente", "F00001")
        self.oHelper.SetValue("TES Saida", "939")
        self.oHelper.SetValue("Serie", "NF1")

        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()

    

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

        
