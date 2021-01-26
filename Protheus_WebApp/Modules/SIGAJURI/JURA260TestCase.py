from tir import Webapp
import unittest

class JURA260(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','20/10/2020','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA162')
		inst.oHelper.AddParameter("MV_JMULLIM", "", ".T.", "", "")
		inst.oHelper.SetParameters()

	def test_JURA260_CT001(self):
		#tela de pesquisa
		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.SetValue("NSZ_COD","0000000162")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickLabel("Alterar")
		self.oHelper.WaitHide("Carregando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		#Tela de liminar
		#Preenche o form Master
		self.oHelper.SetButton("Outras Ações","Liminares")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("O0S_CTIPLI","00004")
		self.oHelper.SetValue("O0S_DTINLI","23/10/2020")
		self.oHelper.SetValue("O0S_DTFILI","26/10/2020")
		self.oHelper.SetValue("O0S_SITINT","3")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.CheckHelp(text_problem="Problema:  O campo Data Cumprim deve ser preenchido, quando a Situação da Liminar for Cumprida", button="Fechar")
		self.oHelper.SetValue("O0S_DTCUMP","26/10/2020")
		self.oHelper.SetValue("O0S_DTRECE","30/10/2020")
		self.oHelper.SetValue("O0S_DTPRAZ","01/10/2020")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.CheckHelp(text_problem="Problema:  A Data Recebim não pode ser maior que a Data Prazo", button="Fechar")
		self.oHelper.SetValue("O0S_DTRECE","26/10/2020")
		self.oHelper.SetValue("O0S_DTPRAZ","30/10/2020")

		#Preenche o grid
		self.oHelper.ClickGridCell("Cód Multa",row=1)
		self.oHelper.SetValue("O0T_DTBASE","03/11/2020",grid=True)
		self.oHelper.SetValue("O0T_DTTERM","30/11/2020",grid=True)
		self.oHelper.SetValue("O0T_TETMUL","1,00",grid=True)
		self.oHelper.SetValue("O0T_MULDIA","1,00",grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")

		#verifica se a liminar foi incluida
		self.oHelper.SetButton("Outras Ações","Liminares")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.CheckResult("O0S_DTINLI","23/10/2020",name_attr=True)
		self.oHelper.CheckResult("O0S_DTFILI","26/10/2020",name_attr=True)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
