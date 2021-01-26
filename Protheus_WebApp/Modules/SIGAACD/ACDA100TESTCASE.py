#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDA100 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 18/09/2019
#@version P12
#
# 	CT001 - Geração de Ordem de Separação por Ordem de Produção
#	CT002 - Geração de Ordem de Separação por Pedido de Venda			
#	CT003 - Geração de Ordem de Separação por Nota Fiscal
#
#	CT004 - Alteração de Ordem de Separação por Ordem de Produção
#	CT005 - Alteração de Ordem de Separação por Pedido de Venda
#	CT006 - Alteração de Ordem de Separação por Nota Fiscal
#
#	CT007 - Estorno de Ordem de Separação por Ordem de Produção
#	CT008 - Estorno de Ordem de Separação por Pedido de Venda
#	CT009 - Estorno de Ordem de Separação por Nota Fiscal
#
#	CT010 - Visualização de ordem de separação
#	CT011 - Visualização das legendas	
#
#   CT013 - Gerando ordem de separaçao para varios pedidos conferindo os clientes de cada pedido	
#   CT014 - Gerando ordem de separaçao para Pedidos de Venda do mesmo Cliente com Loja Diferente
#   CT015 - Incluir Ordem de Separacao e posicionar Browse no registro incluido
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class ACDA100(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('ACDA100')	

	#CT001 - Geração de uma ordem de separação por ordem de produção		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019

	def test_ACDA100_CT001(self):

		#Definição dos perguntes - F12
		self.oHelper.WaitShow("Ordens de separacao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue('Opcao ?', 'Ordem Producao')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		#Definição do operação
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Ok')
		
		#Definição dos perguntes para filtragem

		self.oHelper.SetValue('Separador ?', '')
		self.oHelper.SetValue('Op de ?', '')
		self.oHelper.SetValue('Op ate ?', 'pcpA1P')
		self.oHelper.SetValue('Data emissao de ?', '18/09/2019')
		self.oHelper.SetValue('Data emissao ate ?', '18/09/2019')
		self.oHelper.SetValue('Pre-Separacao ?', 'Sim')
		
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000328")
		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')
		self.oHelper.SetButton('X')
		self.oHelper.Program("ACDA100")

		self.oHelper.AssertTrue()
	
	#CT002 - Geração de uma ordem de separação por pedido de venda		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019

	def test_ACDA100_CT002(self):

		#Definição dos perguntes - F12
		self.oHelper.WaitShow("Ordens de separacao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue('Opcao ?', 'Pedido Venda')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		#Definição do operação
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Ok')
		
		#Definição dos perguntes para filtragem
		
		self.oHelper.SetValue('Pedido de ?', 'pcpA14')
		self.oHelper.SetValue('Pedido ate ?', 'pcpA14')
		self.oHelper.SetValue('Cliente de ?', 'EST001')
		self.oHelper.SetValue('Cliente ate ?', 'EST001')
		self.oHelper.SetValue('Loja cliente ate ?', 'zz')
		self.oHelper.SetValue('Data liberacao de ?', '18/09/2019')
		self.oHelper.SetValue('Data liberacao ate ?', '18/09/2019')
		
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000328")
		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')
		self.oHelper.SetButton('X')
		self.oHelper.Program("ACDA100")

		self.oHelper.AssertTrue()

	#CT003 - Geração de uma ordem de separação por nota fiscal		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019

	def test_ACDA100_CT003(self):

		#Definição dos perguntes - F12
		time.sleep(2)
		self.oHelper.WaitShow("Ordens de separacao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue('Opcao ?', 'Nota Fiscal')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		#Definição do operação
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Ok')
		
		#Definição dos perguntes para filtragem

		self.oHelper.SetValue('Nota de ?', 'FINA4I')
		self.oHelper.SetValue('Serie de ?', '001')
		self.oHelper.SetValue('Nota ate ?', 'FINA4I')
		self.oHelper.SetValue('Serie ate ?', '001')
		self.oHelper.SetValue('Cliente de ?', 'EST001')
		self.oHelper.SetValue('Loja cliente ate ?', '01')
		self.oHelper.SetValue('Cliente ate ?', 'EST001')
		self.oHelper.SetValue('Loja cliente ate ?', '01')
		self.oHelper.SetValue('Data emissao de ?', '18/09/2019')
		self.oHelper.SetValue('Data emissao ate ?', '18/09/2019')
		
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000328")
		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')
		self.oHelper.SetButton('X')
		self.oHelper.Program("ACDA100")

		self.oHelper.AssertTrue()	

	#CT004 - Alteração de uma ordem de separação por ordem de produção		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019
	def test_ACDA100_CT004(self):

		#Definição do operação
		self.oHelper.SearchBrowse("D MG 01 000012")
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('Operador', '000000')
		self.oHelper.SetButton('Salvar')

		self.oHelper.AssertTrue()


	#CT005 - Alteração de uma ordem de separação por pedido de venda		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019
	def test_ACDA100_CT005(self):

		#Definição do operação
		self.oHelper.SearchBrowse("D MG 01 000013")
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('Operador', '000000')
		self.oHelper.SetButton('Salvar')

		self.oHelper.AssertTrue()

	#CT006 - Alteração de uma ordem de separação por nota fiscal		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019
	def test_ACDA100_CT006(self):

		#Definição do operação
		self.oHelper.SearchBrowse("D MG 01 000014")
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('Operador', '000000')
		self.oHelper.SetButton('Salvar')

		self.oHelper.AssertTrue()

	#CT007 - Estorno de uma ordem de separação por ordem de produção	
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019	

	def test_ACDA100_CT007(self):

		self.oHelper.SearchBrowse("D MG 01 000015")
		self.oHelper.SetButton('Outras Ações','Estornar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()		

	#CT008 - Estorno de uma ordem de separação por pedido de venda	
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019	

	def test_ACDA100_CT008(self):

		self.oHelper.SearchBrowse("D MG 01 000016")
		self.oHelper.SetButton('Outras Ações','Estornar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()		

	#CT009 - Estorno de uma ordem de separação por nota fiscal	
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019	

	def test_ACDA100_CT009(self):

		self.oHelper.SearchBrowse("D MG 01 000017")
		self.oHelper.SetButton('Outras Ações','Estornar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()		
					
	#CT010 - Visualização de uma ordem de separação	
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019
 	
	def test_ACDA100_CT010(self):

		self.oHelper.SearchBrowse("D MG 01 000014")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	#CT011 - Legendas dos estados atuais das ordens de separação
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019

	def test_ACDA100_CT011(self):

		#Verificar legenda
		self.oHelper.SetButton('Outras Ações','Legenda')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()	

	#CT012 - Impressão das ordens de separação
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019	

	def test_ACDA100_CT012(self):

		self.oHelper.SetButton('Impressao')
		self.oHelper.SetButton('Param.')

		self.oHelper.SetValue('Ordem de Sep. De ?', '')
		self.oHelper.SetValue('Ordem de Sep. Ate ?', 'ZZZZZZ')
		self.oHelper.SetValue('Data de Emissao De ?', '02/04/2018')
		self.oHelper.SetValue('Data de Emissao Ate ?', '18/09/2019')

		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Sair')
		self.oHelper.AssertTrue()

	#CT013   GTSER-T49123 (1.0) ACDA100 - CT013_TIR - Geração de uma Ordem de Separação para varios Pedidos de Venda com cliente diferentes		
	#@author: Jefferson Silva de Sousa
	#@date: 20/02/2020
	# GTSER-T49123 (1.0)
	def test_ACDA100_CT013(self):

		#Definição dos perguntes - F12
		self.oHelper.WaitShow("Ordens de separacao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue('Opcao ?                       ', 'Pedido Venda')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Aglutina Pedido ?', 'Não')
		self.oHelper.SetValue('Aglutina Armazem ?', 'Não')
		self.oHelper.SetButton('Ok')

		#Definição do operação
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		
		#Definição dos perguntes para filtragem		
		self.oHelper.SetValue('Pedido de ?', 'pcpAAA')
		self.oHelper.SetValue('Pedido ate ?', 'pcpAAC')		
		self.oHelper.SetValue('Cliente de ?', "EST001")
		self.oHelper.SetValue('Cliente ate ?', 'EST003')
		self.oHelper.SetValue('Loja cliente ate ?', 'zz')
		self.oHelper.SetValue('Data liberacao de ?', '21/02/2020')
		self.oHelper.SetValue('Data liberacao ate ?', '21/02/2020')
		
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000728")
		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000729")
		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000730")
		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')

		self.oHelper.SearchBrowse("D MG 01 pcpAAA",key=2,index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("CB7_CLIENT","EST001")		
		self.oHelper.SetButton("Cancelar")		

		self.oHelper.SearchBrowse("D MG 01 pcpAAB",key=2,index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("CB7_CLIENT","EST002")		
		self.oHelper.SetButton("Cancelar")		

		self.oHelper.SearchBrowse("D MG 01 pcpAAC",key=2,index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("CB7_CLIENT","EST003")		
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()


	#CT014   GTSER-T51540 (1.0) ACDA100 - CT014_TIR - Geracao de Ordem de Separacao, Pedido de Venda Aglutina = Sim e Clientes com o mesmo Codigo e Lojas Diferentes
	#@author: Paulo V. Beraldo
	#@date: Jun/2020
	# GTSER-T51540 (1.0)
	def test_ACDA100_CT014(self):

		#Definição dos perguntes - F12
		self.oHelper.WaitShow("Ordens de separacao")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue('Opcao ?                       ', 'Pedido Venda')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Aglutina Pedido ?', 'Sim')
		self.oHelper.SetButton('Ok')

		#Definição do operação
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		
		#Definição dos perguntes para filtragem
		self.oHelper.SetValue('Separador ?', '000003')
		self.oHelper.SetValue('Pedido de ?', 'PCPAGF')	
		self.oHelper.SetValue('Pedido de ?', 'PCPAGF')
		self.oHelper.SetValue('Pedido ate ?', 'PCPAGH')
		self.oHelper.SetValue('Cliente de ?', 'EST100')
		self.oHelper.SetValue('Cliente ate ?', 'EST100')
		self.oHelper.SetValue('Loja cliente ate ?', 'ZZ')
		self.oHelper.SetValue('Data liberacao de ?', '01/06/2020')
		self.oHelper.SetValue('Data liberacao ate ?', '30/06/2020')
		
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", select_all=True )
		
		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')

		self.oHelper.SearchBrowse("D MG 01 PCPAGF",key=2,index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("CB7_PEDIDO","PCPAGF")
		self.oHelper.CheckResult("CB7_CLIENT","EST100")
		self.oHelper.CheckResult("CB7_LOJA"	 ,"01")
		self.oHelper.CheckResult("CB7_TRANSP","FAT003")
		self.oHelper.CheckResult("CB7_COND"	 ,"000")
		self.oHelper.SetButton("Cancelar")
		time.sleep(2)
		self.oHelper.AssertTrue()

	#CT015   GTSER-T55091 (1.0) ACDA100 - CT015_TIR -Incluir Ordem de Separacao e posicionar Browse no registro incluido
	#@author: cris
	#@date: 19/10/2020
	# GTSER-T55091 (1.0)
	def test_ACDA100_CT015(self):

		#Definicao da operacao
		self.oHelper.SetButton('Outras Ações','Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		#Definicao dos perguntes para filtragem
		self.oHelper.SetValue('Separador ?', '')
		self.oHelper.SetValue('Pedido de ?', 'EST066')	
		self.oHelper.SetValue('Pedido ate ?', 'EST066')
		self.oHelper.SetValue('Cliente de ?', "EST006")
		self.oHelper.SetValue('Cliente ate ?', 'EST006')
		self.oHelper.SetValue('Loja cliente ate ?', 'zz')
		self.oHelper.SetValue('Data liberacao de ?', '18/10/2020')
		self.oHelper.SetValue('Data liberacao ate ?', '18/10/2020')
		#self.oHelper.SetValue('Pre-Separacao ?', '2')

		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("Produto", select_all=True )

		self.oHelper.SetButton('Gerar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("CB7_PEDIDO","EST066")
		self.oHelper.SetButton("Cancelar")
		time.sleep(2)
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()