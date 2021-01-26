from tir import Webapp
import unittest

class GTPA701(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGTP", "25/09/2020", "T1", "D MG 01 ")
        inst.oHelper.Program('GTPA000')

    def test_GTPA701_CT001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue('Órgão', 'TESTE')
        self.oHelper.SetValue('Descrição', 'TESTE')
        self.oHelper.SetValue('Sigla', 'TESTE')
        self.oHelper.ClickGridCell("Cod Tp Linha", row=1, grid_number=1)
        self.oHelper.SetValue('Cod Tp Linha', '000003', grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell("Cód. Categ.", row=1, grid_number=2)
        self.oHelper.SetValue('Cód. Categ.', 'GTP001', grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Outras Ações", "Tarifa")
        self.oHelper.SetValue('Vigencia','25/09/2020')
        self.oHelper.ClickGridCell("Vlr Min Tar.", row=1, grid_number=1)
        self.oHelper.SetValue('Vlr Min Tar.', '50,00', grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetValue('Campo', '1')
        self.oHelper.SetButton("Inserir")
        self.oHelper.SetButton("Limpar Tudo")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetValue('Campo', '3') 
        self.oHelper.SetButton("Inserir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações", "Pedágio")
        self.oHelper.SetValue('Vigencia','25/09/2020')
        self.oHelper.SetValue('Campo', '7')
        self.oHelper.SetButton("Inserir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações", "Tx. Embarque")
        self.oHelper.SetValue('Vigencia','25/09/2020')
        self.oHelper.SetValue('Campo', '6')
        self.oHelper.SetButton("Inserir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
