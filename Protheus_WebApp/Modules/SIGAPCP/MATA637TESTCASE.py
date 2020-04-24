from tir import Webapp
import unittest

class MATA637(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','25/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA637')

	def test_MATA637_002(self):
		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA637_002_PA000000010110', 'Filial+produto + Roteiro + Operacao..')
		self.oHelper.SetButton('Alterar')
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('GF_OPERAC','30', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('GF_PRODUTO','PCP_TIR_MATA637_002_PA00000001')
		self.oHelper.CheckResult('GF_ROTEIRO','01')
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('GF_OPERAC','20', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('GF_COMP','PCP_TIR_MATA637_002_MP00000002', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('GF_OPERAC','30', grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('GF_COMP','PCP_TIR_MATA637_002_MP00000001', grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()