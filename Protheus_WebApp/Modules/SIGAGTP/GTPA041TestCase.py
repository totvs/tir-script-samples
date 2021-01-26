from tir import Webapp
import unittest

class GTPA041(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "20/11/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA041')

	def test_GTPA041_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue('Grup. Cod.', 'GTP001')
		self.oHelper.SetValue('Grup. Desc', 'TESTE')
		self.oHelper.ClickGridCell("Código Dest.", row=1)
		self.oHelper.SetValue('Código Dest.', '000001', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP001", "Grup. Cod.")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue('Grup. Desc', 'TESTE 2')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP001", "Grup. Cod.")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse("GTP001", "Grup. Cod.")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
