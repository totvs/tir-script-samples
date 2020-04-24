from tir import Webapp
import unittest


class CTBA010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/04/2016", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA010")

     
    def test_CTBA010_001(self):
        self.oHelper.WaitShow("Cadastro Calendário Contábil")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Tipo da Interface ?","Assistente")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Data Inicial ?","01/01/2098") 
        self.oHelper.SetValue("Data Final ?","31/12/2098")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Calendario ?","298")
        self.oHelper.SetValue("Exercicio Contabil ?","2098")
        self.oHelper.ClickCheckBox("Amarrar Calendario com Moedas",1)
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Finalizar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Finalizar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SearchBrowse("D MG 01 298")
        self.oHelper.SetButton("Visualizar") 
        self.oHelper.ClickTree("298 - Exercicio : 2098 > Periodo 01 de : 01/01/2098 ate : 31/01/2098", right_click=True)
        self.oHelper.CheckResult('CTG_CALEND','298',name_attr=True)
        self.oHelper.CheckResult('CTG_EXERC','2098',name_attr=True)
        self.oHelper.CheckResult('CTG_PERIOD','01',name_attr=True)
        self.oHelper.CheckResult('CTG_DTINI','01/01/2098',name_attr=True)
        self.oHelper.CheckResult('CTG_DTFIM','31/01/2098',name_attr=True)
        self.oHelper.CheckResult('CTG_STATUS','1 - Aberto',name_attr=True)
        self.oHelper.SetButton("x")
        self.oHelper.SetButton("x")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
