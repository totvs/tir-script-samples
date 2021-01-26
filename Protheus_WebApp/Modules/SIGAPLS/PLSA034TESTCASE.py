from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA034TestCase
TIR - Casos de testes da rotina Horarios especiais

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA034(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA034")

	def test_PLSA034_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue(field = "cCodAti", value = "006", name_attr = True)
		self.oHelper.SetValue(field = "cDesAti", value = "PLS DSAUPS TIR INCLUSAO", name_attr = True)
		self.oHelper.SetValue(field = "cDesc", value = "TIR INCLUSAO", name_attr = True)
		self.oHelper.ClickCheckBox("Domingo",1)
		self.oHelper.SetValue(field = "cHorIni", value = "1200", name_attr = True,check_value = False)
		self.oHelper.SetValue(field = "cHorFin", value = "2359", name_attr = True,check_value = False)
		self.oHelper.SetValue(field = "nPerc", value = "10", name_attr = True,check_value = False)
		self.oHelper.SetValue(field = "dVigIni", value = "01/01/2020", name_attr = True)
		self.oHelper.SetValue(field = "dVigFin", value = "31/12/2020", name_attr = True)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse("M SP    006")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue(field = "nPerc", value = "20", name_attr = True,check_value = False)
		self.oHelper.SetButton("Salvar")

		self.oHelper.SearchBrowse("M SP    006")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult(field = "nPerc", user_value = "20", name_attr = True)
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SearchBrowse("M SP    006")
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()