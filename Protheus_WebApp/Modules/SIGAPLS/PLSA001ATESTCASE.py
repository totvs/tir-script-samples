import unittest
from tir import Webapp
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
dateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA001ATestCase
TIR - Casos de testes da rotina de protocolo de reembolso

@author r.soares
@since 25/08/2020
@version 12
-------------------------------------------------------------------"""


class PLSA001A(unittest.TestCase):
	#-------------------------------------------
	# Inicialiação setUpClass para TIR - PLSA001A 
	#-------------------------------------------
	@classmethod
	def setUpClass(self):
		# inst.oHelper = ApwInternal("config.json")
		# inst.oHelper.Setup()
		self.oHelper = Webapp(autostart=False)
		self.oHelper.SetTIRConfig(config_name="User", value="admin")
		self.oHelper.SetTIRConfig(config_name="Password", value="1234")
		self.oHelper.Start()
		self.oHelper.Setup("SIGAPLS", DateSystem, "T1", "M SP 01 ", "33")
		self.oHelper.Program('PLSA001A')
		self.oHelper.AddParameter("MV_PLCALPG", "", "2", "2", "2")
		self.oHelper.SetParameters()

	#-------------------------------------------
	# Inicio dos casos de testes TIR - PLSA001A 
	#-------------------------------------------
	
# 	"""-------------------------------------------------------------------
# 	/*/{Protheus.doc} TEST_PLSA001A_PL001
# 	TIR - Casos de testes da rotina Reembolso 
# 	Alteracao dos status do protocolo.

# 	@author r.soares
# 	@since 22/06/2020
# 	@version 12
# 	# -------------------------------------------------------------------"""
	def test_PLSA001A_PL001(self):
		chaveTit = "M SP    00012343000001013"

		self.oHelper.SearchBrowse(f'{chaveTit}', key=5, index=True)
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('BOW_STATUS', '1', check_value=False)
		self.oHelper.SetButton('Salvar')

		self.oHelper.SearchBrowse(f'{chaveTit}', key=5, index=True)
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('BOW_STATUS', '2', check_value=False)
		self.oHelper.SetButton('Salvar')

		self.oHelper.SearchBrowse(f'{chaveTit}', key=5, index=True)
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('BOW_STATUS', '3', check_value=False)
		self.oHelper.SetButton('Salvar')

		time.sleep(5)
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	# """-------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA001A_PL002
	# TIR - Casos de testes da rotina Reembolso 
	# EXCLUINDO REEMBOLSO

	# @author r.soares
	# @since 27/08/2020
	# @version 12
	# # -------------------------------------------------------------------"""
	def test_PLSA001A_PL002(self):
		chaveTit = "M SP    00012343000001013"
		self.oHelper.SearchBrowse(f'{chaveTit}', key=5, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	#-------------------------------------------
	# Fim dos casos de testes TIR - PLSA001A 
	#-------------------------------------------

	#-------------------------------------------
	# Encerramento class para TIR - PLSA001A 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()