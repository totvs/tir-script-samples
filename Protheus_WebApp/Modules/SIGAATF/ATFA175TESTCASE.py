from tir import Webapp
import unittest

class ATFA175(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA175")
            
        inst.oHelper.AddParameter("MV_ULTDEPR","", "20160331")
        inst.oHelper.SetParameters()
        
    def test_ATFA175_001(self):

        #Inicio
        self.oHelper.SetButton("Avançar")
        #Tela 1
        self.oHelper.SetValue("Ativacao da Aceleração", True)
        self.oHelper.SetButton("Avançar")

        #Tela 2
        self.oHelper.SetValue("Percentual a Acelerar ?", "10,00")
        self.oHelper.SetButton("Avançar")

        #Tela 3
        self.oHelper.SetValue("Range", True)
        self.oHelper.SetButton("Avançar")

        #Tela 4
        self.oHelper.SetValue("Do Código do Bem  ? ", "ATF175_AT1")
        self.oHelper.SetValue("Até Código do Bem  ? ", "ATF175_AT1")
        self.oHelper.SetValue("Do Item   ? ", "0001")
        self.oHelper.SetValue("Até o Item  ? ", "0001")
        self.oHelper.SetValue("Até o Grupo  ? ", "ZZZZ")
        self.oHelper.SetValue("Até a Conta  ? ", "ZZZZZZZZZZZZZZZZZZZZ")
        self.oHelper.SetValue("Até o Centro de Custo  ? ", "ZZZZZZZZZ")
        self.oHelper.SetValue("Até o Item Contabil  ? ", "ZZZZZZZZZ")
        self.oHelper.SetValue("Até a Classe Contabil  ? ", "ZZZZZZZZZ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Sim")

        #Tela 5
        self.oHelper.SetValue("Contabiliza ? ", "Não")
        self.oHelper.SetValue("Mostra Lanc  ? ", "Não")
        self.oHelper.SetValue("Aglutina Lanc ? ", "Não")

        self.oHelper.SetButton("Finalizar")
        self.oHelper.WaitProcessing("Depreciacao Acelerada")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
