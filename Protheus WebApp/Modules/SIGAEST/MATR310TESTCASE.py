from tir import Webapp
import unittest

class MATR310(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/10/2019','T1','D MG 01')
		inst.oHelper.Program('MATR310')

	def test_MATR310_CT001(self):
		self.oHelper.AddParameter("MV_BLOQUEI", "", ".F.", ".F.", ".F.")	
		self.oHelper.SetParameters()
		self.oHelper.SetButton('Outras Ações', 'Parâmetros')
		self.oHelper.SetValue('Produto de ?','ESTSE0000000000000000000000168')
		self.oHelper.SetValue('Produto ate ?','ESTSE0000000000000000000000171')
		self.oHelper.SetValue('Considera Vlr PIS/COFINS ?','Nao')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Imprimir')
		self.oHelper.SetButton('Sair')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
