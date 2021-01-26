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

        # Efetua a exclusão de um assunto jurídico
        print('CT001 - Efetua a exclusão de um assunto jurídico')
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

    def test_JURA095_CT002(self):
        assjur = '0000000127'

        # Vincula um assunto jurídico
        print('CT002 - Vincula um assunto jurídico')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', assjur)
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.WaitProcessing('Carregando...')
        self.oHelper.SetButton('Outras ações', 'Vinculados')
        self.oHelper.SetButton('Vincular')
        self.oHelper.SetValue('Código do cliente', 'JLT001')
        self.oHelper.SetValue('Loja do cliente', '01')
        self.oHelper.SetValue('Núm Caso', '000019')
        self.oHelper.SetButton('Pesquisar')
        self.oHelper.SetButton('Vincular')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    def test_JURA095_CT003(self):
        assjur = '0000000127'

        # Desvincula um assunto jurídico
        print('CT003 - Desvincula um assunto jurídico')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', assjur)
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.WaitProcessing('Carregando...')
        self.oHelper.SetButton('Outras ações', 'Vinculados')
        self.oHelper.SetButton('Desvincular')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    def test_JURA095_CT004(self):
        assjur = '0000000166'

        # Relaciona um assunto jurídico com um outro
        print('CT004 - Relaciona um assunto jurídico com um outro')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Criminal', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', assjur)
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.WaitProcessing('Carregando...')
        self.oHelper.SetButton('Outras ações', 'Relacionados')
        self.oHelper.SetButton('Vincular')
        self.oHelper.SetValue('Código Assunto Jurídico', '0000000167')
        self.oHelper.SetButton('Pesquisar')
        self.oHelper.SetButton('Vincular')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    def test_JURA095_CT005(self):
        assjur = '0000000166'

        # Desfaz relacionamento de um assunto jurídico com um outro
        print('CT005 - Desfaz relacionamento de um assunto jurídico com um outro')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Criminal', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', assjur)
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Alterar')
        self.oHelper.WaitProcessing('Carregando...')
        self.oHelper.SetButton('Outras ações', 'Relacionados')
        self.oHelper.SetButton('Desvincular')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Sair')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()

    # def test_JURA095_CT006(self):

    #     # Relaciona um assunto jurídico com um outro
    #     assjur = '0000000131'
    #     print('CT006 - Relaciona um assunto jurídico com um outro')
    #     self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
    #     self.oHelper.SetValue('NSZ_COD', assjur)
    #     self.oHelper.ClickLabel('Pesquisar')
    #     self.oHelper.ClickGridCell('Situacao', 1)
    #     self.oHelper.ClickLabel('Alterar')
    #     self.oHelper.WaitProcessing('Carregando...')
    #     self.oHelper.SetButton('Outras ações', 'Incidentes')
    #     self.oHelper.ClickLabel('Abrir Lista de Incidentes')
    #     self.oHelper.SetButton('Vincular')
    #     self.oHelper.SetValue('Código do cliente', 'JLT001')
    #     self.oHelper.SetValue('Loja do cliente', '01')
    #     self.oHelper.SetValue('Núm Caso', '000023')
    #     self.oHelper.SetButton('Pesquisar')
    #     self.oHelper.SetButton('Vincular')
    #     self.oHelper.SetButton('Sim')
    #     self.oHelper.SetButton('Fechar')
    #     self.oHelper.SetButton('Sair')
    #     self.oHelper.SetButton('Confirmar')
    #     self.oHelper.SetButton('Fechar')
    #     self.oHelper.SetButton('Fechar')
    #     self.oHelper.ClickLabel('Sair')
    #     self.oHelper.AssertTrue()

    # def test_JURA095_CT007(self):

    #     # Desfaz relacionamento de um assunto jurídico com um outro
    #     print('CT005 - Desfaz relacionamento de um assunto jurídico com um outro')
    #     self.oHelper.Program('JURA162')
    #     assjur = '0000000131'
    #     self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
    #     self.oHelper.SetValue('NSZ_COD', assjur)
    #     self.oHelper.ClickLabel('Pesquisar')
    #     self.oHelper.ClickGridCell('Situacao', 1)
    #     self.oHelper.ClickLabel('Alterar')
    #     self.oHelper.WaitProcessing('Carregando...')
    #     self.oHelper.SetButton('Outras ações', 'Incidentes')
    #     self.oHelper.ClickLabel('Abrir Lista de Incidentes')
    #     self.oHelper.SetButton('Desvincular')
    #     self.oHelper.SetButton('Sim')
    #     self.oHelper.SetButton('Fechar')
    #     self.oHelper.SetButton('Sair')
    #     self.oHelper.SetButton('Confirmar')
    #     self.oHelper.SetButton('Fechar')
    #     self.oHelper.SetButton('Fechar')
    #     self.oHelper.ClickLabel('Sair')
    #     self.oHelper.AssertTrue()

    def test_JURA095_CT008(self):

        # Desfaz relacionamento de um assunto jurídico com um outro
        print('CT008 - Realiza a correção de valores geral')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue('cValor', 'Contencioso', name_attr=True)
        self.oHelper.SetValue('NSZ_COD', '0000000115')
        self.oHelper.ClickLabel('Pesquisar')
        self.oHelper.ClickGridCell('Situacao', 1)
        self.oHelper.ClickLabel('Correção Monetária')
        self.oHelper.WaitShow("1 registros tiveram os valores atualizados com sucesso.")
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Visualizar')
        self.oHelper.SetButton('Garantias')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('NT2_SGARA','68483203,')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('X')
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickLabel('Sair')
        self.oHelper.AssertTrue()
        self.oHelper.RestoreParameters()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
