from tir import Webapp
import unittest

class MATC010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","04/07/2019","T1","D MG 01 ","04")
        inst.oHelper.Program("MATC010")

    def test_MATC010_001(self):
        self.oHelper.AddParameter("MV_REVPLAN", "", "T", "T", "T")
        self.oHelper.SetParameters()
        self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000145')
        self.oHelper.SetButton("Forma Precos")
        self.oHelper.ClickGridCell("Niv", 2)
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue('Codigo','ESTSE0000000001')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Recalculo")
        self.oHelper.SetButton("Custo")
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickGridCell("Niv", 2)
        self.oHelper.SetButton("Excluir")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Editar")
        self.oHelper.SetValue('Quantidade','11,000000')
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickGridCell("Niv", 2)
        self.oHelper.SetButton("Editar")
        self.oHelper.SetValue('Quantidade','11,000000')
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Planilha")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetValue('Codigo do Produto:','ESTSE0000000000000000000000145')
        self.oHelper.SetButton("Pesquisar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()