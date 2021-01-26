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

        # Efetua o levantamento automatico (Levantamento em massa)
        print('CT001 - Efetua o levantamento automatico (Levantamento em massa)')
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
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    def test_JURA098_CT002(self):

        # Excusão de levantamento automatico (Levantamento em massa)
        print('CT002 - Exclusão de levantamento automatico (Levantamento em massa)')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', '0000000121')
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.SetButton('Garantias')
        self.oHelper.SetButton('Outras ações', 'Levantamento,Exclusão')
        self.oHelper.SetButton('Sim')
        self.oHelper.ClickBox('Tipo', select_all=True)
        self.oHelper.SetButton('Outras Ações', 'Excluir')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    def test_JURA098_CT003(self):

        # Exclusão de levantamento e garantia
        print('CT003 - Exclusão de levantamento e garantia')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', '0000000122')
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.SetButton('Garantias')
        self.oHelper.SearchBrowse('00000001220000000125')
        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SearchBrowse('00000001220000000124')
        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    def test_JURA098_CT004(self):

        # Verifica a validação da exclusão de garantia com levantamento
        print('CT004 - Verifica a validação da exclusão de garantia com levantamento')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', '0000000123')
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.SetButton('Garantias')
        self.oHelper.SearchBrowse('00000001230000000126')
        self.oHelper.SetButton('Outras ações', 'Excluir')
        self.oHelper.SetButton('Confirmar') 
        self.oHelper.CheckHelp(text_problem="Problema: Existe(m) levantamento(s) vinculado(s) a esta garantia. Exclusão não permitida.", button="Fechar")
        self.oHelper.SetButton('Fechar')
        self.oHelper.SearchBrowse('00000001230000000127')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult('NT2_CTPGAR','002')
        self.oHelper.AssertTrue()
        self.oHelper.RestoreParameters()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
