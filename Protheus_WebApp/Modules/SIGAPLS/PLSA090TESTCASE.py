import unittest
import time
from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class PLSA090(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS", DateSystem, "T1", "M SP 01 ", "33")
		inst.oHelper.Program("PLSA094A")
		inst.oHelper.AddParameter("MV_PLEVSAD", "", "1", "1", "1") # Habilita Evolução SADT
		inst.oHelper.AddParameter("MV_PLSSOOL", "", "1", "1", "1") # Habilita Auto. On-Line
		inst.oHelper.AddParameter("MV_PLCALPG", "", "2", "2", "2") # Novo Calendario de Pagamento
		inst.oHelper.SetParameters()
				
	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA090_PL001

	# Teste 01 - Consulta Autorizada
	
	# @author vinicius.queiros
	# @since 02/10/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA090_PL001(self):
		
		# Dados para o teste
		matricula = "00019875000001038"
		rda = "000004"
		cid = "Z000"
		solicitante = "013500"
		tiposaida = "1 - Retorno"
		TipoAtendimento = "04 - Consulta"
		procedimento = "10101012"
		status = "1 - Autorizada"

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue('BE1_USUARI', matricula)
		self.oHelper.SetValue('BE1_CODRDA', rda)
		self.oHelper.SetValue('BE1_CID', cid)
		self.oHelper.SetValue('BE1_REGSOL', solicitante)
		self.oHelper.SetValue('BE1_TIPSAI', tiposaida)
		self.oHelper.SetValue('BE1_TIPATE', TipoAtendimento)
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue('BE2_CODPRO', procedimento)
		self.oHelper.CheckResult("BE2_STATUS", status)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')     
		self.oHelper.AssertTrue()
	
	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA090_PL002

	# Teste 02 - SADT Autorizada
	
	# @author vinicius.queiros
	# @since 02/10/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA090_PL002(self):
		
		# Dados para o teste
		matricula = "00019875000001038"
		rda = "000004"
		cid = "Z000"
		solicitante = "013500"
		tiposaida = "2 - Retorno com SADT"
		TipoAtendimento = "05 - Exame"
		procedimento = "40304361"
		status = "1 - Autorizada"

		self.oHelper.SetValue('BE1_USUARI', matricula)
		self.oHelper.SetValue('BE1_CODRDA', rda)
		self.oHelper.SetValue('BE1_CID', cid)
		self.oHelper.SetValue('BE1_REGSOL', solicitante)
		self.oHelper.SetValue('BE1_TIPSAI', tiposaida)
		self.oHelper.SetValue('BE1_TIPATE', TipoAtendimento)
		self.oHelper.ClickGridCell("Cd. Proc.")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue('BE2_CODPRO', procedimento)
		self.oHelper.CheckResult("BE2_STATUS", status)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')       
		self.oHelper.AssertTrue()

	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA090_PL003

	# Teste 03 - Complemento SADT - Autorizada
	
	# @author vinicius.queiros
	# @since 02/10/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA090_PL003(self):
		
		# Dados para o teste
		procedimento = "40303136"
		status = "1 - Autorizada"
		responsavel = "Responsavel Teste 03"
		chave = "M SP    000120201000000001"
			
		self.oHelper.SearchBrowse(f'{chave}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Evolução Sadt')
		self.oHelper.ClickFolder("Complem. SADT")
		self.oHelper.ClickGridCell("Cd Proc Prin")
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.SetValue('BQV_CODPRO', procedimento)
		self.oHelper.SetValue('BQV_RESAUT', responsavel)
		self.oHelper.CheckResult("BQV_STATUS", status)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Confirmar')    
		self.oHelper.AssertTrue()

	#//------------------------------------------------------------------- 
	# {Protheus.doc} test_PLSA090_PL004

	# Teste 04 - Exclusão - Consulta
	
	# @author vinicius.queiros
	# @since 02/10/2020
	# @version 12
	# @see 
	#//------------------------------------------------------------------- 
	def test_PLSA090_PL004(self):
		
		# Dados para o teste
		chave = "M SP    000120201000000002"
			
		self.oHelper.SearchBrowse(f'{chave}', key=1, index=True)
		self.oHelper.SetButton('Outras Ações',sub_item='Excluir')
		self.oHelper.SetButton('Confirmar')    
		self.oHelper.AssertTrue()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()