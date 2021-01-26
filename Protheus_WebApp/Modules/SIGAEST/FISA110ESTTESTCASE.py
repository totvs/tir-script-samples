from tir import Webapp
import unittest
import time
#//-------------------------------------------------------------------
#@author Squad Entradas
#@since 31/08/2020
#@version 1.0
#/*/
#//-------------------------------------------------------------------
class FISA110(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIS","31/08/2020","T1","D MG 01")
		inst.oHelper.Program("FISA110")
		inst.oHelper.AddParameter("MV_CAT8309", "", ".T.", ".T.", ".T.")
		inst.oHelper.SetParameters()

	def test_FISA110_001(self):
		#Definições dos perguntes iniciais
		self.oHelper.SetValue('Data Inicial ?', '31/08/2020')
		self.oHelper.SetValue('Data Final ?', '31/08/2020')
		self.oHelper.SetValue('Seleciona Filiais ?', '2-Não')
		self.oHelper.SetValue('Grv Doc.Entrada ?', '2-Não')
		self.oHelper.SetValue('Grv Doc.Saídas ?', '2-Não')
		self.oHelper.SetValue('Grv Mov.Interno ?', '1-Sim')
		self.oHelper.SetValue('Sobrepõe ?', '1-Sim')
		self.oHelper.SetButton("OK")

		self.oHelper.WaitShow("Processo finalizado com Sucesso")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Finalizar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
