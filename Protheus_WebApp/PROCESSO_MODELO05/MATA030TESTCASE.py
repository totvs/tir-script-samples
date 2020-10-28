from tir import Webapp
import unittest
from datetime import datetime

class MATA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.grupo = "T1"

		inst.oHelper = Webapp()  # INSTANCIAR A CLASSE
		inst.oHelper.Setup('SIGAFAT', '09/06/2020', inst.grupo, 'D MG 01 ', '05')
		inst.oHelper.SetLateralMenu("Atualizações > Cadastros > Clientes")

	def test_MATA030_CT001(self, oHelper=None):
		"""
		teste 1
		:return:
		"""

		if oHelper:
			self.oHelper = oHelper

		today = datetime.today()
		#
		cod = (f"{str(today.hour)[-1:]}{str(today.minute)}{str(today.second)}{str(today.microsecond)[-1:]}")

		self.oHelper.SetButton('Incluirr')

		self.oHelper.SetBranch('D MG 01 ')
		self.oHelper.SetValue('A1_COD', cod)
		self.oHelper.SetValue('A1_LOJA','01')

		self.oHelper.SetValue('A1_PESSOA','F - Fisica')
		self.oHelper.SetValue('A1_NOME','PESSOA FISICA')
		self.oHelper.SetValue('A1_NREDUZ','TIR')
		self.oHelper.SetValue('A1_END','Rua Salete, 154')
		self.oHelper.SetValue('A1_TIPO','F')
		self.oHelper.SetValue('A1_EST','SP')
		self.oHelper.SetValue('A1_COD_MUN','50308')
		self.oHelper.SetValue('A1_BAIRRO','Santana')
		self.oHelper.SetValue('A1_CEP','02403010')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse(f'D MG    {cod}')
		# self.oHelper.SearchBrowse(f'01   {cod}', 'Codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.CheckResult('A1_COD', cod)
		self.oHelper.CheckResult('A1_LOJA','01')
		self.oHelper.CheckResult('A1_PESSOA','F - Fisica')
		self.oHelper.CheckResult('A1_NOME','PESSOA FISICA')
		self.oHelper.CheckResult('A1_NREDUZ','TIR')
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