from tir import Webapp
import unittest
from datetime import datetime

class COTEPE35(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        DateSystem = datetime.today()
        inst.oHelper.Setup('SIGAFIS', DateSystem.strftime(
            '%d/%m/%Y'), 'T1', 'X FIS10', '09')
        inst.oHelper.Program('COTEPE35')

    def test_COTEPE35_CT001(self):
        '''
        Test Case 001
        '''

        # PARAMETROS
        self.oHelper.SetValue('Opção de Geração ?            ', 'Arq magnético')
        self.oHelper.SetValue('Seleciona Filiais ?', 'Sim')
        self.oHelper.SetValue('Reg.0210 - Estrutura Produto ?', 'Completa')
        self.oHelper.SetValue('Aglutina seleção por CNPJ+IE ?', 'Sim')
        self.oHelper.SetValue('Considerar entrada ou baixa ?', 'Baixa')

        #CONFIRMA PARAMETROS 
        self.oHelper.SetButton('OK')

        #ESCOLHE A FILIAL A SER CONSIDERADA
        self.oHelper.ClickBox('Filial', 'X FIS25')  

        # CLICA EM OK PARA CONFIRMAR A FILIAL A SER CONSIDERADA
        self.oHelper.SetButton('Ok')

        # CLICA EM AVANÇAR PARA COMEÇAR A PREENCHER AS INFORMAÇÕES NECESSÝRIAS PARA A GERAÇÃO DO MEIO-MAGNÉTICO QUE TRATA O ATO COTEPE N.35/05
        self.oHelper.SetButton('Avançar >>')

        # PARAMETROS PARA GERACAO
        self.oHelper.SetValue('Data de', '01/11/2018')
        self.oHelper.SetValue('Data até', '30/11/2018')
        self.oHelper.SetValue('Livro', '*')
        self.oHelper.SetValue('Diretório do Arquivo Destino', 'C:\\')
        self.oHelper.SetValue('Nome do Arquivo Destino', 'COTEPE35.TXT')
        self.oHelper.SetValue('Gera Inventário', '1')
        self.oHelper.SetValue('Gera Registros Complentares de Frete', '1')
        self.oHelper.SetValue('Gera Detalhe de Notas Fiscais (Blocos C e D)', '1')
        self.oHelper.SetValue('Contribuinte do Simples - Nacional', '1')
        self.oHelper.SetValue('Data Inventário', '//')
        self.oHelper.SetValue('Gera Registro B350?', '1')
        self.oHelper.SetValue('Gera Registro B475?', '1')
        self.oHelper.SetValue('Gera Bloco E?', '2')
        self.oHelper.SetValue('Titulo RPS Autonomos?', '1')
        # self.oHelper.SetValue('Motivo do InventÃ¡rio','1')
        # self.oHelper.SetValue('Programa de adesÃ£o Ã  Nota Legal','2')

        self.oHelper.SetButton('Avançar >>')

        #IDENTIFICAÇÃO DO CONTRIBUINTE)
        self.oHelper.SetValue('Código da Finalidade do Arquivo', '00')
        self.oHelper.SetValue('Indicador de Centralização de escrituração', '0')
        # DADOS CADASTRAIS
        self.oHelper.SetValue('E-Mail', 'SQA_FISCAL@TOTVS.COM.BR')

        self.oHelper.SetButton('Avançar >>')

        #DADOS DO CONTABILISTA
        self.oHelper.SetValue('Nome', 'Antonio Alves')
        self.oHelper.SetValue('CNPJ', '')
        self.oHelper.SetValue('CPF', '96848518476')
        self.oHelper.SetValue('CRC', '1SP308673')
        self.oHelper.SetValue('UF', 'DF')
        self.oHelper.SetValue('CEP', '70002900')
        self.oHelper.SetValue('Endereço', 'Sbn Quadra 1 Bloco A')
        self.oHelper.SetValue('Número', '100')
        self.oHelper.SetValue('Complemento', 'Terreo')
        self.oHelper.SetValue('Bairro', 'Asa Norte')
        self.oHelper.SetValue('CEP Caixa Postal', '70002900')
        self.oHelper.SetValue('Caixa Postal', '755092')
        self.oHelper.SetValue('Fone', '6140225050')
        self.oHelper.SetValue('Fax', '6140225051')
        self.oHelper.SetValue('E-Mail', 'ANTONIO@TOTVS.COM.BR')

        self.oHelper.SetButton('Avançar >>')    

        #DADOS DO TÉCNICO/EMPRESA
        self.oHelper.SetValue('Nome', 'Joao Alves')
        self.oHelper.SetValue('CNPJ', '')
        self.oHelper.SetValue('CPF', '85989334222')
        self.oHelper.SetValue('Fone', '6140225050')
        self.oHelper.SetValue('Fax', '6140225051')
        self.oHelper.SetValue('E-Mail', 'JOAO@TOTVS.COM.BR')

        self.oHelper.SetButton('Finalizar')

        self.oHelper.WaitHide("Processing")

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()