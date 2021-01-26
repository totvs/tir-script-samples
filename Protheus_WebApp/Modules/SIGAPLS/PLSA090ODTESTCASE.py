import unittest
from tir import Webapp
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
# -------------------------------------------------------------------
# /*/{Protheus.doc} PLSA090ODTestCase
# TIR - Casos de testes da rotina Odontologica 

# @author r.soares
# @since 27/05/2020
# @version 12
# -------------------------------------------------------------------


class PLSA090OD(unittest.TestCase):
	#-------------------------------------------
	# Inicialiação setUpClass para TIR - PLSA090OD 
	#-------------------------------------------
	@classmethod
	def setUpClass(self):
		# inst.oHelper = ApwInternal("config.json")		
		# inst.oHelper.Setup()
		self.oHelper = Webapp()
		self.oHelper.SetTIRConfig(config_name="User", value="admin")
		self.oHelper.SetTIRConfig(config_name="Password", value="1234")
		self.oHelper.Start()
		self.oHelper.Setup("SIGAPLS", DateSystem, "T1", "M SP 01 ", "33")
		self.oHelper.Program('PLSA094D')
		self.oHelper.AddParameter("MV_PLCALPG", "", "2", "2", "2")
		self.oHelper.SetParameters()

	#-------------------------------------------
	# Inicio dos casos de testes TIR - PLSA090OD 
	#-------------------------------------------

# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL001
	# TIR - Casos de testes da rotina Odontologica 
	# Incluindo guia

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# # # -------------------------------------------------------------------
	def test_PLSA090OD_PL001(self):
		
		self.oHelper.WaitShow("Liberação Odontológica") 
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		# self.oHelper.SetButton('Ok')
		# self.oHelper.SetButton('Gerar Protoc.')
		# self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Outras Ações',sub_item='Limpa')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CODRDA', '000004')
		self.oHelper.SetButton('Outras Ações',sub_item='Financ')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Outras Ações',sub_item='Cliente')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Outras Ações',sub_item='Cobranca')
		self.oHelper.SetValue('Ano Base ?', '2020')
		self.oHelper.SetValue('Mes Base ?', '06')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_CODPAD", "03", name_attr=True)
		self.oHelper.SetValue("BE2_CODPRO", "0001", name_attr=True)
		self.oHelper.SetValue("BE2_DENREG", "11", name_attr=True)
		self.oHelper.SetValue("BE2_FADENT", "D", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')

		time.sleep(5)
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL002
	# TIR - Casos de testes da rotina Odontologica 
	# Incluindo interacao na guia

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# # -------------------------------------------------------------------
	def test_PLSA090OD_PL002(self):

		chaveTit = "M SP    00010020000001"


		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)

		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL003
	# TIR - Casos de testes da rotina Odontologica 
	# Excluindo uma guia PLSA090OD

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# # -------------------------------------------------------------------
	def test_PLSA090OD_PL003(self):

		chaveTit = "M SP    00010020000001"

		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)

		self.oHelper.SetButton('Outras Ações',sub_item='Interação')
		self.oHelper.SetBranch('M SP 01')
		self.oHelper.ClickGridCell("Cod. Tab. Pd")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue('Motivo Padrão', '001')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL004
	# TIR - Casos de testes da rotina Odontologica 
	# Visualizando uma guia PLSA090OD

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL004(self):
			
		chaveTit = "M SP    00010020000001"

		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)

		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('B01_USUARI', '00010020000001014')
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL005
	# TIR - Casos de testes da rotina Odontologica 
	# Imprimindo guia da rotina PLSA090OD

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL005(self):
		
		chaveTit = "M SP    00010020000001"

		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)
		
		self.oHelper.SetButton('Outras Ações',sub_item='Imp.Guia')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Ok')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL006
	# TIR - Casos de testes da rotina Odontologica 
	# Imprimindo varias guias da rotina PLSA090OD

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL006(self):


		chaveTit = "M SP    00010020000001"

		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)
		
		self.oHelper.SetButton('Outras Ações',sub_item='Imp.Varias Guias')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL007
	# TIR - Casos de testes da rotina Odontologica 
	# Adicionando valor no campo de conhecimento

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL007(self):

		chaveTit = "M SP    00010020000001"
		
		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Conhecimento, Guia')
		time.sleep(3)
		self.oHelper.ClickGridCell("Objeto")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetKey("F3", grid=True)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Outras Ações',sub_item='Conhecimento, Item')
		time.sleep(3)
		self.oHelper.SetButton('Pesquisar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Conhecimento')
		self.oHelper.ClickGridCell("Objeto")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetKey("F3", grid=True)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Sair')
		
		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL008
	# TIR - Casos de testes da rotina Odontologica 
	# Copia

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL008(self):

		chaveTit = "M SP    00010020000001"

		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Copiar')
		self.oHelper.SetBranch("M SP 01")
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_QTDPRO", "1,0000", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL009
	# TIR - Casos de testes da rotina Odontologica 
	# Cancelando guia do plsa090od

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL009(self):

		chaveTit = "M SP    00010020000001"

		self.oHelper.WaitShow("Liberação Odontológica") 
		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)
		
		self.oHelper.SetButton('Outras Ações',sub_item='Cancelar Guia')
		time.sleep(3)
		self.oHelper.SetKey("F3")
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Confirma')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()
		
