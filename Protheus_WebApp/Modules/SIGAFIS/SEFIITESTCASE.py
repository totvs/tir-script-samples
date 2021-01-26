from tir import Webapp
# from tir import WebappInternal
import unittest
from datetime import datetime


class SEFII(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''
        inst.oHelper = Webapp()

        DateSystem = datetime.today()

        inst.oHelper.Setup("SIGAFIS", DateSystem.strftime('%d/%m/%Y'), "T1", "M PR 01 ", "09")
        # Nome da rotina do Caso de Teste
        inst.oHelper.Program("SEFII")

    def test_SEFII_001(self):
        '''
        Test Case 001
        '''
        self.oHelper.SetButton('Avançar >>')
        # Parametros para Geração
        self.oHelper.SetValue('Data de', '14/07/2015')
        self.oHelper.SetValue('Data até', '14/07/2015')
        self.oHelper.SetValue('Armazem De:', '')
        self.oHelper.SetValue('Armazem Até:', 'ZZ')
        self.oHelper.SetValue('Livro', "*")
        self.oHelper.SetValue('Diretório do Arquivo Destino', 'C:\\')
        self.oHelper.SetValue('Nome do Arquivo Destino', 'ttnkvx.txt')
        self.oHelper.SetValue('Selecione o Documento a ser gerado', '4')
        self.oHelper.SetValue('Indicador da data do Inventário', '0')
        self.oHelper.SetValue('Seleciona Filiais ?', '0')
        # O ROBÔ NÃO ENCONTRA ESTE ELEMENTO. Ele não se repete nas telas seguintes.
        self.oHelper.SetValue('Gera registro C020 ? (Entrada de Devolução)', '0')
        #
        #     
        self.oHelper.SetValue('Aglutina Seleção por CNPJ + I.E. ?', "1")
        self.oHelper.SetValue('Data Inventário', '')
        # ATENÇÃO: o trecho abaixo é apresentado na tela para ser preenchido toda via no passo-a-passo no JIRA não existe especificação.
        self.oHelper.SetValue('Nome arq. Gerado no Reg. Inv. Mod.P7', '')
        # a label possui mais palavras, porém, o Robô só está reconhecendo apenas este trecho.
        self.oHelper.SetValue('De / Em Terceiros ?', '1')
        self.oHelper.SetValue('Considera Saldo em Processo ?', '0')
        self.oHelper.SetValue('Considera o Saldo Negativo?', '0')
        # Fim dos Parametros para Geração
        self.oHelper.SetButton('Avançar >>')

        # Identificação do Contribuinte
        self.oHelper.SetValue('Código da Finalidade do Arquivo', '0')
        self.oHelper.SetValue('Código do Conteúdo do Arquivo', '30')
        self.oHelper.SetValue('Código de Qualificação do Assinante', '203')
        self.oHelper.SetValue('Nome Responsável', 'TOTVS TESTE')
        self.oHelper.SetValue('CPF Responsável', "09324259920")
        self.oHelper.SetValue('E-Mail', 'teste@teste.com.br')
        # Fim da Identificação do Contribuinte
        self.oHelper.SetButton('Avançar >>')

        # Perfil do Contribuinte
        self.oHelper.SetValue('Indicador de Entrada de Dados', '0')
        self.oHelper.SetValue('Indicador de conteúdo do Arquivo', '7')
        self.oHelper.SetValue('Ind. Exigibilidade Escrit. do ISS:', '9')
        self.oHelper.SetValue('Ind. de Exigibilidade Escrit. do ICMS:', '2')
        self.oHelper.SetValue('Ind. de exigib. do Reg. de Impr. de Doc. Fiscais', "0")
        self.oHelper.SetValue('Ind. de exigib. do Reg. de Utiliz. de Doc. Fiscais', '1')
        self.oHelper.SetValue('Ind. de exigib. do Livro de Mov. de Combustíveis', '1')
        self.oHelper.SetValue('Ind. de exigib. do Registro de Veículos', '1')
        self.oHelper.SetValue('Ind. de exigibilidade do Registro de Inventário', '0')
        self.oHelper.SetValue('Indicador da escrituração contábil','0')
        self.oHelper.SetValue('Ind.Operações sujeitas ao ISS', "1")
        self.oHelper.SetValue('Ind.Oper.suj.retenção ISS-contrib.substituÍdo', '0')
        self.oHelper.SetValue('Ind. de Op. suj. ao ICMS', '0')
        self.oHelper.SetValue('Ind. Oper. Suj. à Subs. Trib.-Contrib.-Substituto:', '0')
        self.oHelper.SetValue('Ind. Oper. Suj. à antecipação tributária do ICMS:', '0')
        self.oHelper.SetValue('Ind.Operação sujeita ao IPI', '0')
        self.oHelper.SetValue('Ind.apresentação avulsa Registro Inventário', "0")
        # Fim do Perfil do Contribuinte
        self.oHelper.SetButton('Avançar >>')

        # Dados do contabilista
        self.oHelper.SetValue('Nome', 'CONTADOR ALISSON')
        self.oHelper.SetValue('CNPJ', '')
        self.oHelper.SetValue('CPF', "36461082824")
        self.oHelper.SetValue('CRC', '26012562')
        self.oHelper.SetValue('UF', 'SP')
        self.oHelper.SetValue('CEP', '99999999')
        self.oHelper.SetValue('Endereço', 'RUA TESTE')
        self.oHelper.SetValue('Número', '')
        self.oHelper.SetValue('Complemento', "")
        self.oHelper.SetValue('Bairro', 'CENTRO')
        self.oHelper.SetValue('CEP Caixa Postal', '99999')
        self.oHelper.SetValue('Caixa Postal', "99999")
        self.oHelper.SetValue('Fone', '06150013030')
        self.oHelper.SetValue('Fax', '06150013035')
        self.oHelper.SetValue('E-Mail','teste@teste.com.br')# Robô procura o elemento mas não acha. Creio que seja porque o elemento se repete em outro lugar.
        self.oHelper.SetValue('Código Município', '53')
        # Fim dos Dados do contabilista
        self.oHelper.SetButton('Avançar >>')  

        # Dados do técnico/empresa
        self.oHelper.SetValue('Nome', 'ALISON')
        self.oHelper.SetValue('CNPJ', '05056597000100')
        self.oHelper.SetValue('CPF', "36461082824")
        self.oHelper.SetValue('Fone', '99999999')
        self.oHelper.SetValue('Fax', '99999999')
        self.oHelper.SetValue('E-Mail', 'teste@teste.com.br')
        #Fim Dados do técnico/empresa
        self.oHelper.SetButton('Avançar >>')

        #Dados do Bloco 8
        self.oHelper.SetValue('Quadro de Cálculo do Valor Adicionado','1')
        self.oHelper.SetValue('Quadro Aquisição de Bens','1')
        self.oHelper.SetValue('Quadro Controle de Crédito Acumulado','1')
        self.oHelper.SetValue('Indicador de Conteúdo','1')
        self.oHelper.SetValue('Imprime Credito ST','1')
        #Fim Dados do Bloco 8
        self.oHelper.SetButton('Finalizar')

        self.oHelper.ClickBox('Filial','M PR 01')
        self.oHelper.SetButton('Ok')
        self.oHelper.WaitHide("Processing")
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')


        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
