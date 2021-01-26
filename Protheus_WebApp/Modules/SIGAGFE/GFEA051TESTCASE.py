from tir import Webapp
import unittest

class GFEA051(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "11/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA051")

    def test_GFEA051_CT001(self):

        self.oHelper.SetButton("Entrega")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")

        self.oHelper.ScrollGrid(column="Numero Docto", match_value="2810202")

        self.oHelper.SetButton("Entrega")

        self.oHelper.SetValue('Data Entrega:','30/10/2020')
        self.oHelper.SetValue('Hora Entrega:','16:00')

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Entrega")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton('Outras Ações','Cancelar Entrega')

        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()