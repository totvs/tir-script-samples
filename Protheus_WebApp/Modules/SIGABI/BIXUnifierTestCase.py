import unittest
from tir import Webapp

class BIXUNIFIER(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGACFG','12/09/2019','T1', 'D MG 01')
		inst.oHelper.SetLateralMenu('Ambiente > Extrator Bi > Consolidador de Dados')

	def test_BIXUNIFIER_CT001(self):

		self.oHelper.SetValue("HGK - Banco, agência e conta", "2 - BANCO, AGÊNCIA E CONTA")
		self.oHelper.SetValue("HJ7 - Cliente", "3 - CPF DO CLIENTE")
		self.oHelper.SetValue("HJ8 - Item", "2 - CÓDIGO DO ITEM")
		self.oHelper.SetValue("HJC - Representante", "2 - CÓDIGO DO REPRESENTANTE")
		self.oHelper.SetValue("HG0 - CFOP", "2 - CFOP")
		self.oHelper.SetValue("HG1 - Família Comercial", "2 - FAMÍLIA COMERCIAL")
		self.oHelper.SetValue("HYE - Natureza Financeira", "2 - NATUREZA FINANCEIRA")
		self.oHelper.SetValue("HHW - Unidade de Medida do Item", "2 - UNIDADE DE MEDIDA DO ITEM")
		self.oHelper.SetValue("HJ5 - Centro de Custo", "2 - CENTRO DE CUSTO")
		self.oHelper.SetValue("HKJ - Fornecedor", "3 - CPF DO FORNECEDOR")
		self.oHelper.SetValue("HJB - Região Geográfica", "2 - REGIÃO GEOGRÁFICA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
