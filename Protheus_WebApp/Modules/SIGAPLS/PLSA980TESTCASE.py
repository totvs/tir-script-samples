from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA980TestCase
TIR - Casos de testes da rotina Operadores do sistema

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA980(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA980")

	def test_PLSA980_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BX4_CODOPE","000000")
		self.oHelper.SetValue("BX4_CODINT","0176",check_value = False)
		self.oHelper.SetValue("BX4_ALTBIO", "0 - Nao")
		self.oHelper.SetValue("BX4_CANBIO", "0 - Nao")
		self.oHelper.SetValue("BX4_CODDEP","001")
		self.oHelper.SetValue("BX4_CODCAR","001")
		self.oHelper.SetValue("BX4_PROCES", "0 - Não")
		self.oHelper.SetValue("BX4_DIRFAX","C:/TEMP")
		self.oHelper.SetValue("BX4_PERAUD", "2 - Administrativa")
		self.oHelper.SetValue("BX4_INTSAU", "0 - Não")
		self.oHelper.SetValue("BX4_ENCMIN", "0 - Não")
		self.oHelper.SetValue("BX4_DIRDOC","")
		self.oHelper.SetValue("BX4_PARTIC", "0 - Não")
		self.oHelper.SetValue("BX4_MOTFAX", "0 - Não")
		self.oHelper.SetValue("BX4_DIRDOC","C:/TEMP")
		self.oHelper.SetValue("BX4_MOTDOC", "0 - Não")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f'{"M SP    0000000176"}', key=1, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BX4_PADRAO", "1 - Sim")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SearchBrowse(f'{"M SP    0000000176"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BX4_PADRAO", "1 - Sim")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SearchBrowse(f'{"M SP    0000000176"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("x")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()