from tir import Webapp
import unittest

class JURA106(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','20/02/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA106')
		inst.oHelper.AddParameter("MV_JHBPESF", "", "1", "", "")
		inst.oHelper.AddParameter("MV_JTRFWDR", "", "2", "", "")
		inst.oHelper.AddParameter("MV_JBLQFER", "", "2", "", "")
		inst.oHelper.SetParameters()

	def test_JURA106_CT001(self):
		self.oHelper.SetValue("cValor","Contencioso - Fup",name_attr=True)
		self.oHelper.WaitFieldValue("NTA_CTIPO","")
		self.oHelper.ClickLabel("Incluir")
		self.oHelper.SetValue("NTA_CAJURI","0000000063")
		self.oHelper.SetValue("NTA_CTIPO","00005")
		self.oHelper.SetValue("NTA_DTFLWP","01/01/2025")
		self.oHelper.SetValue("NTA_CRESUL","001")
		self.oHelper.SetValue("NTA_DESC","Teste001")
		self.oHelper.ClickGridCell("Sigla part",row=1)
		self.oHelper.SetValue("NTE_SIGLA","JUR",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetValue("cTipoData","2 - Futura",name_attr=True)
		self.oHelper.SetValue("nQtdeDias","2",name_attr=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitFieldValue("NTA_CTIPO","00008")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetValue("cValor","Contencioso - Fup",name_attr=True)
		self.oHelper.WaitFieldValue("NTA_CTIPO","")
		self.oHelper.SetValue("NTA_CTIPO","00005")
		self.oHelper.SetValue("NSZ_CCLIEN","JLT001")
		self.oHelper.SetValue("NTA_DTFLWP","01/01/2025")
		self.oHelper.SetValue("NTE_SIGLA","JUR")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.ClickGridCell("Código",row=1)
		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NTA_CAJURI","0000000063")
		self.oHelper.CheckResult("NTA_CTIPO","00005")
		self.oHelper.CheckResult("NTA_DTFLWP","01/01/2025")
		self.oHelper.CheckResult("NTA_CRESUL","001")
		self.oHelper.CheckResult("NTA_DESC","Teste001")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetValue("cValor","Consultivo - Fup",name_attr=True)
		self.oHelper.SetValue("cValor","Contencioso - Fup",name_attr=True)
		self.oHelper.WaitFieldValue("NTA_CTIPO","")
		self.oHelper.SetValue("NTA_CTIPO","00008")
		self.oHelper.SetValue("NSZ_CCLIEN","JLT001")
		self.oHelper.SetValue("NTA_DTFLWP","03/01/2025")
		self.oHelper.SetValue("NTE_SIGLA","JUR")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.ClickGridCell("Código",row=1)
		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NTA_CAJURI","0000000063")
		self.oHelper.CheckResult("NTA_CTIPO","00008")
		self.oHelper.CheckResult("NTA_DTFLWP","03/01/2025")
		self.oHelper.CheckResult("NTA_CRESUL","001")
		self.oHelper.CheckResult("NTA_DESC","DESCRICAO MODELO DE FOLLOW-UP")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		
		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
