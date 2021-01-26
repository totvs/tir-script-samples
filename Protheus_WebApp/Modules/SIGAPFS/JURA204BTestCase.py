from tir import Webapp
import unittest

class JURA204B(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPFS','08/12/2020','T1','M SP 01 ','77')	
	#http://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T35057	
	def test_JURA204B_CT003(self):
		self.oHelper.Program('JURA204')	
		self.oHelper.SearchBrowse("SP100000000179")
		self.oHelper.SetButton("Outras Ações", "Vínculo de Time Sheets")
		#self.oHelper.WaitProcessing("Carregando dados, aguarde...") 
		self.oHelper.SearchBrowse("000000000559",key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetValue("NUE_COD","000000000559")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickBox("Código", "000000000558", select_all=False, grid_number=2)
		self.oHelper.CheckHelp(text_help="J204BSETMK", button="Fechar")
		self.oHelper.SetButton("Visualizar",position =2)
		self.oHelper.SetValue("NUE_COD","000000000558")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickBox("Código", "000000000559")
		self.oHelper.SetButton("Vincular")
		#self.oHelper.WaitProcessing("Aguarde...") 	
		self.oHelper.ClickBox("Código", "000000000559", select_all=False, grid_number=2)
		self.oHelper.CheckHelp(text_help="J204BSETMK", button="Fechar")
		self.oHelper.CheckResult('Código','000000000559', grid=True, line=2, grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
		self.oHelper.SetButton('x')
		self.oHelper.SetButton('x')
	#https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56243	
	def test_JURA204B_CT007(self):
		self.oHelper.Program('JURA204')	
		self.oHelper.SearchBrowse("SP100000000180")
		self.oHelper.SetButton("Outras Ações", "Vínculo de Time Sheets")
		#self.oHelper.WaitProcessing("Carregando dados, aguarde...") 
		self.oHelper.ClickBox("Código", "000000000561")
		self.oHelper.ClickBox("Código",	"000000000562")
		self.oHelper.SetButton("Sim")
		#self.oHelper.WaitHide("Aguarde...")
		self.oHelper.SetButton("Vincular")
		#self.oHelper.WaitProcessing("Aguarde...") 		
		self.oHelper.CheckResult('Cód Caso','000005', grid=True, line=1, grid_number=1)	
		self.oHelper.CheckResult('UT Revisada','2,00000004', grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('Código','000000000561', grid=True, line=2, grid_number=2)
		self.oHelper.CheckResult('Código','000000000562', grid=True, line=3, grid_number=2)	
		self.oHelper.CheckResult('UT Revisada','2,99999994', grid=True, line=3, grid_number=2)	
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
		self.oHelper.SetButton('x')
		self.oHelper.SetButton('x')

	#https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56244
	def test_JURA204B_CT008(self):
		self.oHelper.Program('JURA204')	
		self.oHelper.SearchBrowse("SP100000000178")
		self.oHelper.SetButton("Outras Ações", "Vínculo de Time Sheets")
		self.oHelper.CheckHelp(text_help="JURA204B", button="Fechar")
		self.oHelper.AssertTrue()
		self.oHelper.SetButton('x')

	#https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T56245
	def test_JURA204B_CT009(self):
		self.oHelper.Program('JURA204')	
		self.oHelper.SearchBrowse("SP100MP0000002")
		self.oHelper.SetButton("Outras Ações", "Vínculo de Time Sheets")
		self.oHelper.CheckHelp(text_help="JURA204B", button="Fechar")
		self.oHelper.AssertTrue()
		self.oHelper.SetButton('x')
		
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()