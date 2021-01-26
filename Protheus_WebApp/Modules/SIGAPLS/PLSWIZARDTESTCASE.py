from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA940TestCase
TIR - Casos de testes da rotina Wizard de Atualização

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSWIZARD(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSWIZARD")

	def test_PLSWIZARD_001(self):
		# Incluir
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.ClickCheckBox("Habilitar alteração de registro existente?",1)
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.SetButton("Avançar >>")
		#self.oHelper.SetButton("Avançar >>")
		#self.oHelper.SetButton("Fechar")
		self.oHelper.ClickGridCell("Grupo Emp",row=7, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Avançar >>")
		self.oHelper.ClickGridCell("Código",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Finalizar")
		self.oHelper.SetButton("Sim")

		time.sleep(15)

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()