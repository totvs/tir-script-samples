from cawebhelper import CAWebHelper
import unittest
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# @author..: Marcos.Coutinho@Totvs.com.br
# @date....: 09/01/2018
# @history.: Date         Dev               Objetivo
#            09/01/2018 | Marcos Coutinho | Criação do caso de teste test_GPEA932_001 - INC/VIS
#            09/01/2018 | Marcos Coutinho | Criação do caso de teste test_GPEA932_002 - ALT
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class GPEA932(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")

        # S E T U P
		# Informar o seu ambiente, grupo, filial e dados básicos
        inst.oHelper.SetUp("SIGAGPE","P12117eSocial","ADMIN","","02/01/2018","T2","L MG 01 ")

        inst.oHelper.UTProgram("GPEA932")

    def test_GPEA932_001(self):
    
        # Criando variavel principal de teste
        carreira = "CAR000001"
        
        # Informando inclusão e setando filial
        self.oHelper.SetButton('Incluir', 'L MG 01 ')

        # Informando valores dos campos
        self.oHelper.UTSetValue("aCab","GY_CODIGO", carreira)
        self.oHelper.UTSetValue("aCab","GY_DESC", carreira)
        self.oHelper.UTSetValue("aCab","GY_LEI", "000000000001")
        self.oHelper.UTSetValue("aCab","GY_DATA", "09/01/2018")
        self.oHelper.UTSetValue("aCab","GY_SIT", "1")

        # Solicitando clique no botão confirmar (salvar)
        self.oHelper.SetButton("Confirmar")

        # Solicitando clique no botão fechar (após salvar)
        self.oHelper.SetButton("Fechar")
        
        # Na tela do Browse, seleciona a pesquisa e informa os parâmetros
        self.oHelper.SearchBrowse(' Filial+cod.carreira',"L MG 01 %s" %carreira)

        # Posicionou no registro e selecionou botão visualizar
        self.oHelper.SetButton('Visualizar')

        # Conferindo se os valores dos campos são os mesmos dos informados
        self.oHelper.UTCheckResult("aCab","GY_CODIGO", carreira)
        self.oHelper.UTCheckResult("aCab","GY_DESC", carreira)
        self.oHelper.UTCheckResult("aCab","GY_LEI", "000000000001")
        self.oHelper.UTCheckResult("aCab","GY_DATA", "09/01/2018")
        self.oHelper.UTCheckResult("aCab","GY_SIT", "1")
        
        # Solicitando clique no botão fechar
        self.oHelper.SetButton('Fechar')

        # Retorno resultado em tela
        self.oHelper.AssertTrue()

    def test_GPEA932_002(self):
    
        carreira = "CAR000001"
        
        self.oHelper.SearchBrowse(' Filial+cod.carreira',"L MG 01 %s" %carreira)

        self.oHelper.SetButton('Alterar')

        self.oHelper.UTSetValue("aCab","GY_CODIGO", carreira)
        self.oHelper.UTSetValue("aCab","GY_DESC", carreira)
        self.oHelper.UTSetValue("aCab","GY_LEI", "000000000002")
        self.oHelper.UTSetValue("aCab","GY_DATA", "09/01/2018")
        self.oHelper.UTSetValue("aCab","GY_SIT", "1")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()