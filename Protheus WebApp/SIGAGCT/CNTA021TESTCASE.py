from cawebhelper import CAWebHelper
import unittest

class CNTA021(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")

        # S E T U P
        inst.oHelper.SetUp("SIGAGCT","P12117","ADMIN","","08/01/2018","T1","D MG 01 ","69")

        # M E N U
        inst.oHelper.UTProgram("CNTA020")

    #---------------------------------------------------------------------------------
    # A U T O R: Thamarav@
    # D A T E: 08/01/2018 
    # C T 0 0 1: Incluir (Tipo de Contrato Compra, medição eventual, contrato fixo, 
    # multa/bonificação na medição, não permite multa manual, limite financeiro) 
    #---------------------------------------------------------------------------------

    def test_CNTA021_001(self):
        #------------------------------------------------------
        # Na inclusão, informar no segundo parâmetro a filial
        #------------------------------------------------------
        self.oHelper.SetButton('Incluir', 'D MG 01 ')

        self.oHelper.UTSetValue("aCab","CN1_DESCRI", "COMPRA")
        self.oHelper.UTSetValue("aCab","CN1_MEDEVE", "1") #1=Sim    
        self.oHelper.UTSetValue("aCab","CN1_TPMULT", "2") #2=Medição
        self.oHelper.UTSetValue("aCab","CN1_MULMAN", "1") #1=Não permite
        self.oHelper.UTSetValue("aCab","CN1_ESPCTR", "1") #1=Compra

        #------------------------------------------------------
        # Exemplo de utilização com mudança de pastas 
        #------------------------------------------------------        
        #self.oHelper.ClickFolder('Informativos/Impostos')
        #self.oHelper.UTSetValue("aCab","CN1_ALINSS", "15,00")

        self.oHelper.SetButton("Confirmar")

        #--------------------------------------------
        # Mensagem de registro incluído com sucesso 
        #--------------------------------------------
        self.oHelper.SetButton('Fechar')
        
        #--------------------------------------------
        # Pesquisa de registro
        #--------------------------------------------
        # self.oHelper.SearchBrowse('Filial+codigo + Loja',"D MG    %s" %codigo, True)

        #--------------------------------------------
        # Resultado esperado
        #--------------------------------------------
        self.oHelper.SetButton('Visualizar')

        self.oHelper.UTCheckResult("aCab","CN1_DESCRI", "COMPRA")
        self.oHelper.UTCheckResult("aCab","CN1_MEDEVE", "1") #1=Sim    
        self.oHelper.UTCheckResult("aCab","CN1_TPMULT", "2") #2=Medição
        self.oHelper.UTCheckResult("aCab","CN1_MULMAN", "1") #1=Não permite
        self.oHelper.UTCheckResult("aCab","CN1_ESPCTR", "1") #1=Compra
       
        #-----------------------------------------------------------------------------------------------
        # Análise do resultado esperado dos campos autopreenchidos de acordo com o inicializador padrão
        #-----------------------------------------------------------------------------------------------
        self.oHelper.UTCheckResult("aCab","CN1_MEDAUT", "2") #2-Não
        self.oHelper.UTCheckResult("aCab","CN1_CROFIS", "2") #2-Não
        self.oHelper.UTCheckResult("aCab","CN1_TPLMT" , "2") #1-Financeiro
        self.oHelper.UTCheckResult("aCab","CN1_CROCTB", "2") #2-Nao
        self.oHelper.UTCheckResult("aCab","CN1_CTRFIX", "1") #1-Sim
        self.oHelper.UTCheckResult("aCab","CN1_VLRPRV", "1") # 1-Sim

        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
    
    #------------------------------------------------------------------------------------
    # Método responsável por posicionar o Protheus no browse para execução do próximo CT
    #------------------------------------------------------------------------------------
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()
#-----------------------------------------------------------------------
# Método responsável por só permitir a execução do teste via TestSuite 
# (particularidade o Python)
#-----------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()