from tir import Webapp
import unittest

class ATFA036(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '01052016', 'T1', 'D MG 01 ')
        inst.oHelper.Program('ATFA036')

        inst.oHelper.AddParameter("MV_ULTDEPR","D MG 01","20160430","20160430","20160430")#Parametro de ultima depreciação 
        inst.oHelper.SetParameters()

    @classmethod
    def test_ATFA036_CT001(self):

        self.oHelper.SearchBrowse('D MG 01 100000000200401')
        #N3_FILIAL+N3_CBASE+N3_ITEM+N3_TIPO+N3_BAIXA+N3_SEQ 

        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult('N1_CBASE', '1000000002')
        self.oHelper.CheckResult('N1_ITEM', '005 ')
        self.oHelper.CheckResult('N1_AQUISIC', '01/12/2015')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def test_ATFA036_CT002(self):

        self.oHelper.SearchBrowse('D MG 01 100000000200401')
        #N3_FILIAL+N3_CBASE+N3_ITEM+N3_TIPO+N3_BAIXA+N3_SEQ 

        self.oHelper.SetButton("Outras Ações", "Visualizar Ativo")
        self.oHelper.CheckResult('N1_CBASE', '1000000002')
        self.oHelper.CheckResult('N1_ITEM', '005 ')
        self.oHelper.CheckResult('N1_AQUISIC', '01/12/2015')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA036_CT003(self):
        #Baixa por Lote parcial 75% - ATFA036L chamado pelo/usado pelo atfa036
        PorcBaixL= "75,00" #Percentual da baixa em lote
        
        self.oHelper.SetButton("Outras ações","Baixa em Lote")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("MV_PAR01","D MG 01")#Filial de ?
        self.oHelper.SetValue("MV_PAR02","D MG 01")#Filial ate ?

        self.oHelper.SetValue("MV_PAR03","")#Grupo de Bens De ?
        self.oHelper.SetValue("MV_PAR04","ZZZZ")#Grupo de Bens Ate ?

        self.oHelper.SetValue("MV_PAR05","ATVL000001")#Codigo do Bem De ?
        self.oHelper.SetValue("MV_PAR06","ATVL000001")#Codigo do Bem Ate ?

        self.oHelper.SetValue("MV_PAR07","")#Item do Bem De ?
        self.oHelper.SetValue("MV_PAR08","ZZZZ")#Item do Bem ate ?

        self.oHelper.SetValue("MV_PAR09","01042016")#Data Aquisicao De ?
        self.oHelper.SetValue("MV_PAR10","01042016")#Data Aquisicao ate ?
        
        self.oHelper.SetValue("Gera Nota Fiscal por ?","Item" )#Gera Nota Fiscal Por

        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("FN8_BAIXA",PorcBaixL)
        self.oHelper.SetValue("Marca/Desmarca Todos",True,name_attr=True)
        self.oHelper.CheckResult("FN8_BAIXA",PorcBaixL)

        self.oHelper.ClickFolder("Dados da NF")
        
        self.oHelper.SetValue("FN8_VALNF",PorcBaixL)
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
              
    @classmethod
    def test_ATFA036_CT004(self):

        self.oHelper.SearchBrowse('D MG 01 ATFA0360001')
        
        self.oHelper.SetButton("Outras Ações", "Baixa em Lote")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.CheckHelp("A036LOT") 
        self.oHelper.CheckHelp("Processamento de baixa em Lote cancelada.") 
        self.oHelper.SetButton("Fechar") 

        self.oHelper.SetButton("Outras Ações","Cancelar")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse('D MG 01 ATFA0360001')
        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult ("FN6_DTBAIXA","")
        self.oHelper.CheckResult ("FN6_BAIXA","")
        self.oHelper.CheckResult ("FN6_QTDBX","")
        self.oHelper.CheckResult ("FN6_PERCBX","")
        
               
        self.oHelper.AssertTrue()


    @classmethod
    def test_ATFA036_CT048(self): 

        self.oHelper.WaitShow('Baixa de Ativos')

        self.oHelper.SetButton("Outras ações","Baixa em Lote")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("MV_PAR01","D MG 01")#Filial de ?
        self.oHelper.SetValue("MV_PAR02","D MG 01")#Filial ate ?

        self.oHelper.SetValue("MV_PAR03","")#Grupo de Bens De ?
        self.oHelper.SetValue("MV_PAR04","ZZZZ")#Grupo de Bens Ate ?

        self.oHelper.SetValue("MV_PAR05","ATF36BXLOT")#Codigo do Bem De ?
        self.oHelper.SetValue("MV_PAR06","ATF36BXLOT")#Codigo do Bem Ate ?

        self.oHelper.SetValue("MV_PAR07","0002")#Item do Bem De ?
        self.oHelper.SetValue("MV_PAR08","0003")#Item do Bem ate ?

        self.oHelper.SetValue("MV_PAR09","01012016")#Data Aquisicao De ?
        self.oHelper.SetValue("MV_PAR10","01122016")#Data Aquisicao ate ?
        
        self.oHelper.SetValue("Gera Nota Fiscal por ?","Código Base" )#Gera Nota Fiscal Por
        self.oHelper.SetValue("Exibe Valores ?","Sim" )

        self.oHelper.SetButton("OK")
        
        self.oHelper.SetValue("FN8_BAIXA",'100,00')
        self.oHelper.SetValue("Marca/Desmarca Todos",True,name_attr=True)

        self.oHelper.ClickFolder("Dados da NF")

        self.oHelper.SetValue('Gerar NF','1 - Sim')
        self.oHelper.SetValue('Série','NF1')
        self.oHelper.SetFocus('Cliente',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse('F00001')
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Valor NF', '400,00')
        self.oHelper.SetValue('Cond. Pagto.','000')
        self.oHelper.SetValue('TES Saída','939')
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.ClickGridCell('Valor',row=9,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse('D MG 01 ATF36BXLOT0002')

        self.oHelper.SetButton("Outras ações","Cancelar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.WaitShow('Baixa de Ativos - CANCELAR')

        self.oHelper.ClickGridCell('Valor',row=1,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.ClickGridCell('Valor',row=2,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA036_CT044(self):

        self.oHelper.SearchBrowse('D MG 01 ATF36CANBX0002')
		
        self.oHelper.SetButton("Outras Ações","Cancelar")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.ClickGridCell('Valor',row=1,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.ClickGridCell('Valor',row=2,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA036_CT045(self):

        self.oHelper.SearchBrowse('D MG 01 ATF36BXLOT0001')
		
        self.oHelper.SetButton("Baixar")
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.SetValue('% Baixa','100,00')
        self.oHelper.ClickFolder('Dados da NF')
        self.oHelper.SetButton("Sim")
        
        self.oHelper.SetValue('Gerar NF','1 - Sim')
        self.oHelper.SetValue('Série','NF1')
        self.oHelper.SetFocus('Cliente',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse('F00001')
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Valor NF/Ven', '500,00')
        self.oHelper.SetValue('Cond. Pagto.','000')
        self.oHelper.SetValue('TES Saída','939')

        self.oHelper.ClickBox('Tipo Ativo',contents_list='01')


        self.oHelper.SetButton("Confirmar")

        self.oHelper.ClickGridCell('Valor',row=5,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.ClickGridCell('Valor',row=6,grid_number=1)
        self.oHelper.SetKey('Delete',grid=True)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA036_CT046(self):

        self.oHelper.SearchBrowse('D MG 01 ATF36BXMN0002')
		
        self.oHelper.SetButton("Visualizar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA036_CT049(self):

        self.oHelper.WaitShow('Baixa de Ativos')

        self.oHelper.SetButton("Outras ações","Cancelar (Multi)")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def test_ATFA036_CT047(self): # FALTA KANOAH

        self.oHelper.WaitShow('Baixa de Ativos')

        self.oHelper.SetKey( key = "F12", wait_show="Parametros", step = 3)
        self.oHelper.SetValue('Visualização ?','Baixas de Ativo')
        self.oHelper.SetButton('OK')

        self.oHelper.SetButton("Baixar")
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.SetFocus('Cod. Bem',grid_cell=False)
        self.oHelper.SetKey('F3',grid=False)
        self.oHelper.SearchBrowse('ATF36BXF13')
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Qtd. Baixa','1,0000',check_value=False)
        self.oHelper.SetButton('Sim')

        self.oHelper.ClickBox('Tipo Ativo',contents_list='01')
        self.oHelper.ClickFolder("Dados da NF")

        self.oHelper.SetValue('Valor NF/Ven','500,00')

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()  

if __name__ == '__main__':
    unittest.main()


    

