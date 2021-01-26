from tir import Webapp
import unittest
import time

class WMSA150(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAWMS", "10/12/2020", "T1", "M SP 01", "42")
		inst.oHelper.Program("WMSA150")
		
	def test_WMSA150_CT001(self):
		self.oHelper.SetValue('Servico De','')
		self.oHelper.SetValue('Servico Ate','ZZZ')
		self.oHelper.SetValue('Status do Servico','Nao Executados')
		self.oHelper.SetValue('Documento De','')
		self.oHelper.SetValue('Documento Ate','ZZZZZZZZZ')
		self.oHelper.SetValue('Data De','01/01/2010')
		self.oHelper.SetValue('Data Ate','31/12/2050')
		self.oHelper.SetValue('Produto De','')
		self.oHelper.SetValue('Produto Ate','ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
		self.oHelper.SetValue('Cliente/Fornec De','')
		self.oHelper.SetValue('Cliente/Fornec Ate','ZZZZZZ')
		self.oHelper.SetValue('Loja De','')
		self.oHelper.SetValue('Loja Ate','ZZ')
		self.oHelper.SetValue('Tipo de Servico','Todos')
		self.oHelper.SetValue('Carga De','')
		self.oHelper.SetValue('Carga Ate','ZZZZZZ')
		self.oHelper.SetValue('Refresh Autom. Tela','Sem Refresh')
		self.oHelper.SetValue('Habilita Estorno','Nao')
		self.oHelper.SetValue('Estorna Serv.Autom.','Nao')
		self.oHelper.SetValue('Docto.Conf.Recebto.De ?','')
		self.oHelper.SetValue('Docto.Conf.Recebto.Até ?','ZZZZZZ')
		self.oHelper.SetValue('Unitizador De ?','')
		self.oHelper.SetValue('Unitizador Até ?','ZZZZZZ')
		self.oHelper.SetButton('OK')

		self.oHelper.ClickGridHeader(column = 1 , grid_number =  1)
		self.oHelper.ClickBox('Documento','WMS000015')
		self.oHelper.ClickGridHeader(column = 1 , grid_number =  1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('X')
		
		self.oHelper.AssertTrue()
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		
if __name__ == "__main__":
	unittest.main()
