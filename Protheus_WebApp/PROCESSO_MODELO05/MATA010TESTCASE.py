from tir import Webapp
import unittest
from datetime import datetime

class MATA010(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.grupo = "T1"

		inst.oHelper = Webapp()  # INSTANCIAR A CLASSE
		inst.oHelper.Setup('SIGAFAT', '09/06/2020', inst.grupo, 'D MG 01 ', '05')
		inst.oHelper.SetLateralMenu("Atualizações > Cadastros > Produtos")

	def test_MATA010_CT001(self, oHelper=None):
		"""
		teste 1
		:return:
		"""

		if oHelper:
			self.oHelper = oHelper

		cod = 'ESTSE0000000000000000000000001'

		self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
		self.oHelper.SetButton("X")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()