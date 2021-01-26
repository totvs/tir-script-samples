from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA110 - Solicitacao de Compras
#TABELA SC1, SCX
#
#@author Leandro Nishihata
#@since 11/05/2020
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

    #CRUD SOLICITAÇãO DE COMPRA
    def test_MATA110_001(self):

        sc1 = 'COMTI4'
               
        #Inclusao de SC com rateio        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.WaitShow("Solicitaçäo de Compras - INCLUIR")
        self.oHelper.SetValue("Número", sc1)    
        self.oHelper.SetFocus("Produto", grid_cell = True)
        self.oHelper.SetKey("F3",grid=True)
        self.oHelper.SearchBrowse(f'COMTIR2', 'Código')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("C1_QUANT",'10,00',grid=True,grid_number=1)        
        self.oHelper.LoadGrid()
        
        #Inclusão
        self.oHelper.SetButton('Outras Ações','Rateio')
        self.oHelper.SetButton('Outras Ações','Escolha de Rateio Pre-configurado')
        time.sleep(1)
        self.oHelper.SetKey("F3")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
        
        #Copiar
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton('Outras Ações','Copia')
        self.oHelper.WaitShow("Solicitaçäo de Compras - COPIA")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
                 
        #Visualizar
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
                
        #Alterar
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton("Alterar")        
        self.oHelper.WaitShow("Solicitaçäo de Compras - ALTERAR")
        self.oHelper.SetValue("C1_QUANT",'20,00',grid=True,grid_number=1)        
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton('Outras Ações','Rateio')
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()
        
        #Excluir SC 
        self.oHelper.SearchBrowse(f"D MG 01 {sc1}", "Filial+numero da Sc")       
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow("Solicitaçäo de Compras - EXCLUIR")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        
    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()
        
if __name__ == '__main__':
	unittest.main()