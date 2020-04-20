from tir import Webapp
import unittest

class ACDA150(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','12/01/2020','T1','D MG 01')
		inst.oHelper.Program('ACDA150')	

	def test_ACDA150_CT001(self):
		
		self.oHelper.SearchBrowse("D MG 01 EST00701FIN026",key=2, index=True)
		self.oHelper.SetButton("Consulta")	
		self.oHelper.CheckResult("Produto","ESTSE0000000000000000000000714", grid=True, line=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
			
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()