from cawebhelper import CAWebHelper
import unittest

class GPEA340(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")

        # S E T U P
        inst.oHelper.SetUp("SIGAGPE","P12117","ADMIN","","08/01/2018","T1","D MG 01 ")

        inst.oHelper.UTProgram("GPEA340")
   
    #Inclusão com centro de custo
    def test_GPEA370_001(self):

        codigo = "55"
        
        self.oHelper.SetButton('Incluir', 'D MG 01 ')

        self.oHelper.UTSetValue("aCab","RCE_CODIGO", codigo)
        self.oHelper.UTSetValue("aCab","RCE_DESCRI", "GPE-SINDICATO")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTSetValue("aCab","RCE_CODIGO", codigo)
        self.oHelper.UTSetValue("aCab","RCE_DESCRI", "GPE-SINDICATO")
      
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()