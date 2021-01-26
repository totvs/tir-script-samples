from tir import Webapp
import unittest

class OGA430F(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',"15/07/2020",'T1','D MG 01 ','67')
        inst.oHelper.Program('OGA450')
        
    def test_OGA430F_CT001(self):
        ##Cenario de teste para excluir fixação de contrato de compra a fixar - fixação com status 1=aberto
        ## A fixação deve ser excluida com sucesso pois é a fixação e não possui vinculo com romaneio
        self.oHelper.SetValue("Entidade", "000002")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")
             
        self.oHelper.SearchBrowse("D MG 01 "+"2"+"01"+"1920           "+"AGR-SOJA GRANEL")       
        self.oHelper.ScrollGrid(column="Contrato", match_value="000116", grid_number=2)
        self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True) 
        
        self.oHelper.WaitShow("Fixações do Contrato : 000116")
        self.oHelper.SearchBrowse("D MG 01 "+"000116"+"002")
        self.oHelper.SetButton('Outras Ações',"Excluir")
        self.oHelper.CheckResult("NN8_CODCTR", user_value = "000116")
        self.oHelper.CheckResult("NN8_ITEMFX", user_value = "002")
        self.oHelper.SetButton("Confirmar")   
        self.oHelper.SetButton("Fechar") 
        self.oHelper.AssertTrue() ##foi excluido
        
        self.oHelper.SearchBrowse("D MG 01 "+"000116"+"002") 
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("NN8_CODCTR", user_value = "000116")
        self.oHelper.CheckResult("NN8_ITEMFX", user_value = "002")
        self.oHelper.SetButton("Fechar") 
        self.oHelper.AssertFalse() ##não foi encontrado
        
    def test_OGA430F_CT002(self):
        ##Cenario de teste para excluir fixação de contrato de compra a fixar - fixaçao com status 3=Parcial
        ## A fixação não pode ser excluida pois ja possui romaneio vinculado
        self.oHelper.SetValue("Entidade", "000002")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")
             
        self.oHelper.SearchBrowse("D MG 01 "+"2"+"01"+"1920           "+"AGR-SOJA GRANEL")       
        self.oHelper.ScrollGrid(column="Contrato", match_value="000116", grid_number=2)
        self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True) 
        
        self.oHelper.SearchBrowse("D MG 01 "+"000116"+"001")
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.WaitShow("Ajuda")			
        self.oHelper.CheckHelp(text_problem="Operação não permitida para Fixação com STATUS diferente de 1=Aberto", button="Fechar")
               
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
