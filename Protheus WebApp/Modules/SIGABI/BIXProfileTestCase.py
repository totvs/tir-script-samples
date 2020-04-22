import unittest
from tir import Webapp


class BIXPROFILE(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGACFG','11/12/2018','T1','D MG 01 ')
		inst.oHelper.SetLateralMenu('Ambiente > Extrator Bi > Perfil de Extração')

	def test_BIXPROFILE_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue("Código", "000001")
		self.oHelper.SetValue("Descrição", "Extracao 000001")
		self.oHelper.ClickLabel("Marcar / Desmarcar" )
		self.oHelper.ScrollGrid(column="Tabela", match_value="HL2", grid_number=2)
		self.oHelper.ClickBox("Tabela", contents_list="HL2", grid_number=2)
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
