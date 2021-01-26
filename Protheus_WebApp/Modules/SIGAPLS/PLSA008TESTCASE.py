from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA010TestCase
TIR - Casos de testes da rotina Perfis de acesso

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA008(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")


	def test_PLSA008_001(self):
		self.oHelper.Program("PLSA008")
		self.oHelper.SetButton("Sim")	# Deseja atualizar os menus dos perfis?

		# Grid 1
		self.oHelper.ClickGridCell("Descrição",row=1, grid_number=1)
		self.oHelper.ScrollGrid('Descrição', match_value='PERFIL ADMINISTRADOR', grid_number=1)
		self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue("Descrição","PERFIL ADMINISTRADOR TIR",grid=True,grid_number=1,row=5)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("Tipo Portal","1",grid=True,grid_number=1,row=5)
		self.oHelper.LoadGrid()

		# Grid 2
		self.oHelper.ClickGridCell("Processos",row=1, grid_number=2)
		self.oHelper.SetKey("ENTER", grid=True,  grid_number=2)

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()


	def test_PLSA008_002(self):
		self.oHelper.Program("PLSA008")
		self.oHelper.SetButton("Sim")	# Deseja atualizar os menus dos perfis?

		# Grid
		self.oHelper.ClickGridCell("Sequencial",row=1, grid_number=1)
		self.oHelper.ScrollGrid('Sequencial', match_value='000003', grid_number=1)
		self.oHelper.SetKey("DELETE", grid=True,  grid_number=1)

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()