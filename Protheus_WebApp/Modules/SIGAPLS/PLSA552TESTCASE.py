from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA552TestCase
TIR - Casos de testes da rotina Transferencia Processamento de Contas

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA552(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA552")
		inst.oHelper.AddParameter("MV_TABSSUS","" , "07")
		inst.oHelper.AddParameter("MV_CDLCSUS","" , "0004")
		inst.oHelper.AddParameter("MV_CDTUNEP","" , "0001005")
		inst.oHelper.AddParameter("MV_PLCALPG","" , "2")
		inst.oHelper.SetParameters()

	def teste_PLSA552_001(self):
		self.oHelper.SearchBrowse(f'{"20180164010050060064 1"}', key=2, index=True)
		self.oHelper.SetButton("Selecionar")
		self.oHelper.SearchBrowse(f'{"0001640012224650/2018-01650   00000005"}', key=1, index=True)
		self.oHelper.SetButton("Transf. Contas Médicas")
		self.oHelper.SetButton("Sim")		# Deseja transferir... ?
		time.sleep(15)
		self.oHelper.SetButton("Fechar")	# Processamento incluso no processamento de contas!

		self.oHelper.SearchBrowse(f'{"0001640012224650/2018-01650   00000005"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B0R_IDANS","64010050060064")
		self.oHelper.CheckResult("B0R_OFICIO","650")
		self.oHelper.SetValue("B0R_STATUS","4 - Gerado C.Medicas")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações",sub_item='Transferência em Lote')
		self.oHelper.SetValue(field = "cMesDe", value = "10", name_attr = True) #self.oHelper.SetValue("cMesDe","10")
		self.oHelper.SetValue(field = "cMesAt", value = "10", name_attr = True) #self.oHelper.SetValue("cMesAt","10")
		self.oHelper.SetValue(field = "cAnoDe", value = "2020", name_attr = True) #self.oHelper.SetValue("cAnoDe","2020")
		self.oHelper.SetValue(field = "cAnoAt", value = "2020", name_attr = True) #self.oHelper.SetValue("cAnoAt","2020")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Fechar")	# Não existem atendimentos detro dos parametros informadors
		self.oHelper.SetButton("Cancelar")	# .. fechando tela de Filtro de Atendimentos
		
		self.oHelper.SetButton("x")

		self.oHelper.SearchBrowse(f'{"20180164010050060064 1"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Apagar Ressarc. SUS')
		self.oHelper.SetButton("Sim")		# O processo já possui Contas Médicas Geradas. Deseja continuar?
		self.oHelper.SetButton("Fechar")	# Não foi possível excluir o Ressarcimento. O processo já possui Guias com status diferente de Digitação
		self.oHelper.SetButton("Sim")		# O processo já possui Contas Médicas Geradas. Deseja continuar?
		self.oHelper.SetButton("Fechar")	# Não foi possível excluir o Ressarcimento. O processo já possui Guias com status diferente de Digitação

		self.oHelper.SetButton("Sim")		# O processo já possui Contas Médicas Geradas. Deseja continuar?
		self.oHelper.SetButton("Fechar")	# Não foi possível excluir o Ressarcimento. O processo já possui Guias com status diferente de Digitação

		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()