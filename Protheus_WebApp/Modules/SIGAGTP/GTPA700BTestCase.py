from tir import Webapp
import unittest

class GTPA700B(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGTP", "23/03/2020", "T1", "D MG 01 ")
        inst.oHelper.Program('GTP700AMB')

    def test_GTPA700B_CT001(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Depositos/Titulos")

        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA700B_CT002(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Taxas Avulsas")

        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA700B_CT003(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Taxas de Bilhetes")

        self.oHelper.ClickGridCell("Agrupar", row=1, grid_number=2)
        self.oHelper.ClickBox("Agrupar", contents_list='',
                              select_all=False, grid_number=2)

        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA700B_CT004(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Vendas Cartão")

        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA700B_CT005(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Vendas Canceladas no Cartão")

        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA700B_CT006(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Notas Fiscais de entrada")

        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA700B_CT007(self):

        self.oHelper.SearchBrowse("D MG    000002", "Filial+cod. Caixa")
        self.oHelper.ClickLabel("+ Gerar Título de Taxa")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Ok")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
