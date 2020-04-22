from tir import Webapp
import unittest

class TMSA491(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		
		inst.oHelper.Setup('SIGATMS','30/05/2019','T1','M SP 01 ','43')
		inst.oHelper.Program('TMSA491')
		
		inst.oHelper.AddParameter("MV_FATPREF", "", "TMS")
		inst.oHelper.AddParameter("MV_CLIGEN", "", "TMSCLIGE")
		inst.oHelper.AddParameter("MV_NATFAT", "", "001")
		inst.oHelper.AddParameter("MV_TIPFAT", "", "01")
		inst.oHelper.AddParameter("MV_TMSMFAT", "", "2")
		inst.oHelper.AddParameter("MV_CODCOMP", "", "10")
		inst.oHelper.AddParameter("MV_COMPENT", "", "09")
		inst.oHelper.AddParameter("MV_PROGEN", "", "TMS_PROGEN")
		inst.oHelper.SetParameters()

	#Cenário CT001 - Gerar Fatura com 1 documento
	def test_TMSA491_CT001(self):

		self.oHelper.SetButton('Gerar')
		self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton('Param.')
		
		#Inicia	o preenchimento dos parâmetros

		self.oHelper.SetValue("mv_par01", "01", name_attr=True)
		self.oHelper.SetValue("mv_par02", "15", name_attr=True)
		self.oHelper.SetValue("mv_par03", "TMS001", name_attr=True)
		self.oHelper.SetValue("mv_par04", "01", name_attr=True)
		self.oHelper.SetValue("mv_par05", "TMS001", name_attr=True)
		self.oHelper.SetValue("mv_par06", "01", name_attr=True)
		self.oHelper.SetValue("Tipo de Frete ?", "AMBOS")
		self.oHelper.SetValue("mv_par08", "", name_attr=True)
		self.oHelper.SetValue("mv_par09", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Cons. Titulos Anteriores ?", "Sim")
		self.oHelper.SetValue("Somente Titls Entregues ?", "Não")
		self.oHelper.SetValue("mv_par12", "", name_attr=True)
		self.oHelper.SetValue("mv_par13", "", name_attr=True)
		self.oHelper.SetValue("mv_par14", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Apenas Docs. Serv. Adic. ?", "Não")
		self.oHelper.SetValue("Cód.Negociação De ?", "")
		self.oHelper.SetValue("Cód.Negociação Até ?", "ZZ")
		self.oHelper.SetValue("Serviço De ?", "")
		self.oHelper.SetValue("Serviço Até ?", "ZZZ")		

		self.oHelper.SetButton('OK') #Confirmação da janela dos Parâmetros

		self.oHelper.SetButton('Ok') #Confirma execução da busca
		self.oHelper.SetButton('Outras Ações', 'Detalhar')
		self.oHelper.ClickLabel("Desmarca") 		
		self.oHelper.ClickBox("No.Docto.","000000112", select_all=True)	#Selecionar o documento
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Cancelar')			
		self.oHelper.AssertTrue()

	#Cenário CT002 - Gerar Fatura com varios documentos com Multi-Thread
	def test_TMSA491_CT002(self):

		self.oHelper.AddParameter("MV_TMSTHRC", "", "2")
		self.oHelper.AddParameter("MV_TMSTHRE", "", "2")
		self.oHelper.AddParameter("MV_TPNRNFS", "", "3")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Gerar')
		self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton('Param.')

		#Inicia	o preenchimento dos parâmetros

		self.oHelper.SetValue("mv_par01", "01", name_attr=True)
		self.oHelper.SetValue("mv_par02", "15", name_attr=True)
		self.oHelper.SetValue("mv_par03", "TMS002", name_attr=True)
		self.oHelper.SetValue("mv_par04", "01", name_attr=True)
		self.oHelper.SetValue("mv_par05", "TMS003", name_attr=True)
		self.oHelper.SetValue("mv_par06", "01", name_attr=True)
		self.oHelper.SetValue("Tipo de Frete ?", "AMBOS")
		self.oHelper.SetValue("mv_par08", "", name_attr=True)
		self.oHelper.SetValue("mv_par09", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Cons. Titulos Anteriores ?", "Sim")
		self.oHelper.SetValue("Somente Titls Entregues ?", "Não")
		self.oHelper.SetValue("mv_par12", "", name_attr=True)
		self.oHelper.SetValue("mv_par13", "", name_attr=True)
		self.oHelper.SetValue("mv_par14", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Apenas Docs. Serv. Adic. ?", "Não")
		self.oHelper.SetValue("Cód.Negociação De ?", "")
		self.oHelper.SetValue("Cód.Negociação Até ?", "ZZ")
		self.oHelper.SetValue("Serviço De ?", "")
		self.oHelper.SetValue("Serviço Até ?", "ZZZ")
		

		self.oHelper.SetButton('OK') #Confirmação da janela dos Parâmetros

		self.oHelper.SetButton('Ok') #Confirma execução da busca

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')		
		self.oHelper.SetButton('Cancelar')	
		self.oHelper.AssertTrue()
	
	#Cenário CT003 - Gerar Fatura com varios documentos
	def test_TMSA491_CT003(self):

		self.oHelper.SetButton('Gerar')
		self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton('Param.')
		
		#Inicia	o preenchimento dos parâmetros

		self.oHelper.SetValue("mv_par01", "01", name_attr=True)
		self.oHelper.SetValue("mv_par02", "15", name_attr=True)
		self.oHelper.SetValue("mv_par03", "TMS004", name_attr=True)
		self.oHelper.SetValue("mv_par04", "01", name_attr=True)
		self.oHelper.SetValue("mv_par05", "TMS006", name_attr=True)
		self.oHelper.SetValue("mv_par06", "01", name_attr=True)
		self.oHelper.SetValue("Tipo de Frete ?", "AMBOS")
		self.oHelper.SetValue("mv_par08", "", name_attr=True)
		self.oHelper.SetValue("mv_par09", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Cons. Titulos Anteriores ?", "Sim")
		self.oHelper.SetValue("Somente Titls Entregues ?", "Não")
		self.oHelper.SetValue("mv_par12", "", name_attr=True)
		self.oHelper.SetValue("mv_par13", "", name_attr=True)
		self.oHelper.SetValue("mv_par14", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Apenas Docs. Serv. Adic. ?", "Não")
		self.oHelper.SetValue("Cód.Negociação De ?", "")
		self.oHelper.SetValue("Cód.Negociação Até ?", "ZZ")
		self.oHelper.SetValue("Serviço De ?", "")
		self.oHelper.SetValue("Serviço Até ?", "ZZZ")		

		self.oHelper.SetButton('OK') #Confirmação da janela dos Parâmetros

		self.oHelper.SetButton('Ok') #Confirma execução da busca		
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')		
		self.oHelper.SetButton('Cancelar')	
		self.oHelper.AssertTrue()

	#Cenário CT004 - Gerar Fatura com varios documentos com ajustes
	def test_TMSA491_CT004(self):

		self.oHelper.SetButton('Gerar')
		self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton('Param.')
		
		#Inicia	o preenchimento dos parâmetros

		self.oHelper.SetValue("mv_par01", "01", name_attr=True)
		self.oHelper.SetValue("mv_par02", "15", name_attr=True)
		self.oHelper.SetValue("mv_par03", "TMS001", name_attr=True)
		self.oHelper.SetValue("mv_par04", "01", name_attr=True)
		self.oHelper.SetValue("mv_par05", "TMS001", name_attr=True)
		self.oHelper.SetValue("mv_par06", "01", name_attr=True)
		self.oHelper.SetValue("Tipo de Frete ?", "AMBOS")
		self.oHelper.SetValue("mv_par08", "", name_attr=True)
		self.oHelper.SetValue("mv_par09", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Cons. Titulos Anteriores ?", "Sim")
		self.oHelper.SetValue("Somente Titls Entregues ?", "Não")
		self.oHelper.SetValue("mv_par12", "", name_attr=True)
		self.oHelper.SetValue("mv_par13", "", name_attr=True)
		self.oHelper.SetValue("mv_par14", "ZZZZZZZZ", name_attr=True)
		self.oHelper.SetValue("Apenas Docs. Serv. Adic. ?", "Não")
		self.oHelper.SetValue("Cód.Negociação De ?", "")
		self.oHelper.SetValue("Cód.Negociação Até ?", "ZZ")
		self.oHelper.SetValue("Serviço De ?", "")
		self.oHelper.SetValue("Serviço Até ?", "ZZZ")		

		self.oHelper.SetButton('OK') #Confirmação da janela dos Parâmetros

		self.oHelper.SetButton('Ok') #Confirma execução da busca		

		self.oHelper.SetButton('Outras Ações', 'Detalhar')
		self.oHelper.ClickLabel("Desmarca") 		
		self.oHelper.ClickBox("No.Docto.","000000117", select_all=True)	#Selecionar o documento

		self.oHelper.SetButton('Outras Ações', 'Ajustes')
		self.oHelper.SetValue("Fil.Docto.", "M SP 01 ", grid=True, grid_number=1)
		self.oHelper.SetValue("No.Docto.", "000000117", grid=True, grid_number=1)
		self.oHelper.SetValue("Serie Docto.", "117", grid=True, grid_number=1)
		self.oHelper.SetValue("Valor a faturar", "20", grid=True, grid_number=1)

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')		
		self.oHelper.SetButton('Cancelar')	

		self.oHelper.AssertTrue()

	#Cenário CT005 - Cancelamento total com vários documentos
	def test_TMSA491_CT005(self):
		
		self.oHelper.SearchBrowse("M SP 01 TMS000018      A")
		self.oHelper.SetButton("Outras Ações","Cancelar")
		self.oHelper.ClickLabel("Marca") 
		self.oHelper.AssertTrue()

	#Cenário CT006 - Cancelamento total com vários documentos e Multi-Thread
	def test_TMSA491_CT006(self):
		
		self.oHelper.AddParameter("MV_TMSTHRC", "", "2")
		self.oHelper.AddParameter("MV_TMSTHRE", "", "2")
		self.oHelper.AddParameter("MV_TPNRNFS", "", "3")
		self.oHelper.SetParameters()

		self.oHelper.SearchBrowse("M SP 01 TMS000013      A")
		self.oHelper.SetButton("Outras Ações","Cancelar")
		self.oHelper.ClickLabel("Marca") 
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()