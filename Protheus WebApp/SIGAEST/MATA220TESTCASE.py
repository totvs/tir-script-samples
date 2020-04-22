#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA220
#
#@author carlos.capeli
#@since 20/09/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA220(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','20/09/2019','T1','D MG 01')
		inst.oHelper.Program('MATA220')		

	def test_MAT220_001(self):

		self.oHelper.AddParameter("MV_GRADE", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto','ESTMATA220GRADETIR00000000')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Qtd.Inic.Mes','50,00')
		self.oHelper.SetValue('[BR] BRANCO','50,00', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('Qt.Ini.2a UM','800,00')
		self.oHelper.SetValue('[BR] BRANCO','800,00', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Outras Ações', 'Inf. lote')
		self.oHelper.SetValue('Lote','0000000001', grid=True, grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MAT220_002(self):

		self.oHelper.AddParameter("MV_GRADE", "", ".F.", ".F.", ".F.")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto','ESTMATA220TIR00000000000000000')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Qtd.Inic.Mes','100,00')
		self.oHelper.SetButton('Outras Ações', 'Inf. lote')
		self.oHelper.SetValue('Lote','0000000001', grid=True)
		self.oHelper.SetValue('Potência','5,00', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MAT220_003(self):

		self.oHelper.SearchBrowse("D MG 01 ESTMATA220TIR00000000000000001")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('Produto','ESTMATA220TIR00000000000000001')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MAT220_004(self):

		self.oHelper.SearchBrowse("D MG 01 ESTMATA220TIR00000000000000002")
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Qtd.Inic.Mes','101,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MAT220_005(self):

		self.oHelper.SearchBrowse("D MG 01 ESTMATA220TIR00000000000000003")
		self.oHelper.SetButton('Outras Ações', 'Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	#CT006 INCLUIR SALDO INICIAL PARA PRODUTO EMPENHADO EM OP	
	#@author Jefferson silva
	#@since 26/11/2019
	#@version 1.0	
	#
	def test_MAT220_006(self):

		self.oHelper.AddParameter("MV_RASTRO", "", "S", "S", "S")
		self.oHelper.AddParameter("MV_LOCALIZ", "", "S", "S", "S")
		self.oHelper.SetParameters()	

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto','ESTSE0000000000000000000000584')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Qtd.Inic.Mes','10,00')
		
		self.oHelper.SetButton('Outras Ações', 'Inf. lote')
		self.oHelper.SetValue('Lote','X', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')		
		self.oHelper.SetButton("X")
		
		self.oHelper.Program("MATA390")
		self.oHelper.SearchBrowse("D MG 01 ESTSE000000000000000000000058401X",key='Filial+produto + Armazem + Lote +...')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B8_PRODUTO", "ESTSE0000000000000000000000584")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("X")		     
		
		self.oHelper.Program("MATA265")
		self.oHelper.SearchBrowse("D MG 01 ESTSE000000000000000000000058401X",key='Filial+produto + Armazem + Lote')
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("DA_PRODUTO", "ESTSE0000000000000000000000584")
		self.oHelper.CheckResult("DA_SALDO", "10,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("X")
		
		self.oHelper.Program("MATA220")
		self.oHelper.SetButton("X")

		self.oHelper.AssertTrue()

	#CT007 Valida se quantidade fisica e igual ao saldo do lote
	#@author Gabriel Oliveira
	#@since 11/12/2019
	#@version 1.
	#
	def test_MAT220_007(self):

		self.oHelper.AddParameter("MV_RASTRO", "", "S", "S", "S")
		self.oHelper.SetParameters()
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto','ESTSE0000000000000000000000589')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Qtd.Inic.Mes','999999999,99')
		
		self.oHelper.SetButton('Outras Ações', 'Inf. lote')
		self.oHelper.CheckResult("Quantidade", "999999999,99", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Cancelar')		
		self.oHelper.SetButton("X")
			
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()