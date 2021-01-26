from tir import Webapp
import unittest

class CNTA300(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGCT','25/04/2019','T1','D MG 01 ','69')
		inst.oHelper.Program('CNTA300')
	
	#==========================================================================
	# CT001 - Inclusão de contrato com cronograma financeiro, físico e contábil
	#==========================================================================
	def test_CNTA300_CT001(self):
		data = '25/04/2019'
		fornecedor = 'GC0001'
		loja = '01'
		
		self.oHelper.SetButton('Incluir',sub_item='Compra')
		self.oHelper.SetBranch('D MG 01')
		
		#Cabeçalho do contrato (Aba cadastrais)
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.SetValue('CN9_NUMERO', 'TIR_CNTA300CT01')
		self.oHelper.SetValue('CN9_DTINIC', data)
		self.oHelper.SetValue('CN9_UNVIGE', '2')
		self.oHelper.SetValue('CN9_VIGE', '6')
		self.oHelper.SetValue('CN9_MOEDA', '1')
		
		self.oHelper.F3(field='CN9_TPCTO',name_attr=True )
		self.oHelper.SearchBrowse(f'050', 'Código')
		self.oHelper.SetButton('Ok')
		
		self.oHelper.F3(field='CN9_CONDPG', name_attr=True )
		self.oHelper.SearchBrowse(f'003', 'Código')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('CN9_FLGREJ', '2')
		self.oHelper.SetValue('CN9_FLGCAU', '2')

		#Grid de fornecedores do contrato (no momento de criação desse script, não era suportado o uso de F3 em grids, por isso o uso de setvalue)
		self.oHelper.ClickFolder('Fornecedores')
		self.oHelper.SetValue('CNC_CODIGO', fornecedor, grid=True, grid_number=1, ignore_case=True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('CNC_LOJA', loja, grid=True, grid_number=1, ignore_case=True, row=1)
		self.oHelper.LoadGrid()

        #Grid de planilhas do contrato
		self.oHelper.ClickFolder('Planilhas')
		self.oHelper.SetValue('CNA_FORNEC', fornecedor, grid=True, grid_number=1, ignore_case=True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('CNA_LJFORN', loja, grid=True, grid_number=1, ignore_case=True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('CNA_TIPPLA', 'GC1', grid=True, grid_number=1, ignore_case=True, row=1)
		self.oHelper.LoadGrid()
		
		#Grid de Itens da planilha
		self.oHelper.ClickFolder('Itens')
		self.oHelper.SetValue('CNB_PRODUT', 'GCT00000000000000000CNTA300-01', grid=True, grid_number=2, ignore_case=True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('CNB_QUANT', '50,00000000', grid=True, grid_number=2, ignore_case=True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetValue('CNB_VLUNIT', '250,50', grid=True, grid_number=2, ignore_case=True, row=1)
		self.oHelper.LoadGrid()

		#inclusão do cronograma financeiro
		self.oHelper.ClickFolder('Cronograma Financeiro')
		self.oHelper.SetButton('Outras Ações', sub_item='Incluir cronograma financeiro/físico')
		self.oHelper.SetValue('Periodicidade ?', 'Mensal')
		self.oHelper.SetValue('Dia(s) ?', '30')
		self.oHelper.SetValue('Útimo dia do mês ?', 'Sempre')
		self.oHelper.SetValue('Competência de início ?', '04/2019')
		self.oHelper.SetValue('Data prevista 1ª medição ?', data)
		self.oHelper.SetValue('Quantidade de parcelas ?', '6')
		self.oHelper.SetButton('OK')

		#inclusão do cronograma contábil
		self.oHelper.ClickFolder('Cronograma Contábil')
		self.oHelper.SetButton('Outras Ações', sub_item='Incluir cronograma contábil')
		self.oHelper.SetValue('Data prevista 1ª medição ?', data)
		self.oHelper.SetValue('Quantidade de parcelas ?', '6')
		self.oHelper.SetValue('Histórico ?', 'Teste TIR')
		self.oHelper.SetValue('Periodicidade ?', 'Mensal')
		self.oHelper.SetValue('Dia(s) ?', '30')
		self.oHelper.SetButton('OK')

        #Gravação do registro
		self.oHelper.SetButton('Confirmar')
        #Fechamento da mensagem "registro incluído com sucesso"
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()