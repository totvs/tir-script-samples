from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} COMXCOL - Monitor TOTVS Colaboração
#@author Leandro Nishihata
#@since 14/05/2020
#//-------------------------------------------------------------------

class COMXCOL(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","19/05/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("COMXCOL")

    def test_COMXCOL_001(self):
             
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Reprocessar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.ClickBox("Arquivo",select_all=True, grid_number=1)
        self.oHelper.SetButton("Ok")   
        self.oHelper.WaitShow("Atenção")    
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickBox("Num. Doc", "000024721")
        # self.oHelper.SearchBrowse("D MG 01 "+ "000024721")  
        # self.oHelper.SetKey("ENTER")    
        self.oHelper.SetButton('Outras Ações','Excluir')  
        self.oHelper.WaitShow("Atenção")      
        self.oHelper.SetButton("Sim")
        self.oHelper.SetKey("ENTER")   
        self.oHelper.SetButton("Reprocessar")
        self.oHelper.SetBranch("D MG 01 ") 
        self.oHelper.ClickLabel("Excluidos")
        self.oHelper.ClickBox("Arquivo",select_all=True, grid_number=1)
        self.oHelper.SetButton("Excluir")   
        self.oHelper.WaitShow("Excluir")    
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("OK")
        self.oHelper.SearchBrowse("D MG 01 "+ "000024723")  
        self.oHelper.SetButton('Alterar')  
        self.oHelper.WaitShow("Monitor TOTVS Colaboração - ALTERAR")
        self.oHelper.SetButton('Outras Ações','PC (Item)')        
        self.oHelper.ClickBox("Numero PC", "PMS91A")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("TOTVS")    
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton('Outras Ações','Desvincular') 
        self.oHelper.ClickBox("Numero PC", "PMS91A")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton('Outras Ações','PC (Doc.)')        
        self.oHelper.ClickBox("Numero PC", "PMS91A")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.ClickBox("Num. Doc", "000024723")
        self.oHelper.SetKey("ENTER")        
        self.oHelper.SetButton('Outras Ações','Gerar Docto')         
        self.oHelper.WaitShow("Atenção")    
        self.oHelper.SetButton("Sim")
        self.oHelper.WaitShow("Divergência Fiscal")    
        self.oHelper.SetButton("Ignorar")
        self.oHelper.AssertTrue()
    @classmethod    
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()