from tir import Webapp
import unittest

class WMSC015(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAWMS", "10/12/2020", "T1", "M SP 01", "42")
        inst.oHelper.Program("WMSC015")

    def test_WMSC015_CT001(self):

        self.oHelper.SetValue('Armazém De ?', '')
        self.oHelper.SetValue('Armazém Até ?', 'ZZ')
        self.oHelper.SetValue('Produto De ?', '')
        self.oHelper.SetValue('Produto Até ?', 'ZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Filial De ?', 'D MG 01')
        self.oHelper.SetValue('Filial Até ?', 'XSFIS22')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Kardex')

        self.oHelper.SetButton('X')

        self.oHelper.ClickFolder('Lote')
        self.oHelper.ClickFolder('Endereço')
        self.oHelper.ClickFolder('Sequencia de Abastecimento')
        self.oHelper.ClickFolder('Picking Fixo')
        self.oHelper.ClickFolder('Zona Alternativa')
        self.oHelper.ClickFolder('Pedido Liberado')
        self.oHelper.ClickFolder('Lote com Bloqueio')
        self.oHelper.ClickFolder('Empenhado')
        self.oHelper.ClickFolder('Serviço')
        self.oHelper.ClickFolder('OP')
        self.oHelper.ClickFolder('Empenho OP')
        self.oHelper.ClickFolder('Movimentos Internos')

        self.oHelper.SetButton('X')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()

