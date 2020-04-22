from tir import Webapp
import unittest
import time

class FINA171(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''

		#Endereco do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializacao
		inst.oHelper.Setup('SIGAFIN','12/09/2019','T1','D MG 01 ','06')

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("FINA171")

	### CT006
	### Inclusão e Exclusão de Aplicação CDB
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44171
	def test_FINA171_CT006(self):
		'''
		Test Case 006
		'''
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('Numero','FITIR1')
		self.oHelper.SetValue('Modelo',"A")
		self.oHelper.SetValue('Operacao',"CDB")
		self.oHelper.SetValue('Banco',"033")
		self.oHelper.SetValue('Agencia', '00001')
		self.oHelper.SetValue('Conta Banco', '0000000004')
		self.oHelper.SetValue('Vlr.Operacao', '1000,00')
		self.oHelper.SetValue('Moeda', '1')

		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult('EH_NUMERO','FITIR1')
		self.oHelper.CheckResult('EH_APLEMP','APL')
		self.oHelper.CheckResult('EH_TIPO','CDB')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','1000,00')

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 FITIR101")
		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.CheckResult('EH_NUMERO','FITIR1')
		self.oHelper.CheckResult('EH_APLEMP','APL')
		self.oHelper.CheckResult('EH_TIPO','CDB')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','1000,00')

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	### CT007
	### Inclusão e Exclusão de um empréstimo CDI
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44176
	def test_FINA171_CT007(self):
		'''
		Test Case 007
		'''
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('Numero','FITIR2')	
		self.oHelper.SetValue('Modelo',"E")
		self.oHelper.SetValue('Operacao',"CDI")
		self.oHelper.SetValue('Banco',"033")
		self.oHelper.SetValue('Agencia', '00001')
		self.oHelper.SetValue('Conta Banco', '0000000004')
		self.oHelper.SetValue('Vlr.Operacao', '3555,66')
		self.oHelper.SetValue('Moeda', '1')

		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult('EH_NUMERO','FITIR2')
		self.oHelper.CheckResult('EH_APLEMP','EMP')
		self.oHelper.CheckResult('EH_TIPO','CDI')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','3555,66')

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 FITIR201")
		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.CheckResult('EH_NUMERO','FITIR2')
		self.oHelper.CheckResult('EH_APLEMP','EMP')
		self.oHelper.CheckResult('EH_TIPO','CDI')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','3555,66')

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	### CT008
	### Inclusão e Exclusão de Aplicação FAF com contrato de cotas.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44179
	def test_FINA171_CT008(self):
		'''
		Test Case 008
		'''
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('Numero','FITIR3')
		self.oHelper.SetValue('Modelo',"A")
		self.oHelper.SetValue('Operacao',"FAF")
		self.oHelper.SetValue('Banco',"033")
		self.oHelper.SetValue('Agencia', '00001')
		self.oHelper.SetValue('Conta Banco', '0000000004')
		self.oHelper.SetValue('Qtd.Cota/Tit', '133439,07341000')
		self.oHelper.SetValue('Numero Contr', 'CTR000000000002')
		self.oHelper.SetValue('Moeda', '1')

		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult('EH_NUMERO','FITIR3')
		self.oHelper.CheckResult('EH_APLEMP','APL')
		self.oHelper.CheckResult('EH_TIPO','FAF')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_QUOTAS','133439,07341')
		self.oHelper.CheckResult('EH_CONTRAT','CTR000000000002')
		self.oHelper.CheckResult('EH_VALOR','448031,43')

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 FITIR301")
		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.CheckResult('EH_NUMERO','FITIR3')
		self.oHelper.CheckResult('EH_APLEMP','APL')
		self.oHelper.CheckResult('EH_TIPO','FAF')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_QUOTAS','133439,07341')
		self.oHelper.CheckResult('EH_CONTRAT','CTR000000000002')
		self.oHelper.CheckResult('EH_VALOR','448031,43')

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	### CT009
	### Inclusão e Exclusão de Empréstimo gerando 2 parcelas.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44183
	def test_FINA171_CT009(self):
		'''
		Test Case 009
		'''
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('Numero','FITIR4')
		self.oHelper.SetValue('Modelo',"E")
		self.oHelper.SetValue('Operacao',"EMP")
		self.oHelper.SetValue('Banco',"033")
		self.oHelper.SetValue('Agencia', '00001')
		self.oHelper.SetValue('Conta Banco', '0000000004')
		self.oHelper.SetValue('Vlr.Operacao', '10000,00')
		self.oHelper.SetValue('Moeda', '1')
		self.oHelper.SetValue('Gera Parcela', '1')
		self.oHelper.SetValue('Prazo', '2')
		self.oHelper.SetValue('Amortização', '1')

		self.oHelper.SetButton("Salvar")
		
		self.oHelper.SetButton("Outras Ações", "Definir Fornecedor")

		self.oHelper.F3('Fornecedor ? ')
		self.oHelper.SearchBrowse(f'COM011', 'Código')		
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Confirmar")

		self.oHelper.WaitShow("Aguarde, gravando as parcelas no contas a pagar...")

		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult('EH_NUMERO','FITIR4')
		self.oHelper.CheckResult('EH_APLEMP','EMP')
		self.oHelper.CheckResult('EH_TIPO','EMP')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','10000,00')
		self.oHelper.CheckResult('EH_AMORTIZ','1')

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 FITIR401")
		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.CheckResult('EH_NUMERO','FITIR4')
		self.oHelper.CheckResult('EH_APLEMP','EMP')
		self.oHelper.CheckResult('EH_TIPO','EMP')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','10000,00')
		self.oHelper.CheckResult('EH_AMORTIZ','1')

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	### CT010
	### Inclusão e Exclusão de Empréstimo com carência gerando 4 parcelas.
	### TestCase: https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T44184
	def test_FINA171_CT010(self):
		'''
		Test Case 010
		'''
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('Numero','FITIR5')
		self.oHelper.SetValue('Modelo',"E")
		self.oHelper.SetValue('Operacao',"EMP")
		self.oHelper.SetValue('Banco',"033")
		self.oHelper.SetValue('Agencia', '00001')
		self.oHelper.SetValue('Conta Banco', '0000000004')
		self.oHelper.SetValue('Vlr.Operacao', '15000,00')
		self.oHelper.SetValue('Moeda', '1')
		self.oHelper.SetValue('Gera Parcela', '1')
		self.oHelper.SetValue('Prazo', '4')
		self.oHelper.SetValue('Amortização', '2')
		self.oHelper.SetValue('Carencia', '1')

		self.oHelper.SetButton("Salvar")
		
		self.oHelper.SetButton("Outras Ações", "Definir Fornecedor")

		self.oHelper.F3('Fornecedor ? ')
		self.oHelper.SearchBrowse(f'COM000', 'Código')		
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Confirmar")

		self.oHelper.WaitShow("Aguarde, gravando as parcelas no contas a pagar...")

		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult('EH_NUMERO','FITIR5')
		self.oHelper.CheckResult('EH_APLEMP','EMP')
		self.oHelper.CheckResult('EH_TIPO','EMP')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','15000,00')
		self.oHelper.CheckResult('EH_AMORTIZ','2')
		self.oHelper.CheckResult('EH_CARENCI','1')
		self.oHelper.AssertTrue()

		self.oHelper.SetButton("Cancelar")

		self.oHelper.SearchBrowse(f"D MG 01 FITIR501")
		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.CheckResult('EH_NUMERO','FITIR5')
		self.oHelper.CheckResult('EH_APLEMP','EMP')
		self.oHelper.CheckResult('EH_TIPO','EMP')
		self.oHelper.CheckResult('EH_BANCO','033')
		self.oHelper.CheckResult('EH_AGENCIA','00001')
		self.oHelper.CheckResult('EH_CONTA','0000000004')
		self.oHelper.CheckResult('EH_VALOR','15000,00')
		self.oHelper.CheckResult('EH_AMORTIZ','2')
		self.oHelper.CheckResult('EH_CARENCI','1')

		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()