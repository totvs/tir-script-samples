from tir import Webapp
import unittest

class ACDA100(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('ACDA100')	

	def test_ACDA100_CT001(self):

		#Definição dos perguntes - F12
		self.oHelper.WaitShow("Ordens de separacao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue('Opcao ?', 'Ordem Producao')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		#Definição do operação
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Ok')
		
		#Definição dos perguntes para filtragem

		self.oHelper.SetValue('Separador ?', '')
		self.oHelper.SetValue('Op de ?', '')
		self.oHelper.SetValue('Op ate ?', 'pcpA1P')
		self.oHelper.SetValue('Data emissao de ?', '18/09/2019')
		self.oHelper.SetValue('Data emissao ate ?', '18/09/2019')
		self.oHelper.SetValue('Pre-Separacao ?', 'Sim')
		
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000328")
		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')

		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()