from tir import Webapp
import time
import unittest

class PMSMONIT(unittest.TestCase):

    @classmethod
    def setUpClass(inst):   
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAPMS','13/09/2019','T1','D MG 01 ','44')
        inst.oHelper.Program('PMSMONIT')

    def test_PMSMONIT_010(self):
        self.oHelper.SetValue("Recurso", "PMSMONIT")
        
        self.oHelper.SetValue("Data Inicial", "12/09/2011")
        self.oHelper.SetValue("Data Final", "26/09/2019")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Outras Ações","Equipe")  
        self.oHelper.SetValue("Filial de", "D MG 01")
        self.oHelper.SetValue("Filial ate", "D MG 01")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Outras Ações","Opções")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Filial de", "D MG 01")
        self.oHelper.SetValue("Filial ate", "D MG 01")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Outras Ações","Check List")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_PMSMONIT_011(self):
        self.oHelper.Program('PMSMONIT')
        self.oHelper.SetValue("Recurso", "COM000000000001")
        
        self.oHelper.SetValue("Data Inicial", "12/09/2011")
        self.oHelper.SetValue("Data Final", "26/09/2019")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Outras Ações","Equipe")  
        self.oHelper.SetValue("Filial de", "D MG 01")
        self.oHelper.SetValue("Filial ate", "D MG 01")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Confirmar") 
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 