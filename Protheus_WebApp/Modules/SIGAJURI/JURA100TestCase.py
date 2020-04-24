from tir import Webapp
import unittest

class JURA100(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','20/02/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA162')
		inst.oHelper.AddParameter("MV_JMULLIM", "", ".T.", "", "")
		inst.oHelper.AddParameter("MV_JTVRSEN", "", "1", "", "")
		inst.oHelper.AddParameter("MV_JTRFWDR", "", "2", "", "")
		inst.oHelper.AddParameter("MV_JVINCAF", "", "1", "", "")
		inst.oHelper.AddParameter("MV_JFLXCOR", "", "1", "", "")
		inst.oHelper.AddParameter("MV_JHBPESF", "", "2", "", "")
		inst.oHelper.SetParameters()

	def test_JURA100_CT001(self):
		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.SetValue("NSZ_COD","0000000120")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickLabel("Alterar")
		self.oHelper.WaitHide("Carregando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.SetButton("Andamentos")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NT4_CATO","010")
		self.oHelper.SetValue("NT4_DESC","AUTOMAÇÃO TIR JURA100 - CT001 VALIDAÇÃO LIMINAR 2=Liminar")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		self.oHelper.ClickGridCell("Data Base",row=1)
		self.oHelper.SetValue("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.SetValue("O0S_DTINLI","25/11/2019",name_attr=True)
		self.oHelper.SetValue("O0S_DTFILI","25/12/2019",name_attr=True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Outras Ações","Liminares")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.CheckResult("O0S_DTINLI","25/11/2019",name_attr=True)
		self.oHelper.CheckResult("O0S_DTFILI","25/12/2019",name_attr=True)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
