from tir import Webapp
import unittest

class GTPA600A(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "10/04/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA600')

	def test_GTPA600A_CT001(self):
		self.oHelper.SearchBrowse("D MG    000298000289", "Filial+oportunidade + Proposta")
		self.oHelper.SetButton("Outras Ações","Alt Dt Viagem")
		self.oHelper.SetValue('G6R_DTIDA','16/04/2020')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
