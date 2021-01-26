from tir import Webapp
import unittest
from datetime import datetime
import time
DateSystem = datetime.today().strftime("%d/%m/%Y")

class TMKA090(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.SetTIRConfig(config_name="User",value="Admin")
        self.oHelper.SetTIRConfig(config_name="Password",value="1234")
        self.oHelper.Setup("SIGATMK", DateSystem, "T1", "D MG 01 ", "13")
        self.oHelper.Program("TMKA090")

    def test_TMKA090_CT001(self):
        """
        Test Case CT001 - Cadastro de Operadores - Inclusão de um OPERADOR TELEMARKETING
        """
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitShow('Atualização de Operadores - INCLUIR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetValue('Procurar','000390')
        self.oHelper.SetButton('Localizar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Endereco','END.OP.TELEMARKETING')
        self.oHelper.SetValue('Bairro','BAI.OP.TELEMARKETING')
        self.oHelper.SetValue('Municipio','MUN.OP.TELEMKT')
        self.oHelper.SetValue('Estado','SP')
        self.oHelper.SetValue('CEP','01000000')
        self.oHelper.SetValue('CPF/CNPJ','47927781820')
        self.oHelper.SetValue('FAX','01112345678')
        self.oHelper.SetValue('Telefone','01112345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Atendimento','1')
        self.oHelper.SetValue('Regiao','SP')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','01')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Equipe','02')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Equipe','03')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Equipe','04')
        self.oHelper.SetButton('Incluir')
        self.oHelper.ClickGridCell('Grupo', row=3, grid_number=1)
        self.oHelper.SetButton('Apagar')
        self.oHelper.WaitShow("Confirmar a exclusão da Equipe 04?")
        self.oHelper.SetButton('Não')
        self.oHelper.SetButton('Apagar')
        self.oHelper.WaitShow("Confirmar a exclusão da Equipe 04?")
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','e-mail')
        self.oHelper.SetValue('Conta','mail@test.com')
        self.oHelper.SetValue('Senha','1234')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMKA090_CT002(self):
        """
        Test Case CT002 - Cadastro de Operadores - Inclusão de um OPERADOR TELEVENDAS
        """
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitShow('Atualização de Operadores - INCLUIR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetValue('Procurar','000392')
        self.oHelper.SetButton('Localizar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Endereco','END.OP.TELEVENDAS')
        self.oHelper.SetValue('Bairro','BAI.OP.TELEVENDAS')
        self.oHelper.SetValue('Municipio','MUN.OP.TELEVDS')
        self.oHelper.SetValue('Estado','RJ')
        self.oHelper.SetValue('CEP','21000000')
        self.oHelper.SetValue('CPF/CNPJ','28064945755')
        self.oHelper.SetValue('FAX','02112345678')
        self.oHelper.SetValue('Telefone','02112345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','1')
        self.oHelper.SetValue('Atendimento','2')
        self.oHelper.SetValue('Regiao','RJ')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','01')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Equipe','02')
        self.oHelper.SetButton('Incluir')
        self.oHelper.ClickGridCell('Grupo', row=1, grid_number=1)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMKA090_CT003(self):
        """
        Test Case CT003 - Cadastro de Operadores - Inclusão de um OPERADOR TELECOBRANÇA
        """
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitShow('Atualização de Operadores - INCLUIR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetValue('Procurar','000509')
        self.oHelper.SetButton('Localizar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Endereco','END.OP.TELECOBRANCA')
        self.oHelper.SetValue('Bairro','BAI.OP.TELECOBRANCA')
        self.oHelper.SetValue('Municipio','MUN.OP.TELECOB')
        self.oHelper.SetValue('Estado','PE')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','39449131406')
        self.oHelper.SetValue('FAX','08912345678')
        self.oHelper.SetValue('Telefone','08912345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Atendimento','3')
        self.oHelper.SetValue('Regiao','PE')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','01')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMKA090_CT004(self):
        """
        Test Case CT004 - Cadastro de Operadores - Inclusão de um OPERADOR TODOS
        """
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitShow('Atualização de Operadores - INCLUIR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetValue('Procurar','000185')
        self.oHelper.SetButton('Localizar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Endereco','END.OP.TODOS')
        self.oHelper.SetValue('Bairro','BAI.OP.TODOS')
        self.oHelper.SetValue('Municipio','MUN.OP.TODOS')
        self.oHelper.SetValue('Estado','RS')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','45561635018')
        self.oHelper.SetValue('FAX','05512345678')
        self.oHelper.SetValue('Telefone','05512345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Atendimento','4')
        self.oHelper.SetValue('Regiao','RS')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','01')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMKA090_CT005(self):
        """
        Test Case CT005 - Cadastro de Operadores - Inclusão de um OPERADOR TMK/TLV
        """
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitShow('Atualização de Operadores - INCLUIR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetValue('Procurar','000093')
        self.oHelper.SetButton('Localizar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Endereco','END.OP.TMKTLV')
        self.oHelper.SetValue('Bairro','BAI.OP.TMKTLV')
        self.oHelper.SetValue('Municipio','MUN.OP.TMKTLV')
        self.oHelper.SetValue('Estado','GO')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','31847239170')
        self.oHelper.SetValue('FAX','06212345678')
        self.oHelper.SetValue('Telefone','06212345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Atendimento','5')
        self.oHelper.SetValue('Regiao','GO')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','01')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMKA090_CT006(self):
        """
        Test Case CT006 - Cadastro de Operadores - Inclusão de um OPERADOR TELEATENDIMENTO
        """
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitShow('Atualização de Operadores - INCLUIR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetValue('Procurar','000053')
        self.oHelper.SetButton('Localizar')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('Endereco','END.OP.TELEATD')
        self.oHelper.SetValue('Bairro','BAI.OP.TELEATD')
        self.oHelper.SetValue('Municipio','MUN.OP.TELEATD')
        self.oHelper.SetValue('Estado','MT')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','79308100113')
        self.oHelper.SetValue('FAX','04412345678')
        self.oHelper.SetValue('Telefone','04412345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Atendimento','6')
        self.oHelper.SetValue('Regiao','MT')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','01')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    def test_TMKA090_CT007(self):
        """
        Test Case CT007 - Cadastro de Operadores - Alteração de um OPERADOR TELEMARKETING
        """
        self.oHelper.SearchBrowse("D MG 01 TMK012")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Atualização de Operadores - ALTERAR')

        self.oHelper.SetValue('Endereco','END.OP.TELEMARKETING')
        self.oHelper.SetValue('Bairro','BAI.OP.TELEMARKETING')
        self.oHelper.SetValue('Municipio','MUN.OP.TELEMKT')
        self.oHelper.SetValue('Estado','SP')
        self.oHelper.SetValue('CEP','01000000')
        self.oHelper.SetValue('CPF/CNPJ','48509355835')
        self.oHelper.SetValue('FAX','01112345678')
        self.oHelper.SetValue('Telefone','01112345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Regiao','SP')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.ClickGridCell('Grupo', row=1, grid_number=1)
        self.oHelper.SetButton('Apagar')
        self.oHelper.WaitShow("Confirmar a exclusão da Equipe 01?")
        self.oHelper.SetButton('Sim')
        self.oHelper.SetValue('Equipe','02')
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetValue('Equipe','03')
        self.oHelper.SetButton('Incluir')
        self.oHelper.ClickGridCell('Grupo', row=1, grid_number=1)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','e-mail')
        self.oHelper.SetButton("Ok")
        self.oHelper.CheckHelp(text_help="NO_DADOS", button="Fechar")
        self.oHelper.SetValue('Conta','mail@test.com')
        self.oHelper.SetValue('Senha','1234')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Status')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK012')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')

        self.oHelper.CheckResult('U7_COD','TMK012')
        self.oHelper.CheckResult('U7_END','END.OP.TELEMARKETING')
        self.oHelper.CheckResult('U7_BAIRRO','BAI.OP.TELEMARKETING')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_TMKA090_CT008(self):
        """
        Test Case CT008 - Cadastro de Operadores - Alteração de um OPERADOR TELEVENDAS
        """
        self.oHelper.SearchBrowse("D MG 01 TMK013")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Atualização de Operadores - ALTERAR')

        self.oHelper.SetValue('Endereco','END.OP.TELEVENDAS')
        self.oHelper.SetValue('Bairro','BAI.OP.TELEVENDAS')
        self.oHelper.SetValue('Municipio','MUN.OP.TELEVDS')
        self.oHelper.SetValue('Estado','RJ')
        self.oHelper.SetValue('CEP','21000000')
        self.oHelper.SetValue('CPF/CNPJ','92235911714')
        self.oHelper.SetValue('FAX','02112345678')
        self.oHelper.SetValue('Telefone','02112345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','1')
        self.oHelper.SetValue('Regiao','RJ')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','02')
        self.oHelper.SetButton('Incluir')
        self.oHelper.ClickGridCell('Grupo', row=1, grid_number=1)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK013')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')
        self.oHelper.CheckResult('U7_COD','TMK013')
        self.oHelper.CheckResult('U7_END','END.OP.TELEVENDAS')
        self.oHelper.CheckResult('U7_BAIRRO','BAI.OP.TELEVENDAS')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_TMKA090_CT009(self):
        """
        Test Case CT009 - Cadastro de Operadores - Alteração de um OPERADOR TELECOBRANCA
        """
        self.oHelper.SearchBrowse("D MG 01 TMK014")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Atualização de Operadores - ALTERAR')

        self.oHelper.SetValue('Endereco','END.OP.TELECOBRANCA')
        self.oHelper.SetValue('Bairro','BAI.OP.TELECOBRANCA')
        self.oHelper.SetValue('Municipio','MUN.OP.TELECOB')
        self.oHelper.SetValue('Estado','PE')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','46153600450')
        self.oHelper.SetValue('FAX','08912345678')
        self.oHelper.SetValue('Telefone','08912345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Regiao','PE')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Grupos')
        self.oHelper.SetValue('Equipe','02')
        self.oHelper.SetButton('Incluir')
        self.oHelper.ClickGridCell('Grupo', row=2, grid_number=1)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK014')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')
        self.oHelper.CheckResult('U7_COD','TMK014')
        self.oHelper.CheckResult('U7_END','END.OP.TELECOBRANCA')
        self.oHelper.CheckResult('U7_BAIRRO','BAI.OP.TELECOBRANCA')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_TMKA090_CT010(self):
        """
        Test Case CT010 - Cadastro de Operadores - Alteração de um OPERADOR TODOS
        """
        self.oHelper.SearchBrowse("D MG 01 TMK015")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Atualização de Operadores - ALTERAR')

        self.oHelper.SetValue('Endereco','END.OP.TODOS')
        self.oHelper.SetValue('Bairro','BAI.OP.TODOS')
        self.oHelper.SetValue('Municipio','MUN.OP.TODOS')
        self.oHelper.SetValue('Estado','RS')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','85610300037')
        self.oHelper.SetValue('FAX','05512345678')
        self.oHelper.SetValue('Telefone','05512345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Regiao','RS')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK015')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')
        self.oHelper.CheckResult('U7_COD','TMK015')
        self.oHelper.CheckResult('U7_END','END.OP.TODOS')
        self.oHelper.CheckResult('U7_BAIRRO','BAI.OP.TODOS')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_TMKA090_CT011(self):
        """
        Test Case CT011 - Cadastro de Operadores - Alteração de um OPERADOR TMK/TLV
        """
        self.oHelper.SearchBrowse("D MG 01 TMK016")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Atualização de Operadores - ALTERAR')

        self.oHelper.SetValue('Endereco','END.OP.TMKTLV')
        self.oHelper.SetValue('Bairro','BAI.OP.TMKTLV')
        self.oHelper.SetValue('Municipio','MUN.OP.TMKTLV')
        self.oHelper.SetValue('Estado','GO')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','98638270100')
        self.oHelper.SetValue('FAX','06212345678')
        self.oHelper.SetValue('Telefone','06212345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Regiao','GO')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK016')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')
        self.oHelper.CheckResult('U7_COD','TMK016')
        self.oHelper.CheckResult('U7_END','END.OP.TMKTLV')
        self.oHelper.CheckResult('U7_BAIRRO','BAI.OP.TMKTLV')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_TMKA090_CT012(self):
        """
        Test Case CT012 - Cadastro de Operadores - Alteração de um OPERADOR TELEATENDIMENTO
        """
        self.oHelper.SearchBrowse("D MG 01 TMK017")
        self.oHelper.SetButton('Alterar')
        self.oHelper.WaitShow('Atualização de Operadores - ALTERAR')

        self.oHelper.SetValue('Endereco','END.OP.TELEATD')
        self.oHelper.SetValue('Bairro','BAI.OP.TELEATD')
        self.oHelper.SetValue('Municipio','MUN.OP.TELEATD')
        self.oHelper.SetValue('Estado','MT')
        self.oHelper.SetValue('CEP','89000000')
        self.oHelper.SetValue('CPF/CNPJ','04371420192')
        self.oHelper.SetValue('FAX','04412345678')
        self.oHelper.SetValue('Telefone','04412345678')
        self.oHelper.SetValue('Participante','000002')

        self.oHelper.ClickFolder('Perfil')
        self.oHelper.SetValue('Vendedor','2')
        self.oHelper.SetValue('Regiao','MT')
        self.oHelper.SetValue('Habilidade','000001')

        self.oHelper.SetButton('Outras Ações','Habilidade')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Outras Ações','Tool Bar')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(5)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        time.sleep(3)
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')

        time.sleep(5)

        self.oHelper.SearchBrowse("D MG 01 TMK017")
        self.oHelper.SetButton('Visualizar')
        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')
        self.oHelper.CheckResult('U7_COD','TMK017')
        self.oHelper.CheckResult('U7_END','END.OP.TELEATD')
        self.oHelper.CheckResult('U7_BAIRRO','BAI.OP.TELEATD')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    def test_TMKA090_CT013(self):
        """
        Test Case CT013 - Cadastro de Operadores - Exclusão de um OPERADOR TELEMARKETING
        """
        self.oHelper.SearchBrowse("D MG 01 TMK018")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow('Atualização de Operadores - EXCLUIR')

        self.oHelper.SetButton('Confirmar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK018')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('U7_COD','TMK018')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertFalse()

    def test_TMKA090_CT014(self):
        """
        Test Case CT014 - Cadastro de Operadores - Exclusão de um OPERADOR TELEVENDAS
        """
        self.oHelper.SearchBrowse("D MG 01 TMK019")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow('Atualização de Operadores - EXCLUIR')

        self.oHelper.SetButton('Confirmar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK019')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('U7_COD','TMK019')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertFalse()

    def test_TMKA090_CT015(self):
        """
        Test Case CT015 - Cadastro de Operadores - Exclusão de um OPERADOR TELECOBRANCA
        """
        self.oHelper.SearchBrowse("D MG 01 TMK020")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow('Atualização de Operadores - EXCLUIR')

        self.oHelper.SetButton('Confirmar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK020')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('U7_COD','TMK020')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertFalse()

    def test_TMKA090_CT016(self):
        """
        Test Case CT016 - Cadastro de Operadores - Exclusão de um OPERADOR TODOS
        """
        self.oHelper.SearchBrowse("D MG 01 TMK021")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow('Atualização de Operadores - EXCLUIR')

        self.oHelper.SetButton('Confirmar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK021')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('U7_COD','TMK021')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertFalse()

    def test_TMKA090_CT017(self):
        """
        Test Case CT017 - Cadastro de Operadores - Exclusão de um OPERADOR TMK/TLV
        """
        self.oHelper.SearchBrowse("D MG 01 TMK022")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow('Atualização de Operadores - EXCLUIR')

        self.oHelper.SetButton('Confirmar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK022')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('U7_COD','TMK022')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertFalse()

    def test_TMKA090_CT018(self):
        """
        Test Case CT018 - Cadastro de Operadores - Exclusão de um OPERADOR TELEATENDIMENTO
        """
        self.oHelper.SearchBrowse("D MG 01 TMK023")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.WaitShow('Atualização de Operadores - EXCLUIR')

        self.oHelper.SetButton('Confirmar')

        time.sleep(5)

        self.oHelper.SearchBrowse('D MG 01 TMK023')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.CheckResult('U7_COD','TMK023')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertFalse()

    def test_TMKA090_CT019(self):
        """
        Test Case CT019 - Cadastro de Operadores - Consulta de um OPERADOR TELEMARKETING
        """
        self.oHelper.SearchBrowse("D MG 01 TMK012")
        self.oHelper.SetButton('Visualizar')

        self.oHelper.WaitShow('Atualização de Operadores - VISUALIZAR')
        self.oHelper.SetButton('Outras Ações','Usuarios')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.CheckResult('U7_COD','TMK012')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case.
        """
        self.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()