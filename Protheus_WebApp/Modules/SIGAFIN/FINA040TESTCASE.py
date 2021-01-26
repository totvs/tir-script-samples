from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

"""-------------------------------------------------------------------
/*/{Protheus.doc} FINA040TestCase
TIR - Casos de testes da rotina contas a receber 

@author Marcelo Ferreira
@since 09/11/2018
@version 12
-------------------------------------------------------------------"""

indice1 = "Filial+prefixo + No. Titulo + Parce..."

class FINA040(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINA040 
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN",DateSystem,"T1","D MG 01 ","06")
		inst.oHelper.Program('FINA040')


	#-------------------------------------------
	# Inicio dos casos de testes TIR - FINA040 
	#-------------------------------------------


	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT001
	TIR - Casos de testes da rotina contas a receber 
	Inclusão de títulos com ISS e verificação da aba impostos

	@author Marcelo Ferreira
	@since 09/11/2018
	@version 12
	-------------------------------------------------------------------"""
	def test_FINA040_CT001(self):

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetValue("Contabiliza on line ?" ,"Nao")
		self.oHelper.SetValue("Contab.Tit.Provisor ?" ,"Nao")
		self.oHelper.SetValue("Rateia Valor ?" ,"Bruto")
		self.oHelper.SetValue("Valores Acessórios Inclusão ?" ,"Não")
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E1_PREFIXO', "FIN")
		self.oHelper.SetValue('E1_NUM','FINA40133')
		self.oHelper.SetValue('E1_TIPO','NF')
		self.oHelper.SetValue('E1_NATUREZ','FINA040133')
		self.oHelper.SetValue('E1_CLIENTE','FIN184')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO','10/10/2018')
		self.oHelper.SetValue('E1_VENCTO','10/10/2018')
		self.oHelper.SetValue('E1_VENCREA','10/10/2018')
		self.oHelper.SetValue('E1_VALOR','10.000,00')
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT002
	TIR - Casos de testes da rotina contas a receber 
	Simulação da inclusão de título sem impostos

	@author Rodrigo Oliveira
	@since 03/06/2019
	@version 12
	-------------------------------------------------------------------"""
	def test_FINA040_CT002(self):

		titulo = 'NFTIR001'

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_TIPO','NF')
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'DINHEIRO', 'Código')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('E1_CLIENTE','000001')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO','25/04/2019')
		self.oHelper.SetValue('E1_VENCTO','25/04/2019')
		self.oHelper.SetValue('E1_VENCREA','25/04/2019')
		self.oHelper.SetValue('E1_VALOR','10.000,00')
		self.oHelper.SetButton('Cancelar') 
		self.oHelper.AssertTrue()

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT003
	TIR - Casos de testes da rotina contas a receber 
	Inclusão de Títulos com Múltiplas Naturezas

	@author santos.renato
	@since 21/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/project/10231/testCase?folderId=2585
	-------------------------------------------------------------------"""
	def test_FINA040_CT003(self):

		self.oHelper.AddParameter("MV_MULNATR","",".T.",".T.",".T.")  
		self.oHelper.SetParameters()
		
		prefixo = 'AUT'
		titulo  = 'FIN000001'
		parcela = ''
		tipo    = 'NF'

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'AUT0000001', 'Código')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('E1_CLIENTE','FIN001')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO',DateSystem)
		self.oHelper.SetValue('E1_VENCTO',DateSystem)
		self.oHelper.SetValue('E1_VALOR','10000,00')

		self.oHelper.ClickFolder('Administrativo')
		self.oHelper.SetValue('E1_MULTNAT', '1')
		self.oHelper.SetButton('Salvar')
		
		self.oHelper.SetValue('EV_NATUREZ', 'AUT0000003', grid=True)
		self.oHelper.SetValue('EV_VALOR', '5000,00', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey("DOWN", grid=True)

		self.oHelper.SetValue('EV_NATUREZ', 'AUT0000002', grid=True)
		self.oHelper.SetValue('EV_VALOR', '5000,00', grid=True)
		self.oHelper.SetValue('EV_RATEICC', '1', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetValue('EZ_CCUSTO', '002', grid=True)
		self.oHelper.SetValue('EZ_VALOR', '2500,00', grid=True)
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue('EZ_CCUSTO', '003', grid=True)
		self.oHelper.SetValue('EZ_VALOR', '2500,00', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')


		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Cancelar')	
		
		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SearchBrowse("D MG 01 AUTFIN000001 NF ", indice1)
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.CheckResult('E1_PREFIXO', prefixo)
		self.oHelper.CheckResult('E1_NUM', titulo)
		self.oHelper.CheckResult('E1_PARCELA', parcela)
		self.oHelper.CheckResult('E1_TIPO', tipo)
		self.oHelper.CheckResult("E1_NATUREZ", "AUT0000001")
		self.oHelper.CheckResult("E1_VALOR", "10.000,00")

		self.oHelper.SetButton('Confirmar')	
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()

		
		"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT074
	TIR - Casos de testes da rotina contas a receber 
	Substituir títulos a receber provisorios(sem impostos)

	@author santos.renato
	@since 21/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T12054
	-------------------------------------------------------------------"""
	def test_FINA040_CT074(self):

		prefixo = 'FIN'
		titulo  = 'FINA04017'
		parcela = ''
		tipo    = 'NF'
		cliente = '000022'
		loja    = '01'

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetButton("Outras Ações", "Substituir")
		self.oHelper.SetValue('cCodigo ', cliente, name_attr=True)
		self.oHelper.SetValue('cLoja', loja, name_attr=True)
		self.oHelper.SetButton('Ok')

		self.oHelper.ClickBox("No. Titulo", "FINA04014")
		self.oHelper.ClickBox("No. Titulo", "FINA04015")
		self.oHelper.SetButton('Confirmar')


		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'001', 'Código')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('E1_EMISSAO',DateSystem)
		self.oHelper.SetValue('E1_VENCTO',DateSystem)
		self.oHelper.SetValue('E1_VENCREA',DateSystem)

		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()
		

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT103
	TIR - Casos de testes da rotina contas a receber 
	Inclusão de título a receber já inserindo valor acessório vinculado

	@author Renato.ito
	@since 12/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T19269
	-------------------------------------------------------------------"""
	def test_FINA040_CT103(self):
		
		prefixo = 'VA'
		titulo  = 'FIN000307'
		parcela = ''
		tipo    = 'NF'

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valores Acessórios Inclusão ?", "Sim")
		self.oHelper.SetButton('Ok') 

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'000001', 'Código')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('E1_CLIENTE','FIN168')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO','25/04/2019')
		self.oHelper.SetValue('E1_VENCTO','25/04/2019')
		self.oHelper.SetValue('E1_VENCREA','25/04/2019')
		self.oHelper.SetValue('E1_VALOR','1.000,00')
		self.oHelper.SetButton('Salvar')
		self.oHelper.WaitShow("Deseja cadastrar os valores acessórios deste título agora?")
		self.oHelper.SetButton('Sim')
		self.oHelper.SetValue('FKD_CODIGO','VA0001', grid=True)
		self.oHelper.SetValue('FKD_VALOR','15,00', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.CheckHelp('Registro alterado com sucesso.','Fechar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Valores Acessórios Inclusão ?", "Não")
		self.oHelper.SetButton('Ok') 
		self.oHelper.AssertTrue()

		
	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT110
	TIR - Casos de testes da rotina contas a receber 
	Inclusão de RA com impostos na baixa

	@author santos.renato
	@since 21/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T19405
	-------------------------------------------------------------------"""
	def test_FINA040_CT110(self):

		self.oHelper.AddParameter("MV_RARTIMP","","1","1","1")  
		self.oHelper.AddParameter("MV_BQ10925","","2","2","2")  
		self.oHelper.AddParameter("MV_BR10925","","1","1","1")  
		self.oHelper.SetParameters()
		
		prefixo = ''
		titulo  = 'FIN000313'
		parcela = ''
		tipo    = 'RA'
		banco   = '241'
		agencia = '07891'
		conta 	= '0001000222'
		hist    = 'Teste|com|pipe'
		
		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.SetValue('cBancoAdt', banco, name_attr=True)
		self.oHelper.SetValue('cAgenciaAdt', agencia, name_attr=True)
		self.oHelper.SetValue('cNumCon', conta, name_attr=True)
		self.oHelper.SetButton("Ok")
		

		self.oHelper.SetValue('E1_NATUREZ', 'FIN4000000')
		self.oHelper.SetValue('E1_CLIENTE','FIN183')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO',DateSystem)
		self.oHelper.SetValue('E1_VENCTO',DateSystem)
		self.oHelper.SetValue('E1_VENCREA',DateSystem)
		self.oHelper.SetValue('E1_VALOR','10000,00')
		self.oHelper.SetValue('E1_HIST', hist)

		self.oHelper.ClickFolder('Impostos')
		self.oHelper.CheckResult('E1_BASEIRF', '10.000,00')
		self.oHelper.CheckResult('E1_IRRF '  , '150,00')
		self.oHelper.CheckResult('E1_CSLL'	 , '100,00')
		self.oHelper.CheckResult('E1_COFINS' , '300,00')
		self.oHelper.CheckResult('E1_PIS'    , '65,00')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
	
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()


	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT154
	TIR - Casos de testes da rotina contas a receber 
	Inclusão de título a receber com desdobramento e imposto (PCC + IR)

	@author Renato.ito
	@since 12/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T37961
	-------------------------------------------------------------------"""
	def test_FINA040_CT154(self):

		prefixo = 'FIN'
		titulo  = 'FINDSDB01'
		parcela = ''
		tipo    = 'NF'

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'FIN0000088', 'Código')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('E1_CLIENTE','FIN259')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO',DateSystem)
		self.oHelper.SetValue('E1_VENCTO',DateSystem)
		self.oHelper.SetValue('E1_VENCREA',DateSystem)
		self.oHelper.SetValue('E1_VALOR','11.000,00')
		self.oHelper.ClickFolder('Administrativo')
		self.oHelper.SetValue('E1_DESDOBR','1')
		self.oHelper.SetValue('Número de Parcelas','5')
		self.oHelper.SetValue('Periodo de Vencto. (em dias)','30')
		self.oHelper.SetButton('Ok')
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_VALOR','10.000,00')
		self.oHelper.SetButton('Salvar') 
		self.oHelper.SetButton('Cancelar') 
		self.oHelper.AssertTrue()
		# Exlusão
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.WaitShow("DESDOBRAD")
		self.oHelper.CheckHelp('DESDOBRAD','Fechar')
		self.oHelper.SetButton("Outras Ações", "Canc.Desdobr.")
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')
		self.oHelper.AssertTrue()		

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINA040_CT161
	TIR - Casos de testes da rotina contas a receber 
	Validar a inclusão de abatimento (AB-) para um título que possui outro com o mesmo prefixo numero e parcela

	@author Renato.ito
	@since 12/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T42027
	-------------------------------------------------------------------"""
	def test_FINA040_CT161(self):

		prefixo = 'TIR'
		titulo  = '1'
		parcela = '1'
		tipo    = 'NF'

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetValue("Contabiliza on line ?" ,"Nao")
		self.oHelper.SetValue("Contab.Tit.Provisor ?" ,"Nao")
		self.oHelper.SetValue("Rateia Valor ?" ,"Bruto")
		self.oHelper.SetValue("Valores Acessórios Inclusão ?" ,"Não")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Dados Gerais')
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'001', 'Código')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('E1_CLIENTE','FIN259')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO',DateSystem)
		self.oHelper.SetValue('E1_VENCTO',DateSystem)
		self.oHelper.SetValue('E1_VENCREA',DateSystem)
		self.oHelper.SetValue('E1_VALOR','1,00')
		self.oHelper.SetButton('Salvar')
		tipo	= 'DP'
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.F3(field='E1_NATUREZ', name_attr=True)
		self.oHelper.SearchBrowse(f'001', 'Código')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('E1_CLIENTE','FIN259')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO',DateSystem)
		self.oHelper.SetValue('E1_VENCTO',DateSystem)
		self.oHelper.SetValue('E1_VENCREA',DateSystem)
		self.oHelper.SetValue('E1_VALOR','10.000,00')
		self.oHelper.SetButton('Salvar')
		tipo	= 'AB-'
		self.oHelper.SetValue('E1_PREFIXO', prefixo)
		self.oHelper.SetValue('E1_NUM', titulo)
		self.oHelper.SetValue('E1_PARCELA', parcela)
		self.oHelper.SetValue('E1_TIPO', tipo)
		self.oHelper.SetValue('E1_VALOR','550,00')
		self.oHelper.SetButton('Salvar')
		
		self.oHelper.ClickGridCell("Tipo",row=1)
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Cancelar') 
		self.oHelper.AssertTrue()

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} test_FINA040_CT205
	TIR - Casos de testes da rotina contas a receber 
	Alteração do valor do tí­tulo em CNAB e acessando a rotina no menu ações relacionadas Instruções.

	@author		Rafael Riego
	@since 		25/08/2020
	@version 	12.1.027
	@See 		https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53777
	/*/
	-------------------------------------------------------------------"""
	def test_FINA040_CT205(self):

		chaveTitulo = "D MG 01 " + "FIN" + "TIR000205" + "1" + "NF "

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SearchBrowse(chaveTitulo, indice1)

		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickFolder("Dados Gerais")
		self.oHelper.SetValue("E1_VALOR", "3.500,00")
		self.oHelper.SetButton("Outras Ações", "Instruções")
		self.oHelper.SetValue('Ocorrencia', "14", grid=True, grid_number=1, ignore_case = True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')
		self.oHelper.WaitShow("Confirma ocorrências?")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton('Salvar')
		self.oHelper.AssertTrue()

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} test_FINA040_CT207
	TIR - Casos de testes da rotina contas a receber 
	Exclusão de tí­tulo com pendências de contabilização.

	@author		Rafael Riego
	@since 		31/08/2020
	@version 	12.1.027
	@See 		https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T54080
	/*/
	-------------------------------------------------------------------"""
	def test_FINA040_CT207(self):

		prefixo = "FIN"
		titulo = "TIRCT0207"
		parcela = "1"
		tipo = "NF "

		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SearchBrowse("D MG 01 " + prefixo + titulo + parcela + tipo, indice1)
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.CheckResult('E1_PREFIXO', prefixo)
		self.oHelper.CheckResult('E1_NUM', titulo)
		self.oHelper.CheckResult('E1_PARCELA', parcela)
		self.oHelper.CheckResult('E1_TIPO', tipo)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.WaitShow("Foram encontrados movimentos pendentes de contabilização.")
		self.oHelper.SetButton("Cancela")
		self.oHelper.AssertTrue()		

	"""-------------------------------------------------------------------
	/*/{Protheus.doc} test_FINA040_CT215
	TIR - Não deletar cheque - Mensagem

	@author		rafael rondon
	@since 		28//12/2020
	@version 	12.1.027
	@See 		https://jiraproducao.totvs.com.br/secure/Tests.jspa#/project/10231/testCase?folderId=2585
	/*/
	-------------------------------------------------------------------"""
	def test_FINA040_CT215(self):

		prefixo = "FIN"
		titulo = "FIN070CHQ"
		parcela = " "
		tipo = "NF "

		self.oHelper.SearchBrowse("D MG 01 " + prefixo + titulo + parcela + tipo, indice1)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetButton("Outras Ações", "Cheques")

		self.oHelper.SetValue("Valor ref. baixa", "2000,00", grid=True, row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
		self.oHelper.LoadGrid()		

		self.oHelper.CheckHelp(text='TOTVS',button='Fechar')		

		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()					

	#-------------------------------------------
	# Fim dos casos de testes TIR - FINA040 
	#-------------------------------------------


	#-------------------------------------------
	# Encerramento class para TIR - FINA040 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()