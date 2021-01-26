from cawebhelper import CAWebHelper
import unittest

class GPEA370(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")

        # S E T U P
        inst.oHelper.SetUp("SIGAGPE","P12117","ADMIN","","08/01/2018","T1","D MG 01 ")

        inst.oHelper.UTProgram("GPEA370")
   
    #Inclusão com centro de custo
    def test_GPEA370_001(self):

        codigo = "55555"
        
        self.oHelper.SetButton('Incluir', 'D MG 01 ')

        self.oHelper.UTSetValue("aCab","Q3_CARGO", codigo)
        self.oHelper.UTSetValue("aCab","Q3_DESCSUM", "GPE-CARGO")
        self.oHelper.UTSetValue("aCab","Q3_CC", "000000001")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTCheckResult("aCab","Q3_CARGO", codigo)
        self.oHelper.UTCheckResult("aCab","Q3_DESCSUM", "GPE-CARGO")
        self.oHelper.UTCheckResult("aCab","Q3_CC", "000000001")
      
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #Alteração da descrição
    def test_GPEA370_002(self):
        
        codigo = "55555"
        
        self.oHelper.SearchBrowse('Filial+cargo + Centro Custo',"D MG    %s" %codigo, True)

        self.oHelper.SetButton("Alterar")

        self.oHelper.UTSetValue("aCab","Q3_DESCSUM", "GPE-CARGO ALTERADO")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTCheckResult("aCab","Q3_CARGO", codigo)
        self.oHelper.UTCheckResult("aCab","Q3_DESCSUM", "GPE-CARGO ALTERADO")
        self.oHelper.UTCheckResult("aCab","Q3_CC", "000000001")
      
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    #Exclusão
    def test_GPEA370_003(self):
        
        codigo = "55555"
        
        self.oHelper.SearchBrowse('Filial+cargo + Centro Custo',"D MG    %s" %codigo)

        self.oHelper.SetButton("Outras Ações", 'Excluir')

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.SearchBrowse('Filial+cargo + Centro Custo',"D MG    %s" %codigo)

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.UTCheckResult("aCab","Q3_CARGO", codigo)
        self.oHelper.UTCheckResult("aCab","Q3_DESCSUM", "GPE-CARGO ALTERADO")
        self.oHelper.UTCheckResult("aCab","Q3_CC", "000000001")
      
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertFalse()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()