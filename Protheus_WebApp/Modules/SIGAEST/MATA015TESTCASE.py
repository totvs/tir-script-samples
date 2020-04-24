from tir import Webapp
import unittest

class MATA015(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","13/09/2019","T1","D MG 01 ","04")
        inst.oHelper.Program("MATA015")

    def test_MATA015_001(self):       
        self.oHelper.SetButton('Outras Ações','ocupacao')        
        self.oHelper.SetValue("Armazem De ?", '')
        self.oHelper.SetValue("Armazem Ate ?",'ZZ')
        self.oHelper.SetValue("Zona de Armaz. De ?",'')
        self.oHelper.SetValue("Zona de Armaz. Ate ?",'ZZZZ')
        self.oHelper.SetValue("Estrut. Fisica De ?",'')
        self.oHelper.SetValue("mv_par06",'ZZZZZ')
        self.oHelper.SetValue("Endereco De ?",'')
        self.oHelper.SetValue("Endereco Ate",'ZZZZZ')        
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("OK")       

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()