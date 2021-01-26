#//-------------------------------------------------------------------
#@author PEDRO ANTONIO MISSAGLIA
#@since 26/06/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA105(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATA105')		
	def test_MATA105_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Número','EST010')
		self.oHelper.SetValue('Solicitante','pedro.missaglia')
		self.oHelper.SetValue('Data de Emissäo','04/07/2019')

		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000235", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("Armazem", "01", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Outras Ações', 'Rateio')

		self.oHelper.SetValue("% Rat.", "50,00", grid=True)
		self.oHelper.SetValue("C. de Custo", "ESTSE0001", grid=True)
		self.oHelper.SetValue("C Contabil", "ESTSE000000000000001", grid=True)
		self.oHelper.SetValue("Item Conta", "EST000001", grid=True)
		self.oHelper.SetValue("Classe Valor", "EST000001", grid=True)
		self.oHelper.LoadGrid()	

		self.oHelper.SetKey("DOWN", grid=True)

		self.oHelper.SetValue("% Rat.", "50,00", grid=True)
		self.oHelper.SetValue("C. de Custo", "ESTSE0002", grid=True)
		self.oHelper.SetValue("C Contabil", "ESTSE000000000000001", grid=True)
		self.oHelper.SetValue("Item Conta", "EST000001", grid=True)
		self.oHelper.SetValue("Classe Valor", "EST000001", grid=True)
		self.oHelper.LoadGrid()	
		
		self.oHelper.SetButton('Salvar')
		time.sleep(2)
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MATA105_CT002(self):

		#Visualização		
		self.oHelper.SearchBrowse("D MG 01 EST011 01")
		self.oHelper.SetButton('Visualizar')
		
		self.oHelper.CheckResult('Número','EST011')
		self.oHelper.CheckResult('Solicitante', 'pedro.missaglia')
		self.oHelper.CheckResult('Data de Emissäo','04/07/2019')

		self.oHelper.CheckResult('Produto','ESTSE0000000000000000000000236', grid=True, line=1)
		self.oHelper.CheckResult('Quantidade','1,00', grid=True, line=1)
		self.oHelper.CheckResult('Armazem','01', grid=True, line=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	def test_MATA105_CT003(self):

		#Alteração
		self.oHelper.SearchBrowse("D MG 01 EST012 01")
		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Solicitante','pedro.missaglia')
		self.oHelper.SetValue('Data de Emissäo','04/07/2019')

		self.oHelper.SetButton('Outras Ações', 'Rateio')
		self.oHelper.SetValue("C. de Custo", "ESTSE0001", grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.SetButton('Salvar')

		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000237", grid=True)
		self.oHelper.SetValue("Quantidade", "2,00", grid=True)
		self.oHelper.LoadGrid()		
		
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Outras Ações', 'Rateio')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		
		self.oHelper.AssertTrue()	

	def test_MATA105_CT004(self):

		#Legenda
		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_MATA105_CT005(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('OK')
		
		self.oHelper.SetButton('Outras Ações', '1o.Nivel')	
		
		time.sleep(5)
		self.oHelper.SetKey('F3')		
		time.sleep(5)
		
		self.oHelper.SearchBrowse("pcpA2101001")
		self.oHelper.SetButton('OK')
		self.oHelper.SetKey('DOWN')
		self.oHelper.SetButton('OK')

		#Verificando resultados
		self.oHelper.CheckResult('Produto','ESTSE0000000000000000000000352', grid=True, line=1)
		self.oHelper.CheckResult('Produto','ESTSE0000000000000000000000353', grid=True, line=2)
		self.oHelper.LoadGrid()		
		self.oHelper.SetButton("Salvar")
		time.sleep(3)
		self.oHelper.SetButton("Cancelar")
		
		self.oHelper.AssertTrue()

	def test_MATA105_CT006(self):
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Número','EST035')		
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000565", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("Armazem", "01", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Sim')
		time.sleep(4)
		self.oHelper.SetButton('Cancelar')
		time.sleep(4)	
		self.oHelper.SearchBrowse(f"D MG 01 ESTSE0000000000000000000000565EST03501", "Filial+produto + Nr.s.a. + Item S.a.")      
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
	
	def test_MATA105_CT007(self):

		# Funcao Copia
		self.oHelper.SearchBrowse(f"D MG 01 EST020", "Filial+nr.s.a.")

		self.oHelper.SetButton('Outras Ações','Copia')
		
		self.oHelper.SetValue('Número','EST061')		
		self.oHelper.SetValue("Produto", "ESTSE0001000000000000000000T21", grid=True)
		self.oHelper.SetValue("Quantidade", "5,00", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SearchBrowse(f"D MG 01 EST061", "Filial+nr.s.a.")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_MATA105_CT008(self):

		# Inclusao de Conhecimento/Impressao/Exclusao
		self.oHelper.SearchBrowse(f"D MG 01 EST062", "Filial+nr.s.a.")

		# Conhecimento
		self.oHelper.SetButton('Outras Ações','Conhecimento')
				
		self.oHelper.SetValue("AC9_OBJETO", "0000000046", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		# Impressao
		self.oHelper.SearchBrowse(f"D MG 01 EST062", "Filial+nr.s.a.")
		self.oHelper.SetButton('Outras Ações','IMprimir')
		self.oHelper.SetButton('Imprimir')
		#self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Sair')

		# Exclusao
		self.oHelper.SearchBrowse(f"D MG 01 EST062", "Filial+nr.s.a.")
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
	
	def test_MATA105_CT009(self):

		# Solicitacao com Rateio - Inclusao/Exclusao

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Número','EST063')		
		self.oHelper.SetValue("Produto", "ESTSE0003000000000000000000T21", grid=True)
		self.oHelper.SetValue("Quantidade", "10,00", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Outras Ações','Rateio')
		self.oHelper.SetValue('GS_PERC','50,00', grid=True)
		self.oHelper.SetValue('GS_CC','00001', grid=True)
		self.oHelper.SetValue('GS_CONTA','001', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetKey("DOWN", grid=True)

		self.oHelper.SetValue('GS_PERC','50,00', grid=True)
		self.oHelper.SetValue('GS_CC','002', grid=True)
		self.oHelper.SetValue('GS_CONTA','001', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse(f"D MG 01 EST063", "Filial+nr.s.a.")

		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_MATA105_CT010(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Número','ESTAAZ')
		self.oHelper.SetValue('Solicitante','beraldo')
		self.oHelper.SetValue('Data de Emissäo','21/06/2019')

		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000235", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("Armazem", "01", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetKey("DOWN", grid=True)
		time.sleep(2)

		self.oHelper.SetButton('Cancelar')

		time.sleep(2)

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Número','ESTAB0')
		self.oHelper.SetValue('Solicitante','beraldo')		
		
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000235", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("Armazem", "01", grid=True)		
		self.oHelper.LoadGrid()		
		time.sleep(2)
		
		self.oHelper.SetButton('Salvar')
		time.sleep(2)
		self.oHelper.SetButton('Cancelar')
		time.sleep(2)

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()