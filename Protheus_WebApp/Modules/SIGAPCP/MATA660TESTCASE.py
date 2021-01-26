from tir import Webapp
import unittest

class MATA660(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','26/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA660')

	def test_MATA660_001(self):
    		
		self.oHelper.SetButton('Outras Ações', 'Incluir')

		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetValue('H9_RECURSO','MT6601')
		self.oHelper.SetValue('H9_MOTIVO','QUEBRA DE EQUIPAMENTO')
		self.oHelper.SetValue('H9_DTINI','25/04/2019')
		self.oHelper.SetValue('H9_DTFIM','27/04/2019')
		self.oHelper.SetValue('H9_HRINI','10:00')
		self.oHelper.SetValue('H9_HRFIM','15:00')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult('H9_RECURSO','MT6601')
		self.oHelper.CheckResult('H9_CCUSTO','PCP000001')
		self.oHelper.CheckResult('H9_MOTIVO','QUEBRA DE EQUIPAMENTO')
		self.oHelper.CheckResult('H9_DTINI','25/04/2019')
		self.oHelper.CheckResult('H9_DTFIM','27/04/2019')
		self.oHelper.CheckResult('H9_HRINI','10:00')
		self.oHelper.CheckResult('H9_HRFIM','15:00')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA660_002(self):
  
		self.oHelper.SearchBrowse('D MG 01 BPCP000001MT6602')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('H9_DTINI','26/04/2019')
		self.oHelper.SetValue('H9_HRFIM','18:00')
		
		self.oHelper.SetButton('Salvar')
		
		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult('H9_RECURSO','MT6602')
		self.oHelper.CheckResult('H9_CCUSTO','PCP000001')
		self.oHelper.CheckResult('H9_MOTIVO','QUEBRA DE EQUIPAMENTO')
		self.oHelper.CheckResult('H9_DTINI','26/04/2019')
		self.oHelper.CheckResult('H9_DTFIM','27/04/2019')
		self.oHelper.CheckResult('H9_HRINI','10:00')
		self.oHelper.CheckResult('H9_HRFIM','18:00')
		
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()


	def test_MATA660_003(self):
    		
    	
		self.oHelper.SearchBrowse('D MG 01 BPCP000001MT6603')
		self.oHelper.SetButton('Outras Ações', 'Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_MATA660_004(self):
    		
		self.oHelper.SetButton('Assistente')

		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetValue('H9_RECURSO','MT6604')
		self.oHelper.SetValue('H9_MOTIVO','QUEBRA DE EQUIPAMENTO')
		self.oHelper.SetValue('H9_DTINI','26/04/2019')
		self.oHelper.SetValue('H9_DTFIM','26/04/2019')
		self.oHelper.SetValue('H9_HRINI','10:00')
		self.oHelper.SetValue('H9_HRFIM','15:00')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult('H9_RECURSO','MT6604')
		self.oHelper.CheckResult('H9_CCUSTO','PCP000001')
		self.oHelper.CheckResult('H9_MOTIVO','QUEBRA DE EQUIPAMENTO')
		self.oHelper.CheckResult('H9_DTINI','26/04/2019')
		self.oHelper.CheckResult('H9_DTFIM','26/04/2019')
		self.oHelper.CheckResult('H9_HRINI','10:00')
		self.oHelper.CheckResult('H9_HRFIM','15:00')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()