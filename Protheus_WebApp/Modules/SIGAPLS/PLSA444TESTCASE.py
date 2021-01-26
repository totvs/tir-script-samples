from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA444TestCase
TIR - Casos de testes da rotina Cadastros de Terminologias TISS

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA444(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		#inst.oHelper.Program("PLSA444")
		#inst.oHelper.SetLateralMenu('Miscelanea > Tiss > Cad. Terminologias Tiss')


	# -------------------------------------------------------------------
		# /*/{Protheus.doc} test_PLSA444_001
		# Sugestão De-Para

		#@author Silvia SantAnna
		#@since 10/2020
		#@version 12
	# -------------------------------------------------------------------
	def test_PLSA444_001(self):
		self.oHelper.SetLateralMenu('Miscelanea > Tiss > Cad. Terminologias Tiss')
		time.sleep(3)

		# -- Outras Ações > Sugestão De-Para
		self.oHelper.SearchBrowse("M SP 01 87")
		self.oHelper.SetButton("Outras Ações",sub_item='Sugestão De-Para')
		# Grids
		self.oHelper.ClickGridCell("Cod Tabela",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		# Grids
		self.oHelper.ClickGridCell("Código",row=1, grid_number=2)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		self.oHelper.SetButton("Gravar")
		self.oHelper.SetButton("Sim")		# Realizar o vínculo entre os dois itens abaixo?
		time.sleep(3)
		self.oHelper.SetButton("Fechar")	# Vinculação realizada com sucesso
		time.sleep(3)
		self.oHelper.ClickCheckBox("Exibir termos já vinculados",1)
		time.sleep(3)
		self.oHelper.ClickCheckBox("Mostrar Todos",1)
		time.sleep(3)
		self.oHelper.SetButton("Sair")
		# -- Fim Sugestões De-Para

		self.oHelper.SetButton('x')

		self.oHelper.AssertTrue()

	# -------------------------------------------------------------------
		# /*/{Protheus.doc} test_PLSA444_002
		# Sugestão De-Para > De/Para Automático

		#@author Silvia SantAnna
		#@since 10/2020
		#@version 12
	# -------------------------------------------------------------------
	def test_PLSA444_002(self):
		self.oHelper.SetLateralMenu('Miscelanea > Tiss > Cad. Terminologias Tiss')
		time.sleep(3)

		# -- Outras Ações > Sugestão De-Para > De/Para Automático
		self.oHelper.SearchBrowse("M SP 01 22")
		self.oHelper.SetButton("Outras Ações",sub_item='Sugestão De-Para')
		self.oHelper.SetButton("De/Para Automático")
		time.sleep(3)
		self.oHelper.SetButton("Sim")
		time.sleep(3)
		self.oHelper.SetButton("Fechar")
		time.sleep(3)
		self.oHelper.SetButton("Sair")
		# -- Fim De/Para Automático

		self.oHelper.SetButton('x')

		self.oHelper.AssertTrue()


	# -------------------------------------------------------------------
		# /*/{Protheus.doc} test_PLSA444_003
		# Inclusao, Alteracao e Exclusao de uma Terminologia TISS

		#@author Silvia SantAnna
		#@since 10/2020
		#@version 12
	# -------------------------------------------------------------------
	def test_PLSA444_003(self):
		self.oHelper.SetLateralMenu('Miscelanea > Tiss > Cad. Terminologias Tiss')
		time.sleep(3)

		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("BTP_CODTAB","70")
		self.oHelper.SetValue("BTP_DESCRI","PLS DSAUPC TIR TISS")
		self.oHelper.SetValue("BTP_VIGDE","01/01/2020",check_value = False)
		self.oHelper.SetValue("BTP_VIGATE","31/12/2020",check_value = False)
		self.oHelper.SetValue("BTP_DATFIM","31/12/2020",check_value = False)
		self.oHelper.SetValue("BTP_TAMCOD","5")
		self.oHelper.SetValue("BTP_ALIAS","BA1")
		self.oHelper.SetValue("BTP_CHVTAB","BA1_CODINT+BA1_CODEMP+BA1_MATRIC+BA1_TIPREG+BA1_DIGITO")
		self.oHelper.SetValue("BTP_BUSDIR", "1 - Sim")
		## Grids
		#self.oHelper.ClickGridCell("Alias Vinc.",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		#self.oHelper.SetValue("BVL_ALIAS","BA1")
		## Grids
		#self.oHelper.ClickGridCell("Chave Tabela",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		#self.oHelper.SetValue("BVL_CHVTAB","BA1_CODINT+BA1_CODEMP+BA1_MATRIC+BA1_TIPREG+BA1_DIGITO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Alterar
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BTP_DESCRI","PLS DSAUPC TIR TISS ALTERADO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Visualizar
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BTP_DESCRI","PLS DSAUPC TIR TISS ALTERADO")
		self.oHelper.SetButton("Fechar")

		# -- Outras Ações > Atualizar Terminologias
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Outras Ações",sub_item='Atualizar Terminologias')
		# Tempo para importar as terminologias de getNewPar("MV_PLURTIS", "https://arte.engpro.totvs.com.br,/public/sigapls/TISS/") -- function PLSA444REC()
		self.oHelper.WaitProcessing("Aguarde, os arquivos estão sendo baixados")	#time.sleep(120)
		#self.oHelper.SetButton("Sim")	# Deseja importar todas as terminologias?
		self.oHelper.SetButton("Não")	# Deseja importar todas as terminologias?

		# Grid - Selecione o(s) arquivos(s) a serem importados
		self.oHelper.ClickGridCell("Terminologia",row=1, grid_number=1)
		self.oHelper.ScrollGrid('Terminologia', match_value='DEMAIS TERMINOLOGIAS', grid_number=1)
		self.oHelper.SetKey("ENTER", grid=True, grid_number=1)
		self.oHelper.LoadGrid()	
		self.oHelper.SetButton("Confirmar")
		self.oHelper.WaitProcessing("Processando")	#time.sleep(200)
		self.oHelper.SetButton("Ok")	# Processamento finalizado
		# -- Fim Atualizar Terminologias

		# -- Outras Ações > Itens da terminologia
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Outras Ações",sub_item='Itens da Terminologia')
		# Visualizar
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BTQ_CODTAB","70")
		self.oHelper.CheckResult("BTQ_CDTERM","PAPEL")
		self.oHelper.SetButton("Fechar")
		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("BTQ_CDTERM","TESTE TIR")
		self.oHelper.SetValue("BTQ_DESTER","TESTE TIR")
		self.oHelper.SetValue("BTQ_VIGDE","01/01/2020",check_value = False)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Alterar
		self.oHelper.SearchBrowse("70TESTE TIR")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BTQ_DESTER","TESTE TIR ALT")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Excluir
		self.oHelper.SearchBrowse("70TESTE TIR")
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton('x')
		# -- Fim Itens da Terminologia

		# -- Outras Ações > Protheus x TISS
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Outras Ações",sub_item='Protheus x TISS')
		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("BTU_VLRSIS","TESTE TIR 1234")
		self.oHelper.SetValue("BTU_VLRBUS","TESTE TIR 1234")
		self.oHelper.SetValue("BTU_CDTERM","PAPEL")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Alterar
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BTU_VLRBUS","TESTE TIR 12345")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Visualizar
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BTU_VLRBUS","TESTE TIR 12345")
		self.oHelper.SetButton("Fechar")
		# Excluir
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Close")
		# -- Fim Protheus x TISS

		# -- Outras Ações > Campos Adic.
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Outras Ações",sub_item='Campos Adic.')
		# Grids
		self.oHelper.ClickGridCell("Campo Adicio",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BTD_CAMPO","BTQ_SIGLA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# -- Fim Campos Adic.

		# -- Outras Ações > Excluir
		self.oHelper.SearchBrowse("M SP 01 70")
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# -- Fim Excluir

		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()