from tir import Webapp
import unittest

class MATA230(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','14/11/2019','T1','D MG 01')
		inst.oHelper.Program('MATA230')		

	def test_MATA230_CT001(self):
		self.oHelper.SearchBrowse("D MG 01 701")
		self.oHelper.SetButton("Outras Ações","Permissões por TM")		
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetValue("usuário","000000",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Outras Ações","Permissões por TM")
		self.oHelper.CheckResult("nome","Administrador",grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.AssertTrue()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()