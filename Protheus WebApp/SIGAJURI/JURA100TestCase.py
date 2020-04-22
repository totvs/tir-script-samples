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
		#tela de pesquisa
		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.SetValue("NSZ_COD","0000000120")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickLabel("Alterar")
		self.oHelper.WaitHide("Carregando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		#inclusão do andamento
		self.oHelper.SetButton("Andamentos")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NT4_CATO","010")
		self.oHelper.SetValue("NT4_DESC","AUTOMAÇÃO TIR JURA100 - CT001 VALIDAÇÃO LIMINAR 2=Liminar")
		self.oHelper.SetButton("Confirmar")
		#inclusão da liminar
		self.oHelper.SetButton("Sim")
		self.oHelper.ClickGridCell("Data Base",row=1)
		self.oHelper.SetValue("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.SetValue("O0S_DTINLI","25/11/2019",name_attr=True)
		self.oHelper.SetValue("O0S_DTFILI","25/12/2019",name_attr=True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		#verifica se a liminar foi incluida
		self.oHelper.SetButton("Outras Ações","Liminares")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.CheckResult("O0S_DTINLI","25/11/2019",name_attr=True)
		self.oHelper.CheckResult("O0S_DTFILI","25/12/2019",name_attr=True)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.AssertTrue()

	def test_JURA100_CT002(self):
		#inclusão do andamento
		self.oHelper.SetButton("Andamentos")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NT4_CATO","011")
		self.oHelper.SetValue("NT4_DESC","AUTOMAÇÃO TIR JURA100 - CT002 VALIDAÇÃO LIMINAR Campos da liminar não atualizados")
		self.oHelper.F3(field="NT4_CPERIT",name_attr=True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.F3(field="NT4_CFWLP",name_attr=True)
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		#não inclui liminar
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Ok")
		#inclui justificativa
		self.oHelper.SetValue("NUV_CMOTIV","0003")
		self.oHelper.SetValue("NUV_JUSTIF","AUTOMAÇÃO TIR JURA100 - CT002")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		#inclusão do andamento
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NT4_CATO","011")
		self.oHelper.SetValue("NT4_DESC","AUTOMAÇÃO TIR JURA100 - CT002 VALIDAÇÃO LIMINAR 1=Decisao")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		#inclusão da liminar 
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.SetValue("O0S_DTINLI","25/01/2020",name_attr=True)
		self.oHelper.SetValue("O0S_DTFILI","25/02/2020",name_attr=True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickGridCell("Código",row=2)
		#verifica se a liminar foi incluida
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("O0S_CTIPLI","00004",name_attr=True)
		self.oHelper.CheckResult("O0S_DTINLI","25/01/2020",name_attr=True)
		self.oHelper.CheckResult("O0S_DTFILI","25/02/2020",name_attr=True)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Fechar")
		#exclui os andamentos para recalcular a estimativa de término
		self.oHelper.ClickGridCell("Dt Andamento",row=2)
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sair da página")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()


	def test_JURA100_CT003(self):
		#inclusão de follow-up (gera andamento)
		self.oHelper.Program('JURA106')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NTA_CAJURI","0000000120")
		self.oHelper.SetValue("NTA_CTIPO","00012")
		self.oHelper.SetValue("NTA_DTFLWP","29/10/2019")
		self.oHelper.SetValue("NTA_CRESUL","002")
		self.oHelper.SetValue("NTA_CATO","009")
		self.oHelper.SetValue("NTA_CFASE","003")
		self.oHelper.ClickGridCell("Sigla part",row=1)
		self.oHelper.SetValue("NTE_SIGLA","CRS",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("NTA_DESC","AUTOMAÇÃO TIR JURA100 - CT003 VALIDAÇÃO EXCLUSAO DE ANDAMENTO VINCULADO A FUP.")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		#tela de pesquisa
		self.oHelper.Program('JURA162')
		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.SetValue("NSZ_COD","0000000120")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickLabel("Alterar")
		self.oHelper.WaitHide("Carregando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		#inclusão do andamento
		self.oHelper.SetButton("Andamentos")
		self.oHelper.SearchBrowse("", key=3, index=True)
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Excluír")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
