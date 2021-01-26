from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSCADLAYTestCase
TIR - Casos de testes da rotina LAYOUT GENERICO WEB

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSCADLAY(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSCADLAY")


	def test_PLSCADLAY_001(self):

		# INCLUIR
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("B90_CHAVE","DSAUPC")
		self.oHelper.SetValue("B90_TITULO","PLS DSAUPC TIR LAY")
		self.oHelper.SetValue("B90_FUNGRV","PLS DSAUPC TIR 1")
		self.oHelper.SetValue("B90_FUNLOA","PLS DSAUPC TIR 2")
		self.oHelper.SetValue("B90_IMGUP","PLS DSAUPC TIR 3")
		self.oHelper.SetValue("B90_ATIVO ","1 - Sim")
		self.oHelper.SetValue("B90_FUNPRE","PLS DSAUPC TIR 4")
		self.oHelper.SetValue("B90_FUNPOS","PLS DSAUPC TIR 5")
		self.oHelper.SetValue("B90_INCLJS","PLS DSAUPC TIR 6")
		self.oHelper.SetValue("B90_FNRELD","PLS DSAUPC TIR 7")

		# Grid Grupo de Campos
		self.oHelper.ClickGridCell("Ordem",row=1, grid_number=1)
		self.oHelper.SetValue("B7C_ORDEM","01",grid=True,grid_number=1,row=1)						# Ordem
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue("B7C_ALIAS","BB8",grid=True,grid_number=1,row=1)						# Tabela Ref.
		self.oHelper.LoadGrid()	
		self.oHelper.SetButton("Sim")																# Deseja carregar os campos da tabela [001] ?
		time.sleep(5)
		self.oHelper.SetValue("B7C_DESCRI","PLS DSAUPC TIR GRID",grid=True,grid_number=1,row=1)		# Descrição
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_TIPO", "C - Grupo de Campos",grid=True,grid_number=1,row=1)		# Tipo
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_GRUPAI","PLS",grid=True,grid_number=1,row=1)						# Grupo Pai
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_LINOK","PLS DSAUPC TIR",grid=True,grid_number=1,row=1)			# Fun Incluir
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_NOMGRI","PLS DSAUPC TIR",grid=True,grid_number=1,row=1)			# Nome Grid
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_VARGRU","PLS DSAUPC TIR",grid=True,grid_number=1,row=1)			# Var. Grupo
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_FUNSAV","PLS DSAUPC TIR",grid=True,grid_number=1,row=1)			# Fun. Salvar
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_CPOREL","PLS DSAUPC TIR",grid=True,grid_number=1,row=1)			# Campo relaci
		self.oHelper.LoadGrid()
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)									# checkbox Preenc Obr
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_INDICE","01",grid=True,grid_number=1,row=1)						# Indice
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_CHVIND","PLS DSAUPC TIR",grid=True,grid_number=1,row=1)			# chave
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B7C_QTDGRD","10",grid=True,grid_number=1,row=1)						# Qtd. Itens
		self.oHelper.LoadGrid()

		## Grid Campos
		#self.oHelper.ClickGridCell("Descricao",row=1, grid_number=2)
		#self.oHelper.SetValue("B91_DESCRI","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Descricao
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_CAMPO","PLS",grid=True,grid_number=2,row=1)						# Campo Tabela
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_CONDIC","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Condicao
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_NOMXMO","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Variavel Por
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_TAMANH","10",grid=True,grid_number=2,row=1)						# Tamanho
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_TIPO", "C - Texto",grid=True,grid_number=2,row=1)				# Tipo Campo
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_GRUPO","01",grid=True,grid_number=2,row=1)						# Grupo
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_VALID","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Validacao
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_INIPAD","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Inic. Padrao
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_F3","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)				# Cons. Padrao
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_CBOX","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Opcoes Combo
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_KEYPRE","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Keypress
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_KEYDOW","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Keydown
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_CHANGE","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# OnChange
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_ACTION","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Funcao Campo
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_GATILH","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Gatilho
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_CHVGAT","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_DADSRV","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Dado Padrão
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_VARREL","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Var Relacion
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_ORDEM","01",grid=True,grid_number=2,row=1)						# Ordem
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_TOOTIP","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Tooltip
		#self.oHelper.LoadGrid()
		#self.oHelper.SetValue("B91_POSICI","PLS DSAUPC TIR",grid=True,grid_number=2,row=1)			# Posicione
		#self.oHelper.LoadGrid()

		# Grid Configuração complementar
		self.oHelper.ClickGridCell("Variavel",row=1, grid_number=3)
		self.oHelper.SetValue("B2C_VAR","VALIDA",grid=True,grid_number=3,row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue("B2C_VALOR",".T.",grid=True,grid_number=3,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# ALTERAR
		#self.oHelper.SearchBrowse(f'{"M SP    DSAUPC"}', key=2, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B90_TITULO","PLS DSAUPC TIR LAY ALTERADO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# VISUALIZAR
		#self.oHelper.SearchBrowse(f'{"M SP    DSAUPC"}', key=2, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B90_TITULO","PLS DSAUPC TIR LAY ALTERADO")
		self.oHelper.SetButton("Fechar")

		# COPIAR
		#self.oHelper.SearchBrowse(f'{"M SP    DSAUPC"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Copiar')
		self.oHelper.SetValue("B90_CHAVE","DSAUPC2")
		self.oHelper.SetValue("B90_TITULO","PLS DSAUPC TIR LAY COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# IMPRIMIR BROWSE
		#self.oHelper.SearchBrowse(f'{"M SP    DSAUPC2"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Imprimir Browse')
		self.oHelper.SetButton("Imprimir")
		#self.oHelper.SetButton("Sim") # O arquivo \SPOOL\PLSCADLAY.rpt já existe. Deseja sobrescreve-lo?
		self.oHelper.SetButton("Sair")

		# EXCLUIR
		#self.oHelper.SearchBrowse(f'{"M SP    DSAUPC"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# EXCLUIR
		#self.oHelper.SearchBrowse(f'{"M SP    DSAUPC2"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()