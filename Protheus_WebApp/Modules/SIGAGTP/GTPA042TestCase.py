from tir import Webapp
import unittest


class GTPA042(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '14/08/2020', 'T1', 'D MG 01 ')
        inst.oHelper.Program('GTPA042')
       
    # Efetua o cadastro de evento para envio de e-mail
    print('CT001 - inclui evento para Envio de e-mails')

    def test_GTPA042_CT001(self):
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('GZ8_DESEVE', 'AUTOMACAO ENVIO DE EMAIL')
        self.oHelper.SetValue('GZ8_TEXTO', 'AUTOMACAO ENVIO DE EMAIL TEXTO E-MAIL')
        self.oHelper.SetValue('GZ8_STATUS', '1')
        self.oHelper.SetValue('GZ8_TITULO', 'AUTOMACAO ENVIO DE EMAIL TITULO')
        self.oHelper.SetValue('GZ8_RECOR', '2')
        self.oHelper.SetValue('GZ6_CODIGO', '000002')
        self.oHelper.SetButton('Outras Ações','Automação')
        self.oHelper.SetValue('GY5_ENTIDA', 'G57')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetValue('GY6_CAMPO1', 'G57_AGENCI')
        self.oHelper.SetValue('GY6_CONTEU', '000050')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
