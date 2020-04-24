from tir import Webapp
import unittest

class MATA099(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','23/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA099')

	def test_MATA099_002(self):
		self.oHelper.SearchBrowse('D MG 01 PCP002', 'Filial+conjunto')
		self.oHelper.SetButton('Alterar')
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BX_DESC', 'PCP_TIR_001_CONJUNTOS_ALTE0001', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('BW_CONJUN', 'PCP002')
		self.oHelper.CheckResult('BW_DESC', 'PCP_TIR_002_CONJUNTOS_CONJ0001')
		self.oHelper.CheckResult('BX_CODOP', '001', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BX_DESC', 'PCP_TIR_001_CONJUNTOS_ALTE0001', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MATA099_003(self):
		self.oHelper.SearchBrowse('D MG 01 PCP003', 'Filial+conjunto')
		self.oHelper.SetButton('Outras Ações', 'Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()