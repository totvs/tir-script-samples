from tir import Webapp
import unittest

class FINA171(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN','12/09/2019','T1','D MG 01 ','06')
		inst.oHelper.Program("FINA171")

	def test_FINA171_CT006(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('Numero','FITIR1')
		self.oHelper.SetValue('Modelo',"A")
		self.oHelper.SetValue('Operacao',"CDB")
		self.oHelper.SetValue('Banco',"033")
		self.oHelper.SetValue('Agencia', '00001')
		self.oHelper.SetValue('Conta Banco', '0000000004')
		self.oHelper.SetValue('Vlr.Operacao', '1000,00')
		self.oHelper.SetValue('Moeda', '1')
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult('EH_NUMERO','FITIR1')
		self.oHelper.CheckResult('EH_APLEMP','APL')
		self.oHelper.CheckResult('EH_TIPO','CDB')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','1000,00')
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SearchBrowse(f"D MG 01 FITIR101")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.CheckResult('EH_NUMERO','FITIR1')
		self.oHelper.CheckResult('EH_APLEMP','APL')
		self.oHelper.CheckResult('EH_TIPO','CDB')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','1000,00')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()