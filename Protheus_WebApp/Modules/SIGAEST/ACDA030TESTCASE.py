from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDA030 - Mestre de Inventario
#
#@author ADRIANO VIEIRA
#@since 17/10/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class ACDA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''
		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializacao
		inst.oHelper.Setup("SIGAEST","17/10/2019","T1","D MG 01 ","04")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("ACDA030")

	def test_ACDA030_001(self):
		
		#TIR001 - Inclusao simples de Mestre com Produto
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.AddParameter("MV_INTACD", "D MG 01", "1", "1", "1")
		self.oHelper.AddParameter("MV_CBPE012", "D MG 01", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Incluir")

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("Data", "17/10/2019")
		self.oHelper.SetValue("Contagens", "1")
		self.oHelper.SetValue("Almoxarifado", "01")
		self.oHelper.SetValue("Tipo", "1 - Produto")
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000002349")
		
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	
	def test_ACDA030_002(self):
		
		#TIR002 - Alteracao simples de Mestre
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000008",  key="Filial+cod.invent.")

		self.oHelper.SetButton("Alterar")

		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000006349")
		self.oHelper.SetValue("Classe A", "1 - Sim")
		self.oHelper.SetValue("Classe B", "1 - Sim")
		self.oHelper.SetValue("Classe C", "1 - Sim")
		
		self.oHelper.SetButton("Salvar")

		self.oHelper.AssertTrue()
	
	def test_ACDA030_003(self):
		
		#TIR003 - Inclusao simples de Mestre com Endereco
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SetButton("Incluir")

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("Data", "17/10/2019")
		self.oHelper.SetValue("Contagens", "1")
		self.oHelper.SetValue("Almoxarifado", "01")
		self.oHelper.SetValue("Tipo", "2 - Endereco")
		self.oHelper.SetValue("Endereco", "EST001")
		self.oHelper.SetValue("Classe A", "1 - Sim")
		self.oHelper.SetValue("Classe B", "1 - Sim")
		self.oHelper.SetValue("Classe C", "1 - Sim")
		
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	def test_ACDA030_004(self):
		
		#TIR004 - Visualizacao de Mestre
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000009",  key="Filial+cod.invent.")

		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
	
	def test_ACDA030_005(self):
		
		#TIR005 - Exclusão simples de Mestre
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse(f"D MG 01 000000010", "Filial+cod.invent.")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
		
	def test_ACDA030_006(self):
		
		#TIR006 - Relatorio - Legenda - Monitor - 
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000007",  key="Filial+cod.invent.")

		self.oHelper.SetButton('Outras Ações','Relatorio')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Sair')
		self.oHelper.SetButton('Outras Ações','Legenda')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse("D MG 01 000000001",  key="Filial+cod.invent.")  
		self.oHelper.SetButton('Outras Ações','Monitor')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_ACDA030_007(self):
		
		#TIR007 - Automatico 
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000007",  key="Filial+cod.invent.")

		self.oHelper.SetButton('Outras Ações','Automatico')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('OK')
		self.oHelper.WaitShow('O numero de contagens nao pode ser igual ou inferior a zero, favor verificar !!!')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()
	
	def test_ACDA030_008(self):
		
		#TIR008 - Exclusão de Mestre - Status "Em Andamento"
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse(f"D MG 01 000000011", "Filial+cod.invent.")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
	
	def test_ACDA030_009(self):
		
		#TIR009 - Exclusão de Mestre - Status "Finalizado"
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000012")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Sim')
		#self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
	
	def test_ACDA030_010(self):
		
		#TIR010 - Exclusão de Mestre -  Inventário Não Finalizado
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000013")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.WaitShow('Nao e permitida a exclusao de Mestres de Inventario com contagens em andamento!!!')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()
	
	def test_ACDA030_011(self):
		
		#TIR011 - Exclusão de Mestre -  Analise "Divergente"
		#@author: ADRIANO VIEIRA
		#@date: 17/10/2019	

		self.oHelper.SearchBrowse("D MG 01 000000014")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_ACDA030_012(self):

        #TIR012 - Execução do acerto de inventário e tentativa de exclusão
		#@author: GABRIEL OLIVEIRA
		#@date: 17/10/2019

		self.oHelper.SearchBrowse("D MG 01 000000020")
		self.oHelper.SetButton("Outras Ações","Monitor")
		self.oHelper.SetValue("Atualiza Browse ?", "Não")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Outras Ações","Executa Acerto de Inventario")
		self.oHelper.SetButton("Sim")
		
        #Validações após execução do acerto de inventário
		self.oHelper.SearchBrowse("D MG 01 000000020")
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	def test_ACDA030_013(self):

        #TIR013 - GTSER-T51407 - Registros de Inventário no Monitor do ACD exibindo somente produtos relacionados

		#@author: carlos.capeli
		#@date: 27/05/2020

		self.oHelper.SearchBrowse("D MG 01 000000024")
		self.oHelper.SetButton("Outras Ações","Monitor")
		self.oHelper.SetButton("OK")
		self.oHelper.ClickFolder("Registros de Inventario")
		self.oHelper.CheckResult("Produto","ACDACDA03000000000000000000001",grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()