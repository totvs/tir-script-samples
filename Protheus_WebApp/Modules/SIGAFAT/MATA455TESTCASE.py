from tir import Webapp
import unittest

class MATA455(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','02/03/2020','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA455')

	def test_MATA455_004(self):
		pedido = 'pcpABB'
		
		self.oHelper.AddParameter("MV_SELLOTE","D MG 01","1","1","1")
		self.oHelper.SetParameters()
		self.oHelper.SetValue('Restringir Bloqueio ?', 'Sem Restricao')
		self.oHelper.SetButton('OK')
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}')
		self.oHelper.SetButton('Outras Ações','Nova Liberacao')
		self.oHelper.SetValue("Qtd.neste item", "5,00")
		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse(f'D MG 01 {pedido}')
		self.oHelper.SetButton('Outras Ações','Nova Liberacao')
		self.oHelper.CheckResult("Qtd.neste item", "5,00")
		self.oHelper.RestoreParameters()
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()