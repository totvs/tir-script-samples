from tir import Webapp
import unittest

class JURA095(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '19/11/2019', 'T1', 'D MG 01 ', '76')
        inst.oHelper.Program('JURA162')
        inst.oHelper.AddParameter('MV_JFTJURI', '', '2', '', '')
        inst.oHelper.AddParameter('MV_JINTVAL', '', '1', '', '')
        inst.oHelper.AddParameter('MV_JALCADA', '', '2', '', '')
        inst.oHelper.AddParameter('MV_JEXCFLH', '', '1', '', '')
        inst.oHelper.SetParameters()

    def test_JURA095_CT001(self):
        assjur = '0000000126'
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', assjur)
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Excluir')
        self.oHelper.WaitProcessing('Carregando...')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.WaitShow('Registro excluído com sucesso.')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Limpar')
        self.oHelper.SetValue('NSZ_COD', assjur)
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
