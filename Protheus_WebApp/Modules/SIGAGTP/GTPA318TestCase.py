from tir import Webapp
import unittest

class GTPA318(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "05/08/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA318')

	def test_GTPA318_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue('G56_CODIGO', 'TESGTP')
		self.oHelper.SetValue('G56_VIAGEM', '000001')
		self.oHelper.SetValue('G56_LOCORI', 'LOC001')
		self.oHelper.SetValue('G56_LOCDES', 'LOC002')
		self.oHelper.SetValue('G56_MEMO'  , 'TESTE INCLUSAO')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	
	def test_GTPA318_CT002(self):
		self.oHelper.SearchBrowse("D MG    000006", "Filial+código")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult('G56_CODIGO', '000006')
		self.oHelper.CheckResult('G56_VIAGEM', '000003')
		self.oHelper.CheckResult('G56_LOCORI', 'LOC001')
		self.oHelper.CheckResult('G56_LOCDES', 'LOC002')
		self.oHelper.CheckResult('G56_MEMO', 'TESTE VISUALIZACAO')
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		
	def test_GTPA318_CT003(self):
		self.oHelper.SearchBrowse("D MG    000006", "Filial+código")
		self.oHelper.SetButton("Outras Ações", "Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
	
	def test_GTPA318_CT004(self):
		self.oHelper.SearchBrowse("D MG    000007", "Filial+código")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.CheckResult('G56_CODIGO', '000007')
		self.oHelper.CheckResult('G56_VIAGEM', '000005')
		self.oHelper.CheckResult('G56_LOCORI', 'LOC001')
		self.oHelper.CheckResult('G56_LOCDES', 'LOC002')
		self.oHelper.CheckResult('G56_MEMO', 'TESTE EXCLUSAO')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
