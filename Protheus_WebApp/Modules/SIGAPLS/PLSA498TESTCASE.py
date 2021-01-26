from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA940TestCase
TIR - Casos de testes da rotina Digitacao de Contas

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""

class PLSA498(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","13/10/2020","T1","M SP 01","33")	#DateSystem
#		inst.oHelper.Program("PLSA498")
#		inst.oHelper.AddParameter("MV_PLCALPG","" , "2")
#		inst.oHelper.SetParameters()


	# -------------------------------------------------------------------
		# /*/{Protheus.doc} test_PLSA498_001
		# Inclusão de uma PEG e Guia

		#@author Silvia SantAnna
		#@since 10/2020
		#@version 12
	# -------------------------------------------------------------------
	def test_PLSA498_001(self):

		self.oHelper.Program("PLSA498")
		self.oHelper.AddParameter("MV_PLCALPG","" , "2")
		self.oHelper.SetParameters()

		self.oHelper.WaitShow("Tipos de Guia") 

		# -- Filtro inicial
		self.oHelper.SetValue("Mes de:" ,"10")		#DateSystem[3:5]
		self.oHelper.SetValue("Mes ate:","10")		#DateSystem[3:5]
		self.oHelper.SetValue("Ano de:" ,"2020")	#DateSystem[6:10]
		self.oHelper.SetValue("Ano ate:","2020")	#DateSystem[6:10]
		self.oHelper.SetValue("RDA de:" ,"000007")
		self.oHelper.SetValue("RDA ate:","000007")
		self.oHelper.SetButton("Confirmar")
		# -- Fim Filtro inicial

		# -- Inclusão de PEG
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("BCI_CODRDA","000007")
		self.oHelper.SetValue("BCI_TIPGUI","02")
		self.oHelper.SetValue("BCI_QTDEVE","1",check_value = False)
		self.oHelper.SetValue("BCI_VLRGUI","1",check_value = False)
		self.oHelper.SetValue("BCI_DATREC","13/10/2020",check_value = False)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Fechar")
		# -- Fim Inclusão de PEG

		self.oHelper.SetButton("Cancelar")



		# -- Inclusão da Guia
		self.oHelper.SetButton("Outras Ações",sub_item='Selecionar')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("BD5_TIPPAC","1")
		self.oHelper.SetValue("BD5_NUMIMP","DSAUPC12345678900001")
		self.oHelper.SetValue("BD5_DATPRO","13/10/2020",check_value = False)
		self.oHelper.SetValue("BD5_USUARI","00010100000002012")
		self.oHelper.SetValue("BD5_LOCATE","001001",check_value = False)
		self.oHelper.SetValue("BD5_CODESP","010")
		self.oHelper.SetValue("BD5_CID","J159")
		self.oHelper.SetValue("BD5_OPESOL","0001",check_value = False)
		self.oHelper.SetValue("BD5_REGSOL","19011985")
		self.oHelper.SetValue("BD5_REGEXE","19011985")
		self.oHelper.SetValue("BD5_NRAOPE","DSAUPC123001")
		self.oHelper.SetValue("BD5_TIPATE", "05 - Exame Amb")
		# Aba Eventos Processamentos Contas
		self.oHelper.ClickFolder("Eventos Processamentos Contas  ")
		# Grid
		self.oHelper.ClickGridCell("Cd.Proc.",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BD6_CODPAD","01")
		self.oHelper.SetValue("BD6_CODPRO","40304361")
		self.oHelper.SetValue("BD6_QTDPRO","1",check_value = False)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")
		# Fim Inclusão de Guia

		self.oHelper.SetButton("Cancelar")

		# -- Mudança de Fase > Ativa e Em Conferencia
		self.oHelper.SetButton("Outras Ações",sub_item='Mudança Fase')
		self.oHelper.SetButton("Sim")
		# -- Fim Mudança de Fase

		# Visualizar > pasta Financeiro
		self.oHelper.SetButton("Visualizar")
		self.oHelper.ClickFolder("Financeiro")
		self.oHelper.CheckResult("BD5_VLRPAG","1,01")
		self.oHelper.CheckResult("BD5_VLRGLO","0,00")
		# Visualizar > pasta Outros
		self.oHelper.ClickFolder("Outros",position=1)
		self.oHelper.CheckResult("BD5_FASE  ","2 - Conferencia") 	# 1=Digitacao;2=Conferencia;3=Pronta;4=Faturada;5=Processando
		self.oHelper.CheckResult("BD5_SITUAC","1 - Ativa") 			# 1=Ativa;2=Cancelada;3=Bloqueada
		self.oHelper.SetButton("Confirmar")

		# -- Analisar Glosas > Reconsiderar
		self.oHelper.SetButton("Outras Ações",sub_item='Analisar Glosas')
		# Grid
		self.oHelper.ClickGridCell("Cod Proced.",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BDX_CODOPE","0001")
		self.oHelper.SetValue("BDX_ACAO", "2 - Reconsiderar")
		self.oHelper.SetValue("BDX_RESPAL","PLS DSAUPC JUSTIFICATIVA GLOSA")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Confirmar")
		# -- Fim Analisar Glosas

		# Visualizar > pasta Financeiro
		self.oHelper.SetButton("Visualizar")
		self.oHelper.ClickFolder("Financeiro")
		self.oHelper.CheckResult("BD5_VLRPAG","1,01")
		self.oHelper.CheckResult("BD5_VLRGLO","0,00")
		# Visualizar > pasta Outros
		self.oHelper.ClickFolder("Outros",position=1)
		self.oHelper.CheckResult("BD5_FASE  ","3 - Pronta")	# 1=Digitacao;2=Conferencia;3=Pronta;4=Faturada;5=Processando
		self.oHelper.CheckResult("BD5_SITUAC","1 - Ativa") 	# 1=Ativa;2=Cancelada;3=Bloqueada
		self.oHelper.SetButton("Confirmar")

		# -- Incluir glosa manual
		self.oHelper.SetButton("Outras Ações",sub_item='Incluir glosa manual')
		# Grid
		self.oHelper.ClickGridCell("Cd.Proc.",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue(field = "cCodGlo", value = "004", name_attr = True)
		self.oHelper.SetButton("Adicionar a Glosa")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Confirmar")
		# -- Fim Incluir glosa manual

		# -- Hist. de Glosa
		self.oHelper.SetButton("Outras Ações",sub_item='Hist. de Glosa')
		self.oHelper.CheckResult("Cod Glosa", user_value = "004", grid=True, line=4)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Fechar")
		# -- Fim Hist. de Glosa

		# Visualizar > pasta Financeiro
		self.oHelper.SetButton("Visualizar")
		self.oHelper.ClickFolder("Financeiro")
		self.oHelper.CheckResult("BD5_VLRPAG","0,00")
		self.oHelper.CheckResult("BD5_VLRGLO","1,01")
		# Visualizar > pasta Outros
		self.oHelper.ClickFolder("Outros",position=1)
		self.oHelper.CheckResult("BD5_FASE  ","3 - Pronta") # 1=Digitacao;2=Conferencia;3=Pronta;4=Faturada;5=Processando
		self.oHelper.CheckResult("BD5_SITUAC","1 - Ativa") 	# 1=Ativa;2=Cancelada;3=Bloqueada
		self.oHelper.SetButton("Confirmar")

		# -- Exibe Erro Cont
		self.oHelper.SetButton("Outras Ações",sub_item='Exibe Erro Cont')
		self.oHelper.SetButton("Fechar")
		# -- Fim Exibe Erro Cont

		# -- Revalorizar Cobrança
		self.oHelper.SetButton("Outras Ações",'Outras Opções,Revalorizar Cobrança')
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		# -- Fim Revalorizar Cobrança

		#self.oHelper.SetButton("Outras Ações",'Outras Opções,Revalorizar Pagamento')
		#self.oHelper.SetButton("Sim")
		#self.oHelper.SetButton("x")

		# Retorno Fase
		self.oHelper.SetButton("Outras Ações",sub_item='Retorno Fase')
		self.oHelper.SetButton("Sim")
		# Mudança Fase
		self.oHelper.SetButton("Outras Ações",sub_item='Mudança Fase')
		self.oHelper.SetButton("Sim")

		# -- Ret./Glos. Guia Inteira
		self.oHelper.SetButton("Outras Ações",sub_item='Ret./Glos. Guia Inteira')
		self.oHelper.SetValue(field = "cCodGlo", value = "529", name_attr = True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# -- Fim Ret./Glos. Guia Inteira

		# Visualizar > pasta Financeiro
		self.oHelper.SetButton("Visualizar")
		self.oHelper.ClickFolder("Financeiro")
		self.oHelper.CheckResult("BD5_VLRPAG","0,00")
		self.oHelper.CheckResult("BD5_VLRGLO","1,01")
		# Visualizar > pasta Outros
		self.oHelper.ClickFolder("Outros",position=1)
		self.oHelper.CheckResult("BD5_FASE  ","4 - Faturada")	# 1=Digitacao;2=Conferencia;3=Pronta;4=Faturada;5=Processando
		self.oHelper.CheckResult("BD5_SITUAC","1 - Ativa")		# 1=Ativa;2=Cancelada;3=Bloqueada
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')
		# -- Fim Inclusão Guia



		# -- De volta para a PEG
		# Status do PEG
		self.oHelper.SetButton("Outras Ações",sub_item='Status do Peg')
		self.oHelper.SetButton("Fechar")
		# Ret./Glos. PEG Integralmente
		self.oHelper.SetButton("Outras Ações",sub_item='Ret./Glos. PEG Integralmente')
		self.oHelper.SetButton("Sim")
		# Mudança Fase
		self.oHelper.SetButton("Outras Ações",sub_item='Mudanca Fase')
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		# et./Glos. PEG Integralmente
		self.oHelper.SetButton("Outras Ações",sub_item='Ret./Glos. PEG Integralmente')
		self.oHelper.SetValue(field = "cCodGlo", value = "007", name_attr = True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		# Rev.Cobr./Pagto
		self.oHelper.SetButton("Outras Ações",sub_item='Rev.Cobr./Pagto')
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		# Revalor. Cobr.
		self.oHelper.SetButton("Outras Ações",sub_item='Revalor. Cobr.')
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		# -- Fim da PEG

		self.oHelper.SetButton('x')

		self.oHelper.AssertTrue()


	# -------------------------------------------------------------------
		# /*/{Protheus.doc} test_PLSA498_002
		# Outras Ações > Pesquisar

		#@author Silvia SantAnna
		#@since 10/2020
		#@version 12
	# -------------------------------------------------------------------
	def test_PLSA498_002(self):

		self.oHelper.Program("PLSA498")
		self.oHelper.AddParameter("MV_PLCALPG","" , "2")
		self.oHelper.SetParameters()

		self.oHelper.WaitShow("Tipos de Guia") 

		# -- Filtro inicial
		self.oHelper.SetValue("Mes de:" ,"11")		#DateSystem[3:5]
		self.oHelper.SetValue("Mes ate:","11")		#DateSystem[3:5]
		self.oHelper.SetValue("Ano de:" ,"2020")	#DateSystem[6:10]
		self.oHelper.SetValue("Ano ate:","2020")	#DateSystem[6:10]
		self.oHelper.SetValue("RDA de:" ,"000007")
		self.oHelper.SetValue("RDA ate:","000007")
		self.oHelper.SetValue(field = "cProtDe", value = "00000442", name_attr = True)
		self.oHelper.SetValue(field = "cProtAte", value = "00000442", name_attr = True)
		self.oHelper.SetButton("Confirmar")
		# -- Fim Filtro inicial

		# Pasta Numero do PEG <F5>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F5")		# self.oHelper.ClickFolder('Numero do PEG')
		self.oHelper.SetValue(field = "cPEG", value = "00000442", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BCI_CODPEG","00000442")
		self.oHelper.CheckResult("BCI_CODRDA","000007")
		self.oHelper.SetButton('Cancelar')

		# Pasta Codigo da Rede de Atendimento <F6>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F6")		# self.oHelper.ClickFolder('Codigo da Rede de Atendimento')
		self.oHelper.SetValue(field = "cCodRDA", value = "000007", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BCI_CODPEG","00000442")
		self.oHelper.CheckResult("BCI_CODRDA","000007")
		self.oHelper.SetButton('Cancelar')

		# Pasta Nome do Prestador <F7>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F7")		# self.oHelper.ClickFolder('Nome do Prestador')
		self.oHelper.SetValue(field = "cNomRDA", value = "PLS DSAUPC RDA SILVIA SANT ANNA", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BCI_CODPEG","00000442")
		self.oHelper.CheckResult("BCI_CODRDA","000007")
		self.oHelper.SetButton('Cancelar')

		# Pasta Numero da Guia <F8>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F8")		# self.oHelper.ClickFolder('Numero da Guia')
		self.oHelper.SetValue(field = "cNumGuia", value = "00000001", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Ok")

		# Pasta Numero Impresso <F9>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F9")		# self.oHelper.ClickFolder('Numero Impresso')
		self.oHelper.SetValue(field = "cNumImp", value = "DSAUPC12345678900000", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BD5_NUMIMP","DSAUPC12345678900000")
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('x')

		# Pasta Senha <F10>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F10")		# self.oHelper.ClickFolder('Senha')
		self.oHelper.SetValue(field = "cNumSen", value = "", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Ok')

		# Pasta Nr Aut Operadora <F11>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F11")		# self.oHelper.ClickFolder('Nr Aut Operadora')
		self.oHelper.SetValue(field = "cNuSeOp", value = "DSAUPC123000", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BD5_NRAOPE","DSAUPC123000")
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('x')

		# Pasta Nr Autor./Liber. <F12>
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetKey("F12")		# self.oHelper.ClickFolder('Nr Autor./Liber.')
		self.oHelper.SetValue(field = "cNuNuAut", value = "12345", name_attr = True)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('x')

		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()