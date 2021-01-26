from tir import Webapp
import unittest

class GFEX100(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','28/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEX100')

	def test_GFEX100_CT001(self):

		self.oHelper.SetValue('Pré-fatura ?','Dt.Criacao')
		self.oHelper.SetValue('Doc. Frete ?','Dt.Emissao')
		self.oHelper.SetValue('Fatura ?','Dt. Emissão')
		self.oHelper.SetValue('Contrato ?','Dt. Criação')
		self.oHelper.SetValue('Filial de ?','')
		self.oHelper.SetValue('Filial até ?','ZZZZZZZZ')
		self.oHelper.SetValue('Data de ?','01/01/2000')
		self.oHelper.SetValue('Data até ?','31/12/2049')
		self.oHelper.SetValue('Situação ?','Ambos')
		self.oHelper.SetValue('Apto ?','Ambos')

		self.oHelper.SetButton('OK')
		
		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Situação Financeiro')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
