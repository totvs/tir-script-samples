from tir import Webapp
import unittest

class GFEC003(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "25/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC003")

    def test_GFEC003_CT001(self):   
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'      
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse('004')

        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Outras Ações','Doc Cargas')

        self.oHelper.SetButton('X')

        self.oHelper.SetButton('Outras Ações','Ocorrências')

        self.oHelper.SetButton('Sair')
        
        self.oHelper.SetButton('Outras Ações','Estatísticas')
        
        self.oHelper.SetButton('Sair')
        
        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
