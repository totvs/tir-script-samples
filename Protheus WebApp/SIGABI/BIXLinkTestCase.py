# -*- coding: utf-8 -*-

import unittest

from tir import Webapp


class BIXLINK(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGACFG','11/12/2018','T1','D MG 01 ')
		inst.oHelper.SetLateralMenu('Ambiente > Extrator Bi')

	def test_BIXLINK_CT001(self):
		self.oHelper.SetLateralMenu('Configuração de Parâmetros')
		self.oHelper.SetButton('Avançar >>') # Bem vindo
		
		self.oHelper.SetValue("Servidor DBAccess", "10.171.67.220")
		self.oHelper.SetValue("Porta do Servidor DBAccess", "7920")
		self.oHelper.SetValue("Alias no DBAcess", "STAGE")
		
		self.oHelper.SetButton('Avançar >>') # Configuração de acesso
		self.oHelper.SetButton('Fechar') # Fechar
		self.oHelper.WaitShow("Selecione as áreas utilizadas na configuração dos extratores Protheus.")

		# Seleciona o primeiro indice da coluna
		self.oHelper.ClickGridHeader(column = 1, grid_number = 1)

		self.oHelper.SetButton('Avançar >>') # Definição das Áreas

		self.oHelper.WaitShow("Selecione as Moedas utilizadas nas fatos")
		self.oHelper.SetButton('Avançar >>') # Moedas utilizadas nas fatos

		self.oHelper.WaitShow("Configuração da Macrorregião")
		self.oHelper.SetButton('>>') # Seleciona todos os países
		self.oHelper.SetButton('<<') # Deseleciona todos os países
		self.oHelper.SetButton('Avançar >>') # Configuração de macroregião

		self.oHelper.WaitShow("Consolidação de Moedas")
		self.oHelper.SetButton('Avançar >>') # Consolidação de moedas

		self.oHelper.WaitShow("Caso seja necessário, configure o(s) parâmetro(s) abaixo para adequar a execução dos")
		self.oHelper.ClickLabel("Considerar dados do cliente na dimensão região geográfica?")
		self.oHelper.SetButton('Avançar >>') # Parâmetros Genéricos

		self.oHelper.WaitShow("Área Comercial")
		self.oHelper.ClickLabel("Indica se o representante será obtido através do cadastro do cliente, ao invés dos dados da nota/pedido.")
		self.oHelper.ClickLabel("Devolução de Vendas - Considerar documentos de entrada com cliente diferente do documento de saída.")
		self.oHelper.SetButton('Avançar >>') # Área Comercial 

		self.oHelper.WaitShow("Área Comercial, Financeiro e Materiais.")
		self.oHelper.ClickLabel("Comercial, Financeiro, Materiais - Utilizar a Taxa Negociada na conversão de moeda.")
		self.oHelper.SetButton('Avançar >>') # Área Comercial, Financeiro e Materiais

		self.oHelper.WaitShow("Selecione os itens que serão utilizados como Contas de Resultado.")
		self.oHelper.SetButton('Avançar >>') # Área Controladoria

		self.oHelper.WaitShow("Configuração de Parâmetros da área Controladoria")
		self.oHelper.ClickLabel("Considerar as Contas Bloqueadas no plano de contas?") # Marcar
		self.oHelper.SetButton('Avançar >>') # Considerar as contas bloqueadas

		self.oHelper.WaitShow("Área Materiais")
		self.oHelper.SetButton('Avançar >>') # Área Materiais

		self.oHelper.WaitShow("Área de Produção")
		self.oHelper.SetButton('Avançar >>') # Área Produção
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetValue("Até", "3", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Avançar >>') # Área RH - Tempo de Cargo
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Tempo de Casa
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Faixas etárias
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Faixas salariais

		self.oHelper.WaitShow("Área de DL")
		self.oHelper.SetButton('Avançar >>') # Área de DL

		self.oHelper.WaitShow("Área de Varejo")
		self.oHelper.SetButton('Avançar >>') # Área de Varejo

		self.oHelper.WaitShow("Área CRM")
		self.oHelper.SetButton('Finalizar')
		
		self.oHelper.AssertTrue()

	def test_BIXLINK_CT002(self):
		# Comercial, Materiais, RH e Varejo
		self.oHelper.SetLateralMenu('Configuração de Parâmetros')
		self.oHelper.SetButton('Avançar >>') # Bem vindo
		
		self.oHelper.SetButton('Avançar >>') # Configuração de acesso
		self.oHelper.SetButton('Fechar') # Fechar
		self.oHelper.WaitShow("Selecione as áreas utilizadas na configuração dos extratores Protheus.")
			
		#desmarca as áreas abaixo
		self.oHelper.ClickBox('Descrição da Área', 'Controladoria') #false
		self.oHelper.ClickBox('Descrição da Área', 'Financeiro') #false
		self.oHelper.ClickBox('Descrição da Área', 'Produção') #false
		self.oHelper.ClickBox('Descrição da Área', 'DL') #false
		self.oHelper.ClickBox('Descrição da Área', 'Serviços') #false
		self.oHelper.ClickBox('Descrição da Área', 'CRM')#false
		self.oHelper.ClickBox('Descrição da Área', 'Jurídico')#false
		self.oHelper.SetButton('Avançar >>') # Definição das Áreas

		self.oHelper.WaitShow("Selecione as Moedas utilizadas nas fatos")
		self.oHelper.SetButton('Avançar >>') # Moedas utilizadas nas fatos

		self.oHelper.WaitShow("Configuração da Macrorregião")
		self.oHelper.SetButton('>>') # Seleciona todos os países
		self.oHelper.SetButton('<<') # Deseleciona todos os países
		self.oHelper.SetButton('Avançar >>') # Configuração de macroregião

		self.oHelper.WaitShow("Ao habilitar a opção de consolidação, será necessário informar pelo menos um código de moeda.")		
		self.oHelper.SetButton('Avançar >>') # Consolidação de moedas

		self.oHelper.WaitShow("Caso seja necessário, configure o(s) parâmetro(s) abaixo para adequar a execução dos")
		self.oHelper.SetButton('Avançar >>') # Parâmetros Genéricos

		self.oHelper.WaitShow("Área Comercial")
		self.oHelper.SetButton('Avançar >>') # Área Comercial 

		self.oHelper.WaitShow("Área Comercial, Financeiro e Materiais.")
		self.oHelper.SetButton('Avançar >>') # Área Comercial, Financeiro e Materiais

		self.oHelper.WaitShow("Área Materiais")
		self.oHelper.SetButton('<< Voltar') # Área Materiais para Área Comercial, Financeiro e Materiais
		self.oHelper.WaitShow("Área Comercial, Financeiro e Materiais.")
		self.oHelper.SetButton('Avançar >>') # Área Comercial, Financeiro e Materiais
		self.oHelper.WaitShow("Área Materiais")
		self.oHelper.SetButton('Avançar >>') # Área Materiais
		
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('<< Voltar') # Área RH

		self.oHelper.WaitShow("Área Materiais")
		self.oHelper.SetButton('Avançar >>') # Área Materiais

		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Tempo de Cargo
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Tempo de Casa
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Faixas etárias
		self.oHelper.WaitShow("Informe os dados utilizados pelo extrator para classificar as informações da área de RH.")
		self.oHelper.SetButton('Avançar >>') # Área RH - Faixas salariais

		self.oHelper.WaitShow("Área de Varejo")
		self.oHelper.SetButton('Finalizar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
	
