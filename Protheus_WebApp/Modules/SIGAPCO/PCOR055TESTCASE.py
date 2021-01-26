from tir import Webapp
import unittest

class PCOR055(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAPCO', '20092020', 'T1', 'M SP 01')
        inst.oHelper.Program('PCOR055')
    
    @classmethod
    def test_PCOR055_002(self):

        self.oHelper.SetValue("Codigo Visao Gerencial ?",'055')
        self.oHelper.SetValue("Tipo Periodo ?",'Quinzenal')
        self.oHelper.SetValue("Periodo de ?",'01/09/2020')
        self.oHelper.SetValue("Periodo Ate ?",'31/12/2020')
        self.oHelper.SetButton("OK")
        self.oHelper.CheckHelp(text="PCOA1801", button="Fechar")
        self.oHelper.SetButton("Outras Ações", "Parâmetros")
        self.oHelper.SetValue("Periodo de ?",'01/09/2020')
        self.oHelper.SetValue("Perioo ate ?",'31/12/2020')
        self.oHelper.SetButton("OK")
        # self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Imprimir")
        self.oHelper.SetButton("Sair")

        self.oHelper.AssertTrue()   

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()  

if __name__ == '__main__':
    unittest.main()


    