# # -------------------------------------------------------------------
# 	# /*/{Protheus.doc} TEST_PLSA090OD_PL010
# 	# TIR - Casos de testes da rotina Odontologica 
# 	# Incluindo guia com pagamento na fatura sem a guia comprada

# 	# @author r.soares
# 	# @since 27/05/2020
# 	# @version 12
# 	# # # -------------------------------------------------------------------
	def test_PLSA090OD_PL010(self):
		

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_SIGLA', 'CRM')
		self.oHelper.SetValue('B01_ESTSOL', 'SP')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.SetValue('B01_QUACOB', '2')
		self.oHelper.SetKey('Enter')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_CODPAD", "03", name_attr=True)
		self.oHelper.SetValue("BE2_CODPRO", "81000030", name_attr=True)
		self.oHelper.SetValue("BE2_GUIACO", "0", name_attr=True)
		self.oHelper.SetValue("BE2_QUACOB", "2", name_attr=True)
		self.oHelper.SetValue("BE2_DENREG", "11", name_attr=True)
		self.oHelper.SetValue("BE2_FADENT", "D", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL011
	# TIR - Casos de testes da rotina Odontologica 
	# Incluindo guia com pagamento na fatura com a guia comprada

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# # # -------------------------------------------------------------------
	def test_PLSA090OD_PL011(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_SIGLA', 'CRM')
		self.oHelper.SetValue('B01_ESTSOL', 'SP')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.SetValue('B01_QUACOB', '2')
		self.oHelper.SetKey('Enter')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_CODPAD", "03", name_attr=True)
		self.oHelper.SetValue("BE2_CODPRO", "82000026", name_attr=True)
		self.oHelper.SetValue("BE2_GUIACO", "1", name_attr=True)
		self.oHelper.SetValue("BE2_QUACOB", "2", name_attr=True)
		self.oHelper.SetValue("BE2_DENREG", "11", name_attr=True)
		self.oHelper.SetValue("BE2_FADENT", "D", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Outras Ações',sub_item='Comprar')
		self.oHelper.SetButton('Fechar', check_error= False)
		self.oHelper.SetButton('Outras Ações',sub_item='Co-Part.')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
		# -------------------------------------------------------------------
		# /*/{Protheus.doc} TEST_PLSA090OD_PL012
		# TIR - Casos de testes da rotina Odontologica 
		# Incluindo guia com pagamento no ato sem a guia estar comprada

		# @author r.soares
		# @since 27/05/2020
		# @version 12
		# # # -------------------------------------------------------------------
	def test_PLSA090OD_PL012(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_SIGLA', 'CRM')
		self.oHelper.SetValue('B01_ESTSOL', 'SP')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.SetValue('B01_QUACOB', '1')
		self.oHelper.SetKey('Enter')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_CODPAD", "03", name_attr=True)
		self.oHelper.SetValue("BE2_CODPRO", "82000026", name_attr=True)
		self.oHelper.SetValue("BE2_GUIACO", "0", name_attr=True)
		self.oHelper.SetValue("BE2_QUACOB", "2", name_attr=True)
		self.oHelper.SetValue("BE2_DENREG", "11", name_attr=True)
		self.oHelper.SetValue("BE2_FADENT", "D", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL013
	# TIR - Casos de testes da rotina Odontologica 
	# Incluindo guia com pagamento no ato com a guia comprada

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------
	def test_PLSA090OD_PL013(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CODRDA', '000001')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_SIGLA', 'CRM')
		self.oHelper.SetValue('B01_ESTSOL', 'SP')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.SetValue('B01_QUACOB', '1')
		self.oHelper.SetKey('Enter')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_CODPAD", "03", name_attr=True)
		self.oHelper.SetValue("BE2_CODPRO", "0001", name_attr=True)
		self.oHelper.SetValue("BE2_GUIACO", "1", name_attr=True)
		self.oHelper.SetValue("BE2_QUACOB", "1", name_attr=True)
		self.oHelper.SetValue("BE2_DENREG", "11", name_attr=True)
		self.oHelper.SetValue("BE2_FADENT", "D", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')
		time.sleep(2)
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL014
	# TIR - Casos de testes da rotina Odontologica 
	# Inclusao da rotina de autorizacao Odontologica com refer�ncia na libera��o odonto

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------

	def test_PLSA090OD_PL014(self):

		self.oHelper.Start()
		self.oHelper.Setup("SIGAPLS", DateSystem, "T1", "M SP 01 ", "33")
		self.oHelper.Program('PLSA094C')
		self.oHelper.WaitShow("Autorização Odontológica") 
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('B01_NUMLIB', '000120200900000006', grid=False, grid_number=1, ignore_case=True,row=None, name_attr=False, check_value=False)	
		self.oHelper.SetValue('B01_CODRDA', '000001')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BE2_CODPAD", "03", name_attr=True)
		self.oHelper.SetValue("BE2_CODPRO", "82000026", name_attr=True)
		self.oHelper.SetValue("BE2_DENREG", "11", name_attr=True)
		self.oHelper.SetValue("BE2_FADENT", "D", name_attr=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')

		time.sleep(5)
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		
	# -------------------------------------------------------------------
	# /*/{Protheus.doc} TEST_PLSA090OD_PL015
	# TIR - Casos de testes da rotina Odontologica 
	# Copia da rotina de autorizacao Odontologica

	# @author r.soares
	# @since 27/05/2020
	# @version 12
	# -------------------------------------------------------------------

	def test_PLSA090OD_PL015(self):

		# self.oHelper.WaitShow("Autorização Odontológica") 

		chaveTit = "M SP    00010020000001"
		self.oHelper.SearchBrowse(f'{chaveTit}', key=2, index=True)
		
		self.oHelper.SetButton('Outras Ações',sub_item='Copiar')
		self.oHelper.SetBranch("M SP 01")
		self.oHelper.SetValue('B01_USUARI', '00010020000001014')
		self.oHelper.SetValue('B01_CODRDA', '000001')
		self.oHelper.SetValue('B01_CID', 'F12')
		self.oHelper.SetValue('B01_REGSOL', '1234')
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
	
	#-------------------------------------------
	# Fim dos casos de testes TIR - PLSA090OD 
	#-------------------------------------------

	#-------------------------------------------
	# Encerramento class para TIR - PLSA090OD 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()