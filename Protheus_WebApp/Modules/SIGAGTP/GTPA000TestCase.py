from tir import Webapp
import unittest

class GTPA000(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA000')

	def test_GTPA000_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue('Órgão', 'GTP000')
		self.oHelper.SetValue('Descrição', 'TESTE')
		self.oHelper.SetValue('Sigla', 'ANTT')
		self.oHelper.ClickGridCell("Cod Tp Linha", row=1, grid_number=1)
		self.oHelper.SetValue('Cod Tp Linha', '000001', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Cód. Categ.", row=1, grid_number=2)
		self.oHelper.SetValue('Cód. Categ.', 'GTP001', grid=True, grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP000", "Órgão")
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickGridCell("Reaj. Tarifa", row=1, grid_number=1)
		self.oHelper.SetValue('Reaj. Tarifa', '2', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Reaj.Pedágio", row=1, grid_number=1)
		self.oHelper.SetValue('Reaj.Pedágio', '2', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Reaj.Taxa", row=1, grid_number=1)
		self.oHelper.SetValue('Reaj.Taxa', '2', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP000", "Órgão")
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickGridCell("Reaj. Tarifa", row=1, grid_number=1)
		self.oHelper.SetValue('Reaj. Tarifa', '3', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Reaj.Pedágio", row=1, grid_number=1)
		self.oHelper.SetValue('Reaj.Pedágio', '3', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.ClickGridCell("Reaj.Taxa", row=1, grid_number=1)
		self.oHelper.SetValue('Reaj.Taxa', '3', grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP000", "Órgão")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP000", "Órgão")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
