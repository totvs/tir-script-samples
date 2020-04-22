#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA185 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 11/07/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA185(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA185')		

	def test_MATA185_CT001(self):

		#self.oHelper.AddParameter("MV_ESTNEG", "", "S", "S", "S")
		#self.oHelper.AddParameter("MV_BXPRERQ", "", "T", "T", "T")
		#self.oHelper.SetParameters()

		self.oHelper.SearchBrowse("D MG 01 PMS032 01")

		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Toda a Pre-Req")
		self.oHelper.SetButton('Ok')	

		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')
		self.oHelper.ClickCheckBox("Selecionar Todos os Itens",1)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('TM','501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT002(self):	

		self.oHelper.SearchBrowse("D MG 01 PMS032 01")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT003(self):	

		self.oHelper.SearchBrowse("D MG 01 PMS033 01")
		self.oHelper.SetButton('Outras Ações', 'EStorno')
		self.oHelper.SetButton('Confirmar')	
		self.oHelper.AssertTrue()

	def test_MATA185_CT004(self):	

		self.oHelper.SearchBrowse("D MG 01 PMS034 01")
		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Item da Pre-Req")
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')	
		self.oHelper.SetValue('Quantidade a requisitar', '30,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('TP Movimento', '501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT005(self):		

		self.oHelper.AddParameter("MV_ESTNEG", "", "F", "F", "F")
		self.oHelper.AddParameter("MV_BXPRERQ", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SearchBrowse("D MG 01 PMS035 01")
		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Item da Pre-Req")
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Baixar')	
		self.oHelper.SetButton('Confirma')
		self.oHelper.SetValue('Quantidade a requisitar', '30,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('TP Movimento', '501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT006(self):

		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')	
		self.oHelper.AssertTrue()
	#CT007 Verifica se help é apresentado em tela referente a requisiçao ja baixada
	def test_MATA185_CT007(self):
						
		self.oHelper.SearchBrowse("D MG 01 ESTSE0000000000000000000000581PMS04101","Filial+produto + Nr.s.a. + Item S.a.")
		
		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')
		self.oHelper.WaitShow("A185BX")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()