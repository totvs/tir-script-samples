from tir import Webapp
import unittest

class GCPA200(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGCP','24/06/2019','T1','D MG 01 ','87')
		inst.oHelper.Program('GCPA200')
	
	def test_GCPA200_CT001(self):
		edital = 'GCPTIRTRACKER01'
		processo = 'GCPTIRTRACKER01'
		
		self.oHelper.SearchBrowse(f'D MG 01 {edital}{processo}', key=1, index=True)
		self.oHelper.SetButton('Visualizar')
		self.oHelper.WaitShow('Processo Licitatório - Visualizar')	
		self.oHelper.SetButton('Outras Ações', sub_item='Tracker')
		self.oHelper.SetButton('Rastrear')
		self.oHelper.ClickTree('Cod. Edital / Num.Pro - GCPTIRTRACKER01 / GCPTIRTRACKER01')
		self.oHelper.ClickTree('Pedido de Compra  - PMS510')
		self.oHelper.ClickTree('Pedido de Compra  - PMS511')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()