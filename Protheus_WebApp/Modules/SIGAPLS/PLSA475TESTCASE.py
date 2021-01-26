from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA475TestCase
TIR - Casos de testes da rotina Mudança / Retorno de fase por lote

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA475(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		#inst.oHelper.Program("PLSA475")

	def test_PLSA475_001(self):
		self.oHelper.Program("PLSA475")
		# Tela - processamento de guias por lote
		self.oHelper.SetButton("Param.")				# Chama o Pergunte PLS475
		self.oHelper.SetValue("mv_par01","")			# Operadora De
		self.oHelper.SetValue("mv_par02","ZZZZ")		# Operadora Ate
		self.oHelper.SetValue("mv_par03","")			# Local Dig. De
		self.oHelper.SetValue("mv_par04","ZZZZ")		# Local Dig. Ate
		self.oHelper.SetValue("mv_par05","00000417")	# Numero PEG de
		self.oHelper.SetValue("mv_par06","00000417")	# Numero PEG Ate
		self.oHelper.SetValue("mv_par07","")			# Rede Atend. De
		self.oHelper.SetValue("mv_par08","ZZZZZZ")		# Rede Atend. Ate
		self.oHelper.SetValue("mv_par09","")			# Ano De
		self.oHelper.SetValue("mv_par10","ZZZZ")		# Ano Ate
		self.oHelper.SetValue("mv_par11","01")			# Mes De
		self.oHelper.SetValue("mv_par12","12")			# Mes Ate
		#self.oHelper.SetValue("mv_par13","Mudar a Fase")# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		#self.oHelper.SetValue("mv_par13",1)				# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		#self.oHelper.SetValue(field="mv_par13", value="Mudar a Fase", name_attr=True)
		#self.oHelper.SetValue(field="mv_par13", value=1, name_attr=True)
		self.oHelper.SetValue("Tipo ?","Mudar a Fase")	# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		self.oHelper.SetValue("mv_par14","")			# Grupo Empresa De
		self.oHelper.SetValue("mv_par15","ZZZZ")		# Grupo Empresa Ate
		self.oHelper.SetValue("mv_par16","")			# Contrato De
		self.oHelper.SetValue("mv_par17","ZZZZZZZZZZZZ")# Contrato Ate
		self.oHelper.SetValue("mv_par18","")			# SubContrato De
		self.oHelper.SetValue("mv_par19","ZZZZZZZZZ")	# SubContrato Ate
		#self.oHelper.SetValue("mv_par20","Sim")			# Rep.Regras Cadastro = 1-Sim; 2-Nao
		#self.oHelper.SetValue("mv_par20",1)				# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("Rep.Regras Cadastro ?","Sim")# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("mv_par21","")			# Grp Cobr BA3/BQC De
		self.oHelper.SetValue("mv_par22","ZZZZ")		# Grp Cobr BA3/BQC Ate
		self.oHelper.SetValue("mv_par23","/  /", check_value=False)	# Dt Evento De
		self.oHelper.SetValue("mv_par24","/  /", check_value=False)	# Dt Evento Ate
		self.oHelper.SetValue("mv_par25","")			# Local Atendimento De
		self.oHelper.SetValue("mv_par26","ZZZ")			# Local Atencimento Ate
		self.oHelper.SetValue("mv_par27","CLI,DEN,HOS,LAB,MED,OPE")	# Classe RDA
		#self.oHelper.SetValue("mv_par28","Nao")			# Somente c/ valor zero = 1-Nao; 2-Sim
		#self.oHelper.SetValue("mv_par28",1)				# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("Somente c/ valor zero ?","Nao")	# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("mv_par29","")			# Protocolo De
		self.oHelper.SetValue("mv_par30","ZZZZZZZZZZZZ")# Protocolo Ate
		self.oHelper.SetValue("mv_par31","")			# Grupo Pagamento De
		self.oHelper.SetValue("mv_par32","ZZZZ")		# Grupo Pagamento Ate
		self.oHelper.SetValue("mv_par33","")			# Numero da NFSS De
		self.oHelper.SetValue("mv_par34","ZZZZZZZZZZ")	# Numero da NFSS Ate
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton("Ok")	# inicia o processamento
		self.oHelper.SetButton("Sim")	# Confirma a mudança de fase dos PEGs de acordo com os parâmetros informados ?
		time.sleep(30)	# Aguardando status do processamento..
		self.oHelper.CheckResult("Aberta", "Sim", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")	# Fecha telinha de statuso do processamento

		self.oHelper.SetButton("Cancelar")	# Fecha telinha de Processamento de Guias por Lote

		self.oHelper.AssertTrue()


	def test_PLSA475_002(self):
		self.oHelper.Program("PLSA475")
		# Tela - processamento de guias por lote
		self.oHelper.SetButton("Param.")				# Chama o Pergunte PLS475
		self.oHelper.SetValue("mv_par01","")			# Operadora De
		self.oHelper.SetValue("mv_par02","ZZZZ")		# Operadora Ate
		self.oHelper.SetValue("mv_par03","")			# Local Dig. De
		self.oHelper.SetValue("mv_par04","ZZZZ")		# Local Dig. Ate
		self.oHelper.SetValue("mv_par05","00000419")	# Numero PEG de
		self.oHelper.SetValue("mv_par06","00000419")	# Numero PEG Ate
		self.oHelper.SetValue("mv_par07","")			# Rede Atend. De
		self.oHelper.SetValue("mv_par08","ZZZZZZ")		# Rede Atend. Ate
		self.oHelper.SetValue("mv_par09","")			# Ano De
		self.oHelper.SetValue("mv_par10","ZZZZ")		# Ano Ate
		self.oHelper.SetValue("mv_par11","01")			# Mes De
		self.oHelper.SetValue("mv_par12","12")			# Mes Ate
		self.oHelper.SetValue("Tipo ?","Retornar a Fase")	# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		self.oHelper.SetValue("mv_par14","")			# Grupo Empresa De
		self.oHelper.SetValue("mv_par15","ZZZZ")		# Grupo Empresa Ate
		self.oHelper.SetValue("mv_par16","")			# Contrato De
		self.oHelper.SetValue("mv_par17","ZZZZZZZZZZZZ")# Contrato Ate
		self.oHelper.SetValue("mv_par18","")			# SubContrato De
		self.oHelper.SetValue("mv_par19","ZZZZZZZZZ")	# SubContrato Ate
		self.oHelper.SetValue("Rep.Regras Cadastro ?","Sim")# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("mv_par21","")			# Grp Cobr BA3/BQC De
		self.oHelper.SetValue("mv_par22","ZZZZ")		# Grp Cobr BA3/BQC Ate
		self.oHelper.SetValue("mv_par23","/  /", check_value=False)	# Dt Evento De
		self.oHelper.SetValue("mv_par24","/  /", check_value=False)	# Dt Evento Ate
		self.oHelper.SetValue("mv_par25","")			# Local Atendimento De
		self.oHelper.SetValue("mv_par26","ZZZ")			# Local Atencimento Ate
		self.oHelper.SetValue("mv_par27","CLI,DEN,HOS,LAB,MED,OPE")	# Classe RDA
		self.oHelper.SetValue("Somente c/ valor zero ?","Nao")	# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("mv_par29","")			# Protocolo De
		self.oHelper.SetValue("mv_par30","ZZZZZZZZZZZZ")# Protocolo Ate
		self.oHelper.SetValue("mv_par31","")			# Grupo Pagamento De
		self.oHelper.SetValue("mv_par32","ZZZZ")		# Grupo Pagamento Ate
		self.oHelper.SetValue("mv_par33","")			# Numero da NFSS De
		self.oHelper.SetValue("mv_par34","ZZZZZZZZZZ")	# Numero da NFSS Ate
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton("Ok")	# inicia o processamento
		self.oHelper.SetButton("Sim")	# Confirma a mudança de fase dos PEGs de acordo com os parâmetros informados ?
		time.sleep(30)	# Aguardando status do processamento..
		self.oHelper.CheckResult("Aberta", "Sim", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")	# Fecha telinha de statuso do processamento

		self.oHelper.SetButton("Cancelar")	# Fecha telinha de Processamento de Guias por Lote

		self.oHelper.AssertTrue()



	def test_PLSA475_003(self):
		self.oHelper.Program("PLSA475")
		# Tela - processamento de guias por lote
		self.oHelper.SetButton("Param.")				# Chama o Pergunte PLS475
		self.oHelper.SetValue("mv_par01","")			# Operadora De
		self.oHelper.SetValue("mv_par02","ZZZZ")		# Operadora Ate
		self.oHelper.SetValue("mv_par03","")			# Local Dig. De
		self.oHelper.SetValue("mv_par04","ZZZZ")		# Local Dig. Ate
		self.oHelper.SetValue("mv_par05","00000440")	# Numero PEG de
		self.oHelper.SetValue("mv_par06","00000440")	# Numero PEG Ate
		self.oHelper.SetValue("mv_par07","")			# Rede Atend. De
		self.oHelper.SetValue("mv_par08","ZZZZZZ")		# Rede Atend. Ate
		self.oHelper.SetValue("mv_par09","")			# Ano De
		self.oHelper.SetValue("mv_par10","ZZZZ")		# Ano Ate
		self.oHelper.SetValue("mv_par11","01")			# Mes De
		self.oHelper.SetValue("mv_par12","12")			# Mes Ate
		self.oHelper.SetValue("Tipo ?","Revalor. Pagto")# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		self.oHelper.SetValue("mv_par14","")			# Grupo Empresa De
		self.oHelper.SetValue("mv_par15","ZZZZ")		# Grupo Empresa Ate
		self.oHelper.SetValue("mv_par16","")			# Contrato De
		self.oHelper.SetValue("mv_par17","ZZZZZZZZZZZZ")# Contrato Ate
		self.oHelper.SetValue("mv_par18","")			# SubContrato De
		self.oHelper.SetValue("mv_par19","ZZZZZZZZZ")	# SubContrato Ate
		self.oHelper.SetValue("Rep.Regras Cadastro ?","Sim")# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("mv_par21","")			# Grp Cobr BA3/BQC De
		self.oHelper.SetValue("mv_par22","ZZZZ")		# Grp Cobr BA3/BQC Ate
		self.oHelper.SetValue("mv_par23","/  /", check_value=False)	# Dt Evento De
		self.oHelper.SetValue("mv_par24","/  /", check_value=False)	# Dt Evento Ate
		self.oHelper.SetValue("mv_par25","")			# Local Atendimento De
		self.oHelper.SetValue("mv_par26","ZZZ")			# Local Atencimento Ate
		self.oHelper.SetValue("mv_par27","CLI,DEN,HOS,LAB,MED,OPE")	# Classe RDA
		self.oHelper.SetValue("Somente c/ valor zero ?","Nao")	# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("mv_par29","")			# Protocolo De
		self.oHelper.SetValue("mv_par30","ZZZZZZZZZZZZ")# Protocolo Ate
		self.oHelper.SetValue("mv_par31","")			# Grupo Pagamento De
		self.oHelper.SetValue("mv_par32","ZZZZ")		# Grupo Pagamento Ate
		self.oHelper.SetValue("mv_par33","")			# Numero da NFSS De
		self.oHelper.SetValue("mv_par34","ZZZZZZZZZZ")	# Numero da NFSS Ate
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton("Ok")	# inicia o processamento
		self.oHelper.SetButton("Sim")	# Confirma a mudança de fase dos PEGs de acordo com os parâmetros informados ?
		time.sleep(30)	# Aguardando status do processamento..
		self.oHelper.CheckResult("Aberta", "Sim", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")	# Fecha telinha de statuso do processamento

		self.oHelper.SetButton("Cancelar")	# Fecha telinha de Processamento de Guias por Lote

		self.oHelper.AssertTrue()


	def test_PLSA475_004(self):
		self.oHelper.Program("PLSA475")
		# Tela - processamento de guias por lote
		self.oHelper.SetButton("Param.")				# Chama o Pergunte PLS475
		self.oHelper.SetValue("mv_par01","")			# Operadora De
		self.oHelper.SetValue("mv_par02","ZZZZ")		# Operadora Ate
		self.oHelper.SetValue("mv_par03","")			# Local Dig. De
		self.oHelper.SetValue("mv_par04","ZZZZ")		# Local Dig. Ate
		self.oHelper.SetValue("mv_par05","00000440")	# Numero PEG de
		self.oHelper.SetValue("mv_par06","00000440")	# Numero PEG Ate
		self.oHelper.SetValue("mv_par07","")			# Rede Atend. De
		self.oHelper.SetValue("mv_par08","ZZZZZZ")		# Rede Atend. Ate
		self.oHelper.SetValue("mv_par09","")			# Ano De
		self.oHelper.SetValue("mv_par10","ZZZZ")		# Ano Ate
		self.oHelper.SetValue("mv_par11","01")			# Mes De
		self.oHelper.SetValue("mv_par12","12")			# Mes Ate
		self.oHelper.SetValue("Tipo ?","Revalor. Cobr.")# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		self.oHelper.SetValue("mv_par14","")			# Grupo Empresa De
		self.oHelper.SetValue("mv_par15","ZZZZ")		# Grupo Empresa Ate
		self.oHelper.SetValue("mv_par16","")			# Contrato De
		self.oHelper.SetValue("mv_par17","ZZZZZZZZZZZZ")# Contrato Ate
		self.oHelper.SetValue("mv_par18","")			# SubContrato De
		self.oHelper.SetValue("mv_par19","ZZZZZZZZZ")	# SubContrato Ate
		self.oHelper.SetValue("Rep.Regras Cadastro ?","Sim")# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("mv_par21","")			# Grp Cobr BA3/BQC De
		self.oHelper.SetValue("mv_par22","ZZZZ")		# Grp Cobr BA3/BQC Ate
		self.oHelper.SetValue("mv_par23","/  /", check_value=False)	# Dt Evento De
		self.oHelper.SetValue("mv_par24","/  /", check_value=False)	# Dt Evento Ate
		self.oHelper.SetValue("mv_par25","")			# Local Atendimento De
		self.oHelper.SetValue("mv_par26","ZZZ")			# Local Atencimento Ate
		self.oHelper.SetValue("mv_par27","CLI,DEN,HOS,LAB,MED,OPE")	# Classe RDA
		self.oHelper.SetValue("Somente c/ valor zero ?","Nao")	# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("mv_par29","")			# Protocolo De
		self.oHelper.SetValue("mv_par30","ZZZZZZZZZZZZ")# Protocolo Ate
		self.oHelper.SetValue("mv_par31","")			# Grupo Pagamento De
		self.oHelper.SetValue("mv_par32","ZZZZ")		# Grupo Pagamento Ate
		self.oHelper.SetValue("mv_par33","")			# Numero da NFSS De
		self.oHelper.SetValue("mv_par34","ZZZZZZZZZZ")	# Numero da NFSS Ate
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton("Ok")	# inicia o processamento
		self.oHelper.SetButton("Sim")	# Confirma a mudança de fase dos PEGs de acordo com os parâmetros informados ?
		time.sleep(30)	# Aguardando status do processamento..
		self.oHelper.CheckResult("Aberta", "Sim", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")	# Fecha telinha de statuso do processamento

		self.oHelper.SetButton("Cancelar")	# Fecha telinha de Processamento de Guias por Lote

		self.oHelper.AssertTrue()



	def test_PLSA475_005(self):
		self.oHelper.Program("PLSA475")
		# Tela - processamento de guias por lote
		self.oHelper.SetButton("Param.")				# Chama o Pergunte PLS475
		self.oHelper.SetValue("mv_par01","")			# Operadora De
		self.oHelper.SetValue("mv_par02","ZZZZ")		# Operadora Ate
		self.oHelper.SetValue("mv_par03","")			# Local Dig. De
		self.oHelper.SetValue("mv_par04","ZZZZ")		# Local Dig. Ate
		self.oHelper.SetValue("mv_par05","00000440")	# Numero PEG de
		self.oHelper.SetValue("mv_par06","00000440")	# Numero PEG Ate
		self.oHelper.SetValue("mv_par07","")			# Rede Atend. De
		self.oHelper.SetValue("mv_par08","ZZZZZZ")		# Rede Atend. Ate
		self.oHelper.SetValue("mv_par09","")			# Ano De
		self.oHelper.SetValue("mv_par10","ZZZZ")		# Ano Ate
		self.oHelper.SetValue("mv_par11","01")			# Mes De
		self.oHelper.SetValue("mv_par12","12")			# Mes Ate
		self.oHelper.SetValue("Tipo ?","Rev.Cob./Pagto")# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		self.oHelper.SetValue("mv_par14","")			# Grupo Empresa De
		self.oHelper.SetValue("mv_par15","ZZZZ")		# Grupo Empresa Ate
		self.oHelper.SetValue("mv_par16","")			# Contrato De
		self.oHelper.SetValue("mv_par17","ZZZZZZZZZZZZ")# Contrato Ate
		self.oHelper.SetValue("mv_par18","")			# SubContrato De
		self.oHelper.SetValue("mv_par19","ZZZZZZZZZ")	# SubContrato Ate
		self.oHelper.SetValue("Rep.Regras Cadastro ?","Sim")# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("mv_par21","")			# Grp Cobr BA3/BQC De
		self.oHelper.SetValue("mv_par22","ZZZZ")		# Grp Cobr BA3/BQC Ate
		self.oHelper.SetValue("mv_par23","/  /", check_value=False)	# Dt Evento De
		self.oHelper.SetValue("mv_par24","/  /", check_value=False)	# Dt Evento Ate
		self.oHelper.SetValue("mv_par25","")			# Local Atendimento De
		self.oHelper.SetValue("mv_par26","ZZZ")			# Local Atencimento Ate
		self.oHelper.SetValue("mv_par27","CLI,DEN,HOS,LAB,MED,OPE")	# Classe RDA
		self.oHelper.SetValue("Somente c/ valor zero ?","Nao")	# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("mv_par29","")			# Protocolo De
		self.oHelper.SetValue("mv_par30","ZZZZZZZZZZZZ")# Protocolo Ate
		self.oHelper.SetValue("mv_par31","")			# Grupo Pagamento De
		self.oHelper.SetValue("mv_par32","ZZZZ")		# Grupo Pagamento Ate
		self.oHelper.SetValue("mv_par33","")			# Numero da NFSS De
		self.oHelper.SetValue("mv_par34","ZZZZZZZZZZ")	# Numero da NFSS Ate
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton("Ok")	# inicia o processamento
		self.oHelper.SetButton("Sim")	# Confirma a mudança de fase dos PEGs de acordo com os parâmetros informados ?
		time.sleep(30)	# Aguardando status do processamento..
		self.oHelper.CheckResult("Aberta", "Sim", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")	# Fecha telinha de statuso do processamento

		self.oHelper.SetButton("Cancelar")	# Fecha telinha de Processamento de Guias por Lote

		self.oHelper.AssertTrue()



	def test_PLSA475_006(self):
		self.oHelper.Program("PLSA475")
		# Tela - processamento de guias por lote
		self.oHelper.SetButton("Param.")				# Chama o Pergunte PLS475
		self.oHelper.SetValue("mv_par01","")			# Operadora De
		self.oHelper.SetValue("mv_par02","ZZZZ")		# Operadora Ate
		self.oHelper.SetValue("mv_par03","")			# Local Dig. De
		self.oHelper.SetValue("mv_par04","ZZZZ")		# Local Dig. Ate
		self.oHelper.SetValue("mv_par05","00000411")	# Numero PEG de
		self.oHelper.SetValue("mv_par06","00000411")	# Numero PEG Ate
		self.oHelper.SetValue("mv_par07","")			# Rede Atend. De
		self.oHelper.SetValue("mv_par08","ZZZZZZ")		# Rede Atend. Ate
		self.oHelper.SetValue("mv_par09","")			# Ano De
		self.oHelper.SetValue("mv_par10","ZZZZ")		# Ano Ate
		self.oHelper.SetValue("mv_par11","01")			# Mes De
		self.oHelper.SetValue("mv_par12","12")			# Mes Ate
		self.oHelper.SetValue("Tipo ?","Mudar a Fase")	# Tipo = 1-Mudar a fase; 2-Retornar a fase; 3-Revalor. Pagto; 4-Revalor Cobr.; 5-Rev.Cob./Pagto
		self.oHelper.SetValue("mv_par14","")			# Grupo Empresa De
		self.oHelper.SetValue("mv_par15","ZZZZ")		# Grupo Empresa Ate
		self.oHelper.SetValue("mv_par16","")			# Contrato De
		self.oHelper.SetValue("mv_par17","ZZZZZZZZZZZZ")# Contrato Ate
		self.oHelper.SetValue("mv_par18","")			# SubContrato De
		self.oHelper.SetValue("mv_par19","ZZZZZZZZZ")	# SubContrato Ate
		self.oHelper.SetValue("Rep.Regras Cadastro ?","Nao")# Rep.Regras Cadastro = 1-Sim; 2-Nao
		self.oHelper.SetValue("mv_par21","")			# Grp Cobr BA3/BQC De
		self.oHelper.SetValue("mv_par22","ZZZZ")		# Grp Cobr BA3/BQC Ate
		self.oHelper.SetValue("mv_par23","/  /", check_value=False)	# Dt Evento De
		self.oHelper.SetValue("mv_par24","/  /", check_value=False)	# Dt Evento Ate
		self.oHelper.SetValue("mv_par25","")			# Local Atendimento De
		self.oHelper.SetValue("mv_par26","ZZZ")			# Local Atencimento Ate
		self.oHelper.SetValue("mv_par27","CLI,DEN,HOS,LAB,MED,OPE")	# Classe RDA
		self.oHelper.SetValue("Somente c/ valor zero ?","Sim")	# Somente c/ valor zero = 1-Nao; 2-Sim
		self.oHelper.SetValue("mv_par29","")			# Protocolo De
		self.oHelper.SetValue("mv_par30","ZZZZZZZZZZZZ")# Protocolo Ate
		self.oHelper.SetValue("mv_par31","")			# Grupo Pagamento De
		self.oHelper.SetValue("mv_par32","ZZZZ")		# Grupo Pagamento Ate
		self.oHelper.SetValue("mv_par33","")			# Numero da NFSS De
		self.oHelper.SetValue("mv_par34","ZZZZZZZZZZ")	# Numero da NFSS Ate
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton("Ok")	# inicia o processamento
		self.oHelper.SetButton("Sim")	# Confirma a mudança de fase dos PEGs de acordo com os parâmetros informados ?
		time.sleep(30)	# Aguardando status do processamento..
		self.oHelper.CheckResult("Aberta", "Sim", grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Confirmar")	# Fecha telinha de statuso do processamento

		self.oHelper.SetButton("Cancelar")	# Fecha telinha de Processamento de Guias por Lote

		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()