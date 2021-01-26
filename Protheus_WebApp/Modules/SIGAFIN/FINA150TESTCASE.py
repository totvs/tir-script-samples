from tir import Webapp
import unittest
import time

class FINA150(unittest.TestCase):

	@classmethod
	def setUpClass(inst):

		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()
		#Parametros de inicialização
		inst.oHelper.Setup('SIGAFIN','28/07/2020','T1','D MG 01 ','06')
		#Nome da rotina do Caso de Teste

		inst.oHelper.Program("FINA150")

		#Setup dos parametros
		inst.oHelper.AddParameter("MV_LOCENV" , "", "/SYSTEM/", "/SYSTEM/", "/SYSTEM/")
		inst.oHelper.SetParameters()

	def test_FINA150_CT006(self):

		self.oHelper.SetValue('Do Bordero ?'         	,'A0001A')
		self.oHelper.SetValue('Ate o Bordero ?'     	,'A0001A')
		self.oHelper.SetValue('Arquivo de Config. ?'	,'TST.2RE')
		self.oHelper.SetValue('Arquivo de Saida ?'		,'FINA150_CT006')
		self.oHelper.SetValue('Codigo do Banco ?'		,'FIN')
		self.oHelper.SetValue('Codigo da Agencia ?'		,'150')
		self.oHelper.SetValue('Codigo da Conta ?'		,'FINA150')
		self.oHelper.SetValue('Codigo da Sub-conta ?'	,'002')
		self.oHelper.SetValue('Configuracao CNAB ?'		,'Modelo 2')
		self.oHelper.SetValue('Consid.Filiais ?'		,'Sim')
		self.oHelper.SetValue('Da Filial ?'				,'D MG 01')
		self.oHelper.SetValue('Ate Filial ?'			,'D MG 01')
		self.oHelper.SetValue('Quebra por ?'			,'Não Quebra')
		self.oHelper.SetValue('Seleciona Filiais ?'		,'Nao')

		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Ok")

		self.oHelper.AssertTrue()

	def test_FINA150_CT007(self):
		#Setup dos parametros
		self.oHelper.AddParameter("MV_LOCENV" , "", "/NAOEXISTE/", "/NAOEXISTE/", "/NAOEXISTE/")
		self.oHelper.SetParameters()

		self.oHelper.SetValue('Do Bordero ?'         	,'A0001B')
		self.oHelper.SetValue('Ate o Bordero ?'     	,'A0001B')
		self.oHelper.SetValue('Arquivo de Config. ?'	,'TST.2RE')
		self.oHelper.SetValue('Arquivo de Saida ?'		,'FINA150_CT007')
		self.oHelper.SetValue('Codigo do Banco ?'		,'FIN')
		self.oHelper.SetValue('Codigo da Agencia ?'		,'150')
		self.oHelper.SetValue('Codigo da Conta ?'		,'FINA150')
		self.oHelper.SetValue('Codigo da Sub-conta ?'	,'002')
		self.oHelper.SetValue('Configuracao CNAB ?'		,'Modelo 2')
		self.oHelper.SetValue('Consid.Filiais ?'		,'Sim')
		self.oHelper.SetValue('Da Filial ?'				,'D MG 01')
		self.oHelper.SetValue('Ate Filial ?'			,'D MG 01')
		self.oHelper.SetValue('Quebra por ?'			,'Não Quebra')
		self.oHelper.SetValue('Seleciona Filiais ?'		,'Nao')

		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()