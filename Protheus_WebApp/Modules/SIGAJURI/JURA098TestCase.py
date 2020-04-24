from tir import Webapp
import unittest

class JURA098(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '15/10/2018', 'T1', 'D MG 01 ', '05')
        inst.oHelper.Program('JURA162')
        inst.oHelper.AddParameter('MV_JFTJURI', '', '2', '', '')
        inst.oHelper.AddParameter('MV_JINTVAL', '', '1', '', '')
        inst.oHelper.AddParameter('MV_JALCADA', '', '2', '', '')
        inst.oHelper.SetParameters()

    def test_JURA098_CT001(self):
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', '0000000121')
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.SetButton('Garantias')
        self.oHelper.SetButton('Outras ações', 'Levantamento,Inclusão')
        self.oHelper.SetButton('Sim')
        self.oHelper.ClickBox('Tipo', select_all=True)
        self.oHelper.SetButton('Outras Ações', 'Confirmar')
        self.oHelper.SetValue('NT2_CTPGAR', '002')
        self.oHelper.SetValue('NT2_CNATUT', '0001')
        self.oHelper.SetValue('NT2_CTIPOT', 'AF')
        self.oHelper.F3(field='NT2_CFORNT', name_attr=True)
        self.oHelper.SetButton('Limpar')
        self.oHelper.SetValue('Palavra-chave', '000002')
        self.oHelper.SetButton('Pesquisar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.WaitProcessing('PROCESSANDO')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
