from tir import Webapp
import unittest


class CTBA101(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/01/2019", "T1", "D MG 01", "34")

        inst.oHelper.Program("CTBA101")

    def test_CTBA101_001(self):
        # Estorno
        COD = "000000004           01/06/2015"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Debito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Estornar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA101_002(self):
        # Excluir
        COD = "000000005           02/06/2015"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Credito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Credito + Data Lcto")

        self.oHelper.AssertTrue()

    def test_CTBA101_003(self):
        # Visualizar
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_CTBA101_004(self):
        # Alterar
        COD = "000000003           02/01/2020"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Credito + Data Lcto")

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok")        
        
        self.oHelper.ClickFolder("Conversoes")

        self.oHelper.CheckResult(
            "crit", "Informada", grid=True, line=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
