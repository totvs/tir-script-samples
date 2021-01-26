from tir import Webapp
import unittest

class PCOXPNJ(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '26/02/2019', 'T1', 'M SP 01 ')
        inst.oHelper.Program('PCOA490')
        inst.oHelper.AddParameter("MV_PCOVSAL", "", "GV")
        inst.oHelper.SetParameters()
    
    #Inclusao
    @classmethod
    def test_PCOXPNJ_CT001(self):   ##gerar custos diretos

        codigoCT004 = 'PCOA49000000017'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA490005PA-CUSTO DIRETO - PCO CONTROL    ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Gerar Custos Diretos', right_click=False)#Excluir Despesas Diretas

        self.oHelper.ClickLabel('Estrutura')
        self.oHelper.SetValue('De Tipo  ?','Pa')
        self.oHelper.SetValue('Até Tipo  ?','SV')
        self.oHelper.ClickLabel('Custo Standard')

        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()

    def test_PCOXPNJ_CT002(self):       ##Alterar Distribuição

        codigoCT004 = 'PCOA49000000018'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','01-Receitas',name_attr=True)
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('PCOA4900002-SQUAD CONTROL PCOA490           ',right_click=True)
        self.oHelper.ClickMenuPopUpItem('Alterar Distribuição ', right_click=False)

        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('01/01/2020 - 30/06/2020','50,00')
        self.oHelper.SetValue('01/07/2020 - 31/12/2020','100,00')

        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('01/01/2020 - 30/06/2020','50,00')
        self.oHelper.SetValue('01/07/2020 - 31/12/2020','100,00')

        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.ClickLabel('Custo Standard')
        self.oHelper.ClickLabel('Estrutura')
        self.oHelper.SetValue('Custo Standard',True,position=2)
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue()


    def test_PCOXPNJ_CT003(self):   ##gerar planilha

        codigoCT004 = 'PCOA49000000018'
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Outras Ações', 'Gerar Planilha')

        self.oHelper.ClickLabel('Sim')

        self.oHelper.SetButton('Ok')

        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')
        self.oHelper.AssertTrue() 


    def test_PCOXPNJ_CT004(self):       ##Alterar Distribuição

        codigoCT004 = 'PLAN00000000020'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','04-Folha de Pagamento'  ,name_attr=True )
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('080001-FOLHA PCOA490 > 00025-DESENVOLVEDOR', right_click=False)
        self.oHelper.ClickIcon('Editar')   

        self.oHelper.SetValue("ALX_CO","PCOA490000CO",grid=True,row=1)
        self.oHelper.SetValue("ALX_CLASSE","000001",grid=True,row=1)
        self.oHelper.SetValue("ALX_CC","080001",grid=True,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.ClickTree('080001-FOLHA PCOA490', right_click=False)
        self.oHelper.ClickTree('00025-DESENVOLVEDOR', right_click=True)

        self.oHelper.ClickMenuPopUpItem('Alterar Distribuição ', right_click=False)

        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('01/01/2020 - 31/01/2020','100,00')
        self.oHelper.SetValue('01/02/2020 - 29/02/2020','100,00')
        self.oHelper.SetValue('01/03/2020 - 31/03/2020','100,00')
        self.oHelper.SetValue('01/04/2020 - 30/04/2020','100,00')
        self.oHelper.SetValue('01/05/2020 - 31/05/2020','100,00')

        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('01/01/2020 - 31/01/2020','100,00')
        self.oHelper.SetValue('01/02/2020 - 29/02/2020','100,00')
        self.oHelper.SetValue('01/03/2020 - 31/03/2020','100,00')
        self.oHelper.SetValue('01/04/2020 - 30/04/2020','100,00')
        self.oHelper.SetValue('01/05/2020 - 31/05/2020','100,00')

        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','04-Folha de Pagamento'  ,name_attr=True )
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('080001-FOLHA PCOA490 > 00025-DESENVOLVEDOR', right_click=True)

        self.oHelper.ClickMenuPopUpItem('Gerar verbas Relacionadas', right_click=False)

        self.oHelper.SetValue('MV_PAR01','R490'  ,name_attr=True )
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()


    def test_PCOXPNJ_CT005(self):       ##Alterar Distribuição

        codigoCT004 = 'PLAN00000000021'

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','04-Folha de Pagamento'  ,name_attr=True )
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('080001-FOLHA PCOA490 > 00025-DESENVOLVEDOR', right_click=False)
        self.oHelper.ClickIcon('Editar')   

        self.oHelper.SetValue("ALX_CO","PCOA490000CO",grid=True,row=1)
        self.oHelper.SetValue("ALX_CLASSE","000001",grid=True,row=1)
        self.oHelper.SetValue("ALX_CC","080001",grid=True,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.ClickTree('080001-FOLHA PCOA490', right_click=False)
        self.oHelper.ClickTree('00025-DESENVOLVEDOR', right_click=True)

        self.oHelper.ClickMenuPopUpItem('Alterar Distribuição ', right_click=False)

        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('01/01/2020 - 31/01/2020','100,00')
        self.oHelper.SetValue('01/02/2020 - 29/02/2020','100,00')
        self.oHelper.SetValue('01/03/2020 - 31/03/2020','100,00')
        self.oHelper.SetValue('01/04/2020 - 30/04/2020','100,00')
        self.oHelper.SetValue('01/05/2020 - 31/05/2020','100,00')

        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetValue('01/01/2020 - 31/01/2020','100,00')
        self.oHelper.SetValue('01/02/2020 - 29/02/2020','100,00')
        self.oHelper.SetValue('01/03/2020 - 31/03/2020','100,00')
        self.oHelper.SetValue('01/04/2020 - 30/04/2020','100,00')
        self.oHelper.SetValue('01/05/2020 - 31/05/2020','100,00')

        self.oHelper.SetButton('Avançar >>')
        self.oHelper.SetButton('Avançar >>')

        self.oHelper.SetButton('Finalizar')

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Planejar')

        self.oHelper.WaitShow('Tipo de Planejamento ? ')
        self.oHelper.SetValue('MV_PAR01','04-Folha de Pagamento'  ,name_attr=True )
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickTree('080001-FOLHA PCOA490 > 00025-DESENVOLVEDOR', right_click=True)

        self.oHelper.ClickMenuPopUpItem('Gerar Grupo Verba Salarios', right_click=False)

        self.oHelper.SetValue('MV_PAR01','000010'  ,name_attr=True )
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("X")
        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()

    def test_PCOXPNJ_CT006(self):   ##gerar planilha

        codigoCT004 = 'PLAN00000000025'
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Outras Ações', 'Gerar Planilha')

        self.oHelper.ClickCheckBox("Gerar Receita", 1)
        self.oHelper.ClickCheckBox("Gerar Despesa", 1)
        self.oHelper.ClickCheckBox("Gerar Mov.não Oper.", 1)
        self.oHelper.ClickCheckBox("Gerar Folha de Pag.", 1)

        self.oHelper.ClickLabel('Sim')

        self.oHelper.SetButton('Ok')
        

        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue()


    def test_PCOXPNJ_CT007(self):   ##gerar planilha

        codigoCT004 = 'PLAN00000000026'
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT004}0001')
        
        self.oHelper.SetButton('Outras Ações', 'Gerar Planilha')

        """ self.oHelper.ClickCheckBox("Gerar Receita", 1)
        self.oHelper.ClickCheckBox("Gerar Despesa", 1)
        self.oHelper.ClickCheckBox("Gerar Mov.não Oper.", 1)
        self.oHelper.ClickCheckBox("Gerar Folha de Pag.", 1) """

        self.oHelper.ClickLabel('Sim')

        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Sim')

        self.oHelper.WaitShow('Cadastro de Planejamento Orçamentário')

        self.oHelper.AssertTrue() 

    
    

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    