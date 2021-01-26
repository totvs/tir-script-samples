from tir import Webapp
import unittest

class PCOA490(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '26/02/2019', 'T1', 'M SP 01 ')
        inst.oHelper.Program('PCOA490')
    
    #Inclusao
    @classmethod
    def test_PCOA490_CT001(self):

        codigoCT001 = '000000000000003'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 01')

        self.oHelper.SetValue('ALV_CODIGO', codigoCT001)
        self.oHelper.SetValue('ALV_DESCRI', '00PCO INCLUSAO')
        self.oHelper.SetValue('ALV_TPPERI', '6'             )
        self.oHelper.SetValue('ALV_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('ALV_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('ALV_CTRUSR', '1'             )

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT001}0001')

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult('ALV_CODIGO', codigoCT001      )
        self.oHelper.CheckResult('ALV_DESCRI', '00PCO INCLUSAO' )
        self.oHelper.CheckResult('ALV_TPPERI','6'               )
        self.oHelper.CheckResult('ALV_INIPER','01/01/2019'      )
        self.oHelper.CheckResult('ALV_FIMPER','31/12/2019'      )
        self.oHelper.CheckResult('ALV_CTRUSR','1'               )

        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()
    
    #Alteração
    @classmethod
    def test_PCOA490_CT002(self):

        codigoCT002 = '000000000000004'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT002}0001')
        
        self.oHelper.SetButton('Outras ações', 'Alterar')

        self.oHelper.SetValue('ALV_DESCRI', '00PCO ALTERADO')
        self.oHelper.SetValue('ALV_TPPERI', '5'              )
        self.oHelper.SetValue('ALV_INIPER', '01/01/2019'     )
        self.oHelper.SetValue('ALV_FIMPER', '30/06/2019'     )
        self.oHelper.SetValue('ALV_CTRUSR', '1'              )

        self.oHelper.SetButton('Salvar')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT002}0001')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.CheckResult('ALV_CODIGO', codigoCT002      )
        self.oHelper.CheckResult('ALV_DESCRI', '00PCO ALTERADO' )
        self.oHelper.CheckResult('ALV_TPPERI','5'               )
        self.oHelper.CheckResult('ALV_INIPER','01/01/2019'      )
        self.oHelper.CheckResult('ALV_FIMPER','30/06/2019'      )
        self.oHelper.CheckResult('ALV_CTRUSR','1'               )

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    #Exclusao
    @classmethod
    def test_PCOA490_CT003(self):
        
        codigoCT003 = '000000000000005'
        
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT003}0001')

        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Sim')
        
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT003}0001')

        self.oHelper.AssertTrue()

    #Mudança de grid, nas linhas e ao salvar
    @classmethod
    def test_PCOA490_CT004(self):

        codigoCT004 = '000000000000010'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','02-Despesas',name_attr=True)

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('9001-DESP. AUTOMACAO')
        self.oHelper.ClickIcon('Editar')        

        ##Validando ao mudar de linha
        self.oHelper.SetValue("ALX_CLASSE","000001",grid=True,row=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("UP")
        self.oHelper.CheckResult("ALX_CLASSE","000001",grid=True,line=2)
        self.oHelper.LoadGrid()

        ##Validando ao mudar de linha e Confirmar
        self.oHelper.SetValue("ALX_CLASSE","000002",grid=True,row=2)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("ALX_CLASSE","000002",grid=True,line=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("UP")

        self.oHelper.SetValue("ALX_CLASSE","000001",grid=True,row=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("UP")
        self.oHelper.CheckResult("ALX_CLASSE","000001",grid=True,line=2)
        self.oHelper.LoadGrid()

        #self.oHelper.WaitShow
        self.oHelper.SetButton("Confirmar")
        self.oHelper.LoadGrid()

        ###Aguardando automação
        self.oHelper.ClickIcon('Visualizar Rateio') 
        self.oHelper.SetButton("ok")
        self.oHelper.ClickTree('9001-DESP. AUTOMACAO',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Visualizar Distribuição ', right_click=False)
        self.oHelper.SetButton("Sair")

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()
    

    def test_PCOA490_CT005(self):

        codigoCT004 = 'PCOA490000000001'
        

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','001-Receitas',name_attr=True)

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA49000000001-PCOA49000000001 SQUAD CONTROL                                                   ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Adicionar Produto', right_click=False)
        self.oHelper.SetValue('Produto de ?','PCOA49000000004',name_attr=False)
        self.oHelper.SetValue('Produto ate ?','PCOA49000000004',name_attr=False)  
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA49000000004-PCOA490 RATEIO RECEITA        ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Receita Direta', right_click=False)
        self.oHelper.ClickTree('PCOA49000000004-PCOA490 RATEIO RECEITA        ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Produto', right_click=False)

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT008(self): ## Gerar despesa direta

        codigoCT004 = 'PCOA49000000003'
        

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','002-Despesas',name_attr=True)    

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('TIND-DESPESAS INDIRETAS  ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Gerar Despesas Diretas    ', right_click=False)#Excluir Despesas Diretas
        self.oHelper.SetValue('Regra Rec. Diretas ?','000010',name_attr=False)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Avançar')
        self.oHelper.SetButton('Avançar')
        self.oHelper.SetValue('Valor a ser rateado ? ','1000,00',name_attr=False)
        self.oHelper.SetButton('Avançar')
        self.oHelper.SetButton('Avançar')
        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT009(self):  ##Excluir despesas indiretas e excluir tipo de despesa

        codigoCT004 = '000000000000010'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','02-Despesas',name_attr=True)

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('9001-DESP. AUTOMACAO',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Despesas Indiretas', right_click=False)#Excluir Despesas Diretas
        self.oHelper.ClickTree('9001-DESP. AUTOMACAO',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Tipo de Despesa', right_click=False)

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT010(self): ## Incluir Rateio

        codigoCT004 = 'PCOA49000000007'
        

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        # self.oHelper.ClickTree('PCOA49000000001-PCOA490 -> REGRAS             ',right_click=False)
        self.oHelper.ClickLabel('PCOA49000000002-PCOA490 RECEITAS DIRETAS      ')

        self.oHelper.ClickIcon('Visualizar Rateio') 
        self.oHelper.SetButton("X")

        self.oHelper.ClickIcon('Incluir Rateio')

        self.oHelper.SetValue('MV_PAR01','PCX',name_attr=True)
        
        self.oHelper.CheckHelp(text='REGNOIS',button='Fechar')
        self.oHelper.SetValue('MV_PAR01','PCO',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Ratear')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()


    def test_PCOA490_CT011(self): ## Excluir Rateio

        codigoCT004 = 'PCOA49000000007'
        

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        # self.oHelper.ClickTree('PCOA49000000001-PCOA490 -> REGRAS             ',right_click=False)
        self.oHelper.ClickLabel('PCOA49000000002-PCOA490 RECEITAS DIRETAS      ')

        self.oHelper.ClickIcon('Excluir Rateio')
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT012(self): ## Gerar despesa Indiretas

        codigoCT004 = 'PCOA49000000011'
        

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','02-Despesas',name_attr=True)    

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('TIND-DESPESAS INDIRETAS  ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Gerar Despesas Indiretas', right_click=False)#Excluir Despesas Diretas
        self.oHelper.SetValue('Regra Desp. Indiretas ?','000010',name_attr=False)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Avançar')
        self.oHelper.SetButton('Avançar')
        self.oHelper.SetValue('Valor a ser rateado ? ','1000,00',name_attr=False)
        self.oHelper.SetButton('Avançar')
        self.oHelper.SetButton('Avançar')
        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT013(self): ## Excluir despesa Indiretas

        codigoCT004 = 'PCOA49000000012'
        

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')

        self.oHelper.SetValue('MV_PAR01','02-Despesas',name_attr=True)    

        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('TIND-DESPESAS INDIRETAS  ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Despesas Indiretas', right_click=False)#Excluir Despesas Diretas

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()


    def test_PCOA490_CT014(self): ## Gerar Custos Diretos

        codigoCT004 = 'PCOA49000000007'

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA49000000002-PCOA490 RECEITAS DIRETAS      ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Gerar Custos Diretos', right_click=False)#Excluir Despesas Diretas

        self.oHelper.ClickLabel('Produto')
        
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT015(self): ## GERAR RECEITA RELACIONADA

        codigoCT004 = 'PCOA49000000007'

        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA49000000002-PCOA490 RECEITAS DIRETAS      ',right_click=True)
        # self.oHelper.ClickLabel('PCOA49000000002-PCOA490 RECEITAS DIRETAS      ')
        self.oHelper.ClickMenuPopUpItem('Gerar Receitas Relacionadas', right_click=False)#Excluir Despesas Diretas

        self.oHelper.SetValue('Regra Rec. Relacionadas ?','000001')

        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOA490_CT016(self): ## GERAR RECEITAS 

        ## Alterar dados de acordo com cadadtro do luis
        codigoCT004 = 'PCOA49000000013'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA4900001-SQUAD CONTROL PCOA490         ',right_click=True)
        # self.oHelper.ClickLabel('PCOA49000000002-PCOA490 RECEITAS DIRETAS      ')
        self.oHelper.ClickMenuPopUpItem('Gerar Receitas ', right_click=False)#Excluir Despesas Diretas

        self.oHelper.SetValue('Regra Rec. Diretas ?','RDESP ')

        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Valor a ser rateado ? ','50,00')
        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()


    def test_PCOA490_CT017(self): ## Gera movimento relacionado

        codigoCT004 = 'PCOA49000000014'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA4900002-SQUAD CONTROL PCOA490           ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Gerar Movimentos Relacionados', right_click=False)#Excluir Despesas Diretas
        self.oHelper.SetFocus('Regra Mov. Relacionados ?',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse('AM5001')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()


    def test_PCOA490_CT018(self): ## Reajustar Receita


        codigoCT004 = 'PCOA49000000014'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA4900002-SQUAD CONTROL PCOA490           ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Reajustar Receita', right_click=False)  #  Excluir Despesas Diretas

        self.oHelper.SetValue('Valor ou Percentual ? ','1.000,00')
        self.oHelper.SetValue('Data Inicial Periodo ? ','01/01/2020')
        self.oHelper.SetValue('Data Final do Periodo ? ','31/12/2020')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()

    def test_PCOA490_CT019(self): ## Gerar movimento nao operacional


        codigoCT004 = 'PCOA49000000014'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','03-Não Operacionais',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA49000000014-RECEITAS MOVIMENTO RELACIONADOS                                                 ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Adicionar Movimentos não operacionais', right_click=False)  #  Excluir Despesas Diretas

        self.oHelper.SetValue('Movimentos de ? ?','MNOP')
        self.oHelper.SetValue('Movimentos ate ? ?','MNOP')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()

    def test_PCOA490_CT020(self): ## Gerar distribuição 


        codigoCT004 = 'PCOA49000000015'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','03-Não Operacionais',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('MNOP-MOVIMENTO NAO OPERACIONAL',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Gerar Distribuição', right_click=False)  #  Excluir Despesas Diretas

        self.oHelper.SetValue('Regra Mov. Não Operac. ?','RDESP')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('Valor a ser rateado ? ','2.000,00')
        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()

    def test_PCOA490_CT021(self): ## Excluir distribuição e movimento nao operacional


        codigoCT004 = 'PCOA49000000016'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','03-Não Operacionais',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('MNOP-MOVIMENTO NAO OPERACIONAL',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Visualizar Distribuição ', right_click=False)  
        self.oHelper.SetButton('Sair')

        self.oHelper.ClickTree('MNOP-MOVIMENTO NAO OPERACIONAL',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Movimento não operacional', right_click=False)  
        self.oHelper.SetButton('OK')

        self.oHelper.ClickTree('MNOP-MOVIMENTO NAO OPERACIONAL',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Distribuição', right_click=False)  

        self.oHelper.ClickTree('MNOP-MOVIMENTO NAO OPERACIONAL',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Excluir Movimento não operacional', right_click=False)  

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()



    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    