from tir import Webapp
import unittest
import time
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")
#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA120 - Pedido de Compra
#TABELA SC7
#
#@author KEVIN ALEXANDER
#@since 24/02/2020
#@version P12
#/*/
#//-------------------------------------------------------------------

class MATA120(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","01/01/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("MATA121")

    #CRUD PEDIDO DE COMPRA
    def test_MATA120_001(self):
        prod1 = 'COMTIR1'
        prod2 = 'COMTIR2'
        pc1 = 'COMTI1'
        pc2 = 'COMTI2'
        cc1 = 'COMTIR1'
        cc2 = 'COMTIR2'
        for1 = '000003'
        loj1 = '01'
        condpag = '000'
        
        #Inclusão de PC com rateio        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        time.sleep(1)
        self.oHelper.SetValue("Numero", pc1)
        self.oHelper.SetValue("Fornecedor", for1)
        self.oHelper.SetValue("Loja", loj1) 
        self.oHelper.SetValue("Cond. Pagto", condpag)                
        self.oHelper.SetValue("C7_PRODUTO",prod1,grid=True,grid_number=1)
        self.oHelper.SetValue("C7_QUANT",'10,00',grid=True,grid_number=1)   
        self.oHelper.SetValue("C7_PRECO",'10,00',grid=True,grid_number=1) 
        self.oHelper.SetValue("C7_TOTAL",'100,00',grid=True,grid_number=1)        
        self.oHelper.LoadGrid()
        
        #Adiciona o segundo item
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.SetValue("C7_PRODUTO",prod2,grid=True,grid_number=1)
        self.oHelper.SetValue("C7_QUANT",'20,00',grid=True,grid_number=1)
        self.oHelper.SetValue("C7_PRECO",'10,00',grid=True,grid_number=1) 
        self.oHelper.SetValue("C7_TOTAL",'200,00',grid=True,grid_number=1)   
        self.oHelper.LoadGrid()

        #Adiciona o rateio
        self.oHelper.SetButton('Outras Ações','Rateio')
        time.sleep(2)
        #Linha 1
        self.oHelper.SetValue("CH_PERC",'50,00',grid=True,grid_number=1)
        self.oHelper.SetValue("CH_CC",cc1,grid=True,grid_number=1)
        self.oHelper.LoadGrid()

        #Linha 2
        self.oHelper.SetKey("DOWN",grid=True,grid_number=1)
        self.oHelper.SetValue("CH_PERC",'50,00',grid=True,grid_number=1)
        self.oHelper.SetValue("CH_CC",cc2,grid=True,grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Todos")
        time.sleep(1)
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
        time.sleep(1)

        #Inclusão de PC sem rateio        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        time.sleep(1)
        self.oHelper.SetValue('Numero', pc2)
        self.oHelper.SetValue("Fornecedor", for1)
        self.oHelper.SetValue("Loja", loj1) 
        self.oHelper.SetValue("Cond. Pagto", condpag)                
        self.oHelper.SetValue("C7_PRODUTO",prod1,grid=True,grid_number=1)
        self.oHelper.SetValue("C7_QUANT",'10,00',grid=True,grid_number=1)   
        self.oHelper.SetValue("C7_PRECO",'10,00',grid=True,grid_number=1) 
        self.oHelper.SetValue("C7_TOTAL",'100,00',grid=True,grid_number=1)          
        self.oHelper.LoadGrid()
        
        #Adiciona o segundo item
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.SetValue("C7_PRODUTO",prod2,grid=True,grid_number=1)
        self.oHelper.SetValue("C7_QUANT",'20,00',grid=True,grid_number=1)
        self.oHelper.SetValue("C7_PRECO",'10,00',grid=True,grid_number=1) 
        self.oHelper.SetValue("C7_TOTAL",'200,00',grid=True,grid_number=1)  
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
        time.sleep(1)

        #Visualizar
        self.oHelper.SearchBrowse(f"D MG 01 {pc2}", "Filial+numero Pc")       
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)
        
        #Alterar
        self.oHelper.SearchBrowse(f"D MG 01 {pc2}", "Filial+numero Pc")
        time.sleep(1)       
        self.oHelper.SetButton("Alterar")
        time.sleep(2)
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetValue('Quantidade','9,00',grid=True,grid_number=1)  
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()
        time.sleep(1) 

        #Excluir PC com rateio 
        self.oHelper.SearchBrowse(f"D MG 01 {pc1}", "Filial+numero Pc")       
        self.oHelper.SetButton('Outras Ações','Excluir')        
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)
        
        #Excluir PC sem rateio 
        self.oHelper.SearchBrowse(f"D MG 01 {pc2}", "Filial+numero Pc")       
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)
    #Teste de Inclusão LGPD
    def test_MATA120_002(self):
        #Acessa sistema com novo Usuario
        self.oHelper.SetTIRConfig(config_name='user', value='APROVADOR7')
        self.oHelper.SetTIRConfig(config_name='password', value='a')
        self.oHelper.SetButton('x')
        self.oHelper.Finish()
        #Preenchimento de parametros do ambiente 
        self.oHelper.Setup('SIGAADV',DateSystem, 'T1', 'D MG 01 ', '02')
        self.oHelper.Program('MATA121')
        #Só executa inclusão se a release for superior ou igual a 12.1.27
        if self.oHelper.get_release() >= "12.1.27":         
            self.oHelper.SetButton("Incluir")
            self.oHelper.SetBranch("D MG 01 ")
            self.oHelper.SetValue("Numero", "TIR002")
            self.oHelper.SetValue("Fornecedor", "01FORN")
            self.oHelper.SetValue("Loja", "01") 
            self.oHelper.SetValue("Cond. Pagto", "001")                
            self.oHelper.SetValue("C7_PRODUTO","0001",grid=True,grid_number=1)
            self.oHelper.SetValue("C7_QUANT",'50,00',grid=True,grid_number=1)   
            self.oHelper.SetValue("C7_PRECO",'10,00',grid=True,grid_number=1) 
            self.oHelper.SetValue("C7_TOTAL",'500,00',grid=True,grid_number=1)        
            self.oHelper.LoadGrid()

            self.oHelper.ClickFolder("Inf. Fornecedor")
            self.oHelper.CheckResult("Nome", "FORNECEDOR 01", grid=True, line=1, grid_number=1)
            self.oHelper.SetButton("Salvar")
            self.oHelper.AssertTrue()
            time.sleep(1)
            #Visualizar
            self.oHelper.SetTIRConfig(config_name='user', value='APROVADOR6')
            self.oHelper.SetTIRConfig(config_name='password', value='a')
            self.oHelper.SetButton('x')
            self.oHelper.Finish()
            #Preenchimento de parametros do ambiente 
            self.oHelper.Setup('SIGAADV',DateSystem, 'T1', 'D MG 01 ', '02')
            self.oHelper.Program('MATA121')
            self.oHelper.SearchBrowse("D MG 01 TIR002", "Filial+numero Pc")       
            self.oHelper.SetButton("Visualizar")
            self.oHelper.ClickFolder("Inf. Fornecedor")
            self.oHelper.SetButton("Mais Inf.")
            self.oHelper.SetButton('OK')
            time.sleep(2)
            self.oHelper.CheckHelp(text_help="DADO_PROTEGIDO", button="Fechar")
            self.oHelper.SetButton("Confirmar")
            self.oHelper.AssertTrue()
        time.sleep(1)

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
