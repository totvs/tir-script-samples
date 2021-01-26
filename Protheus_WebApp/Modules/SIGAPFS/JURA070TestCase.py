from tir import Webapp
import unittest

class JURA070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPFS','08/12/2020','T1','M SP 01 ','77')
		inst.oHelper.Program('JURA070')
	'''
	//-------------------------------------------------------------------
	test_JURA070_CT010 - Alteração de caso sem contrato (com loja automática)

	@author Abner Fogaça de Oliveira
	@since  07/05/2020
	@obs    GTSER-T52498 - https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T52498
	//-------------------------------------------------------------------
	'''
	def test_JURA070_CT010(self):
		self.oHelper.AddParameter("MV_JLOJAUT", "", "1", "", "")
		self.oHelper.AddParameter("MV_JURHS1", "", ".T.", "", "")
		self.oHelper.SetParameters()
		self.oHelper.SetButton("Outras Ações","Casos sem contrato")
		self.oHelper.SetValue("A1_COD","PFS011")
		self.oHelper.SetValue("NVE_DTENTR","08/12/2020")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickFolder("Histórico do Caso")
		self.oHelper.SetValue("Tab Honor", "1000", grid = True, grid_number = 1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult("Tab Honor", "1000", grid = True, line = 1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","Atualizar")
		self.oHelper.SetButton("X")
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()