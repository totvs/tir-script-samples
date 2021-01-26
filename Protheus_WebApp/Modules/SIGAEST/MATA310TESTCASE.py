#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA310 - 

#@author hebert.santos
#@since 23/10/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA310(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','','T1','D MG 01','04')
		inst.oHelper.Program('MATA310')

	def test_MATA310_001(self):

		self.oHelper.SetValue('De  produto ? ','ESTSE0000000000000000000000354')
		self.oHelper.SetValue('Ate produto ?','ESTSE0000000000000000000000354')
		self.oHelper.SetValue('Ate filial ?','D RJ 01')
		self.oHelper.SetValue('Ate armazem ?','02')
		self.oHelper.SetValue('Ate tipo ?','ZZ')
		self.oHelper.SetValue('Ate grupo ?','9999')
		self.oHelper.SetValue('Filtra produtos por categ. ?  ', 'Nao')
		self.oHelper.SetValue('Quebra informacoes ?','Por armazem')
		self.oHelper.SetValue('TES para notas de saida ?','549')
		self.oHelper.SetValue('Gera documento de entrada ?','Classificado')
		self.oHelper.SetValue('TES para notas de entrada ?','400')
		self.oHelper.SetValue('Condicao de pagamento ?','101')
		self.oHelper.SetValue('Considera como preco no PV ?','Tabela de Preco')
		self.oHelper.SetValue('Dados da origem ?','Todas filiais')
		self.oHelper.SetValue('Utilizar Saldo de Terceiros ?','Nao')
		self.oHelper.SetValue('Espécie documento de entrada ?','NF')
		self.oHelper.SetValue('Descrição de produtos ?','Não')
		self.oHelper.SetValue('Informa prod. manualmente ?','Não')
		self.oHelper.SetValue('Abre tela da nota de entrada ?','Não')
		self.oHelper.SetButton('OK')
		
		self.oHelper.ClickTree('Filial D MG 01  Filial BELO HOR > Armazem 01 > ESTSE0000000000000000000000354 -               100,00')
		
		self.oHelper.ClickTree('Filial D RJ 01  Filial RIO DE J', position=2)
		self.oHelper.ClickTree('Armazem 01 > ESTSE0000000000000000000000354 -                 0,00', position=0)

		self.oHelper.SetButton('Outras Ações', 'Relacao')

		self.oHelper.SetValue('Lote','LOTE01')
		self.oHelper.SetValue('Endereço','ENDSE01')
		self.oHelper.SetValue('Quantidade','10,00')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('OK')
		time.sleep(50)
		self.oHelper.Program('MATA310')

		self.oHelper.AssertTrue()
		
	def test_MATA310_002(self):

		self.oHelper.SetValue('De  produto ? ','ESTSE0000000000000000000000363')
		self.oHelper.SetValue('Ate produto ?','ESTSE0000000000000000000000363')
		self.oHelper.SetValue('Ate filial ?','D RJ 01')
		self.oHelper.SetValue('Ate armazem ?','02')
		self.oHelper.SetValue('Ate tipo ?','ZZ')
		self.oHelper.SetValue('Ate grupo ?','9999')
		self.oHelper.SetValue('Filtra produtos por categ. ?  ', 'Nao')
		self.oHelper.SetValue('Quebra informacoes ?','Por armazem')
		self.oHelper.SetValue('TES para notas de saida ?','549')
		self.oHelper.SetValue('Gera documento de entrada ?','Classificado')
		self.oHelper.SetValue('TES para notas de entrada ?','400')
		self.oHelper.SetValue('Condicao de pagamento ?','101')
		self.oHelper.SetValue('Considera como preco no PV ?','Tabela de Preco')
		self.oHelper.SetValue('Dados da origem ?','Todas filiais')
		self.oHelper.SetValue('Utilizar Saldo de Terceiros ?','Nao')
		self.oHelper.SetValue('Espécie documento de entrada ?','NF')
		self.oHelper.SetValue('Descrição de produtos ?','Não')
		self.oHelper.SetValue('Informa prod. manualmente ?','Não')
		self.oHelper.SetValue('Abre tela da nota de entrada ?','Não')
		self.oHelper.SetButton('OK')

		self.oHelper.ClickTree('Filial D MG 01  Filial BELO HOR > Armazem 01 > ESTSE0000000000000000000000363 -               100,00')
		self.oHelper.ClickTree('Filial D RJ 01  Filial RIO DE J', position=2)
		self.oHelper.ClickTree('Armazem 01 > ESTSE0000000000000000000000363 -                 0,00', position=0)

		self.oHelper.SetButton('Outras Ações', 'Relacao')

		self.oHelper.SetValue('Lote', 'LOTE01')
		self.oHelper.SetValue('Endereço', 'ENDSE01')
		self.oHelper.SetValue('Quantidade', '10,00')
		self.oHelper.SetButton('Confirmar')
		time.sleep(10)

		self.oHelper.SetButton('Outras Ações', 'Estorno')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.Program('MATA310')

		self.oHelper.AssertTrue()

	def test_MATA310_003(self):

		self.oHelper.SetValue('De  produto ? ', 'ESTSE0000000000000000000000363')
		self.oHelper.SetValue('Ate produto ?','ESTSE0000000000000000000000363')
		self.oHelper.SetValue('Ate filial ?','D RJ 01')
		self.oHelper.SetValue('Ate armazem ?','02')
		self.oHelper.SetValue('Ate tipo ?','ZZ')
		self.oHelper.SetValue('Ate grupo ?','9999')
		self.oHelper.SetValue('Filtra produtos por categ. ?  ', 'Nao')
		self.oHelper.SetValue('Quebra informacoes ?','Por armazem')
		self.oHelper.SetValue('TES para notas de saida ?','549')
		self.oHelper.SetValue('Gera documento de entrada ?','Classificado')
		self.oHelper.SetValue('TES para notas de entrada ?','400')
		self.oHelper.SetValue('Condicao de pagamento ?','101')
		self.oHelper.SetValue('Considera como preco no PV ?','Tabela de Preco')
		self.oHelper.SetValue('Dados da origem ?','Todas filiais')
		self.oHelper.SetValue('Utilizar Saldo de Terceiros ?','Nao')
		self.oHelper.SetValue('Espécie documento de entrada ?','NF')
		self.oHelper.SetValue('Descrição de produtos ?','Não')
		self.oHelper.SetValue('Informa prod. manualmente ?','Não')
		self.oHelper.SetValue('Abre tela da nota de entrada ?','Não')
		self.oHelper.SetButton('OK')

		self.oHelper.ClickTree('Filial D MG 01  Filial BELO HOR > Armazem 01 > ESTSE0000000000000000000000363 -               100,00')
		self.oHelper.ClickTree('Filial D RJ 01  Filial RIO DE J', position=2)
		self.oHelper.ClickTree('Armazem 01 > ESTSE0000000000000000000000363 -                 0,00', position=0)

		self.oHelper.SetButton('Outras Ações', 'Relacao')

		self.oHelper.SetValue('Lote', 'LOTE01')
		self.oHelper.SetValue('Endereço', 'ENDSE01')
		self.oHelper.SetValue('Quantidade', '10,00')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Outras Ações', 'Itens')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Outras Ações', 'Pesquisar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()
		self.oHelper.Finish()

	def test_MATA310_004(self):		
		if self.oHelper.GetRelease() >= '12.1.030':
			self.oHelper.AddParameter("MV_TRFVLDP", "","2","2","2")
			self.oHelper.SetParameters()	
					
			self.oHelper.SetValue('De  produto ? ', 'ESTSE0000000000000000000000962')
			self.oHelper.SetValue('Ate produto ?','ESTSE000000000000964')
			self.oHelper.SetValue('Ate filial ?','D RJ 01')
			self.oHelper.SetValue('Ate armazem ?','02')
			self.oHelper.SetValue('Ate tipo ?','ZZ')
			self.oHelper.SetValue('De  grupo ?','TRF')
			self.oHelper.SetValue('Ate grupo ?','TRF')
			self.oHelper.SetValue('Filtra produtos por categ. ?  ', 'Nao')
			self.oHelper.SetValue('Quebra informacoes ?','Por armazem')
			self.oHelper.SetValue('TES para notas de saida ?','549')
			self.oHelper.SetValue('Gera documento de entrada ?','Classificado')
			self.oHelper.SetValue('TES para notas de entrada ?','400')
			self.oHelper.SetValue('Condicao de pagamento ?','101')
			self.oHelper.SetValue('Considera como preco no PV ?','C Unitario')
			self.oHelper.SetValue('Dados da origem ?','Todas filiais')
			self.oHelper.SetValue('Utilizar Saldo de Terceiros ?','Nao')
			self.oHelper.SetValue('Espécie documento de entrada ?','NF')
			self.oHelper.SetValue('Descrição de produtos ?','Não')
			self.oHelper.SetValue('Informa prod. manualmente ?','Não')
			self.oHelper.SetValue('Abre tela da nota de entrada ?','Não')
			self.oHelper.SetButton('OK')

			self.oHelper.ClickTree('Filial D MG 01  Filial BELO HOR > Armazem 01 > ESTSE000000000000964 -            10.000,00')
			self.oHelper.ClickTree('Filial D RJ 01  Filial RIO DE J', position=2)
			self.oHelper.ClickTree('Armazem 01 > ESTSE0000000000000000000000964 -                 0,00', position=0)

			self.oHelper.SetButton('Outras Ações', 'Relacao')

			self.oHelper.SetValue('Quantidade', '100,00')
			self.oHelper.SetButton('Confirmar')
			self.oHelper.SetButton('Confirmar')

			self.oHelper.SetButton('Ok')
			self.oHelper.SetButton('OK')
			time.sleep(50)
			self.oHelper.Program('MATA310')		
		self.oHelper.AssertTrue()
		self.oHelper.Finish()
	def test_MATA310_005(self):
		if self.oHelper.GetRelease() >= '12.1.030':			
			self.oHelper.AddParameter("MV_TRFVLDP", "","3","3","3")
			self.oHelper.SetParameters()

			self.oHelper.SetValue('De  produto ? ', 'ESTSE0000000000000000000000962')
			self.oHelper.SetValue('Ate produto ?','ESTSE0000000000000000000000963')
			self.oHelper.SetValue('Ate filial ?','D RJ 01')
			self.oHelper.SetValue('Ate armazem ?','02')
			self.oHelper.SetValue('Ate tipo ?','ZZ')
			self.oHelper.SetValue('De  grupo ?','TRF5')
			self.oHelper.SetValue('Ate grupo ?','TRF5')
			self.oHelper.SetValue('Filtra produtos por categ. ?  ', 'Nao')
			self.oHelper.SetValue('Quebra informacoes ?','Por armazem')
			self.oHelper.SetValue('TES para notas de saida ?','549')
			self.oHelper.SetValue('Gera documento de entrada ?','Classificado')
			self.oHelper.SetValue('TES para notas de entrada ?','400')
			self.oHelper.SetValue('Condicao de pagamento ?','101')
			self.oHelper.SetValue('Considera como preco no PV ?','C Unitario')
			self.oHelper.SetValue('Dados da origem ?','Todas filiais')
			self.oHelper.SetValue('Utilizar Saldo de Terceiros ?','Nao')
			self.oHelper.SetValue('Espécie documento de entrada ?','NF')
			self.oHelper.SetValue('Descrição de produtos ?','Não')
			self.oHelper.SetValue('Informa prod. manualmente ?','Não')
			self.oHelper.SetValue('Abre tela da nota de entrada ?','Não')
			self.oHelper.SetButton('OK')

			self.oHelper.ClickTree('Filial D MG 01  Filial BELO HOR > Armazem 01 > ESTSE0000000000000000000000962 -            10.000,00')
			self.oHelper.ClickTree('Filial D RJ 01  Filial RIO DE J', position=2)
			self.oHelper.ClickTree('Armazem 01 > ESTSE0000000000000000000000963 -                 0,00', position=0)

			self.oHelper.SetButton('Outras Ações', 'Relacao')

			self.oHelper.SetValue('Quantidade', '100,00')
			self.oHelper.SetButton('Confirmar')
			self.oHelper.SetButton('Confirmar')

			self.oHelper.SetButton('Ok')
			self.oHelper.SetButton('OK')
			time.sleep(50)
			self.oHelper.Program('MATA310')			
		self.oHelper.AssertTrue()
		self.oHelper.Finish()	
	def test_MATA310_006(self):
        
		self.oHelper.AddParameter("MV_M310TRV", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()
		
		self.oHelper.SetValue('De  produto ? ','EST000000000000000000000000025')
		self.oHelper.SetValue('Ate produto ?','EST000000000000000000000000025')
		self.oHelper.SetValue('Ate filial ?','D RJ 01')
		self.oHelper.SetValue('Ate armazem ?','98')
		self.oHelper.SetValue('Ate tipo ?','ZZ')
		self.oHelper.SetValue('Ate grupo ?','9999')
		self.oHelper.SetValue('Filtra produtos por categ. ?  ', 'Nao')
		self.oHelper.SetValue('Quebra informacoes ?','Por armazem')
		self.oHelper.SetValue('TES para notas de saida ?','672')
		self.oHelper.SetValue('Gera documento de entrada ?','Classificado')
		self.oHelper.SetValue('TES para notas de entrada ?','072')
		self.oHelper.SetValue('Condicao de pagamento ?','001')
		self.oHelper.SetValue('Considera como preco no PV ?','C Unitario')
		self.oHelper.SetValue('Dados da origem ?','Todas filiais')
		self.oHelper.SetValue('Utilizar Saldo de Terceiros ?','Nao')
		self.oHelper.SetValue('Espécie documento de entrada ?','NF')
		self.oHelper.SetValue('Descrição de produtos ?','Não')
		self.oHelper.SetValue('Informa prod. manualmente ?','Não')
		self.oHelper.SetValue('Abre tela da nota de entrada ?','Não')
		self.oHelper.SetButton('OK')
		
		self.oHelper.ClickTree('Filial D MG 01  Filial BELO HOR > Armazem 98 > EST000000000000000000000000025 -               100,00')
		
		self.oHelper.ClickTree('Filial D MG 02  Filial Uberaba', position=2)
		self.oHelper.ClickTree('Armazem 98 > EST000000000000000000000000025 -                 0,00', position=0)

		self.oHelper.SetButton('Outras Ações', 'Relacao')
		self.oHelper.SetButton('Outras Ações', 'Consulta Saldo CQ')
		self.oHelper.SetButton('OK')

		self.oHelper.SetValue('Quantidade','10,00')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('OK')
		time.sleep(50)
		self.oHelper.Program('MATA310')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
