from tir import Webapp
import unittest

class GTPA111(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "13/08/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA111')

	def test_GTPA111_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('GQQ_CODIGO', 'GTP002')
		self.oHelper.SetValue('GQQ_CODFUN', '000002')
		self.oHelper.SetValue('GQQ_NUMVAL', 'GTPTES')
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sair da página")
		self.oHelper.AssertTrue()

	def test_GTPA111_CT002(self):
		self.oHelper.SearchBrowse("D MG    GTPTESGTP001", "Filial+num. do Vale + Código")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult('GQQ_CODIGO', 'GTP001')
		self.oHelper.CheckResult('GQQ_CODFUN', '000002')
		self.oHelper.CheckResult('GQQ_NUMVAL', 'GTPTES')
		self.oHelper.CheckResult('GQQ_VALOR' ,  '100')
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	def test_GTPA111_CT003(self):
		self.oHelper.SearchBrowse("D MG    GTPTESGTP001", "Filial+num. do Vale + Código")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.CheckResult('GQQ_CODIGO', 'GTP001')
		self.oHelper.CheckResult('GQQ_CODFUN', '000002')
		self.oHelper.CheckResult('GQQ_NUMVAL', 'GTPTES')
		self.oHelper.CheckResult('GQQ_VALOR' ,  '100')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
