from tir import Webapp
import unittest

class JURA106_2(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','20/02/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA106')
		inst.oHelper.AddParameter("MV_JHBPESF", "", "2", "", "")
		inst.oHelper.AddParameter("MV_JTRFWDR", "", "2", "", "")
		inst.oHelper.AddParameter("MV_JFLXCOR", "", "2", "", "")
		inst.oHelper.SetParameters()

	def test_JURA106_2_CT001(self):
		assjur = "0000000133"

		print('CT001 - Inclusão de follow-ups que geram outro follow-up de forma manual e automática')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NTA_CAJURI",assjur)
		self.oHelper.SetValue("NTA_CTIPO","00013")
		self.oHelper.SetValue("NTA_DTFLWP","05/12/2019")
		self.oHelper.F3(field="NTA_CADVCR",name_attr=True)
		self.oHelper.ScrollGrid(column="Contato",match_value="JUR001")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetValue("NTA_CATO","009")
		self.oHelper.ClickGridCell("Sigla part",row=1)
		self.oHelper.SetValue("NTE_SIGLA","JUR",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		# Inclusão de andamento
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetValue("nQtdeDias","1",name_attr=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SearchBrowse(assjur, key=2, index=True)
		self.oHelper.ClickGridCell("Desc Tipo",row=2)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetValue("NTA_CAJURI",assjur)
		self.oHelper.CheckResult("NTA_CTIPO","00014")
		self.oHelper.CheckResult("NTA_DTFLWP","04/12/2019")
		self.oHelper.CheckResult("NTA_DESC","TIR JURA106_2 - MODELO FOLLOW-UP - Inclusão de follow-ups que geram outro follow-up de forma manual e automatica.")
		self.oHelper.SetButton("Fechar")
		# Follow-up gerado automaticamente
		self.oHelper.SearchBrowse(assjur, key=2, index=True)	
		self.oHelper.ClickGridCell("Desc Tipo",row=3)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetValue("NTA_CAJURI",assjur)
		self.oHelper.CheckResult("NTA_CTIPO","00014")
		self.oHelper.CheckResult("NTA_DTFLWP","06/12/2019")
		self.oHelper.CheckResult("NTA_DESC","TIR JURA106_2 - MODELO AUTOMATICO FOLLOW-UP - Inclusão de follow-ups que geram outro follow-up de forma manual e automatica.")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	def test_JURA106_2_CT002(self):
		assjur = "0000000133"

		print('CT002 - Exclusão de um follow-up que possui follow-ups filhos e andamentos gerados.')
		self.oHelper.SearchBrowse(assjur, key=2, index=True)
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.ClickGridCell("Código",row=4)
		self.oHelper.SetButton("Excluír")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.Program('JURA162')
		self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
		self.oHelper.SetValue('NSZ_COD', assjur)
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.ClickGridCell('Situacao', 1)
		self.oHelper.ClickLabel('Alterar')
		self.oHelper.SetButton("Follow-ups")
		self.oHelper.SearchBrowse(assjur, key=2, index=True)
		self.oHelper.CheckHelp(text_problem="Problema: Não foi possivel encontrar registro com esta chave de pesquisa.", button="Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel('Sair')
		self.oHelper.AssertTrue()

	def test_JURA106_2_CT003(self):
		assjur = "0000000133"
		
		print('CT003 - Geração de follow-up automático a partir da alteração de correspondente.') 
		self.oHelper.Program('JURA162')
		self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
		self.oHelper.SetValue('NSZ_COD', assjur)
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.SetValue("NSZ_CAREAJ","JUR01")
		self.oHelper.ClickLabel('Alterar')
		self.oHelper.ClickGridCell('Cód Corresp',row=1, grid_number=2)
		self.oHelper.SetValue("NUQ_CCORRE","JTIR01",grid=True,grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("NUQ_LCORRE","01",grid=True,grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Follow-ups")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("NTA_DESC","TIR JURA106_2 - MODELO AUTOMATICO FOLLOW-UP - Inclusão de follow-ups que geram outro follow-up de forma manual e automatica.")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
