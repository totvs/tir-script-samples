from tir import Webapp
import unittest
import datetime

class OMSA210(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGAOMS',dataAtual,'T1','D MG 01 ','39')
        inst.oHelper.Program("OMSA210")

    #Associação
    def test_OMSA210_CT001(self):

        self.oHelper.WaitShow('Associacao do Veiculo')
        
        self.oHelper.SetButton("Associacao")      
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.ClickBox("Codigo","000019",grid_number = 1)
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetValue("nQtdeUni", "1", name_attr=True)  
        self.oHelper.SetValue("cCodUni", "000001", name_attr=True)  
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    #Estorno
    def test_OMSA210_CT002(self): 

        self.oHelper.SetButton("Outras Ações","Estorno") 
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()    

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
