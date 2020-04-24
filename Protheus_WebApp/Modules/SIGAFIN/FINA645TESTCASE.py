from tir import Webapp
import unittest

class FINA645(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN','12/05/2019','T1','D MG 01 ','06')
		inst.oHelper.Program("FINA645")

	def test_FINA645_CT001(self):
		self.oHelper.SetButton("Constituição")
		self.oHelper.SetValue('Data Referencia ?','12/05/2019')
		self.oHelper.SetValue('Dias de Atraso ?','1')
		self.oHelper.SetValue('Transferir para Provisao ?', 'Vct apos atraso')                
		self.oHelper.SetValue('Cliente De ?','PDD001')
		self.oHelper.SetValue('Loja De ?','01')
		self.oHelper.SetValue('Cliente Ate ?','PDD001')
		self.oHelper.SetValue('Loja Ate ?','01')
		self.oHelper.SetValue('Emissao De ?','10/05/2019')
		self.oHelper.SetValue('Emissao Ate ?','10/06/2019')
		self.oHelper.SetValue('Seleciona Filial ?','Não')
		self.oHelper.SetValue('Sit Cobranca PDD ?','8')
		self.oHelper.SetValue('Seleciona Sit. de Cobrança ?','Não')
		self.oHelper.SetValue('Considera Negociados ? ','Não')
		self.oHelper.SetButton("OK")
		self.oHelper.WaitShow("Transferência PDD\\PPSC - Provisão PDD")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult('FJX_DTPROC','12052019')
		self.oHelper.CheckResult('FJX_DTREF','12052019')
		self.oHelper.CheckResult('FJX_TIPO','1')
		self.oHelper.AssertTrue()
		self.oHelper.SetButton("Fechar")

	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()