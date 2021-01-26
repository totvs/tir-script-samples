from tir import Webapp
import unittest


class GTPA421(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '29/04/2020', 'T1', 'D MG 01 ', '05')
        inst.oHelper.Program('GTPA421')

    def test_GTPA421_CT002(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG')

        self.oHelper.SetValue('Agência', '000005')
        self.oHelper.SetValue('Dt. Inicial', '29/04/2020')
        self.oHelper.SetValue('Dt. Final', '27/04/2020')
        self.oHelper.CheckHelp(text='Dt. Final', button='Fechar')
        self.oHelper.CheckResult('Dt. Final', '27/04/2020')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AssertTrue()

    def test_GTPA421_CT003(self):

        self.oHelper.SearchBrowse("D MG    000009", "Filial+agência + Data Remessa + Data Caixa + Data Movim")
        self.oHelper.SetButton("Outras Ações","Conferência de Taxas")
        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Conferir Todos")
        self.oHelper.SetButton("Outras Ações","Altera Contr. Docto.")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
