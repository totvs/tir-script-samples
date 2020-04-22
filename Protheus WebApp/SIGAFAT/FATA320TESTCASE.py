from tir import Webapp
from datetime import datetime
from datetime import timedelta 
DataSystem = datetime.today()+timedelta(days=3) 
DataSystem = DataSystem.strftime('%d/%m/%Y')
import time
import unittest

class FATA320(unittest.TestCase):

    @classmethod
    def setUpClass(inst):   
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAFAT','20/09/2019','T1','D MG 01 ','05')
        inst.oHelper.Program('FATA320')

    def test_FATA320_011(self):
        
        self.oHelper.SetButton("Prg.Visitas")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetButton("Param.")
        self.oHelper.SetValue("Cliente de","FAT001")
        self.oHelper.SetValue("Cliente ate","FAT001")
        self.oHelper.SetValue("Vendedor de","APIGET")
        self.oHelper.SetValue("Vendedor ate","APIGET")
        self.oHelper.SetValue("Programar ate",DataSystem)
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("OK")
        
        self.oHelper.AssertTrue()

    def test_FATA320_012(self):

        self.oHelper.SetButton("Outras Ações","Exc.Visitas")
        self.oHelper.SetButton("Param.")
        self.oHelper.SetValue("Cliente de","FAT001")
        self.oHelper.SetValue("Cliente ate","FAT001")
        self.oHelper.SetValue("Vendedor de","APIGET")
        self.oHelper.SetValue("Vendedor ate","APIGET")
        self.oHelper.SetValue("Programar ate",DataSystem)
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("X")
        

        self.oHelper.AssertTrue()
        
    def test_FATA320_013(self):
         
        self.oHelper.Program('TMKA260')
        self.oHelper.SearchBrowse("D MG    FAT320  ")
        self.oHelper.SetButton("Outras Ações","Ag.Visita")
        self.oHelper.SetValue("Tempo da Visita","02:00")
        self.oHelper.SetValue("Data da Visita",DataSystem)
        self.oHelper.SetButton("OK")
       
      
        self.oHelper.AssertTrue()

  
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main() 