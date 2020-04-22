#Importes para execução do Teste
from cawebhelper import CAWebHelper
import unittest

class FATA080(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = CAWebHelper("http://localhost:1666/","FIREFOX")

        # S E T U P
        inst.oHelper.SetUp("SIGAFAT","Robo_12.1.17","admin","","","T1","D MG 01 ")
        inst.oHelper.UTProgram("FATA080")

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
        #Selecionando a Filial
        self.oHelper.SetFilial('D MG 01 ')
        
        #Pegando o Código Gerado pela Rotina
        codigo = self.oHelper.GetValue('aCab', 'ACO_CODREG')
        
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.UTSetValue('aCab','ACO_DESCRI',"FATA080 RG DESC INCLUIR")
        self.oHelper.UTSetValue('aCab','ACO_CODCLI','FAT256')
        self.oHelper.UTSetValue('aCab','ACO_LOJA','01')
        self.oHelper.UTSetValue('aCab','ACO_CODTAB','001')
        self.oHelper.UTSetValue('aCab','ACO_CONDPG','000')
        self.oHelper.UTSetValue('aCab', 'ACO_FORMPG', 'R$')            
        self.oHelper.UTSetValue('aCab','ACO_FAIXA','1.050,00')
        self.oHelper.UTSetValue('aCab','ACO_MOEDA','2')
        self.oHelper.UTSetValue('aCab','ACO_PERDES','0,00')
        self.oHelper.UTSetValue('aCab','ACO_TPHORA','1')       
        self.oHelper.UTSetValue('aCab','ACO_HORADE','10:00')
        self.oHelper.UTSetValue('aCab','ACO_HORATE','20:00')
        self.oHelper.UTSetValue('aCab','ACO_DATDE', '25/03/2019')
        self.oHelper.UTSetValue('aCab','ACO_DATATE', '25/03/2019')        

        #Alterando os itens do grid na posição linha
        self.oHelper.UTSetValue('aItens','ACP_CODPRO','000000000000000', linha)
        self.oHelper.UTSetValue('aItens','ACP_PERDES','25,00', linha)
           
        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Pressionando o botão
        self.oHelper.SetButton('Cancelar')
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_DESCRI',"FATA080 RG DESC INCLUIR")
        self.oHelper.UTCheckResult('aCab','ACO_CODCLI','FAT256')
        self.oHelper.UTCheckResult('aCab','ACO_LOJA','01')
        self.oHelper.UTCheckResult('aCab','ACO_CODTAB','001')
        self.oHelper.UTCheckResult('aCab','ACO_CONDPG','000')
        self.oHelper.UTCheckResult('aCab', 'ACO_FORMPG', 'R$')              
        self.oHelper.UTCheckResult('aCab','ACO_FAIXA','1.050,00')
        self.oHelper.UTCheckResult('aCab','ACO_MOEDA','2')
        self.oHelper.UTCheckResult('aCab','ACO_PERDES','0,00')
        self.oHelper.UTCheckResult('aCab','ACO_TPHORA','1')       
        self.oHelper.UTCheckResult('aCab','ACO_HORADE','10:00')
        self.oHelper.UTCheckResult('aCab','ACO_HORATE','20:00')
        self.oHelper.UTCheckResult('aCab','ACO_DATDE', '25/03/2019')
        self.oHelper.UTCheckResult('aCab','ACO_DATATE', '25/03/2019')        

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.UTCheckResult('aItens','ACP_CODPRO','000000000000000', linha)
        self.oHelper.UTCheckResult('aItens','ACP_PERDES','25,00', linha)
        
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
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Aplicando as alterações nos campos - Alterar
        self.oHelper.UTSetValue('aCab','ACO_DESCRI',"FATA080 RG DESC 000011 ALTERAR")   
        self.oHelper.UTSetValue('aCab','ACO_FAIXA','250,00')
        self.oHelper.UTSetValue('aCab','ACO_PERDES','15,00')       
        self.oHelper.UTSetValue('aCab','ACO_HORADE','09:00')
        self.oHelper.UTSetValue('aCab','ACO_HORATE','22:00')
        self.oHelper.UTSetValue('aCab','ACO_DATDE', '25/03/2018')
        self.oHelper.UTSetValue('aCab','ACO_DATATE', '25/03/2018')
        
        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_DESCRI',"FATA080 RG DESC 000011 ALTERAR")
        self.oHelper.UTCheckResult('aCab','ACO_FAIXA','250,00')
        self.oHelper.UTCheckResult('aCab','ACO_PERDES','15,00')
        self.oHelper.UTCheckResult('aCab','ACO_HORADE','09:00')
        self.oHelper.UTCheckResult('aCab','ACO_HORATE','22:00')
        self.oHelper.UTCheckResult('aCab','ACO_DATDE', '25/03/2018')
        self.oHelper.UTCheckResult('aCab','ACO_DATATE', '25/03/2018') 

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_CODCLI','FAT256')
        self.oHelper.UTCheckResult('aCab','ACO_LOJA','01')
        self.oHelper.UTCheckResult('aCab','ACO_CODTAB','CR6')
        self.oHelper.UTCheckResult('aCab','ACO_CONDPG','000')
        self.oHelper.UTCheckResult('aCab','ACO_FORMPG','BOL')
        self.oHelper.UTCheckResult('aCab','ACO_MOEDA','1')
        self.oHelper.UTCheckResult('aCab','ACO_TPHORA','1')
        #self.oHelper.UTCheckResult('aCab','ACO_MSBLQL', '2')
        self.oHelper.UTCheckResult('aCab','ACO_GRPVEN', '')  
        
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
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Aplicando as alterações nos campos - Alterar
        self.oHelper.UTSetValue('aCab','ACO_DESCRI',"FATA080 RG DESC 000012 ALTERAR")
        self.oHelper.UTSetValue('aCab','ACO_FORMPG','CC')   
        self.oHelper.UTSetValue('aCab','ACO_FAIXA','450,00')
        self.oHelper.UTSetValue('aCab','ACO_PERDES','50,00')       
        self.oHelper.UTSetValue('aCab','ACO_TPHORA','2')
        self.oHelper.UTSetValue('aCab','ACO_HORADE','22:00')
        self.oHelper.UTSetValue('aCab','ACO_HORATE','23:00')
        self.oHelper.UTSetValue('aCab','ACO_DATDE', '17/03/2018')
        self.oHelper.UTSetValue('aCab','ACO_DATATE', '17/05/2018')

        #Pressionando o botão 
        self.oHelper.SetButton('Salvar')
        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão 
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_DESCRI',"FATA080 RG DESC 000012 ALTERAR")
        self.oHelper.UTCheckResult('aCab','ACO_FORMPG','CC')
        self.oHelper.UTCheckResult('aCab','ACO_FAIXA','450,00')
        self.oHelper.UTCheckResult('aCab','ACO_PERDES','50,00')
        self.oHelper.UTCheckResult('aCab','ACO_TPHORA','2')
        self.oHelper.UTCheckResult('aCab','ACO_HORADE','22:00')
        self.oHelper.UTCheckResult('aCab','ACO_HORATE','23:00')
        self.oHelper.UTCheckResult('aCab','ACO_DATDE', '17/03/2018')
        self.oHelper.UTCheckResult('aCab','ACO_DATATE', '17/05/2018')
        
        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_MOEDA','1')
        self.oHelper.UTCheckResult('aCab','ACO_CODCLI','')
        self.oHelper.UTCheckResult('aCab','ACO_LOJA','')
        self.oHelper.UTCheckResult('aCab','ACO_CODTAB','CR6')
        self.oHelper.UTCheckResult('aCab','ACO_CONDPG','000')
        self.oHelper.UTCheckResult('aCab','ACO_MSBLQL', '2')
        self.oHelper.UTCheckResult('aCab','ACO_GRPVEN', '000017')  

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
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Informações do Cabeçalho
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.UTSetValue('aCab','ACO_DESCRI',"FATA080 RG DESC 000013 ALTERAR")
        self.oHelper.UTSetValue('aCab','ACO_FORMPG','CD')   
        self.oHelper.UTSetValue('aCab','ACO_FAIXA','550,00')
        self.oHelper.UTSetValue('aCab','ACO_PERDES','10,00')       
        self.oHelper.UTSetValue('aCab','ACO_TPHORA','1')
        self.oHelper.UTSetValue('aCab','ACO_HORADE','22:30')
        self.oHelper.UTSetValue('aCab','ACO_HORATE','23:00')
        self.oHelper.UTSetValue('aCab','ACO_DATDE', '18/04/2018')
        self.oHelper.UTSetValue('aCab','ACO_DATATE', '18/04/2018')

        #Alterando os itens do grid na posição linha
        self.oHelper.UTSetValue('aItens','ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)
    
        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Procutando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)     
        #self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_DESCRI',"FATA080 RG DESC 000013 ALTERAR")
        self.oHelper.UTCheckResult('aCab','ACO_FORMPG','CD')   
        self.oHelper.UTCheckResult('aCab','ACO_FAIXA','550,00')
        self.oHelper.UTCheckResult('aCab','ACO_PERDES','10,00')       
        self.oHelper.UTCheckResult('aCab','ACO_TPHORA','1')
        self.oHelper.UTCheckResult('aCab','ACO_HORADE','22:30')
        self.oHelper.UTCheckResult('aCab','ACO_HORATE','23:00')
        self.oHelper.UTCheckResult('aCab','ACO_DATDE', '18/04/2018')
        self.oHelper.UTCheckResult('aCab','ACO_DATATE','18/04/2018')

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_MOEDA','1')
        self.oHelper.UTCheckResult('aCab','ACO_CODCLI','FAT256')
        self.oHelper.UTCheckResult('aCab','ACO_LOJA','01')
        self.oHelper.UTCheckResult('aCab','ACO_CODTAB','CR6')
        self.oHelper.UTCheckResult('aCab','ACO_CONDPG','000')
        self.oHelper.UTCheckResult('aCab','ACO_GRPVEN', '')

        #Conferindo os itens do grid que foram alterado na posicao linha
        self.oHelper.UTCheckResult('aItens','ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)

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
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão 
        self.oHelper.SetButton('Alterar')

        #Informações do Cabeçalho
        #Aplicando as alterações nos campos - Alterar
        self.oHelper.UTSetValue('aCab','ACO_DESCRI',"FATA080 RG DESC 000014 ALTERAR")
        self.oHelper.UTSetValue('aCab','ACO_FORMPG','CD')   
        self.oHelper.UTSetValue('aCab','ACO_FAIXA','650,00')
        self.oHelper.UTSetValue('aCab','ACO_PERDES','10,00')       
        self.oHelper.UTSetValue('aCab','ACO_TPHORA','1')
        self.oHelper.UTSetValue('aCab','ACO_HORADE','22:30')
        self.oHelper.UTSetValue('aCab','ACO_HORATE','23:00')
        self.oHelper.UTSetValue('aCab','ACO_DATDE', '25/04/2018')
        self.oHelper.UTSetValue('aCab','ACO_DATATE', '26/04/2018')

        #Alterando os itens do grid na posição linha
        self.oHelper.UTSetValue('aItens','ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)
        #self.oHelper.UTSetValue('aItens','ACP_VLRDES','0,00', linha)
        #self.oHelper.UTSetValue('aItens','ACP_GRUPO','0001', linha)
        #self.oHelper.UTSetValue('aItens','ACP_PERDES','10,00', linha)
        #self.oHelper.UTSetValue('aItens','ACP_FAIXA','100,00', linha)
        #self.oHelper.UTSetValue('aItens','ACP_TPDESC','2', linha)

        #Pressionando o botão
        self.oHelper.SetButton('Salvar')
        #Procutando pelo registro através do filtro - Chave[Filial+Codigo]     
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão
        self.oHelper.SetButton('Visualizar')

        #Conferindo os campos alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_DESCRI',"FATA080 RG DESC 000014 ALTERAR")
        self.oHelper.UTCheckResult('aCab','ACO_FORMPG','CD')   
        self.oHelper.UTCheckResult('aCab','ACO_FAIXA','650,00')
        self.oHelper.UTCheckResult('aCab','ACO_PERDES','10,00')       
        self.oHelper.UTCheckResult('aCab','ACO_TPHORA','1')
        self.oHelper.UTCheckResult('aCab','ACO_HORADE','22:30')
        self.oHelper.UTCheckResult('aCab','ACO_HORATE','23:00')
        self.oHelper.UTCheckResult('aCab','ACO_DATDE', '25/04/2018')
        self.oHelper.UTCheckResult('aCab','ACO_DATATE','26/04/2018')

        #Conferindo os campos que não foram alterados - Visualizar
        self.oHelper.UTCheckResult('aCab','ACO_MOEDA','1')
        self.oHelper.UTCheckResult('aCab','ACO_CODCLI','')
        self.oHelper.UTCheckResult('aCab','ACO_LOJA','')
        self.oHelper.UTCheckResult('aCab','ACO_CODTAB','CR6')
        self.oHelper.UTCheckResult('aCab','ACO_CONDPG','000')
        self.oHelper.UTCheckResult('aCab','ACO_MSBLQL', '2')
        self.oHelper.UTCheckResult('aCab','ACO_GRPVEN', '000017')

        #Conferindo os itens do grid que foram alterado na posicao linha
        self.oHelper.UTCheckResult('aItens','ACP_CODPRO','FAT0000000000000000000000FPPPQ', linha)


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
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        #Pressionando o botão        
        self.oHelper.SetButton('Excluir')
        #Pressionando o botão        
        self.oHelper.SetButton('Confirmar')

        #Procurando pelo registro através do filtro - Chave[Filial+Codigo]
        self.oHelper.SearchBrowse('Filial+numero',"D MG    %s" %codigo, True)
        
        #Aguardando a busca retornar Falso
        self.oHelper.AssertFalse()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

# F I N A L I Z A C A O
if __name__ == '__main__':
    unittest.main()