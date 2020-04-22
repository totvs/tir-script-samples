from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class TRKXFUN(unittest.TestCase):

    @classmethod
    def setUpClass(self): 

        self.oHelper = Webapp(autostart=False)
        self.oHelper.SetTIRConfig(config_name="User", value="telemarketing")
        self.oHelper.SetTIRConfig(config_name="Password", value="1")

    '''
    CT001 - Tracker no Call Center - Telemarketing - MV_FATPROP = O
    @author	CRM/FAT
    @since	28/08/2019
    '''

    def test_TRKXFUN_CT001(self):  

        self.oHelper.Start()

        self.oHelper.Setup("SIGATMK",DateSystem,"T1","D MG 01","13")
        self.oHelper.Program("TMKA271")
        self.oHelper.AddParameter("MV_FATPROP","D MG 01","O","O","O") #Parametro = gera Oportunidade
        self.oHelper.SetParameters() 
        self.oHelper.SearchBrowse(f"D MG 01 000020", "Filial+atendimento")
        self.oHelper.SetButton("Visualizar")
        time.sleep(5)
        self.oHelper.SetButton("Outras Ações", "Tracker da Entidade")
        self.oHelper.SetButton("Rastrear") 
        time.sleep(25)
        self.oHelper.ClickTree("Atendimento Telemarketing  - 000020")
        self.oHelper.SetButton("Abandonar") 
        self.oHelper.SetButton("Confirmar") 

        self.oHelper.SetButton("X")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue() 

    '''
    CT002 - Tracker no Call Center - Telemarketing - MV_FATPROP = P
    @author	CRM/FAT
    @since	28/08/2019
    '''
     
    def test_TRKXFUN_CT002(self):  

        self.oHelper.Setup("SIGATMK",DateSystem,"T1","D MG 01","13")
        self.oHelper.Program("TMKA271")
        self.oHelper.AddParameter("MV_FATPROP","D MG 01","P","P","P") #Parametro = gera Oportunidade
        self.oHelper.SetParameters() 
        self.oHelper.SearchBrowse(f"D MG 01 000021", "Filial+atendimento")
        self.oHelper.SetButton("Visualizar")
        time.sleep(5)
        self.oHelper.SetButton("Outras Ações", "Tracker da Entidade")
        self.oHelper.SetButton("Rastrear") 
        time.sleep(25)
        self.oHelper.ClickTree("Atendimento Telemarketing  - 000021")
        self.oHelper.SetButton("Abandonar") 
        self.oHelper.SetButton("Confirmar") 

        self.oHelper.SetButton("X")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue() 

    '''
    CT003 - Tracker no Pedido de Venda - MV_FATPROP = O
    @author	CRM/FAT
    @since	28/08/2019
    '''
    def test_TRKXFUN_CT003(self):  

        order = "pcpA07"

        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")
        self.oHelper.Program("MATA410")
        self.oHelper.AddParameter("MV_FATPROP","D MG 01","O","O","O") #Parametro = gera Oportunidade
        self.oHelper.SetParameters() 
        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Pedidos de Venda - VISUALIZAR")
        self.oHelper.SetButton("Outras Ações", "Tracker")
        self.oHelper.SetButton("Rastrear") 
        time.sleep(25)
        self.oHelper.ClickTree("Pedido de Venda - pcpA07")
        self.oHelper.SetButton("Abandonar") 
        self.oHelper.SetButton("Confirmar") 

        self.oHelper.SetButton("X")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue()

    '''
    CT004 - Tracker no Pedido de Venda - MV_FATPROP = P
    @author	CRM/FAT
    @since	28/08/2019
    '''
    def test_TRKXFUN_CT004(self): 

        order = "pcpA10" 

        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")
        self.oHelper.Program("MATA410")
        self.oHelper.AddParameter("MV_FATPROP","D MG 01","P","P","P") #Parametro = gera Proposta
        self.oHelper.SetParameters() 
        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Pedidos de Venda - VISUALIZAR")
        self.oHelper.SetButton("Outras Ações", "Tracker")
        self.oHelper.SetButton("Rastrear") 
        time.sleep(25)
        self.oHelper.ClickTree("Pedido de Venda - pcpA10")
        self.oHelper.SetButton("Abandonar") 
        self.oHelper.SetButton("Confirmar") 

        self.oHelper.SetButton("X")

        self.oHelper.RestoreParameters()

        self.oHelper.AssertTrue()
 
   
    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()