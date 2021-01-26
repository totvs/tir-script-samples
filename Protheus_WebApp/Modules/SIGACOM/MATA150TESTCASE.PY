from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA150 - Nota fiscal de entrada
#@author Leandro Nishihata
#@since 06/03/2020
#@version P12
#/*/
#//-------------------------------------------------------------------

class MATA150(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","06/03/2020","T1","D MG 01 ","02")
        inst.oHelper.Program("MATA150")

    #Atualiza cotação incluindo desconto.
    def test_MATA150_001(self):
        Cotac = '000011'
      
        #Atualizar cotação 
        self.oHelper.SetButton("Ok")
        self.oHelper.SearchBrowse("D MG 01 " + Cotac)         
        self.oHelper.SetButton('Outras Ações','Atualizar')
        self.oHelper.F3( field = "cCondicao", name_attr = True, send_key = True )
        self.oHelper.SetButton("Ok")  
        self.oHelper.ClickGridCell("C8_PRECO", row=1, grid_number=1)					
        self.oHelper.SetValue("C8_PRECO",'10,00',grid=True)  
        self.oHelper.SetValue("C8_VLDESC",'40,00',grid=True)  
        self.oHelper.LoadGrid()         
        self.oHelper.ClickGridCell("C8_PRECO", row=2, grid_number=1)					
        self.oHelper.SetValue("C8_PRECO",'20,00',grid=True)  
        self.oHelper.SetValue("C8_VLDESC",'30,00',grid=True)  
        self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell("C8_PRECO", row=3, grid_number=1)					
        self.oHelper.SetValue("C8_PRECO",'30,00',grid=True)  
        self.oHelper.SetValue("C8_VLDESC",'20,00',grid=True)  
        self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell("C8_PRECO", row=4, grid_number=1)					
        self.oHelper.SetValue("C8_PRECO",'40,00',grid=True)  
        self.oHelper.SetValue("C8_VLDESC",'10,00',grid=True)  
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("C8_VLDESC", '40,00', grid=True, line=1, grid_number=1)	
        self.oHelper.LoadGrid() 
        self.oHelper.CheckResult("C8_VLDESC", '30,00', grid=True, line=2, grid_number=1)	
        self.oHelper.LoadGrid() 
        self.oHelper.CheckResult("C8_VLDESC", '20,00', grid=True, line=3, grid_number=1)	
        self.oHelper.LoadGrid() 
        self.oHelper.CheckResult("C8_VLDESC", '10,00', grid=True, line=4, grid_number=1)	
        self.oHelper.LoadGrid() 
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()
        time.sleep(5)
    @classmethod
    def tearDownClass(inst):

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
