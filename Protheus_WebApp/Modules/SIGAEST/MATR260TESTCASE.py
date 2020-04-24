from tir import Webapp
import unittest

class MATR260(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','30/09/2019','T1','D MG 01')
		inst.oHelper.Program('MATR260')

	def test_MATR260_CT001(self):
		self.oHelper.SetButton('Outras Ações', 'Parâmetros')
		self.oHelper.SetValue('Aglutina por ?','Armazem')
		self.oHelper.SetValue('Da filial ?','D MG 01')
		self.oHelper.SetValue('Ate a filial ?','D MG 01')
		self.oHelper.SetValue('Do Armazem ?','01')
		self.oHelper.SetValue('Ate Armazem ?','01')
		self.oHelper.SetValue('Do Produto ?','')
		self.oHelper.SetValue('Ate Poduto ?','ZZZZZ')
		self.oHelper.SetValue('Do tipo ?','')
		self.oHelper.SetValue('Ate tipo ?','ZZ')
		self.oHelper.SetValue('Do grupo ?','')
		self.oHelper.SetValue('Ate grupo ?','ZZZ')
		self.oHelper.SetValue('Da Descricao ?','')
		self.oHelper.SetValue('Ate Descricao ?','ZZZZZZ')
		self.oHelper.SetValue('Codigo Item De ?','')
		self.oHelper.SetValue('Codigo Item Ate ?','ZZZZZZ')		
		self.oHelper.SetValue('Imprime produtos ?','Ambos')
		self.oHelper.SetValue('Saldo Do Prod a Considerar ?','Atual')
		self.oHelper.SetValue('Qual Moeda ?','1a moeda')
		self.oHelper.SetValue('Aglutina por UM ?','sim')
		self.oHelper.SetValue('Listar Pords C/ Saldo Zerado?','nao')
		self.oHelper.SetValue('Imprimir o Valor ?','Custo')
		self.oHelper.SetValue('Data Referencia ?','30/09/2019')
		self.oHelper.SetValue('Listar Prods C/ Valor Zerado?','nao')
		self.oHelper.SetValue('QTDE. na 2a. U.M ?','nao')
		self.oHelper.SetValue('Imprime descricao do Armazem ?','nao')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Imprimir')
		self.oHelper.SetButton('sair')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
