from tir import Webapp
import unittest

class MATA450(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','17/07/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA450')

	def test_MATA450_CT001(self):
		self.oHelper.SetValue('Somente Bloqueados ?', 'Sim')
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse("D MG 01 FAT175")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse("D MG 01 FAT175")
		self.oHelper.SetButton('Manual')
		self.oHelper.SetButton('Pedido')
		pedido = self.oHelper.GetValue("C5_NUM")
		if pedido == 'FAT175':
			self.oHelper.AssertFalse()
		else:
			self.oHelper.SetButton('Cancelar')
			self.oHelper.SetButton('Estoque')
			self.oHelper.SetButton('Ok')
			self.oHelper.SetButton('Cancelar')
			self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()