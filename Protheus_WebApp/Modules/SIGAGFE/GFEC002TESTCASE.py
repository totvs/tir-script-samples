from tir import Webapp
import unittest
import time

class GFEC002(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "24/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC002")

    def test_GFEC002_CT001(self):         
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data até ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton("Doc Cargas")

        self.oHelper.SetButton('X')

        self.oHelper.SetButton('Outras Ações','Romaneios')

        self.oHelper.SetButton('X')

        self.oHelper.SetButton('Outras Ações','Agendamentos')
        
        self.oHelper.SetButton('X')
        
        self.oHelper.SetButton('Outras Ações','Ocorrências')
        
        self.oHelper.SetButton('X')

        self.oHelper.SetButton('Outras Ações','Entregas')
        
        self.oHelper.SetButton('Sair')

        self.oHelper.SetButton('Outras Ações','Doc Fretes')
        
        self.oHelper.SetButton('X')
        
        self.oHelper.SetButton('Outras Ações','Pré-Faturas')
        
        self.oHelper.SetButton('X')

        self.oHelper.SetButton('Outras Ações','Contratos')
        
        self.oHelper.SetButton('X')
        
        self.oHelper.SetButton('Outras Ações','Estatísticas')
        
        self.oHelper.SetButton('X')
        
        self.oHelper.SetButton('Outras Ações','Despesas')

        time.sleep(10)

        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
