from tir import Webapp 
import unittest
from datetime import datetime
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
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        self.oHelper.ClickCheckBox('Marca / Desmarca Todos')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()