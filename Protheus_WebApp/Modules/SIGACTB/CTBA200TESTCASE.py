from tir import Webapp
import unittest

class CTBA200(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "03/12/2019", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA200")

#################################################
##      Processo de inclusão via assistente
#################################################
    def test_CTBA200_001(self):
        
        self.oHelper.WaitShow("Amarracao Moeda x Calendario")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Tipo da Interface ?", "Assistente")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("Calendario ?", "TI1")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Avançar")

        self.oHelper.ClickCheckBox("01-REAL")#Desmarcando
        self.oHelper.ClickCheckBox("01-REAL")#Marcando
        #Desmarcando outras moedas.
        self.oHelper.ClickCheckBox("02-DOLAR")
        self.oHelper.ClickCheckBox("03-UFIR")
        self.oHelper.ClickCheckBox("04-EURO")
        self.oHelper.ClickCheckBox("05-IENE")
   
        self.oHelper.SetButton("Finalizar")
        self.oHelper.CheckView("Confirma os Dados")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

#################################################
#               Verificando Help
#################################################
    def test_CTBA200_002(self):

        self.oHelper.WaitShow("Amarracao Moeda x Calendario")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Tipo da Interface ?", "Assistente")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("Calendario ?", "TT")
        
        self.oHelper.SetButton("Ok")

        ##self.oHelper.CheckView("O calendario informado: "X" não existe. Por favor, verifique !!")
        self.oHelper.SetButton("OK")#Clicando na confirmação da mensagem

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()