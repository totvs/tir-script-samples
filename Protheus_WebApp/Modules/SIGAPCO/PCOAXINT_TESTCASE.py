from tir import Webapp 
import unittest

class PCOAXINT(unittest.TestCase):

    @classmethod
    def setUpClass(inst): 
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACOM', '25/08/2020', 'T1', 'M SP 01 ')
        inst.oHelper.Program('MATA110')

        inst.oHelper.AddParameter("MV_PCOINTE", "", "1")
        inst.oHelper.SetParameters()

    def test_PCOAXINT_CT001(self): 

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01")

        self.oHelper.SetValue("Produto","000000000000000000000000000035",grid=True,row=1)
        self.oHelper.SetValue("Quantidade","1,00",grid=True,row=1)
        self.oHelper.SetValue("Vlr Unitario","333,00",grid=True,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')

        self.oHelper.WaitShow("Solicitaçäo de Compras - INCLUIR")
        self.oHelper.ClickFolder("Variaveis")
        self.oHelper.SetValue("cVar",'1',name_attr=True)
        self.oHelper.SetValue("cVar","'A'",name_attr=True)
        self.oHelper.SetValue("cVar",".T.",name_attr=True)
        self.oHelper.SetValue("cVar","{'TESTE','TESTEB'}",name_attr=True)

        self.oHelper.SetButton('x') 
        self.oHelper.SetButton('Cancelar') 

        self.oHelper.AssertTrue()

    def test_PCOAXINT_CT002(self): 

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")

        self.oHelper.SetValue("Produto","000000000000000000000000000035",grid=True,row=1)
        self.oHelper.SetValue("Quantidade","1,00",grid=True,row=1)
        self.oHelper.SetValue("Vlr Unitario","333,00",grid=True,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')

        self.oHelper.WaitShow("Solicitaçäo de Compras - INCLUIR")
        self.oHelper.SetButton('>>')

        self.oHelper.SetButton('x') 
        self.oHelper.SetButton('Cancelar') 

        self.oHelper.AssertTrue()

    def test_PCOAXINT_CT003(self): 

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01")

        self.oHelper.SetValue("Produto","000000000000000000000000000035",grid=True,row=1)
        self.oHelper.SetValue("Quantidade","1,00",grid=True,row=1)
        self.oHelper.SetValue("Vlr Unitario","333,00",grid=True,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')

        self.oHelper.WaitShow("Solicitaçäo de Compras - INCLUIR")

        self.oHelper.SetButton('Salvar') 
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Confirmar')

        self.oHelper.AssertTrue()
    
    ## Para criaçao de mais testcase olhar no setup class e avaliar o valor do parametro MV_PCOINTE
    
        
    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  


if __name__ == "__main__":
    unittest.main()