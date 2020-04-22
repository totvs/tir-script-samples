from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA110 - Solicitacao de Compras
#TABELA SC1, SCX
#
#@author KEVIN ALEXANDER
#@since 19/02/2020
#@version P12
#/*/
#//-------------------------------------------------------------------

class MATA110(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","01/01/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("MATA110")

    #CRUD SOLICITAÇÃO DE COMPRA
    def test_MATA110_001(self):
        prod1 = 'COMTIR1'
        prod2 = 'COMTIR2'
        sc1 = 'COMTI1'
        sc2 = 'COMTI2'
        cc1 = 'COMTIR1'
        cc2 = 'COMTIR2'
        
        #Inclusão de SC com rateio        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Número", sc1)               
        self.oHelper.SetValue("C1_PRODUTO",prod1,grid=True,grid_number=1)
        self.oHelper.SetValue("C1_QUANT",'10,00',grid=True,grid_number=1)        
        self.oHelper.LoadGrid()
        
        #Adiciona o segundo item
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.SetValue("C1_PRODUTO",prod2,grid=True,grid_number=1)
        self.oHelper.SetValue("C1_QUANT",'20,00',grid=True,grid_number=1) 
        self.oHelper.LoadGrid()

        #Adiciona o rateio
        self.oHelper.SetButton('Outras Ações','Rateio')
        time.sleep(2)
        #Linha 1
        self.oHelper.SetValue("CX_PERC",'50,00',grid=True,grid_number=1)
        self.oHelper.SetValue("CX_CC",cc1,grid=True,grid_number=1)
        self.oHelper.LoadGrid()

        #Linha 2
        self.oHelper.SetKey("DOWN",grid=True,grid_number=1)
        self.oHelper.SetValue("CX_PERC",'50,00',grid=True,grid_number=1)
        self.oHelper.SetValue("CX_CC",cc2,grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Todos")
        time.sleep(1)
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()
        time.sleep(1)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
        time.sleep(1)

        #Inclusão de SC sem rateio        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Número", sc2)               
        self.oHelper.SetValue("C1_PRODUTO",prod1,grid=True,grid_number=1)
        self.oHelper.SetValue("C1_QUANT",'10,00',grid=True,grid_number=1)        
        self.oHelper.LoadGrid()
        
        #Adiciona o segundo item
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.SetValue("C1_PRODUTO",prod2,grid=True,grid_number=1)
        self.oHelper.SetValue("C1_QUANT",'20,00',grid=True,grid_number=1) 
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
        time.sleep(1)

        #Copiar
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton('Outras Ações','Copia')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)    
         
        #Visualizar
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)
        
        #Alterar
        self.oHelper.SearchBrowse(f"D MG 01 {sc2}", "Filial+numero da Sc")       
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetValue("C1_OBS",'                             A',grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()
        time.sleep(1) 

        #Excluir SC com rateio 
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)

        #Excluir SC sem rateio 
        self.oHelper.SearchBrowse(f"D MG 01 {sc2}", "Filial+numero da Sc")       
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)
        
        #//-------------------------------------------------------------------
        #@author Mauricio Junior 
        #@since 27/03/2020
        #Transferência das SCs para compra centralizada para processo de compra na filial centralizadora.
        #//-------------------------------------------------------------------
    def test_MATA110_002(self):
        #Pesquisa no browser a SC usando a chave Filial+codigo
        self.oHelper.SearchBrowse("D MG 01 SOL024",key=1,index=True)      
        #Abre a lista de outras ações e seleciona a opção determinada
        self.oHelper.SetButton('Outras Ações','Compra Centralizada')
        #Clica no MarkBrowse
        self.oHelper.ClickGridCell("Filial",1)
        self.oHelper.SetKey("enter")
        self.oHelper.LoadGrid()
        #Pressiona botão confirma
        self.oHelper.SetButton("Confirma")
        #Pressiona botão SIM
        self.oHelper.SetButton("Sim")  
        
        time.sleep(1)
        self.oHelper.AssertTrue()
        #//-------------------------------------------------------------------
        #@author Mauricio Junior 
        #@since 27/03/2020
        #Pesquisar Solicitação de Compras Por Colunas Pré Estabelecidas.
        #//-------------------------------------------------------------------
    def test_MATA110_003(self):
        #Pesquisa no browser a SC usando a chave Filial+codigo
        self.oHelper.SearchBrowse("D MG 01 SOLE12 0001",key=1,index=True)       
    
        time.sleep(1)
        self.oHelper.AssertTrue()

        #//-------------------------------------------------------------------
        #@author Mauricio Junior 
        #@since 06/04/2020
        #Base Conhecimento Solicitação de Compras.
        #//-------------------------------------------------------------------
    def test_MATA110_004(self):
        #Pesquisa no browser a SC usando a chave Filial+codigo
        self.oHelper.SearchBrowse("D MG 01 SOL024",key=1,index=True)      
        #Abre a lista de outras ações e seleciona a opção determinada
        self.oHelper.SetButton('Outras Ações','Conhecimento')
        #Inclui arquivo na base de conhecimento
        self.oHelper.SetValue("AC9_OBJETO", "MONITOR.TXT",grid=True,grid_number=1)
        self.oHelper.LoadGrid()	
        #Pressiona botão confirma
        self.oHelper.SetButton("Salvar")

        #//-------------------------------------------------------------------
        #@author Mauricio Junior 
        #@since 07/04/2020
        #Na inclusão de uma SC apos preencher o rateio por Centro de Custo, preencher o campo C1_CC do grid
        #//-------------------------------------------------------------------
    def test_MATA110_005(self):
        #Inclusão de SC com rateio        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Número", "SOLCT5")               
        self.oHelper.SetValue("C1_PRODUTO","COMTIR5",grid=True,grid_number=1)
        self.oHelper.SetValue("C1_QUANT",'30,00',grid=True,grid_number=1)        
        self.oHelper.LoadGrid()

        #Adiciona o rateio
        self.oHelper.SetButton('Outras Ações','Rateio')
        time.sleep(2)
        #Linha 1
        self.oHelper.SetValue("CX_PERC",'50,00',grid=True,grid_number=1)
        self.oHelper.SetValue("CX_CC","000001",grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        #Linha 2
        self.oHelper.SetKey("DOWN",grid=True,grid_number=1)
        self.oHelper.SetValue("CX_PERC",'50,00',grid=True,grid_number=1)
        self.oHelper.SetValue("CX_CC","000002",grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        #Preenchimento do campo Centro de Custo na linha do grid
        self.oHelper.SetValue("C1_CC","00003",grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        #Seta para mudar para linha de baixo
        self.oHelper.SetKey("DOWN",grid=True,grid_number=1)   
        self.oHelper.LoadGrid()    
    
        self.oHelper.AssertTrue()    
        
        
        time.sleep(1)
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
