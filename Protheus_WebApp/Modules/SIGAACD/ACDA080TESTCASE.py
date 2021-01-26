#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDA080 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 23/09/2019
#@version P12
#
#
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
from datetime import date
import unittest
import time

class ACDA080(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		data_Sistema = date.today()
		data = data_Sistema.strftime('%d/%m/%Y')
		inst.oHelper.Setup('SIGAPCP',data,'T1','D MG 01')
		inst.oHelper.Program('ACDA080')	

	#CT001 - Inclusão de Monitoramento de Produção de Transação tipo Início	
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

	def test_ACDA080_CT001(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Tipo de Producao ?", "PCP MOD2")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Monitoramento da Producao - INCLUIR")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA1T")
		self.oHelper.SetButton("Ok")        

		self.oHelper.SetValue("Operacao", "01")
		self.oHelper.SetValue("Transacao", "01")
		self.oHelper.SetValue("Parc./Total", "T - Total")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		
		self.oHelper.AssertTrue()

	#CT002 - Inclusão de Monitoramento de Produção de Transação tipo Pausa sem apontamento	
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

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

	#CT003 - Inclusão de Monitoramento de Produção de Transação tipo Produção
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

	def test_ACDA080_CT003(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Tipo de Producao ?", "PCP MOD2")
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Monitoramento da Producao - INCLUIR")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA1V")
		self.oHelper.SetButton("Ok")        

		self.oHelper.SetValue("Operacao", "01")
		self.oHelper.SetValue("Transacao", "03")
		self.oHelper.SetValue("Parc./Total", "T - Total")
		self.oHelper.SetValue("Recurso", "EST001")
		self.oHelper.SetValue("Dt. Apont.", "26/09/2019")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()		

	#CT004 - Alteração de Monitoramento de Produção de Transação tipo Pausa sem apontamento	
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

	def test_ACDA080_CT004(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SearchBrowse("D MG 01 pcpA1W01001   02 ")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("Parc./Total", "P - Parcial")
		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()	

	#CT005 - Exclusão de Monitoramento de Produção - Início
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

	def test_ACDA080_CT005(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SearchBrowse("D MG 01 pcpA1X01001   01")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()	

	#CT006 - Exclusão de Monitoramento de Produção - Pausa sem apontamento
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

	def test_ACDA080_CT006(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SearchBrowse("D MG 01 pcpA1Y01001   02")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	#CT007 - Exclusão de Monitoramento de Produção - Produção
	#@author: Pedro Antonio Missaglia
	#@date: 25/09/2019	

	def test_ACDA080_CT007(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SearchBrowse("D MG 01 pcpA1Z01001   03")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()			

	def test_ACDA080_CT008(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SetButton("Outras Ações", "Relatorio")

		self.oHelper.SetButton("Param.")
		self.oHelper.SetValue("Da Data ?", "24/09/2019")
		self.oHelper.SetValue("Ate Data ?", "25/09/2019")
		self.oHelper.SetValue("Ate OP ?", "zzzzzzzzzzzzzz")
		self.oHelper.SetValue("Ate Transacao ?", "zz")
		self.oHelper.SetValue("Ate Operador ?", "zzzzzz")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sair")

		self.oHelper.AssertTrue()			

	def test_ACDA080_CT009(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SetButton("Outras Ações", "Legenda")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()	

	def test_ACDA080_CT010(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()		

	#CT011 - Inclusão de Monitoramento de Produção Parcialmente Apontada
	#@author: Jefferson silva de Sousa
	#@date: 01/10/2019	

	def test_ACDA080_CT011(self):

		self.oHelper.WaitShow("Monitoramento da Producao")
		time.sleep(3)
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Tipo de Producao ?", "PCP MOD2")
		self.oHelper.SetButton("Ok")
		time.sleep(1)

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Monitoramento da Producao - INCLUIR")
		self.oHelper.SetKey("F3")
		time.sleep(1)
		self.oHelper.SearchBrowse("PCPA20")
		self.oHelper.SetButton("Ok")        

		self.oHelper.SetValue("Operacao", "01")
		self.oHelper.SetValue("Transacao", "01")
		self.oHelper.SetValue("Parc./Total", "T - Total")		
		self.oHelper.SetValue("Dt. Apont.", "01/10/2019")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()	



		#CT012 -  Apontamento parcial com apontamentos parciais em operações anteriores
		#@author: Jefferson silva de Sousa
		#@date: 01/10/2019	
	def test_ACDA080_CT012(self):	


		self.oHelper.WaitShow("Monitoramento da Producao")		
		time.sleep(3)
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Tipo de Producao ?", "PCP MOD2")
		self.oHelper.SetButton("Ok")
		time.sleep(1)

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Monitoramento da Producao - INCLUIR")

		self.oHelper.SetValue("CBH_OP", "PCPA2101001")
		self.oHelper.SetValue("Operacao", "01")
		self.oHelper.SetValue("Transacao", "01")		
		self.oHelper.SetValue("CBH_PARTOT", "T - Total")	

		self.oHelper.SetButton("Salvar")
		time.sleep(3)	
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()			

	#CT013 -  Apontamento parcial com apontamentos parciais em operações anteriores
	#@author: Jefferson silva de Sousa
	#@date: 01/10/2019	
	def test_ACDA080_CT013(self):	


		self.oHelper.WaitShow("Monitoramento da Producao")		
		time.sleep(3)
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Tipo de Producao ?", "PCP MOD2")
		self.oHelper.SetButton("Ok")
		time.sleep(1)

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Monitoramento da Producao - INCLUIR")

		self.oHelper.SetValue("CBH_OP", "PCPA2101001")
		self.oHelper.SetValue("Operacao", "01")
		self.oHelper.SetValue("Transacao", "03")
		self.oHelper.SetValue("Recurso", "EST001")			
		self.oHelper.SetValue("Quantidade", "30,00")	

		self.oHelper.CheckResult("CBH_PARTOT", "P - Parci")

		self.oHelper.SetButton("Salvar")
		time.sleep(3)	
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()		
			

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()