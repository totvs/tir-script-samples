from tir import Webapp 
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class TRKXFUN(unittest.TestCase):

    @classmethod
    def setUpClass(self): 

        self.oHelper = Webapp(autostart=False)
        self.oHelper.SetTIRConfig(config_name="User", value="telemarketing")
        self.oHelper.SetTIRConfig(config_name="Password", value="1")

    def test_TRKXFUN_CT001(self):  
        self.oHelper.Start()
        self.oHelper.Setup("SIGATMK",DateSystem,"T1","D MG 01","13")
        self.oHelper.Program("TMKA271")
        self.oHelper.AddParameter("MV_FATPROP","D MG 01","O","O","O")
        self.oHelper.SetParameters() 
        self.oHelper.SearchBrowse(f"D MG 01 000020", "Filial+atendimento")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Outras Ações", "Tracker da Entidade")
        self.oHelper.SetButton("Rastrear") 
        self.oHelper.ClickTree("Atendimento Telemarketing  - 000020")
        self.oHelper.SetButton("Abandonar") 
        self.oHelper.SetButton("Confirmar") 
        self.oHelper.SetButton("X")
        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue() 
   
    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()