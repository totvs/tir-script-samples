#Importes para execução do Teste
from tir import Webapp
import unittest

class FATA080(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAFAT', '11/03/2019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('FATA080')

    '''
    {Protheus.doc} FATA080
    CT001 - Inclusão de regra de desconto On Line.
    @author	Ermerson.silva
    @since		26/02/2018
    @version	12.1.17 
    
    '''
    def test_FATA080_001(self):
        
        #Variaveis
        linha = 1

        #Pressionando o botão 
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton("OK")
        #Pegando o Código Gerado pela Rotina
        codigo = self.oHelper.GetValue('ACO_CODREG')
        
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.SetValue('ACO_DESCRI',"FATA080 RG DESC INCLUIR0000001")
        self.oHelper.SetValue('ACO_CODCLI','FAT256')
        self.oHelper.SetValue('ACO_LOJA','01')
        self.oHelper.SetValue('ACO_CODTAB','001')
        self.oHelper.SetValue('ACO_CONDPG','000')
        self.oHelper.SetValue( 'ACO_FORMPG', 'R$')            
        self.oHelper.SetValue('ACO_FAIXA','1.050,00')
        self.oHelper.SetValue('ACO_MOEDA','2')
        self.oHelper.SetValue('ACO_PERDES','0,00')
        self.oHelper.SetValue('ACO_TPHORA','1')       
        self.oHelper.SetValue('ACO_HORADE','10:00')
        self.oHelper.SetValue('ACO_HORATE','20:00')
        self.oHelper.SetValue('ACO_DATDE', '25/03/2019')
        self.oHelper.SetValue('ACO_DATATE', '25/03/2019')        

        #Alterando os itens do grid na posição linha
        self.oHelper.SetValue("ACP_CODPRO", "FAT00000000000000000000000000D", grid=True)
        self.oHelper.SetValue('ACP_PERDES','25,00', grid=True)
        self.oHelper.LoadGrid()
           
        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        self.oHelper.WaitShow("Manutencao das Regras de Desconto - INCLUIR")
        #Pressionando o botão
        self.oHelper.SetButton('Cancelar')
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.CheckResult('ACO_DESCRI',"FATA080 RG DESC INCLUIR0000001")
        self.oHelper.CheckResult('ACO_CODCLI','FAT256')
        self.oHelper.CheckResult('ACO_LOJA','01')
        self.oHelper.CheckResult('ACO_CODTAB','001')
        self.oHelper.CheckResult('ACO_CONDPG','000')
        self.oHelper.CheckResult('ACO_FORMPG', 'R$')              
        self.oHelper.CheckResult('ACO_FAIXA','1.050,00')
        self.oHelper.CheckResult('ACO_MOEDA','2')
        self.oHelper.CheckResult('ACO_PERDES','0,00')
        self.oHelper.CheckResult('ACO_TPHORA','1')       
        self.oHelper.CheckResult('ACO_HORADE','10:00')
        self.oHelper.CheckResult('ACO_HORATE','20:00')
        self.oHelper.CheckResult('ACO_DATDE', '25/03/2019')
        self.oHelper.CheckResult('ACO_DATATE', '25/03/2019')        

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.CheckResult('ACP_CODPRO','FAT00000000000000000000000000D', linha)
        self.oHelper.CheckResult('ACP_PERDES','25,00', linha)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Cancelar')
        
        #Validando o TestCase 
        self.oHelper.AssertTrue()

    '''
    {Protheus.doc} FATA080
    CT002 - Alteração de regra de desconto On Line com cliente e sem Item.
    @author	Ermerson.silva
    @since		26/02/2018
    @version	12.1.17 
    
    ''' 
    def test_FATA080_002(self):
        
        #Variaveis
        codigo = '000011'
        
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.SetValue('ACO_DESCRI',"FATA080 RG DESC 000011 ALTERAR")   
        self.oHelper.SetValue('ACO_FAIXA','250,00')
        self.oHelper.SetValue('ACO_PERDES','15,00')       
        self.oHelper.SetValue('ACO_HORADE','09:00')
        self.oHelper.SetValue('ACO_HORATE','22:00')
        self.oHelper.SetValue('ACO_DATDE', '25/03/2018')
        self.oHelper.SetValue('ACO_DATATE', '25/03/2018')
        
        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.CheckResult('ACO_DESCRI',"FATA080 RG DESC 000011 ALTERAR")
        self.oHelper.CheckResult('ACO_FAIXA','250,00')
        self.oHelper.CheckResult('ACO_PERDES','15,00')
        self.oHelper.CheckResult('ACO_HORADE','09:00')
        self.oHelper.CheckResult('ACO_HORATE','22:00')
        self.oHelper.CheckResult('ACO_DATDE', '25/03/2018')
        self.oHelper.CheckResult('ACO_DATATE', '25/03/2018') 

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.CheckResult('ACO_CODCLI','FAT256')
        self.oHelper.CheckResult('ACO_LOJA','01')
        self.oHelper.CheckResult('ACO_CODTAB','CR6')
        self.oHelper.CheckResult('ACO_CONDPG','000')
        self.oHelper.CheckResult('ACO_FORMPG','BOL')
        self.oHelper.CheckResult('ACO_MOEDA','1')
        self.oHelper.CheckResult('ACO_TPHORA','1')
        #self.oHelper.CheckResult,'ACO_MSBLQL', '2')
        self.oHelper.CheckResult('ACO_GRPVEN', '')
        self.oHelper.SetButton('Cancelar')  
        
        #Validando o TestCase 
        self.oHelper.AssertTrue()


    '''
    {Protheus.doc} FATA080
    CT003 - Alteração de regra de desconto On Line com grupo de cliente e sem Item.
    @author	Ermerson.silva
    @since		26/02/2018
    @version	12.1.17 
    
    ''' 
    def test_FATA080_003(self):
        
        #Variaveis
        codigo = '000012'
        
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Aplicando as alterações nos campos - Alterar
        self.oHelper.SetValue('ACO_DESCRI',"FATA080 RG DESC 000012 ALTERAR")
        self.oHelper.SetValue('ACO_FORMPG','CC')   
        self.oHelper.SetValue('ACO_FAIXA','450,00')
        self.oHelper.SetValue('ACO_PERDES','50,00')       
        self.oHelper.SetValue('ACO_TPHORA','2')
        self.oHelper.SetValue('ACO_HORADE','22:00')
        self.oHelper.SetValue('ACO_HORATE','23:00')
        self.oHelper.SetValue('ACO_DATDE', '17/03/2018')
        self.oHelper.SetValue('ACO_DATATE', '17/05/2018')

        #Pressionando o botão 
        self.oHelper.SetButton('Salvar')
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão 
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.CheckResult('ACO_DESCRI',"FATA080 RG DESC 000012 ALTERAR")
        self.oHelper.CheckResult('ACO_FORMPG','CC')
        self.oHelper.CheckResult('ACO_FAIXA','450,00')
        self.oHelper.CheckResult('ACO_PERDES','50,00')
        self.oHelper.CheckResult('ACO_TPHORA','2')
        self.oHelper.CheckResult('ACO_HORADE','22:00')
        self.oHelper.CheckResult('ACO_HORATE','23:00')
        self.oHelper.CheckResult('ACO_DATDE', '17/03/2018')
        self.oHelper.CheckResult('ACO_DATATE', '17/05/2018')
        
        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.CheckResult('ACO_MOEDA','1')
        self.oHelper.CheckResult('ACO_CODCLI','')
        self.oHelper.CheckResult('ACO_LOJA','')
        self.oHelper.CheckResult('ACO_CODTAB','CR6')
        self.oHelper.CheckResult('ACO_CONDPG','000')
        self.oHelper.CheckResult('ACO_MSBLQL', '2')
        self.oHelper.CheckResult('ACO_GRPVEN', '000017')
        self.oHelper.SetButton('Cancelar') 

        #Validando o TestCase     
        self.oHelper.AssertTrue()
    
    '''
    {Protheus.doc} FATA080
    CT004 - Alteração de regra de desconto On Line com cliente e com Item.
    @author	Ermerson.silva
    @since		26/02/2018
    @version	12.1.17 
    
    ''' 
    def test_FATA080_004(self):
        
        #Variaveis
        codigo  = '000013'
        linha   = 1
        
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Informações do Cabeçalho
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.SetValue('ACO_DESCRI',"FATA080 RG DESC 000013 ALTERAR")
        self.oHelper.SetValue('ACO_FORMPG','CD')   
        self.oHelper.SetValue('ACO_FAIXA','550,00')
        self.oHelper.SetValue('ACO_PERDES','10,00')       
        self.oHelper.SetValue('ACO_TPHORA','1')
        self.oHelper.SetValue('ACO_HORADE','22:30')
        self.oHelper.SetValue('ACO_HORATE','23:00')
        self.oHelper.SetValue('ACO_DATDE', '18/04/2018')
        self.oHelper.SetValue('ACO_DATATE', '18/04/2018')

        #Alterando os itens do grid na posição linha
        self.oHelper.SetValue('ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)
        self.oHelper.LoadGrid()
    
        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Procutando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")   
        #self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.CheckResult('ACO_DESCRI',"FATA080 RG DESC 000013 ALTERAR")
        self.oHelper.CheckResult('ACO_FORMPG','CD')   
        self.oHelper.CheckResult('ACO_FAIXA','550,00')
        self.oHelper.CheckResult('ACO_PERDES','10,00')       
        self.oHelper.CheckResult('ACO_TPHORA','1')
        self.oHelper.CheckResult('ACO_HORADE','22:30')
        self.oHelper.CheckResult('ACO_HORATE','23:00')
        self.oHelper.CheckResult('ACO_DATDE', '18/04/2018')
        self.oHelper.CheckResult('ACO_DATATE','18/04/2018')

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.CheckResult('ACO_MOEDA','1')
        self.oHelper.CheckResult('ACO_CODCLI','FAT256')
        self.oHelper.CheckResult('ACO_LOJA','01')
        self.oHelper.CheckResult('ACO_CODTAB','CR6')
        self.oHelper.CheckResult('ACO_CONDPG','000')
        self.oHelper.CheckResult('ACO_GRPVEN', '')

        #Conferindo os itens do grid que foram alterado na posicao linha
        self.oHelper.CheckResult('ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Cancelar') 

        #Validando o TestCase    
        self.oHelper.AssertTrue()

    '''
    {Protheus.doc} FATA080
    CT005 - Alteração de regra de desconto On Line com grupo cliente e com Item.
    @author	Ermerson.silva
    @since		26/02/2018
    @version	12.1.17 
    
    '''     
    def test_FATA080_005(self):
        
        #Variaveis
        codigo  = '000014'
        linha   = 1
        
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Informações do Cabeçalho
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.SetValue('ACO_DESCRI',"FATA080 RG DESC 000014 ALTERAR")
        self.oHelper.SetValue('ACO_FORMPG','CD')   
        self.oHelper.SetValue('ACO_FAIXA','650,00')
        self.oHelper.SetValue('ACO_PERDES','10,00')       
        self.oHelper.SetValue('ACO_TPHORA','1')
        self.oHelper.SetValue('ACO_HORADE','22:30')
        self.oHelper.SetValue('ACO_HORATE','23:00')
        self.oHelper.SetValue('ACO_DATDE', '25/04/2018')
        self.oHelper.SetValue('ACO_DATATE', '26/04/2018')

        #Alterando os itens do grid na posição linha
        self.oHelper.SetValue('ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)
        self.oHelper.LoadGrid()
        #self.oHelper.SetValue('ACP_VLRDES','0,00', linha)
        #self.oHelper.SetValue('ACP_GRUPO','0001', linha)
        #self.oHelper.SetValue('ACP_PERDES','10,00', linha)
        #self.oHelper.SetValue('ACP_FAIXA','100,00', linha)
        #self.oHelper.SetValue('ACP_TPDESC','2', linha)

        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Procutando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.CheckResult('ACO_DESCRI',"FATA080 RG DESC 000014 ALTERAR")
        self.oHelper.CheckResult('ACO_FORMPG','CD')   
        self.oHelper.CheckResult('ACO_FAIXA','650,00')
        self.oHelper.CheckResult('ACO_PERDES','10,00')       
        self.oHelper.CheckResult('ACO_TPHORA','1')
        self.oHelper.CheckResult('ACO_HORADE','22:30')
        self.oHelper.CheckResult('ACO_HORATE','23:00')
        self.oHelper.CheckResult('ACO_DATDE', '25/04/2018')
        self.oHelper.CheckResult('ACO_DATATE','26/04/2018')

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.CheckResult('ACO_MOEDA','1')
        self.oHelper.CheckResult('ACO_CODCLI','')
        self.oHelper.CheckResult('ACO_LOJA','')
        self.oHelper.CheckResult('ACO_CODTAB','CR6')
        self.oHelper.CheckResult('ACO_CONDPG','000')
        self.oHelper.CheckResult('ACO_MSBLQL', '2')
        self.oHelper.CheckResult('ACO_GRPVEN', '000017')

        #Conferindo os itens do grid que foram alterado na posicao linha
        self.oHelper.CheckResult('ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Cancelar')


        #Validando o TestCase    
        self.oHelper.AssertTrue()
    
    '''
    {Protheus.doc} FATA080
    CT006 - Exclusão de Regra de desconto.
    @author	Ermerson.silva
    @since		26/02/2018
    @version	12.1.17 
    
    ''' 

    def test_FATA080_006(self):        
        #Variaveis
        codigo  = '000015'

        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        #Pressionando o botão        
        self.oHelper.SetButton("Outras Ações", "Excluir")
        #Pressionando o botão        
        self.oHelper.SetButton('Confirmar')

        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse(f"D MG    {codigo}", "Filial+cod. Regra")
        
        #Aguardando a busca retornar Falso
        self.oHelper.AssertFalse()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

# F I N A L I Z A C A O
if __name__ == '__main__':
    unittest.main()