from tir import Webapp
import unittest
import time

class GFEA032(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "26/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA032")

    def test_GFEA032_CT001(self):   

        self.oHelper.SearchBrowse('D MG 01 00000001')
                
        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SearchBrowse('D MG 01 00000001')

        self.oHelper.SetButton('Outras Ações','Cancelar Aprov/Reprov')

        self.oHelper.SetButton('Sim')

        self.oHelper.SearchBrowse('D MG 01 00000001')

        self.oHelper.SetButton('Outras Ações','Aprovar/Reprovar')

        self.oHelper.SetValue('Solução', 'OCORRENCIA REENTREGA DOC CARGA 50003')

        self.oHelper.SetButton('OK')

        time.sleep(5)
        
        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
