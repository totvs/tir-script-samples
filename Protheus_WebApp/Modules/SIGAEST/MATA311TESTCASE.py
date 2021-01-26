#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA311
#
#@author pedro.missaglia
#@since 09/03/2020
#@version P12
#@see https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/143345
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA311(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/01/2021','T1','D MG 01')
		inst.oHelper.Program('MATA311')		

	def test_MAT311_001(self):

		self.oHelper.SearchBrowse("D MG 01 0000000010")
		self.oHelper.SetButton('Outras Ações', 'Copia')
		self.oHelper.CheckResult("NNS_DATA", "21/01/2021")
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Sair da página')

		self.oHelper.AssertTrue()

	def test_MAT311_002(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")
		time.sleep(1)
		
		self.oHelper.ClickGridCell("Produto", 1)
		self.oHelper.SetValue("Produto","ESTSE0000000000000000000001152",grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetFocus("Endereço", grid_cell=True, row_number=1)
		time.sleep(1)
		self.oHelper.SetKey("F4",grid=True)
		self.oHelper.SetButton("Ok")
		time.sleep(2)
		self.oHelper.SetKey("ENTER",grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.CheckResult("Lote","LOTE001",grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()