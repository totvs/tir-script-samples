#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA185 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 11/07/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA185(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA185')		
		#inst.oHelper.Setup('SIGAADV','11/07/2019','T1','D MG 01','04')
		#inst.oHelper.SetLateralMenu('Atualizações > Movimentações > Internas > Armazém > Baixar Pre-requis.')

	def test_MATA185_CT001(self):

		#self.oHelper.AddParameter("MV_ESTNEG", "", "S", "S", "S")
		#self.oHelper.AddParameter("MV_BXPRERQ", "", "T", "T", "T")
		#self.oHelper.SetParameters()

		self.oHelper.SearchBrowse("D MG 01 PMS032 01")

		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Toda a Pre-Req")
		self.oHelper.SetButton('Ok')	

		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')
		self.oHelper.ClickCheckBox("Selecionar Todos os Itens",1)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('TM','501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT002(self):	

		self.oHelper.SearchBrowse("D MG 01 PMS032 01")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT003(self):	

		self.oHelper.SearchBrowse("D MG 01 PMS033 01")
		self.oHelper.SetButton('Outras Ações', 'EStorno')
		self.oHelper.SetButton('Confirmar')	
		self.oHelper.AssertTrue()

	def test_MATA185_CT004(self):	

		self.oHelper.SearchBrowse("D MG 01 PMS034 01")
		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Item da Pre-Req")
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')	
		self.oHelper.SetValue('Quantidade a requisitar', '30,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('TP Movimento', '501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT005(self):		

		self.oHelper.AddParameter("MV_ESTNEG", "", "F", "F", "F")
		self.oHelper.AddParameter("MV_BXPRERQ", "", ".T.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SearchBrowse("D MG 01 PMS035 01")
		self.oHelper.SetButton('Outras Ações', 'Tipo Baixa')
		self.oHelper.SetValue("Baixar Por ?", "Item da Pre-Req")
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Baixar')	
		self.oHelper.SetButton('Confirma')
		self.oHelper.SetValue('Quantidade a requisitar', '30,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('TP Movimento', '501')
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	def test_MATA185_CT006(self):

		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')	
		self.oHelper.AssertTrue()
	#CT007 Verifica se help é apresentado em tela referente a requisiçao ja baixada
	def test_MATA185_CT007(self):
						
		self.oHelper.SearchBrowse("D MG 01 ESTSE0000000000000000000000581PMS04101","Filial+produto + Nr.s.a. + Item S.a.")
		
		self.oHelper.SetButton('Baixar')
		self.oHelper.SetButton('Confirma')
		self.oHelper.CheckHelp(text_help='A185BX', button='Fechar')
		self.oHelper.AssertTrue()

	#GTSER-T51690 - CT008 - Verificar se a Solicitacao de Compras que foi criada ao gerar Pre-Requisicao e excluida juntamente com a Pre-Requisicao
	def test_MATA185_CT008(self):

		self.oHelper.SearchBrowse("D MG 01 EST024", "Filial+nr.s.a. + Item S.a. + Dt Emi...")
		self.oHelper.SetButton("Outras Ações", "Tipo Baixa")
		self.oHelper.SetValue("Qtd em Processo de Compras ?", "Produto")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Baixar")
		self.oHelper.SetButton("Confirma")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Outras Ações", "EXcluir")
		self.oHelper.SetButton("Confirmar")
		#self.oHelper.SetButton("X")
		#self.oHelper.ChangeEnvironment(date="10/06/2020", group="T1", branch="D MG 01 ", module="02")
		#self.oHelper.SetLateralMenu('Atualizações > Solicitações > Solicitação de Comp...')
		#self.oHelper.SearchBrowse("D MG 01 ESTMATA18500000000000000000015", "Filial+produto + Numero da Sc + Ite...")
		self.oHelper.AssertTrue()

	#GTSER-T52439 - CT009 - Verificar se o saldo previsto de entrada e atualizado corretamente ao encerrar uma Pre-Requisicao optando por excluir a SC gerada
	def test_MATA185_CT009(self):

		self.oHelper.SearchBrowse("D MG 01 EST030", "Filial+nr.s.a. + Item S.a. + Dt Emi...")
		self.oHelper.SetButton("Outras Ações", "Encerrar")
		self.oHelper.SetButton("Confirmar")
		#self.oHelper.SetButton("Deleta-la")
		time.sleep(3)
		self.oHelper.SetButton("X")
		self.oHelper.SetLateralMenu('Atualizações > Cadastros > Produto > Produtos')
		self.oHelper.SearchBrowse("D MG 01 ESTMATA18500000000000000000017", "Filial+codigo")
		time.sleep(5)
		self.oHelper.SetKey("F4")
		self.oHelper.CheckResult("Qtd. Entrada Prevista", "0,00")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("X")
		self.oHelper.Program("MATA185")
		self.oHelper.AssertTrue()

	#GTSER-T55000  - CT010 - Exclusao de SA vinculada a SC/PC
	def test_MATA185_CT010(self):

		self.oHelper.SearchBrowse("D MG 01 EST034", "Filial+nr.s.a. + Item S.a. + Dt Emi...")
		self.oHelper.SetButton("Outras Ações", "EXcluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Consultar documentos")
		self.oHelper.WaitShow("Documentos de Compra")
		self.oHelper.SetButton('Fechar')
		self.oHelper.WaitHide("Documentos de Compra")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()