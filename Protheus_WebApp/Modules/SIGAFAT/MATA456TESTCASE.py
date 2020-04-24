from tir import Webapp
import time
import unittest

class MATA456(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','02/03/2020','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA456')

	def test_MATA456_001(self):
		pedido = 'FAT047'
	
		self.oHelper.SetValue('Restringir Bloqueio ?', 'Credito/Estoque')
		self.oHelper.SetButton('OK')
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}')
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}')
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Pedido')
		self.oHelper.CheckResult('C5_NUM',pedido)	
		self.oHelper.AssertFalse()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()