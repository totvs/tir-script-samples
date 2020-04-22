from tir import Webapp
import unittest

class TMSA854(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		
		inst.oHelper.Setup('SIGATMS','19/06/2019','T1','M SP 01 ','43')
		inst.oHelper.Program('TMSA854')

		inst.oHelper.AddParameter("MV_CDRORI", "", "Q50308")
		inst.oHelper.AddParameter("MV_FATPREF", "", "TMS")
		inst.oHelper.AddParameter("MV_TESDR", "", "482")
		inst.oHelper.AddParameter("MV_TMSCFEC", "", ".T.")
		inst.oHelper.AddParameter("MV_CLIGEN", "", "TMSCLIGE")
		inst.oHelper.AddParameter("MV_NATFAT", "", "001")
		inst.oHelper.AddParameter("MV_TIPFAT", "", "01")
		inst.oHelper.AddParameter("MV_TMSMFAT", "", "2")
		inst.oHelper.AddParameter("MV_CODCOMP", "", "10")
		inst.oHelper.AddParameter("MV_COMPENT", "", "09")
		inst.oHelper.AddParameter("MV_PROGEN", "", "TMS_PROGEN")
		inst.oHelper.SetParameters()

	#Cenário CT001 - Gerar Fatura com 1 documento
	def test_TMSA854_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')				
		
		self.oHelper.SetValue("W01_CODBAR", "000000154", name_attr = True, check_value=False)
		self.oHelper.SetButton('Confirmar')	
		self.oHelper.SetButton('Salvar')	
		self.oHelper.AssertTrue()

	#Cenário CT002 - Geração de Fatura com Multithread
	def test_TMSA854_CT002(self):

		self.oHelper.AddParameter("MV_TMSTHRE", "", "2")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')				
		
		self.oHelper.SetValue("W01_CODBAR", "000000155", name_attr = True, check_value=False)
		self.oHelper.SetValue("W01_CODBAR", "000000156", name_attr = True, check_value=False)
		self.oHelper.SetValue("W01_CODBAR", "000000157", name_attr = True, check_value=False)
		self.oHelper.SetValue("W01_CODBAR", "000000158", name_attr = True, check_value=False)

		self.oHelper.SetButton('Confirmar')	
		self.oHelper.SetButton('Salvar')		
		self.oHelper.AssertTrue()

	#Cenário CT003 - Geração de fatura com 1 Doc eletrônico não-autorizado
	def test_TMSA854_CT003(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')				
		
		self.oHelper.SetValue("W01_CODBAR", "000000175", name_attr = True, check_value=False)
		self.oHelper.AssertFalse()

	#Cenário CT004 - Geração de Fatura de documento de Coleta
	def test_TMSA854_CT004(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')				

		self.oHelper.SetValue("W01_CODBAR", "20190315568093380001430000000040000000000000", name_attr = True, check_value=False)
		self.oHelper.SetButton('Fechar', check_error=True )	
		self.oHelper.SetButton('Fechar', check_error=True )	
		self.oHelper.AssertTrue()
	
	#Cenário CT005 - Geração de fatura de Doc. já faturado.
	def test_TMSA854_CT005(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')				

		self.oHelper.SetValue("W01_CODBAR", "000000160", name_attr = True, check_value=False)
		self.oHelper.SetButton('Fechar', check_error=True )	
		self.oHelper.SetButton('Fechar', check_error=True )	
		self.oHelper.AssertTrue()

	#Cenário CT007 - Exclusão de linha inserida
	def test_TMSA854_CT007(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 01')				

		self.oHelper.SetValue("W01_CODBAR", "000000161", name_attr = True, check_value=False)
		self.oHelper.SetValue("W01_CODBAR", "000000162", name_attr = True, check_value=False)
		self.oHelper.SetValue("W01_CODBAR", "000000162", name_attr = True, check_value=False)

		self.oHelper.SetButton('Confirmar')	
		self.oHelper.SetButton('Salvar')		
		self.oHelper.AssertTrue()

	#Cenário CT008 - Visualização de faturas geradas.
	def test_TMSA854_CT008(self):

		self.oHelper.SearchBrowse('M SP 01 TMS000018       ')
		
		self.oHelper.SetButton('Visualizar') #Visualizar
		self.oHelper.SetButton('Confirmar') #Confirmar		
		self.oHelper.AssertTrue()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()