from tir import Webapp
import unittest

class OGC090(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAAGR','20/09/2019','T1','D MG 01 ','67')
		inst.oHelper.Program('OGC090')

	def test_OGC090_CT001(self):		
		self.oHelper.SetButton('Simular')				
		self.oHelper.ClickBox("Romaneio", select_all=True,  grid_number=1)		
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Fechar') #fecha mensagem		
        
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()