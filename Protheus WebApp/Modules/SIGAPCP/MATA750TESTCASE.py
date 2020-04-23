from tir import Webapp
import unittest

class MATA750(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','20/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA750')

	def test_MATA750_001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('HC_PRODUTO', 'PCP_TIR_MATA750_PMP_PA00000001')
		self.oHelper.SetValue('HC_DATA','20/04/2019')
		self.oHelper.SetValue('HC_QUANT','10,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SearchBrowse('D MG 01 20/04/2019PCP_TIR_MATA750_PMP_PA00000001', 'Filial+dt Previsao + Produto')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('HC_PRODUTO', 'PCP_TIR_MATA750_PMP_PA00000001')
		self.oHelper.CheckResult('HC_DATA','20/04/2019')
		self.oHelper.CheckResult('HC_QUANT','10,00')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MATA750_002(self):
		self.oHelper.SearchBrowse('D MG 01 18/04/2019PCP_TIR_MATA750_PMP_PA00000001', 'Filial+dt Previsao + Produto')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('HC_QUANT','20,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('HC_PRODUTO', 'PCP_TIR_MATA750_PMP_PA00000001')
		self.oHelper.CheckResult('HC_DATA','18/04/2019')
		self.oHelper.CheckResult('HC_QUANT','20,00')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()