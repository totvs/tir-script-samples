from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA813TestCase
TIR - Casos de testes da rotina Credenciamento

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA813(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","23/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA813")
		inst.oHelper.AddParameter("MV_PLCALPG","" , "2")
		inst.oHelper.SetParameters()

	def test_PLSA813_001(self):
		# Inclusao
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")

		self.oHelper.SetValue("B9Y_NOME","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetValue("B9Y_CPFCGC","51831698536",check_value = False)
		self.oHelper.SetValue("B9Y_EMAIL","PRESTADORES@DSAUPC.COM.BR",check_value = False)
		self.oHelper.SetValue("B9Y_TEL","11333331234",check_value = False)
		self.oHelper.SetValue("B9Y_CRMNUM","123456")
		self.oHelper.SetValue("B9Y_CRMEST","SP")
		self.oHelper.SetValue("B9Y_TIPOAT","3 - Ambos")
		self.oHelper.SetValue("B9Y_SEXO","2 - Masculino")
		self.oHelper.SetValue("B9Y_NASCTO","01/01/1985",check_value = False)
		self.oHelper.SetValue("B9Y_NATU","3550308")
		self.oHelper.SetValue("B9Y_ECIVIL","S")
		self.oHelper.SetValue("B9Y_FCAPTA","1 - Prestador Portal")
		self.oHelper.SetValue("B9Y_STCRED","1 - Pendente com a Operadora")

		# Pasta Endereco
		self.oHelper.ClickFolder('Endereço')
		self.oHelper.ClickGridCell("CEP",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B9V_CEP","05541000",check_value = False)
		self.oHelper.ClickGridCell("Nº",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B9V_NUMERO","100",check_value = False)

		# Pasta Especialidade
		self.oHelper.ClickFolder('Especialidade')
		self.oHelper.ClickGridCell("Cod Espec",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B9Q_CODESP","002")
		self.oHelper.ClickGridCell("Tempo Formac",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B9Q_TEMFOR","01/01/2015",check_value = False)

		# Pasta Passos do Credenciamento
		self.oHelper.ClickFolder('Passos do Credenciamento')
		self.oHelper.ClickGridCell("Passo",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B2E_CODPAS","0001")
		self.oHelper.SetButton("Sim")

		self.oHelper.SetButton("Confirmar") 
		self.oHelper.SetButton("Fechar")	# O arquivo informado no cadastro de sinalizadores n�o existe
		self.oHelper.SetButton("Fechar")	# O arquivo informado no cadastro de sinalizadores n�o existe

		self.oHelper.SetButton("Fechar")	# O e-mail referente ao Passo 0001 Foi enviado com Sucesso!
		self.oHelper.SetButton("Fechar")	# Registro inserido com sucesso

		#self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC TIR INCLUSAO"}', key=2, index=True)

		self.oHelper.SetButton("Analisar")
		self.oHelper.SetValue("B9Y_STCRED","2 - Pendente com o Prestador")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Analisar")
		self.oHelper.SetValue("B9Y_STCRED","4 - Indeferido")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Analisar")
		self.oHelper.SetValue("B9Y_STCRED","3 - Credenciado")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.SetButton("Analisar")
		self.oHelper.ClickFolder('Endereço')
		self.oHelper.ClickGridCell("Deferido?",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.ClickFolder('Especialidade')
		self.oHelper.ClickGridCell("Deferido?",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.ClickFolder('Passos do Credenciamento')
		self.oHelper.ClickGridCell("Finalizado?",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9Y_NOME","PLS DSAUPC TIR INCLUSAO")	
		self.oHelper.CheckResult("B9Y_STCRED","3 - Credenciado")	
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()