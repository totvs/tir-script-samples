from tir import Webapp
import unittest

class MATA650(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','18/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA650')

	def test_MATA650_001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetValue('C2_PRODUTO', 'PCP_TIR_MATA650_001_PA00000001')
		self.oHelper.SetValue('C2_LOCAL','01')
		self.oHelper.SetValue('C2_QUANT','10,00')
		self.oHelper.SetValue('C2_DATPRI','18/04/2019')
		self.oHelper.SetValue('C2_DATPRF','18/04/2019')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('C2_PRODUTO', 'PCP_TIR_MATA650_001_PA00000001')
		self.oHelper.CheckResult('C2_QUANT','10,00')
		self.oHelper.CheckResult('C2_DATPRI','18/04/2019')
		self.oHelper.CheckResult('C2_DATPRF','18/04/2019')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.WaitShow("Ordens de Producao")

		self.oHelper.SetKey('ESC')

		self.oHelper.SetButton('Sim')

		self.oHelper.Program('MATA650')

		self.oHelper.AssertTrue()

	def test_MATA650_002(self):
    		
		self.oHelper.WaitShow("Ordens de Producao")

		self.oHelper.SearchBrowse('D MG 01 PCP12501001', 'Filial+numero da Op + Item + Seque...')
    
		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('C2_DATPRF','19/04/2019')
		self.oHelper.SetButton('Salvar')

		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('C2_PRODUTO', 'PCP_TIR_MATA650_002_PA00000001')
		self.oHelper.CheckResult('C2_QUANT','10,00')
		self.oHelper.CheckResult('C2_DATPRI','18/04/2019')
		self.oHelper.CheckResult('C2_DATPRF','19/04/2019')

		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MATA650_003(self):
    		
		self.oHelper.SearchBrowse('D MG 01 PCP12601001', 'Filial+numero da Op + Item + Seque...')
    
		self.oHelper.SetButton('Outras Ações', 'Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_MATA650_004(self):
        		
		self.oHelper.SearchBrowse('D MG 01 PCP12701001', 'Filial+numero da Op + Item + Seque...')
    
		self.oHelper.SetButton('Outras Ações', 'Operações da Ordem')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	def test_MATA650_005(self):
    		
		self.oHelper.SearchBrowse('D MG 01 PCP12801001', 'Filial+numero da Op + Item + Seque...')
    	
		self.oHelper.SetButton('Outras Ações', 'Reprioriza')

		self.oHelper.SetValue('Produto para alterar prior. ?','OP Posicionada')
		self.oHelper.SetValue('OP Inicial ?','PCP12801001')
		self.oHelper.SetValue('OP Final ?','PCP12801001')
		self.oHelper.SetValue('OPs intermediaria grava ?','Prior. Propria')
		self.oHelper.SetValue('Armazem Inicial ?','')
		self.oHelper.SetValue('Armazem Final ?','ZZ')
		self.oHelper.SetValue('Produto Inicial ?','PCP_TIR_MATA650_005_PA00000001')
		self.oHelper.SetValue('Produto Final ?','PCP_TIR_MATA650_005_PA00000001')
		self.oHelper.SetValue('Prioridade inicial ?','50')
		self.oHelper.SetValue('Incremento na prioridade ?','50')
		self.oHelper.SetValue('Processar OP\'s ?','Ambas')

		self.oHelper.SetButton('Ok')

		self.oHelper.WaitShow("Ordens de Producao - REPRIORIZA")
		self.oHelper.SearchBrowse('PCP12801001', 'Numero da Op + Item + Sequencia +.')

		self.oHelper.ClickBox('Numero da OP', 'PCP128')

		self.oHelper.SetButton('Reprioriza')

		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('C2_PRODUTO', 'PCP_TIR_MATA650_005_PA00000001')
		self.oHelper.CheckResult('C2_PRIOR','50')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA650_006(self):
    		
		self.oHelper.SetButton('Outras Ações', 'Legenda')

		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	def test_MATA650_007(self):
    
		self.oHelper.SearchBrowse('D MG 01 PCP12901001', 'Filial+numero da Op + Item + Seque...')
		
		self.oHelper.SetButton('Outras Ações', 'Opcionais')

		self.oHelper.SetButton('Ok')

		self.oHelper.AssertTrue()

	def test_MATA650_008(self):
        
		self.oHelper.SetButton('Outras Ações', 'VenDas')

		self.oHelper.SetBranch('D MG 01')
		
		self.oHelper.SetValue('Mostra Pedido com OP ?','Sim')
		self.oHelper.SetValue('Produto Sem Estrutura Gera ?','Ordem de Prod.')
		self.oHelper.SetValue('Do  Cliente ?','PCP001')
		self.oHelper.SetValue('Ate o Cliente ?','PCP001')
		self.oHelper.SetValue('Do  Produto ?','PCP_TIR_MATA650_008_PA00000001')
		self.oHelper.SetValue('Ate o Produto ?','PCP_TIR_MATA650_008_PA00000001')
		self.oHelper.SetValue('Da  Data de Entrega ?','01/01/2019')
		self.oHelper.SetValue('Ate a Data de Entrega ?','31/12/2019')
		self.oHelper.SetValue('Da  TES ?','500')
		self.oHelper.SetValue('Ate a TES ?','999')
		self.oHelper.SetValue('Considerar Armazem Padrão ?','Sim')
		self.oHelper.SetValue('Liberar Bloqueio de Credito ?','Sim')
		self.oHelper.SetValue('Numero Inicial OP ?','')
		self.oHelper.SetValue('Do  Pedido ?','PCP022')
		self.oHelper.SetValue('Ate o Pedido ?','PCP022')
		self.oHelper.SetValue('Do  Armazem ?','01')
		self.oHelper.SetValue('Ate o Armazem ?','01')
		self.oHelper.SetValue('Avalia o Pedido de Venda ?','Individualmente')
		self.oHelper.SetValue('Qtd da Geracao OPs e SCs ?','LE Padrao')
		self.oHelper.SetValue('Mostra apenas PV liber. cred ?','Nao')
		self.oHelper.SetValue('Cons. Saldos de Armazens ?','Nao')
		self.oHelper.SetValue('Exibe PV c/ Fat.Parcial ?','Nao')
		self.oHelper.SetValue('Avaliar os PVs Priorizando ?','Num. Pedido')
		self.oHelper.SetValue('Considera Est. Seguranca ?','Nao')
		self.oHelper.SetValue('Considera Qtd Liberada PV ?','Não')
		self.oHelper.SetValue('Considera Est Segurança PI ?','Não')
		
		self.oHelper.SetButton('Ok')
		
		self.oHelper.WaitShow("OP por Pedido de Venda")
		self.oHelper.SearchBrowse('PCP02201PCP_TIR_MATA650_008_PA00000001', 'Num. Pedido + Item + Produto')

		self.oHelper.ClickBox('Item','01')

		self.oHelper.SetButton('Gera O.P.')	

		self.oHelper.WaitShow("Ordens de Producao")
	
		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA650_008_PA0000000118042019', 'Filial+produto + Entrega')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('C2_PRODUTO', 'PCP_TIR_MATA650_008_PA00000001')
		self.oHelper.CheckResult('C2_QUANT','10,00')
		self.oHelper.CheckResult('C2_PEDIDO','PCP022')
		self.oHelper.CheckResult('C2_DATPRI','18/04/2019')
		self.oHelper.CheckResult('C2_DATPRF','18/04/2019')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()