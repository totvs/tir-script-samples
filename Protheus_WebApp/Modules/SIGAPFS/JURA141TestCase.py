from tir import Webapp
import unittest

class JURA141(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPFS','28/12/2020','T1','M SP 01 ','77')
		inst.oHelper.Program('JURA141')
	'''
	//-------------------------------------------------------------------
	test_JURA141_CT005 - Não permite WO de faturas com documento fiscal emitido
	@author Abner Fogaça de Oliveira
	@since  23/12/2020
	@obs    T56591 - https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56591
	//-------------------------------------------------------------------
	'''
	def test_JURA141_CT005(self):
		self.oHelper.SearchBrowse("SP100000000181")
		self.oHelper.CheckResult("Cód. Fatura", "000000181", grid = True)
		self.oHelper.LoadGrid()
		self.oHelper.AssertFalse()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()