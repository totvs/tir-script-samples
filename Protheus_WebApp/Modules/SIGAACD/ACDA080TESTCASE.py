from tir import Webapp
from datetime import date
import unittest

class ACDA080(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		data_Sistema = date.today()
		data = data_Sistema.strftime('%d/%m/%Y')
		inst.oHelper.Setup('SIGAPCP',data,'T1','D MG 01')
		inst.oHelper.Program('ACDA080')	

	def test_ACDA080_CT002(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Tipo de Producao ?", "PCP MOD2")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitShow("Monitoramento da Producao - INCLUIR")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA1U")
		self.oHelper.SetButton("Ok")        
		self.oHelper.SetValue("Operacao", "01")
		self.oHelper.SetValue("Transacao", "02")
		self.oHelper.SetValue("Parc./Total", "T - Total")
		self.oHelper.SetValue("Recurso", "EST001")
		self.oHelper.SetValue("Dt. Apont.", "26/09/2019")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()