from tir import Webapp
import unittest


class MATA410(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAFAT","10/08/2017","T1","D RJ 01 ","05")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("MATA410")

    def test_MATA410_001(self):
        '''
        Test Case 001
        '''
        order = 'SEL305'

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","000025")
        self.oHelper.SetValue("C5_CONDPAG","001")

        self.oHelper.SetValue("Produto", "COM000000000000000000000000011", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("C6_PRCVEN", "1,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "1,00", grid=True)
        self.oHelper.SetValue("C6_TPOP", "P", grid=True)
        self.oHelper.SetValue("C6_TES", "501", grid=True)

        self.oHelper.SetKey("DOWN", grid=True)

        self.oHelper.SetValue("Produto", "COM000000000000000000000000011", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("Prc Unitario", "1,00", grid=True)
        self.oHelper.SetValue("C6_VALOR", "1,00", grid=True)
        self.oHelper.SetValue("C6_TPOP", "P", grid=True)
        self.oHelper.SetValue("C6_TES", "501", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","000025")
        self.oHelper.CheckResult("C5_CONDPAG","001")

        self.oHelper.CheckResult("Produto", " COM000000000000000000000000011", grid=True, line=1)
        self.oHelper.CheckResult("C6_TPOP", "Prevista", grid=True, line=1)
        self.oHelper.CheckResult("Quantidade", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("Prc Unitario", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("C6_VALOR", "1,00", grid=True, line=1)

        self.oHelper.CheckResult("Produto", " COM000000000000000000000000011", grid=True, line=2)
        self.oHelper.CheckResult("C6_TPOP", "Prevista", grid=True, line=2)
        self.oHelper.CheckResult("Quantidade", "1,00", grid=True, line=2)
        self.oHelper.CheckResult("Prc Unitario", "1,00", grid=True, line=2)
        self.oHelper.CheckResult("C6_VALOR", "1,00", grid=True, line=2)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()