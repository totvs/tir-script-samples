from tir import Webapp
import unittest

class GFEC054(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "23/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC054")

    def test_GFEC054_CT001(self):
       
        self.oHelper.SetValue('Filial Docto Transporte De ?','')
        self.oHelper.SetValue('Filial Docto Transporte Até ?','ZZZZZZZZ')
        self.oHelper.SetValue('Nro Docto Transporte De ?','0')
        self.oHelper.SetValue('Nro Docto Transporte Até ?','999999999')
        self.oHelper.SetValue('Serie Docto Transporte De ?','')
        self.oHelper.SetValue('Serie Docto Transporte Até ?','ZZZ')
        self.oHelper.SetValue('Sit Integração ?','Todos')
        self.oHelper.SetValue('Emissão Docto Transp. De ?','01/01/2000')
        self.oHelper.SetValue('Emissão Docto Transp. Até ?','31/12/2000')
        self.oHelper.SetValue('Prazo Ent Docto Transp. De ?','')
        self.oHelper.SetValue('Prazo Ent Docto Transp. Até ?','')
        self.oHelper.SetValue('Data da Ocorrencia De ?','')
        self.oHelper.SetValue('Data da Ocorrencia Ate ?','')
        self.oHelper.SetValue('Exibe Doc. sem Ocorrencias ?','Sim')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
