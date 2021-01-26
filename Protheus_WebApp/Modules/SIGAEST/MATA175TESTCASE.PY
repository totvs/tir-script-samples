#//-------------------------------------------------------------------
#@author Jefferson silva de sousa
#@since 25/09/2019
#@version 1.0
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA175(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","14/11/2019","T1","D MG 01")
		inst.oHelper.Program("MATA175")

	def test_MAT175_001(self):
		#liberaR CQ
		filial   = "D MG 01 "
		prod     = "ESTSE0000000000000000000000306"
		numTrans = "SK0017"

		self.oHelper.SearchBrowse(f"{filial}{numTrans}{prod}")

		self.oHelper.SetButton("Liberar/Rejeitar")
		time.sleep(5)
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue("Tipo", "1", grid=True)
		self.oHelper.SetValue("Quantidade", "35550,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Saldo", "500,00", grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Saldo 2a UM", "8,33", grid=True, line=2)
		self.oHelper.LoadGrid()

		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue("Tipo", "2", grid=True)
		self.oHelper.SetValue("Quantidade", "40,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Saldo", "460,00", grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Saldo 2a UM", "7,66", grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Armazem Des.", "98", grid=True, line=3)
		self.oHelper.LoadGrid()

		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue("Tipo", "1", grid=True)		
		self.oHelper.SetValue("Quantidade", "460,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Saldo", "0,00", grid=True, line=4)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Saldo 2a UM", "0,00", grid=True, line=4)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	def test_MAT175_002(self):

		self.oHelper.SearchBrowse("D MG 01 SK001GESTMATA175TIR00000000000000000")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("Cod.Produto","ESTMATA175TIR00000000000000000")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	def test_MAT175_003(self):
		self.oHelper.SearchBrowse("D MG 01 SK001HESTMATA175TIR00000000000000000")
		self.oHelper.SetButton("Outras Ações", "Estornar")
		self.oHelper.SetValue("Estorno", "X", grid=True, grid_number=1, ignore_case=True, row=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
