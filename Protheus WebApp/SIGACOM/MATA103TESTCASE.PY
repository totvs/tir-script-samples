from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA103 - Nota fiscal de entrada
#TABELA SF1, SD1
#
#@author KEVIN ALEXANDER
#@since 28/02/2020
#@version P12
#/*/
#//-------------------------------------------------------------------

class MATA103(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","01/01/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("MATA103")

    #CRUD PEDIDO DE COMPRA
    def test_MATA103_001(self):
        prod1 = 'COMTIR1'
        nf1 = 'COMTIR001'
        serie1 = 'TIR'
        for1 = '000003'
        loj1 = '01'
        tes1 = '018'
        
        #Inclusão de NF       
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        time.sleep(1)
        self.oHelper.SetValue("Tipo da Nota", 'Normal')
        self.oHelper.SetValue("Form. Prop.", 'Nao')
        self.oHelper.SetValue("Numero", nf1)
        self.oHelper.SetValue("Serie", serie1)
        self.oHelper.SetValue("Fornecedor", for1)
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetValue("Espec.Docum.", 'SPED')
        self.oHelper.SetKey("ENTER")
        self.oHelper.SetKey("ENTER")
        time.sleep(1)
                     
        self.oHelper.SetValue("Produto",prod1,grid=True,grid_number=1)
        self.oHelper.SetValue("Quantidade",'10,00',grid=True,grid_number=1)   
        self.oHelper.SetValue("Vlr.Unitario",'10,00',grid=True,grid_number=1) 
        self.oHelper.SetValue("Vlr.Total",'100,00',grid=True,grid_number=1)
        self.oHelper.SetValue("Tipo Entrada",tes1,grid=True,grid_number=1)         
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        time.sleep(2)
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
        
        #Visualizar
        self.oHelper.SearchBrowse("D MG 01 "+ nf1)       
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(1)
        
        #Excluir NF
        self.oHelper.SearchBrowse("D MG 01 "+ nf1)       
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()
        time.sleep(1)

    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
