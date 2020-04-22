#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA270
#
#@author carlos.capeli
#@since 24/10/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA270(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","24/10/2019","T1","D MG 01")
		inst.oHelper.Program("MATA270")

	# Inclusão de registro de inventário - GTSER-T45412
	def test_MAT270_001(self):

		self.oHelper.AddParameter("MV_CONTINV", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SetValue("Valida Existencia do Produto ?","Sim")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Codigo")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Produto")
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")
		self.oHelper.SetValue("Contagem ?","1")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("Produto","ESTMATA270TIR00000000000000000")
		self.oHelper.SetValue("Armazem","01")
		self.oHelper.SetValue("Tp Material","PA")
		self.oHelper.SetValue("Documento","000000003")
		self.oHelper.SetValue("Quantidade","10,00")
		self.oHelper.SetValue("Contagem","3")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		time.sleep(5)
		self.oHelper.AssertTrue()

	# Visualização de registro de inventário - GTSER-T45413
	def test_MAT270_002(self):		
		#self.oHelper.SearchBrowse("D MG 01 000000003ESTMATA270TIR0000000000000000001", "Filial+documento + Produto + Ar...")
		self.oHelper.SearchBrowse("D MG 01 000000003ESTMATA270TIR0000000000000000001", key=3,index=True)
		time.sleep(5)
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('Produto','ESTMATA270TIR00000000000000000')
		self.oHelper.SetButton('Cancelar')
		time.sleep(5)
		self.oHelper.AssertTrue()

	# Inclusão de registro de inventário com controle de lote, endereço e número de série - GTSER-T45414
	def test_MAT270_003(self):
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valida Existencia do Produto ?","Sim")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Endereco")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Produto")
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")
		self.oHelper.SetValue("Contagem ?","1")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("Produto","ESTMATA270TIR00000000000000001")
		self.oHelper.SetValue("Armazem","01")
		self.oHelper.SetValue("Tp Material","PA")
		self.oHelper.SetValue("Documento","000000003")
		self.oHelper.SetValue("Quantidade","1,00")
		self.oHelper.SetValue("Lote","0000000001")
		self.oHelper.SetValue("Endereco","ESTMATA27000000")
		self.oHelper.SetValue("Num de Serie","ABC1234567")
		self.oHelper.SetValue("B7_CONTAGE","3")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		time.sleep(5)
		self.oHelper.AssertTrue()

	# Seleção automática de registro de inventário com controle de lote, endereço e número de série - GTSER-T45416
	def test_MAT270_004(self):
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valida Existencia do Produto ?","Sim")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Codigo")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Produto")
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")
		self.oHelper.SetValue("Contagem ?","1")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 000000001ESTMATA270TIR0000000000000000101",key=3,index=True)
		self.oHelper.SetButton("Outras Ações", "Sel Autom")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		time.sleep(5)
		self.oHelper.AssertTrue()

	# Seleção de registro de inventário por contagem e por produto - GTSER-T45417
	def test_MAT270_005(self):
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valida Existencia do Produto ?","Sim")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Codigo")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Produto")
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")
		self.oHelper.SetValue("Contagem ?","1")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 000000001ESTMATA270TIR0000000000000000001",key=3,index=True)
		self.oHelper.SetButton("Outras Ações", "Sel Contagem")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Seleciona")
		time.sleep(5)
		self.oHelper.AssertTrue()

	# Seleção de registro de inventário por contagem e por Data/Contagem - GTSER-T45418
	def test_MAT270_006(self):
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valida Existencia do Produto ?","Sim")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Codigo")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Data/Contagem")
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")
		self.oHelper.SetValue("Contagem ?","4")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 000000004ESTMATA270TIR0000000000000000001",key=3,index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult('Produto','ESTMATA270TIR00000000000000000')
		self.oHelper.CheckResult('B7_CONTAGE','004')		
		self.oHelper.SetButton("Cancelar")		
		time.sleep(5)
		self.oHelper.AssertTrue()
	
	def test_MAT270_007(self):
	
		self.oHelper.AddParameter("MV_CONTINV", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valida Existencia do Produto ?","Nao")
		self.oHelper.SetValue("Sugere inform. inventario ?","Por Codigo")
		self.oHelper.SetValue("Data p/ opcao sel. autom. ?","24/10/2019")
		self.oHelper.SetValue("Selecionar contagem por ?","Data/Contagem")		
		self.oHelper.SetValue("Data da contagem ?","24/10/2019")		
		self.oHelper.SetValue("Contagem ?","1")
		self.oHelper.SetButton("Ok")

		self.oHelper.SearchBrowse("D MG 01 ESTSE0001ESTSE000000000000000000000036401", key=3,index=True)		
		self.oHelper.ClickGridCell("Produto", 2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Outras Ações", "Sel Autom")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		time.sleep(5)
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()