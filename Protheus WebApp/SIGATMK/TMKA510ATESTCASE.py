from tir import Webapp
import time
import unittest

class TMKA510A(unittest.TestCase):

    @classmethod
    def setUpClass(inst):   
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMK','17/10/2019','T1','D MG 01 ','13')
        inst.oHelper.Program('TMKA510A')

    def test_TMKA510A_001(self):
        
        self.oHelper.SetValue("Do Chamado","") 
        self.oHelper.SetValue("Ate o Chamado","ZZZZZZ")  
        self.oHelper.SetValue("Do Cliente","") 
        self.oHelper.SetValue("Da Loja","") 
        self.oHelper.SetValue("Ate o Cliente","ZZZZZZ") 
        self.oHelper.SetValue("Ate a Loja","ZZ") 
        self.oHelper.SetValue("MV_PAR07","01/01/2004")
        self.oHelper.SetValue("MV_PAR08","20/10/2019")
        self.oHelper.SetValue("Do Analista","") 
        self.oHelper.SetValue("Ate o Analista","ZZZZZZ")  
        self.oHelper.SetButton("OK")

        self.oHelper.ClickGridCell("Contato",2)
        time.sleep(10)
        self.oHelper.SetKey("ENTER")

        self.oHelper.SetButton("Outras Ações","Alterar") 

        
        self.oHelper.SetValue("ADE_CODSB1","FAT000000000000000000000001111")  
        self.oHelper.SetValue("ADE_SEVCOD","1") 
        self.oHelper.SetValue("ADE_INCIDE","ALTERADO") 

        self.oHelper.SetValue("ADF_CODSU9", "000002", grid=True)
        self.oHelper.LoadGrid()  

                       
        self.oHelper.SetButton("Salvar") 
        self.oHelper.AssertTrue() 

        
        
        
    def test_TMKA510A_002(self):
           
        self.oHelper.SetButton("Outras Ações","Incluir")  
               
        self.oHelper.SetValue("Contato","TMK001") 
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("ADE_CODSB1","FAT000000000000000000000001111")  
        self.oHelper.SetValue("ADE_SEVCOD","5") 
        self.oHelper.SetValue("ADE_ASSUNT","000006") 
        self.oHelper.SetValue("ADE_OPERAC","2")
        self.oHelper.SetValue("ADE_INCIDE","TESTE_TMKA510A") 

        self.oHelper.SetValue("ADF_CODSU9", "000001", grid=True)
        self.oHelper.LoadGrid()        
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()

    def test_TMKA510A_003(self):

        self.oHelper.ClickGridCell("Contato",2)
        time.sleep(10)
        self.oHelper.SetKey("ENTER")

        self.oHelper.SetButton("Outras Ações","Visualizar") 
            
        self.oHelper.SetButton("Confirmar") 
        self.oHelper.AssertTrue() 


    def test_TMKA510A_004(self):

        self.oHelper.SetValue("Ordem","2")    
        self.oHelper.SetValue("Ordem","3")  
        self.oHelper.SetValue("Ordem","4")  
        self.oHelper.SetValue("Ordem","5")  
        self.oHelper.SetValue("Ordem","6")
        self.oHelper.SetValue("Ordem","7")  
        self.oHelper.SetValue("Ordem","8")
        self.oHelper.SetValue("Ordem","1")  
      
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 