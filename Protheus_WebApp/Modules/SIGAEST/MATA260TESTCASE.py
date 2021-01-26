from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA260 - transferencia
#
#@author JEFFERSON SILVA DE SOUSA
#@since 17/09/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA260(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAPCP","30/09/2020","T1","D MG 01 ","04")
        inst.oHelper.SetLateralMenu('Atualizações > Saldos > Transf. Simples')      

    #CT001 TRANSFERENCIA ENTRE ARMAZENS
    def test_MATA260_001(self):
        
        #Variaveis de inclusao
        prod        =  'ESTSE0000000000000000000000557'
        armazemOri  =  '02'       
        Qtd         =  "10,00"      

        self.oHelper.SetButton("Incluir")
        time.sleep(2)
        self.oHelper.SetButton("ok")

        self.oHelper.SetValue("Produto", prod)
        self.oHelper.SetValue("Armazem  /  Endereco",armazemOri)       
        self.oHelper.SetValue('Quantidade Primaria',Qtd)        
      
        self.oHelper.SetButton("Salvar")        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_MATA260_002(self):
        
        #Estornar
        prod     = 'ESTSE0000000000000000000000557'       
        armazemDest = '02'       
        filial   = 'D MG 01 '
      
        self.oHelper.SearchBrowse(f"{filial}{prod}{armazemDest}", "Filial+produto + Armazem + Sequen..")

        self.oHelper.SetButton('Outras Ações','Estornar') 

        self.oHelper.SetButton("Confirmar")
        time.sleep(2)
        self.oHelper.SetButton("sim")
        self.oHelper.AssertTrue()
    #CT003 INCLUSAO COM LOTE 
    def test_MATA260_003(self):
        
        #Variaveis de inclusao
        prod        =  'ESTSE0000000000000000000000560'
        armazemOri  =  '02'       
        Qtd         =  "5,00"
        LoteOri     =  'LTX01'
        LoteDest    =  'LTX02'
        ValiDest    =  '31/12/2020'

        self.oHelper.SetButton("Incluir")
        time.sleep(2)
        self.oHelper.SetButton("ok")
        self.oHelper.SetValue("Produto", prod)
        self.oHelper.SetFocus("Armazem  /  Endereco")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"{armazemOri}", "codigo")
        self.oHelper.SetButton("OK") 
        self.oHelper.CheckResult("Armazem  /  Endereco", armazemOri)

        self.oHelper.SetValue("Lote",LoteOri)
        #self.oHelper.SetFocus("Lote")
        #self.oHelper.SetKey("F4")
        #self.oHelper.SetButton("OK")

        self.oHelper.SetValue('Quantidade Primaria',Qtd)
        self.oHelper.SetButton("Fechar")        
      
        self.oHelper.SetButton("Salvar")        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_MATA260_004(self):
        
        #VISUALIZAR
        prod     = 'ESTSE0000000000000000000000562'       
        armazemDest = '02'       
        filial   = 'D MG 01 '
      
        self.oHelper.SearchBrowse(f"{filial}{prod}{armazemDest}", "Filial+produto + Armazem + Sequen..")       

        self.oHelper.SetButton("Visualizar")
        time.sleep(2)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_MATA260_005(self):        
        #C/ Endereçamento
        prod         = 'ESTSE0000000000000000000000561'       
        armazem  = '01'
        LocalizOri   = 'ESTSE001'
        LocalizDest  = 'ESTSE002'        
        Qtd          = '5,00'   

        self.oHelper.SetButton("Incluir")
        time.sleep(2)
        self.oHelper.SetButton("ok")

        self.oHelper.SetValue("Produto", prod)
        self.oHelper.SetFocus("Armazem  /  Endereco")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"{armazem}", "codigo")
        self.oHelper.SetButton("OK")

        self.oHelper.SetFocus("Armazem  /  Endereco")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"{armazem}{LocalizOri}", "Local+Localização")
        self.oHelper.SetButton("ok")

        self.oHelper.SetFocus("Armazem  /  Endereco")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"{armazem}", "codigo")
        self.oHelper.SetButton("ok")

        self.oHelper.SetFocus("Armazem  /  Endereco")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("F3")
        self.oHelper.SearchBrowse(f"{armazem}{LocalizDest}", "Local+Localização")
        self.oHelper.SetButton("ok")

        self.oHelper.SetValue('Quantidade Primaria',Qtd)
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetButton("Salvar")
        time.sleep(2)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()                                         

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()