from tir import Webapp
import unittest

class MATA105(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATA105')		

	def test_MATA105_CT001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Número','EST010')
		self.oHelper.SetValue('Solicitante','pedro.missaglia')
		self.oHelper.SetValue('Data de Emissäo','04/07/2019')
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000235", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("Armazem", "01", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Outras Ações', 'Rateio')
		self.oHelper.SetValue("% Rat.", "50,00", grid=True)
		self.oHelper.SetValue("C. de Custo", "ESTSE0001", grid=True)
		self.oHelper.SetValue("C Contabil", "ESTSE000000000000001", grid=True)
		self.oHelper.SetValue("Item Conta", "EST000001", grid=True)
		self.oHelper.SetValue("Classe Valor", "EST000001", grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue("% Rat.", "50,00", grid=True)
		self.oHelper.SetValue("C. de Custo", "ESTSE0002", grid=True)
		self.oHelper.SetValue("C Contabil", "ESTSE000000000000001", grid=True)
		self.oHelper.SetValue("Item Conta", "EST000001", grid=True)
		self.oHelper.SetValue("Classe Valor", "EST000001", grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()