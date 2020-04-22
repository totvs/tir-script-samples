from tir import Webapp
import unittest


class GTPA700POS(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGTP", "30/03/2020", "T1", "D MG 01 ")
        inst.oHelper.Program('GTP700AMB')

    def test_GTPA700POS_CT001(self):

        self.oHelper.SearchBrowse("D MG    000014", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Vendas Cartão")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()

    def test_GTPA700POS_CT002(self):

        self.oHelper.SearchBrowse("D MG    000014", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("Fechar Caixa")
        self.oHelper.WaitProcessing("Aguarde o fechamento do caixa.")
        self.oHelper.SetButton("Ok")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
