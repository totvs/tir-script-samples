from tir import Webapp
import unittest

class ATFA012(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA012")
            
        inst.oHelper.AddParameter("MV_ULTDEPR","", "20160331")
        inst.oHelper.AddParameter("D RJ 02 MV_ULTDEPR", "", "19801231")
        inst.oHelper.AddParameter("MV_ALTLCTO", "", "N")
        inst.oHelper.AddParameter("MV_PRELAN", "", "S")
        inst.oHelper.SetParameters()

    def test_ATFA012_103(self):
        
        #Posiciona no registro
        codigo = "ATF0000005001    "
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "
        #Botão Excluir Lote
        self.oHelper.SetButton("Outras Ações", "Excluir Lote")

        #Preenche os perguntes    
        self.oHelper.SetValue("MV_PAR01","ATF0000005"	)	#Do codigo  
        self.oHelper.SetValue("MV_PAR02","ATF0000005"	)	#Até o Codigo
        self.oHelper.SetValue("MV_PAR03","001"		)	#Do Item
        self.oHelper.SetValue("MV_PAR04","001"	    )	#Ate o Item
        self.oHelper.SetValue("MV_PAR05","01/11/2015" )	#Da Data de Aquisição STOD("20151101")
        self.oHelper.SetValue("MV_PAR06","01/11/2015" )	#Até a data de Aquisicao
        
        self.oHelper.SetButton("OK")
        #seleciona
        self.oHelper.ClickGridHeader(column=1, column_name='')
        
        self.oHelper.SetButton("X") 

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados")    

        self.oHelper.AssertTrue()

    def test_ATFA012_001(self):
        
        #Posiciona no registro
        codigo = "ATF0000005001    "
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "
        #Botão Excluir Lote
        self.oHelper.SetButton("Outras Ações", "Excluir Lote")

        #Preenche os perguntes    
        self.oHelper.SetValue("MV_PAR01","ATF0000005"	)	#Do codigo  
        self.oHelper.SetValue("MV_PAR02","ATF0000005"	)	#Até o Codigo
        self.oHelper.SetValue("MV_PAR03","001"		)	#Do Item
        self.oHelper.SetValue("MV_PAR04","001"	    )	#Ate o Item
        self.oHelper.SetValue("MV_PAR05","01/11/2015" )	#Da Data de Aquisição STOD("20151101")
        self.oHelper.SetValue("MV_PAR06","01/11/2015" )	#Até a data de Aquisicao
        
        self.oHelper.SetButton("OK")
        #seleciona
        self.oHelper.ClickBox("Cod. do Bem","ATF0000005")        
        self.oHelper.SetButton("Confirmar") 

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados")    

        self.oHelper.AssertTrue()

    def test_ATFA012_002(self):
        #Posiciona no registro
        self.oHelper.SearchBrowse("D MG 01 ATFR033 ", "Filial+cod. do Bem + Item") #"D MG 01 ATF0000005 001 "
        #Botãoo Copia
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("D MG 01 ATFR033 ", "Filial+cod. do Bem + Item") #"D MG 01 ATF0000005 001 "
        self.oHelper.SetButton("Outras Ações", "Copia")
        #self.oHelper.SetButton("Copia")

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados")
        #Botão Copia
        self.oHelper.SetButton("Outras Ações", "Múltiplos")
        #self.oHelper.SetButton("Múltiplos")

        #numero de multiplos
        self.oHelper.SetValue('Número de Bens', "3") #nbens
        self.oHelper.SetButton("Ok")

        #preenche codigo e item do bem
        self.oHelper.SetValue('Cod. do Bem', 'ATVMTL003')
        self.oHelper.SetValue('Item', '0001')
        self.oHelper.SetValue('Num.Plaqueta', 'ATVMTL003')
        #Confirma
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        #Salva Lançamento padrão
        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()

    def test_ATFA012_003(self):

        codigo =  'MS01_TR'

        self.oHelper.SearchBrowse(f"D MG 01 {codigo}")

        self.oHelper.SetButton("Outras ações", "Converte Método")
        #Inicio wizard
        self.oHelper.SetButton("Avançar")
        #Tela 1 - Checkbox
        self.oHelper.SetFocus("", grid_cell=True, row_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Finalizar")
        #Tela 2 - Conversão de Métodos de depreciação
        self.oHelper.SetValue("N3_TPDEPR", "7 - Linear com Valor Max. Depreciacao", grid=True)
        self.oHelper.SetValue("N3_VMXDEPR", "4.000,00", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")

        self.oHelper.SearchBrowse(f"D MG 01 {codigo}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_CBASE", codigo)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigo)
        self.oHelper.CheckResult("N1_CHAPA", "MS01_TR")
        self.oHelper.CheckResult("Tipo deprec", "Linear com Valor Max. Depreciacao", grid=True, line=1)
        self.oHelper.CheckResult("Conta", "ATF012TC", grid=True, line=1)
        self.oHelper.CheckResult("Val Orig M1", "5.000,00", grid=True, line=1)
        self.oHelper.CheckResult("Vl Max Depre", "4.000,00", grid=True, line=1)
        self.oHelper.CheckResult("Tipo deprec", "Linear", grid=True, line=2)
        self.oHelper.CheckResult("Conta", "ATF012TC", grid=True, line=2)
        self.oHelper.CheckResult("Val Orig M1", "5.000,00", grid=True, line=2)
        self.oHelper.LoadGrid()    

        self.oHelper.SetButton("Fechar")    

        self.oHelper.AssertTrue()


    ##########################################################
    # Caso de teste 004 - Inclusão de ativo com grupo de bens#
    # Incluir ativo com grupo de bens e trocar o grupo de    #
    # bens antes de confirmar para reengatilhar a grid.      #
    ##########################################################
    def test_ATFA012_004(self):

        codigoATF = 'ATFTIR009'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 01 ")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("N1_GRUPO", "GAUX")
        self.oHelper.SetValue("N3_VORIG1", "10.000,00", grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("N1_GRUPO", "GTIR")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0091")
        self.oHelper.SetValue("Dt In Deprec", "01042016", grid=True, grid_number=1, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_GRUPO", "GTIR")
        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0091")
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCONTAB", "GB1CTA", grid=True, line=1)
        self.oHelper.CheckResult("N3_CUSTBEM", "GB1CC_BEM", grid=True, line=1)
        self.oHelper.CheckResult("N3_CDEPREC", "GB1DESP", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCDESP", "GB1_CC_DD", grid=True, line=1)
        self.oHelper.CheckResult("N3_SUBCTA", "IC_GBENS", grid=True, line=1)
        self.oHelper.CheckResult("N3_CLVLCON", "GB1_CV_BM", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    #######################################################
    # Caso de teste 005 - Calculo AVP                     #
    # Incluir ativo com Calculo AVP                       #
    #######################################################
    def test_ATFA012_005(self):

        codigoATF = 'ATFTIR007'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 01 ")
        self.oHelper.SetButton("OK")

        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0071")

        self.oHelper.SetValue("N3_TIPO", "10", grid=True, grid_number=1)
        self.oHelper.SetValue("N3_HISTOR", "DEPRECIAAO GERENCIAL", grid=True, grid_number=1)
        self.oHelper.SetValue("N3_CCONTAB", "GB1CTA", grid=True, grid_number=1)

        self.oHelper.SetValue("N3_VORIG1", "10.000,00", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("AVP")

        self.oHelper.SetValue("N1_INDAVP", "01")
        self.oHelper.SetValue("N1_DTAVP", "20/04/2016")

        #Tela calculo AVP
        self.oHelper.SetButton("Outras Ações", "Cálculo AVP")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        #Não há contabilização
        #self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0071")
        #Conferencia linha 1
        self.oHelper.CheckResult("N3_TIPO", "10", grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult("N3_HISTOR", "DEPRECIAAO GERENCIAL", grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult("N3_TPDEPR", "Linear", grid=True, line=1, grid_number=1)
        self.oHelper.CheckResult("N3_CCONTAB", "GB1CTA", grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()

        #Conferencia linha 2
        self.oHelper.CheckResult("N3_TIPO", "14", grid=True, line=2, grid_number=1)
        self.oHelper.CheckResult("N3_TPDEPR", "Linear", grid=True, line=2, grid_number=1)
        self.oHelper.CheckResult("N3_CCONTAB", "GB1CTA", grid=True, line=2, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 006 - Converte método                 #
    # Incluir ativo com grupo de bens e depreciação       #
    # acumulada                                           #
    #######################################################
    def test_ATFA012_006(self):

        codigoATF = 'ATFTIR008'
 
        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 01 ")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("N1_GRUPO", "GAUX")
        self.oHelper.SetValue("N3_VORIG1", "10.000,00", grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue("N1_GRUPO", "GTIR")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0081")
        self.oHelper.SetValue("N3_VRDACM1", "1.000,00", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Dt In Deprec", "01042016", grid=True, grid_number=1, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_GRUPO", "GTIR")
        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0081")
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCONTAB", "GB1CTA", grid=True, line=1)
        self.oHelper.CheckResult("N3_CUSTBEM", "GB1CC_BEM", grid=True, line=1)
        self.oHelper.CheckResult("N3_CDEPREC", "GB1DESP", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCDESP", "GB1_CC_DD", grid=True, line=1)
        self.oHelper.CheckResult("N3_SUBCTA", "IC_GBENS", grid=True, line=1)
        self.oHelper.CheckResult("N3_CLVLCON", "GB1_CV_BM", grid=True, line=1)
        self.oHelper.CheckResult("N3_CLVLCON", "GB1_CV_BM", grid=True, line=1)
        self.oHelper.CheckResult("N3_VRDACM1", "1.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 007 - Inclusão de Ativo com Rateio    #
    # Incluir ativo com grupo de bens e rateio            #
    #######################################################
    def test_ATFA012_007(self):

        codigoATF = 'ATFTIR030'
 
        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 01 ")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("N1_GRUPO", "GTIR")

        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0301")
        self.oHelper.SetValue("N3_VORIG1", "10.000,00", grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Outras Ações", "Rateio")
        self.oHelper.SetValue("NV_PERCEN", "30,00", grid=True, grid_number=1)
        self.oHelper.SetValue("NV_CC", "GB1CC_BEM", grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.SetValue("NV_PERCEN", "70,00", grid=True, grid_number=1)
        self.oHelper.SetValue("NV_CC", "GB1_CC_CD", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        #Salvar contabilização
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_GRUPO", "GTIR")
        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0301")
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCONTAB", "GB1CTA", grid=True, line=1)
        self.oHelper.CheckResult("N3_CUSTBEM", "GB1CC_BEM", grid=True, line=1)
        self.oHelper.CheckResult("N3_CDEPREC", "GB1DESP", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCDESP", "GB1_CC_DD", grid=True, line=1)
        self.oHelper.CheckResult("N3_SUBCTA", "IC_GBENS", grid=True, line=1)
        self.oHelper.CheckResult("N3_CLVLCON", "GB1_CV_BM", grid=True, line=1)
        self.oHelper.CheckResult("N3_RATEIO", "Sim", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 008 - Alteração de Ativo com Rateio   #
    # Alterar rateio do ativo                             #
    #######################################################
    def test_ATFA012_008(self):

        codigoATF = 'ATFTIR015'
 
        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Alterar")

        self.oHelper.WaitShow("Ativo Imobilizado - Ativo Imobilizado")

        self.oHelper.SetButton("Outras Ações", "Rateio")
        #self.oHelper.SetButton("Rateio")
        self.oHelper.SetValue("NV_CC", "GB1_CC_CO", grid=True, grid_number=1, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_GRUPO", "GTIR")
        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0151")
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCONTAB", "GB1CTA", grid=True, line=1)
        self.oHelper.CheckResult("N3_CUSTBEM", "GB1CC_BEM", grid=True, line=1)
        self.oHelper.CheckResult("N3_CDEPREC", "GB1DESP", grid=True, line=1)
        self.oHelper.CheckResult("N3_CCDESP", "GB1_CC_DD", grid=True, line=1)
        self.oHelper.CheckResult("N3_SUBCTA", "IC_GBENS", grid=True, line=1)
        self.oHelper.CheckResult("N3_CLVLCON", "GB1_CV_BM", grid=True, line=1)
        self.oHelper.CheckResult("N3_RATEIO", "Sim", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras Ações", "Rateio")
        self.oHelper.CheckResult("NV_PERCEN", "70,00", grid=True, line=1)
        self.oHelper.CheckResult("NV_CC", "GB1_CC_CO", grid=True, line=1)
        self.oHelper.CheckResult("NV_PERCEN", "30,00", grid=True, line=2)
        self.oHelper.CheckResult("NV_CC", "GB1_CC_CD", grid=True, line=2)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()


        self.oHelper.AssertTrue()
    

    #######################################################
    # Caso de teste 009 - Converte método                 #
    # Incluir ativo com grupo de bens e trocar o grupo de #
    # bens antes de confirmar para reengatilhar a grid.   #
    #######################################################
    def test_ATFA012_009(self):
        
        codigoATF = 'ATFTIR020'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D RJ 02 ")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("N1_GRUPO", "GTIR")
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_AQUISIC", "01/01/1981")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0201")
        self.oHelper.ClickFolder("Valores")
        self.oHelper.SetValue("N3_VORIG1", "999.999.999,00")

        self.oHelper.SetKey("ENTER")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Calcula valor atual do bem?")
        self.oHelper.SetButton("Sim")

        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N3_VORIG1", "0,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 010 - Controle Bens                   #
    # Incluir ativo com Controle terceiro                 #
    #######################################################
    def test_ATFA012_010(self):

        codigoATF = 'ATFTIR081'
        codigoFornec = 'ATFTIR'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 01 ")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("N1_GRUPO", "GAUX")
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0811")
        self.oHelper.SetValue("N1_TPCTRAT", "2 - Terceiro")
        self.oHelper.SetValue("N3_VORIG1", "10.000,00", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras Ações", "Contr.Terceiros")
        #self.oHelper.SetButton("Contr.Terceiros")
        
        self.oHelper.SetValue("NO_FORNEC", codigoFornec)
        self.oHelper.SetValue("NO_LOJA", "01")
        self.oHelper.SetValue("NO_TIPCES", "C - Concessao de direito real de uso")
        self.oHelper.SetValue("NO_VIGINI", "01/04/2016", grid=True, row=1 )
        self.oHelper.SetValue("NO_VIGFIM", "31/12/2016", grid=True, row=1)
        self.oHelper.SetValue("NO_CONTATO", "PAUL LABILE", grid=True, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        #Contabilização
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_GRUPO", "GAUX")
        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0811")
        self.oHelper.CheckResult("N1_FORNEC", codigoFornec)
        self.oHelper.CheckResult("N1_LOJA", "01")
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 011 - Controle Bens                   #
    # Incluir ativo com Controle terceiro                 #
    #######################################################
    def test_ATFA012_011(self):

        codigoATF = 'ATFTIR090'
        codigoCliente = 'AF12TR'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 01 ")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("N1_GRUPO", "GAUX")
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "ATFTIR0901")
        self.oHelper.SetValue("N1_TPCTRAT", "3 - Em Terceiro")
        self.oHelper.SetValue("N3_VORIG1", "10.000,00", grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras Ações", "Cont.em Terceiros")
        #self.oHelper.SetButton("Cont.em Terceiros")
        
        self.oHelper.SetValue("NP_FORNEC", codigoCliente)
        self.oHelper.SetValue("NP_LOJA", "01")
        self.oHelper.SetValue("NP_TIPCES", "C - Concessao de direito real de uso")
        self.oHelper.SetValue("NP_VIGINI", "01/04/2016", grid=True, row=1 )
        self.oHelper.SetValue("NP_VIGFIM", "31/12/2016", grid=True, row=1)
        self.oHelper.SetValue("NP_CONTATO", "PAUL LABILE", grid=True, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        #Contabilização
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N1_GRUPO", "GAUX")
        self.oHelper.CheckResult("N1_CBASE", codigoATF)
        self.oHelper.CheckResult("N1_ITEM", "0001")
        self.oHelper.CheckResult("N1_QUANTD", "1,000")
        self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
        self.oHelper.CheckResult("N1_CHAPA", "ATFTIR0901")
        self.oHelper.CheckResult("N1_FORNEC", codigoCliente)
        self.oHelper.CheckResult("N1_LOJA", "01")
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #######################################################
    # Caso de teste 012 - Importacao Classificacao        #
    # Importação de Classificação de ativos Tipo 10       #
    #######################################################
    def test_ATFA012_012(self):

        codigo = "ATFTIR012 0001"

        #Posiciona no registro
        self.oHelper.SearchBrowse(f"D RJ 01 {codigo}", "Filial+cod. do Bem + Item")     #"D RJ 01 ATFTIR012 0001    "
        #Botão Import Classificação
        self.oHelper.SetButton("Outras Ações", "Import. Classificação")

        self.oHelper.SetBranch("D RJ 01")

        self.oHelper.SetValue("MV_PAR01", "\\baseline\\import_classif.csv", )
        self.oHelper.SetValue("MV_PAR02", "Não", )
        

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Sair")

        self.oHelper.SearchBrowse(f"D RJ 01 {codigo}", "Filial+cod. do Bem + Item") #"D RJ 01 ATFTIR012 0001    "
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("N3_TIPO", "10", grid=True, line=2, name_attr=True)
        self.oHelper.CheckResult("N3_CCONTAB", "102020308", grid=True, line=2, name_attr=True)
        self.oHelper.CheckResult("N3_CUSTBEM", "200200200", grid=True, line=2, name_attr=True)
        self.oHelper.CheckResult("N3_CDEPREC", "102020305", grid=True, line=2, name_attr=True)
        self.oHelper.CheckResult("N3_CCDEPR", "102020306", grid=True, line=2, name_attr=True)
        self.oHelper.CheckResult("N3_VORIG1", "10.000,00", grid=True, line=2, name_attr=True)
        self.oHelper.CheckResult("N3_TXDEPR1", "10,0000", grid=True, line=2, name_attr=True)
        self.oHelper.LoadGrid()
        

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()



    #######################################################
    # Caso de teste 013 - Testes exploratorios            #
    # Testes de interface                                 #
    #######################################################
    def test_ATFA012_013(self):


        #Posiciona no registro
        self.oHelper.SearchBrowse(f"D RJ 01 ATFTIR012", "Filial+num.plaqueta")

        #Botão Import Classificação --Import. Clasificação  
        self.oHelper.SetButton("Outras Ações", "Import. Classificação")

        self.oHelper.SetBranch("D RJ 01")

        self.oHelper.SetButton("Cancelar")

        #Botão Excluir Lote
        self.oHelper.SetButton("Outras Ações", "Excluir Lote")

        self.oHelper.WaitShow("Parametros")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()





    ##########################################################
    # Caso de teste 014 - Inclusão de ativo com grupo de bens#
    # Incluir ativo com grupo de bens e trocar o grupo de    #
    # bens antes de confirmar para reengatilhar a grid.      #
    ##########################################################
    # def test_ATFA012_014(self):
                   
        
    #     self.oHelper.ChangeEnvironment("18/02/2020","T1", "D MG 01 ","57")
    #     self.oHelper.AddParameter("MV_ULTDEPR","", "20191130")
    #     self.oHelper.AddParameter("MV_TIPDEPR", "", "2")
    #     self.oHelper.SetParameters()
       

    #     codigoATF = 'ATFA000018'

    #     self.oHelper.SetButton("Incluir")
    #     self.oHelper.SearchBrowse("D MG 01 ")
    #     self.oHelper.SetButton("OK")
        
                
    #     self.oHelper.SetValue("N1_CBASE", codigoATF)
    #     self.oHelper.SetValue("N1_ITEM", "0001")
    #     self.oHelper.SetValue("N1_AQUISIC", "01/07/2019")
    #     self.oHelper.SetButton("Não")

        
    #     self.oHelper.SetValue("N1_QUANTD", "1,000")
    #     self.oHelper.SetValue("N1_DESCRIC", codigoATF)
    #     self.oHelper.SetValue("N1_CHAPA", "ATFA000018")

    #     self.oHelper.SetValue("N3_TIPO", "01", grid=True, row=1)
    #     self.oHelper.SetValue("N3_HISTOR", "ATFA000018", grid=True, row=1)
    #     self.oHelper.SetValue("N3_CCONTAB", "101010200001", grid=True, row=1)
    #     self.oHelper.SetValue("N3_CDEPREC", "101010200001", grid=True, row=1)
    #     self.oHelper.SetValue("N3_CCDEPR", "101010200002", grid=True, row=1)
    #     self.oHelper.SetValue("N3_CDESP", "101010200001", grid=True, row=1)
    #     self.oHelper.SetValue("N3_CCORREC", "101010200001", grid=True, row=1)
    #     self.oHelper.SetValue("N3_VORIG1", "1000,00", grid=True, row=1)
    #     self.oHelper.SetValue("N3_TXDEPR1", "10,0000", grid=True, row=1)




    #     self.oHelper.LoadGrid()
        
        
    #     self.oHelper.SetButton("Confirmar")
    #     self.oHelper.SetButton("Fechar")

    #     self.oHelper.SearchBrowse(f"D MG 01 {codigoATF}")
    #     self.oHelper.SetButton("Visualizar")

        
        
    #     self.oHelper.CheckResult("N1_CBASE", codigoATF)
    #     self.oHelper.CheckResult("N1_ITEM", "0001")
    #     self.oHelper.CheckResult("N1_AQUISIC", "01/07/2019")

    #     self.oHelper.CheckResult("N1_QUANTD", "1")
    #     self.oHelper.CheckResult("N1_DESCRIC", codigoATF)
    #     self.oHelper.CheckResult("N1_CHAPA", "ATFA000018")          
    #     self.oHelper.CheckResult("N3_TIPO", "01", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_HISTOR", "ATFA000018", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_CCONTAB", "101010200001", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_CDEPREC", "101010200001", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_CCDEPR", "101010200002", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_DESP", "101010200001", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_CC0RREC", "101010200001", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_DINDEPR", "01/03/2020", grid=True, line=1)
    #     self.oHelper.CheckResult("N3_VORIG1", "1000,00", grid=True, line=1)        
    #     self.oHelper.CheckResult("N3_TXDEPR1", "10,0000", grid=True, line=1)


    #     self.oHelper.LoadGrid()

    #     self.oHelper.SetButton("Fechar")

    #     self.oHelper.AssertTrue()

    def test_ATFA012_015(self):
                   
        self.oHelper.AddParameter("MV_PCOINTE", "", "1")
        self.oHelper.SetParameters()
       
        codigoATF = 'TESTE'

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")
        

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")
                
        self.oHelper.SetValue("N1_CBASE", codigoATF)
        self.oHelper.SetValue("N1_ITEM", "0001")
        self.oHelper.SetValue("N1_AQUISIC", "01/04/2016")

        
        self.oHelper.SetValue("N1_QUANTD", "1,000")
        self.oHelper.SetValue("N1_DESCRIC", codigoATF)
        self.oHelper.SetValue("N1_CHAPA", "TESTE")

        self.oHelper.SetValue("N3_TIPO", "01", grid=True, row=1)
        self.oHelper.SetValue("N3_HISTOR", "TESTE", grid=True, row=1)
        self.oHelper.SetValue("N3_CCONTAB", "CTBXATUD", grid=True, row=1)
        self.oHelper.SetValue("N3_VORIG1", "1000,00", grid=True, row=1)
        self.oHelper.SetValue("N3_TXDEPR1", "10,0000", grid=True, row=1)
        self.oHelper.SetValue("N3_VRDACM1", "10,00", grid=True, row=1)

        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        # self.oHelper.SetButton("Confirmar") ## quebro aqui
        self.oHelper.SetButton("Detalhes")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Sair da página")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue()

    def test_ATFA012_016(self): #Visualização de LAUDO
        

        codigo = "LAUDOTIR  0001   "
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "
        self.oHelper.SetButton("Outras Ações", "Laudo")

        self.oHelper.SetButton("Laudo")

        self.oHelper.SetValue('Objeto','0000000046',grid=True,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("x")

        self.oHelper.AssertTrue()

    def test_ATFA012_017(self): 

        self.oHelper.AddParameter("MV_ALTVORI","", ".T.")
        self.oHelper.SetParameters()

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch('D MG 01')

        self.oHelper.SetValue('N1_GRUPO','TIR1',name_attr=True)
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton("Sair da página")

        self.oHelper.AssertTrue()

    def test_ATFA012_018(self):

        self.oHelper.SetButton('x')
        self.oHelper.ChangeEnvironment("01/12/2010","T1", "M PR 02 ","01")

        self.oHelper.AddParameter("MV_ULTDEPR","M PR 02", "20101130")
        self.oHelper.AddParameter("MV_TIPDEPR", "", "1")
        self.oHelper.SetParameters()

        codigo = "ATF_0000020002"
        #Posiciona no registro
        self.oHelper.SearchBrowse(f"M PR 02 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "

        self.oHelper.SetButton("Outras Ações", "Canc.Método")

        self.oHelper.SetButton("Avançar >>")

        self.oHelper.SetFocus('',grid_cell=True,row_number=1)

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    def test_ATFA012_073(self):

        self.oHelper.SetButton('x')
        self.oHelper.ChangeEnvironment("01/12/2010","T1", "M PR 02 ","01")

        self.oHelper.Program("ATFA012")

        codigo = "ATF_0000010001"
        #Posiciona no registro
        self.oHelper.SearchBrowse(f"M PR 02 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "

        self.oHelper.SetButton("Outras Ações", "Converte Método")

        self.oHelper.SetButton("Avançar >>")
        # self.oHelper.ClickBox('', contents_list='Depreciacao Fiscal', select_all=True, grid_number=1)
        # self.oHelper.LoadGrid()
        self.oHelper.SetFocus('',grid_cell=True,row_number=1)

        self.oHelper.SetFocus('',grid_cell=True,row_number=2)

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    def test_ATFA012_019(self):

        codigo = "EXCLUILINH0001"
        #Posiciona no registro
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "

        self.oHelper.SetButton("Alterar")
        # self.oHelper.ClickBox('', contents_list='Depreciacao Fiscal', select_all=True, grid_number=1)
        # self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell('Historico',row=2,grid_number=1)

        self.oHelper.SetKey('Delete',grid=True,grid_number=1)

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados:")

        self.oHelper.AssertTrue()

    def test_ATFA012_101(self):


        codigo = "ATIVOAVP  0001"
        #Posiciona no registro
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "

        self.oHelper.SetButton("Outras Ações", "Converte Método")

        self.oHelper.SetButton("Avançar >>")
        # self.oHelper.ClickBox('', contents_list='Depreciacao Fiscal', select_all=True, grid_number=1)
        # self.oHelper.LoadGrid()
        self.oHelper.SetFocus('',grid_cell=True,row_number=1)

        self.oHelper.SetFocus('',grid_cell=True,row_number=2)

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetValue('Tipo deprec','7 - Linear com Valor Max. Depreciacao',grid=True,row=1)
        self.oHelper.SetValue('Vl Max Depre','100,00',grid=True,row=1)

        self.oHelper.SetValue('Tipo deprec','7 - Linear com Valor Max. Depreciacao',grid=True,row=2)
        self.oHelper.SetValue('Vl Max Depre','100,00',grid=True,row=2)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    def test_ATFA012_102(self):

        self.oHelper.WaitShow("Atualização de Ativos Imobilizados")    

        codigo = "10000000020001"
        #Posiciona no registro
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "

        self.oHelper.SetButton("Outras Ações", "Bloquear/Desb")

        self.oHelper.SetBranch('D MG 01')

        self.oHelper.SetValue('Do Código do Bem ?','1000000002')
        self.oHelper.SetValue('Até o Código do Bem ? ','1000000002')
        self.oHelper.SetValue('Do Item ?','')
        self.oHelper.SetValue('Até o Item ? ','ZZZZ')
        self.oHelper.SetValue('Do Grupo ?','')
        self.oHelper.SetValue('Até o Grupo ? ','ZZZZ')
        self.oHelper.SetValue('Da Data de Aquisição ?','01012015')
        self.oHelper.SetValue('Até a Data de Aquisição ? ','01122020')
        self.oHelper.SetValue('Bloqueia/Desbloq ? ','1-Desbloqueia')

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()

    def test_ATFA012_105(self):

        codigo = "00000000010001"
        
        #Posiciona no registro
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")     #"D MG 01 ATF0000005 001    "

        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Outras Ações", "Responsáveis")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair da página")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
