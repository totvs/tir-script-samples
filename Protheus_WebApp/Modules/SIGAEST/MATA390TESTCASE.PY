#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA390
#
#@author cris
#@since 29/10/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA390(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","29/10/2020","T1","D MG 01")
		inst.oHelper.Program("MATA390")

	# CT001 - Visualizar registros relacionados ao lote posicionado - GTSER-T55308
	def test_MATA390_001(self):	

		self.oHelper.SearchBrowse("D MG 01 ESTMATA39000000000000000000003 01",key=2, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("Lote","AUTO000191",grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Cancelar") 
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()


if __name__ == '__main__':
	unittest.main()
