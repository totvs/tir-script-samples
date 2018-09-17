from tir import Webapp
import unittest

class MATA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN','10/08/2017','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA030')

	def test_MATA030_CT001(self):

		pedido = 'FAT913'

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.SetValue('A1_COD', pedido)
		self.oHelper.SetValue('A1_LOJA','01')
		self.oHelper.SetValue('A1_PESSOA','F - Fisica')
		self.oHelper.SetValue('A1_NOME','PESSOA FISICA')
		self.oHelper.SetValue('A1_NREDUZ','PESSOA FISICA')
		self.oHelper.SetValue('A1_END','RUA SALETE, 154')
		self.oHelper.SetValue('A1_TIPO','F - Cons.Final')
		self.oHelper.SetValue('A1_EST','SP')
		self.oHelper.SetValue('A1_COD_MUN','50308')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse(f'D MG    {pedido}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.CheckResult('A1_COD', pedido)
		self.oHelper.CheckResult('A1_LOJA','01')
		self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
		self.oHelper.CheckResult('A1_NOME','PESSOA FISICA')
		self.oHelper.CheckResult('A1_NREDUZ','PESSOA FISICA')
		self.oHelper.CheckResult('A1_END','RUA SALETE, 154')
		self.oHelper.CheckResult('A1_TIPO','F - Cons.Final')
		self.oHelper.CheckResult('A1_EST','SP')
		self.oHelper.CheckResult('A1_COD_MUN','50308')

		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()