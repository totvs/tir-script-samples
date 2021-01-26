from tir import Webapp
import unittest
import time


class JURA163(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '16/07/2019', 'T1', 'D MG 01 ', '76')
        inst.oHelper.Program('JURA163')

    def test_JURA163_CT001(self):
        self.oHelper.ClickFolder("Grupos")
        self.oHelper.ClickFolder("Principal")
        self.oHelper.ClickGridCell("Descrição", row=1)
        self.oHelper.SetButton("Alterar")
        self.oHelper.ClickFolder("Campos")
        self.oHelper.ScrollGrid(column="Campo", match_value="NSZ_CFCORR")
        self.oHelper.SetValue('Obrigatório', True, grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_JURA163_CT002(self):
        print('CT002 - Inclusão/ Alteração/ Exclusão de Configuração de campos')
        # Inclui configuração de campos
        self.oHelper.ClickFolder('Configura Campo')
        self.oHelper.ClickIcon('Incluir')
        self.oHelper.SetValue('NVH_DESC', 'AAAAA_TIR_J163', name_attr=True)
        self.oHelper.SetValue('NVH_TABELA', 'NSZT10', name_attr=True)
        self.oHelper.SetValue('NVH_CAMPO', 'NSZ_MODPRO', name_attr=True)
        self.oHelper.ClickIcon('Salvar')
        # Altera configuração de campos
        self.oHelper.ClickGridHeader(column_name='Descricao', grid_number=1)
        self.oHelper.ClickGridCell('Descricao', 1)
        self.oHelper.ClickIcon('Alterar')
        self.oHelper.CheckResult('NVH_DESC', 'AAAAA_TIR_J163')
        self.oHelper.SetValue('NVH_DESC', 'AAAAA_TIR_J163', name_attr=True)
        self.oHelper.SetValue('NVH_TPPESQ', '1 - Processo', name_attr=True)
        self.oHelper.ClickIcon('Salvar')
        # Cria configuração de pesquisa com a configuração de campos cadastrada
        self.oHelper.ClickFolder('Configura Pesquisa')
        self.oHelper.SetButton('Nova')
        self.oHelper.SetValue('cDescConf', 'TIR_J163', name_attr=True)
        self.oHelper.SetButton('Adiciona todos Campos')
        self.oHelper.SetValue('NSZ_MODPRO', '1', name_attr=True)
        self.oHelper.SetButton('Salvar')
        self.oHelper.WaitHide("Atualizando...")
        self.oHelper.SetButton('Nova')
        self.oHelper.SetButton('Adiciona Campo')
        self.oHelper.SetButton('Deleta todos Campos')
        self.oHelper.SetButton('Cancelar')
        # Exclui configuração de campo
        self.oHelper.ClickFolder('Configura Campo')
        self.oHelper.ClickGridCell('Descricao', 1)
        self.oHelper.ClickIcon('Excluir')
        self.oHelper.SetButton('Sim')

        self.oHelper.AssertTrue()

    def test_JURA163_CT003(self):
        print('CT003 - Inclusão de Usuario X Pesquisa utilizando o "Criar como..."')
        # Inclui configuração de campo
        self.oHelper.ClickFolder('Grupos')
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue('NZX_DESC', 'TIR_J163')
        self.oHelper.SetValue('NZX_TIPOA', '1')
        self.oHelper.ClickGridCell("Cód Usuário", row=1)
        self.oHelper.SetValue("NZY_CUSER", "000483", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        # Cria Usuario X Pesquisa utilizando o "Criar como..."
        self.oHelper.ClickFolder('Relaciona Pesquisa')
        self.oHelper.ClickGridCell('Código', 1)
        self.oHelper.SetButton("Outras Ações", "Criar Como...")
        time.sleep(3)
        self.oHelper.SetButton("Outras Ações", "Criar Como...")
        self.oHelper.F3(field="NVK_CGRUP", name_attr=True)
        self.oHelper.ScrollGrid(column="Descrição", match_value="TIR_J163")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue('NVK_CPESQ', '078')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        # Exclui o relacionamento Usuario X Pesquisa criado
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.CheckResult('NVK_CPESQ', '078')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("X")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
