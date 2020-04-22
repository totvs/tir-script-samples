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
		inst.oHelper.Setup('SIGAEST','20/09/2019','T1','D MG 01')
		inst.oHelper.Program('MATA311')		

	def test_MAT311_001(self):

		self.oHelper.SearchBrowse("D MG 01 0000000010")
		self.oHelper.SetButton('Outras Ações', 'Copia')
		self.oHelper.CheckResult("NNS_DATA", "20/09/2019")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()