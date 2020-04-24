from tir import Webapp
import unittest

class MATA730(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','29/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA730')

	def test_MATA730_001(self):
		self.oHelper.SetValue('Periodo Inicial ?','29/04/2019')
		self.oHelper.SetValue('Periodo Final ?','29/04/2019')
		self.oHelper.SetValue('Dt.Entrega De ?','29/04/2019')
		self.oHelper.SetValue('Dt.Entrega Ate ?','29/04/2019')
		self.oHelper.SetValue('Ordem de Prod. De ?','PCP13301001')
		self.oHelper.SetValue('Ordem de Prod. Ate ?','PCP13301001')
		self.oHelper.SetValue('Saldo a Considerar ?','Ordem de Prod.')
		self.oHelper.SetValue('Considera informacoes ?','Roteiro operaco')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.ClickBox('Numero da OP','PCP133')
		self.oHelper.SetButton('Calculo')
		self.oHelper.Program('MATA730')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()