import unittest
import time
from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class PLSA092(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS", DateSystem, "T1", "M SP 01 ", "33")
		inst.oHelper.Program("PLSA092")
		inst.oHelper.AddParameter("MV_PLSSOOL", "", "1", "1", "1") # Habilita Prorroga��o de Interna��o
		inst.oHelper.AddParameter("MV_PLCALPG", "", "2", "2", "2") # Novo Calendario de Pagamento
		inst.oHelper.SetParameters()
				
	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA092_PL001

	# Teste 01 - Consulta Autorizada
	
	# @author r.soares
	# @since 05/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA092_PL001(self):
		
		# Dados para o teste
		matricula = '00010022000004010'
		rda = '000004'
		solicitante = '013500'
		grpIntern = '1'
		indClinica = 'teste'
		regInter = '1'
		cid = 'F12'
		procedimento = '10101012'

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('BE4_USUARI', matricula, name_attr=True)
		self.oHelper.SetValue('BE4_CODRDA', rda)
		self.oHelper.F3(field='BE4_CODLOC')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BE4_GRPINT', grpIntern)
		self.oHelper.F3(field='BE4_TIPINT')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.F3(field='BE4_INTSIP')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BE4_CID', cid)
		self.oHelper.SetValue('BE4_REGSOL', solicitante)
		self.oHelper.F3(field='BE4_CIDSEC')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.F3(field='BE4_PADINT')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.F3(field='BE4_PADCON')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BE4_REGEXE', solicitante)
		self.oHelper.SetValue('BE4_INDCLI', indClinica)
		self.oHelper.SetValue('BE4_REGINT', regInter)
		self.oHelper.ClickGridCell("Cod. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue('BEJ_CODPRO', procedimento)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')     
		self.oHelper.SetButton('Cancelar')     		
		self.oHelper.AssertTrue()
	
	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA092_PL002

	# Teste 02 - Interna��o Autorizada
	
	# @author r.soares
	# @since 05/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA092_PL002(self):
		
		# Dados para o teste
		matricula = '00010022000004010'
		rda = '000004'
		solicitante = '013500'
		grpIntern = '1'
		indClinica = 'teste'
		regInter = '1'
		cid = 'F12'
		procedimento = '40304361'

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01")
		time.sleep(3)
		self.oHelper.SetValue('BE4_USUARI', matricula, name_attr=True)
		self.oHelper.SetValue('BE4_CODRDA', rda)
		self.oHelper.F3(field='BE4_CODLOC')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BE4_GRPINT', grpIntern)
		self.oHelper.F3(field='BE4_TIPINT')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.F3(field='BE4_INTSIP')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BE4_CID', cid)
		self.oHelper.SetValue('BE4_REGSOL', solicitante)
		self.oHelper.F3(field='BE4_CIDSEC')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.F3(field='BE4_PADINT')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.F3(field='BE4_PADCON')
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BE4_REGEXE', solicitante)
		self.oHelper.SetValue('BE4_INDCLI', indClinica)
		self.oHelper.SetValue('BE4_REGINT', regInter)
		self.oHelper.ClickGridCell("Cod. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue('BEJ_CODPRO', procedimento)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')    
		self.oHelper.SetButton('Cancelar')     		
		self.oHelper.AssertTrue()

	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA092_PL003

	# Teste 03 - Exclusão - Consulta
	
	# @author r.soares
	# @since 05/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA092_PL003(self):
		
		# Dados para o teste
		chave = "M SP    00010022000004010"
			
		self.oHelper.SearchBrowse(f'{chave}', key=4, index=True)
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('BE4_USUARI', '00010022000004010')
		self.oHelper.SetButton('Confirmar')    
			
		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		self.oHelper.SetButton('Confirmar')    
		self.oHelper.AssertTrue()

	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA092_PL004

	# Teste 04 - Internação e Alta do Beneficiário - Autorizada
	
	# @author r.soares
	# @since 05/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA092_PL004(self):
		
		# Dados para o teste
		TpAlta = "1"
		chave = "M SP    00010022000004010"
			
		self.oHelper.SearchBrowse(f'{chave}', key=4, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Data Internação.')
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetButton('Incluir')    
		self.oHelper.SetButton('Fechar')    
		self.oHelper.SetButton('Ok')    
		self.oHelper.SetButton('Outras Ações',sub_item='Data Alta')
		self.oHelper.SetBranch("M SP 01 ")
		horas 	= datetime.now()
		hora 	= horas.hour
		minuto 	= horas.minute
		HrAlta = str(hora) + str(minuto)
		self.oHelper.SetValue('Hora da Alta', HrAlta, check_value=False)
		time.sleep(3)
		self.oHelper.SetButton('Fechar', check_error=False)
		self.oHelper.SetValue('Tipo de Alta', TpAlta, check_value=False)
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Fechar')	
		
		self.oHelper.AssertTrue()

		#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA092_PL005

	# Teste 05 - Inserindo Visita Profissional
	
	# @author r.soares
	# @since 05/11/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA092_PL005(self):
		
		# Dados para o teste
		medVisi = "013500"
		dataPrev = DateSystem
		chave = "M SP    00010022000006012"
			
		self.oHelper.SearchBrowse(f'{chave}', key=4, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Inserir Visita Profissional')
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.ClickGridCell("med. visi.", row=1)
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue("BOZ_CODM", medVisi, name_attr=True)
		self.oHelper.SetValue("BOZ_DATPRE", dataPrev, name_attr=True)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")

		self.oHelper.AssertTrue()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()