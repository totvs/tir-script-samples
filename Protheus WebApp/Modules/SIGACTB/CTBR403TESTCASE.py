from tir import Webapp
import unittest


class CTBR403(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/06/2015", "T1", "D MG 01 ", "01")

        inst.oHelper.Program("CTBR403")

    def test_CTBR403_001(self):

        self.oHelper.SetValue("mv_par01", "01/06/2015")  # Data Inicial ?
        self.oHelper.SetValue("mv_par02", "02/06/2015")  # Data final ?
        self.oHelper.SetValue("mv_par03", "01")  # Moeda ?
        self.oHelper.SetValue("mv_par04", "1")  # Tipo de Saldo ?
        self.oHelper.SetValue("mv_par05", "55")  # Num.linhas p/ o Razao ?
        self.oHelper.SetValue("mv_par06",
                              "01")  # Descricao na moeda ?
        self.oHelper.SetValue("mv_par07",
                              "01")  # Impri. Até Entidade ?
        # Seleciona filias ?
        self.oHelper.SetValue("Seleciona filiais ?           ", "Nao")

        self.oHelper.SetButton("Ok")

        ##Não clica nesse componente
        ###self.oHelper.SetValue("Da conta ?", "")
        ###self.oHelper.SetValue(
        ###    "Ate a Conta ?", "ZZZZZZZZZZZZZZZZZZZZ")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Imprimir")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
