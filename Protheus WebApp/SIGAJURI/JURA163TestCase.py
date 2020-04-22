from tir import Webapp
import unittest

class JURA163(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','16/07/2019','T1','D MG 01 ','76')
		inst.oHelper.Program('JURA163')

	def test_JURA163_CT001(self):
		self.oHelper.ClickFolder("Grupos")
		self.oHelper.ClickFolder("Principal")
		self.oHelper.ClickGridCell("Descrição",row=1)
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickFolder("Campos")
		self.oHelper.ScrollGrid(column="Campo",match_value="NSZ_CFCORR")
		self.oHelper.SetValue('Obrigatório',True,grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Close")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		
if __name__ == '__main__':
	unittest.main()
