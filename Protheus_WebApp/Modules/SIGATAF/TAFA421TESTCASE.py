from tir import Webapp
import unittest

class TAFA421(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATAF','25/04/2019','T1','D MG 01 ','84')
        inst.oHelper.Program('TAFA421')

    def test_TAFA421_CT001(self):
        trab = 'NOMETRABALHADOR'

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01')
        self.oHelper.ClickLabel('S-2200 - Cad. Inicial do Vínculo e Adm./Ing. de Trabalhador.')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.ClickFolder('Trabalhador')
        self.oHelper.ClickFolder('Informações do Trabalhador')
        self.oHelper.SetValue('C9V_CPF', '99999999999')
        self.oHelper.SetValue('C9V_SEXO','M - Masculino', name_attr=True)
        self.oHelper.SetValue('C9V_RCCOR','1 - Branca', name_attr=True)
        self.oHelper.SetValue('C9V_GRINST','000021')
        self.oHelper.SetValue('C9V_NIS','99999999999')
        self.oHelper.SetValue('C9V_PRIEMP','1 - Sim')
        self.oHelper.SetValue('C9V_NOME', trab)
        self.oHelper.SetValue('C9V_DTNASC','20051984')
        self.oHelper.SetValue('C9V_CODPAI','000001')
        self.oHelper.SetValue('C9V_PAINAC','000001')
        self.oHelper.SetValue('C9V_PAIS','000001')
        self.oHelper.ClickFolder('Vínculo')
        self.oHelper.ClickFolder('Informações do Vínculo')   
        self.oHelper.SetValue('C9V_MATRIC', 'MAT004') 
        self.oHelper.SetValue('C9V_CADINI', '1 - Sim (Cadastramento Inicial)') 
        self.oHelper.SetValue('CUP_TPREGT', '1 - CLT - Consolidação das Leis de Trabalho')
        self.oHelper.SetValue('CUP_TPREGP', '1 - Reg. Geral da Previdência Social - RGPS') 
        self.oHelper.ClickFolder('Contrato de Trabalho')
        self.oHelper.SetValue('CUP_CODCAT', '000001')
        self.oHelper.SetValue('CUP_UNSLFX', '5 - Por Mês')
        self.oHelper.SetValue('CUP_TPCONT', '1 - Prazo indeterminado')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')   
        self.oHelper.SetButton('Alterar')
        self.oHelper.ClickFolder('Trabalhador')
        self.oHelper.ClickFolder('Informações do Trabalhador')
        self.oHelper.SetValue('C9V_NOME', 'NOME DO TRABALHADOR')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SearchBrowse('D MG 01 99999999999', key='Filial+cpf + Reg. Ativo?')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.ClickLabel('S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador.')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Outras Ações','Gerar XML em Lote')
        self.oHelper.ClickLabel('S-2200 - Cadastro do Trabalhador')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()