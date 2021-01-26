from tir import Webapp
import unittest

class GFEC041(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "23/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC041")

    def test_GFEC041_CT001(self):
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial até ?',filial_ate)
        self.oHelper.SetValue('Situação Docto ?','Todos')
        self.oHelper.SetValue('Dt Emissão Inicial ?','01/11/2018')
        self.oHelper.SetValue('Dt Emissão Final ?','30/11/2018')
        self.oHelper.SetValue('Dt prev saída inici. ?','')
        self.oHelper.SetValue('Dt prev saída final ?','')
        self.oHelper.SetValue('Dt saída inicial ?','')
        self.oHelper.SetValue('Dt saída final ?','')
        self.oHelper.SetValue('Dt prev ent inicial ?','')
        self.oHelper.SetValue('Dt prev ent final ?','')
        self.oHelper.SetValue('Dt entrega inicial ?','')
        self.oHelper.SetValue('Dt entrega final ?','')
        self.oHelper.SetValue('Entregas ?','Todas')
        self.oHelper.SetValue('Transp de ?','')
        self.oHelper.SetValue('Transp até ?','ZZZZZZZZZZZZZZ')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Consultar Cliente')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
