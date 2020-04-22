from tir import Webapp
import unittest
from datetime import datetime


class MATA940(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        DateSystem = datetime.today()
        inst.oHelper.Setup('SIGAFIS', DateSystem.strftime(
            '%d/%m/%Y'), 'T1', 'X FIS16', '09')
        inst.oHelper.Program('MATA940')

    def MATA940_001(self):
        '''
        Test Case 001
        '''

        # self.oHelper.SetButton('Livros Fiscais (1)')
        # self.oHelper.SetButton('Arq. Magneticos (1)')
        # self.oHelper.SetButton('Sintegra')

        # CLICA NO BOT�O PARAMETROS
        self.oHelper.SetButton('Param.')

        # SEÇÃO DE DEFINIÇÃO DE PARAMETROS
        self.oHelper.SetValue('Data Inicial ?', '01/05/2016')
        self.oHelper.SetValue('Data Final ?', '31/05/2016')
        self.oHelper.SetValue('LayOut?', 'sintmg05')
        self.oHelper.SetValue('Arquivo Destino?', 'sintmg.txt')
        self.oHelper.SetValue('Finalidade?', 'Normal')
        self.oHelper.SetValue('UF Origem/Destino?', '')
        self.oHelper.SetValue('Processa UF?', 'Exceto a UF')
        self.oHelper.SetValue('Numero do Livro?', '*')
        self.oHelper.SetValue('Equipamento?', '')
        self.oHelper.SetValue('Gera Inventario?', 'Nao')
        self.oHelper.SetValue('Notas Fiscais?', 'Entrada')
        # self.oHelper.SetValue('Gera Reg.60I e 60D ?','')
        self.oHelper.SetValue('Drive Destino ?', 'C:\\')
        self.oHelper.SetValue('Transportadora ?','')
        self.oHelper.SetValue('Data de Fechamento ?', '31052016')
        self.oHelper.SetValue('Gera Registro 60R ?', 'Nao')
        self.oHelper.SetValue('Gera Registro 61R ?', 'Nao')
        self.oHelper.SetValue('Gera NF Produtor ?', 'Nao')
        self.oHelper.SetValue('Meio magnetico ?', 'FITA')
        self.oHelper.SetValue('Fator de bloco ?', '')
        self.oHelper.SetValue('Natureza Operacoes ?', 'Totalidade')
        self.oHelper.SetValue('Destaca PIS/COFINS ?', 'Sim')
        self.oHelper.SetValue('NF De ?', '')
        self.oHelper.SetValue('NF Ate ?', 'ZZZZ')
        self.oHelper.SetValue('Filial de ?', '')
        self.oHelper.SetValue('Filial Ate ?', 'ZZZZZZ')
        self.oHelper.SetValue('Consolidação na mesma UF ?', 'Nao')
        self.oHelper.SetValue('Filtro Tipo Produto ?', '')
        self.oHelper.SetValue('Produto De ?', '')
        self.oHelper.SetValue('Produto Ate ?', 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Armazem De ?', '')
        self.oHelper.SetValue('Armazem Ate ?', 'ZZ')
        self.oHelper.SetValue('Prods.c/Saldo Neg. ?', 'Nao')
        self.oHelper.SetValue('Prods.c/Saldo Zera. ?', 'Nao')
        self.oHelper.SetValue('Prods.c/Saldo Poder 3º. ?', 'Nao')
        self.oHelper.SetValue('Prods.c/Custo Zera. ?', 'Nao')
        self.oHelper.SetValue('Gera 88 MG ?', 'Nao')
        self.oHelper.SetValue('Data 88 ?', '')
        self.oHelper.SetValue('Gera Relat. Rest. MG ?', 'Nao')
        self.oHelper.SetValue('Saldo Processo ?', 'Nao')
        self.oHelper.SetValue('Lista MOD Processo ?', 'Nao')
        self.oHelper.SetValue('Seleciona Filiais ?', 'Sim')
        self.oHelper.SetValue('Gera registro 60I ?', 'Nao')
        self.oHelper.SetValue('Gera reg. Tipo 88 Det. 06 ?', 'Nao')
        self.oHelper.SetValue('Gera reg. 8827 e 8828 ?', 'Nao')
        self.oHelper.SetValue('Gera reg. 8830 ?', 'Nao')
        self.oHelper.SetValue('Simples Nacional ?', 'Nao')
        self.oHelper.SetValue('Arq. Periodo Atual ?', '')
        self.oHelper.SetValue('Gera reg. 53 (Entradas) ?', 'Nao')
        self.oHelper.SetValue('Gera reg. 88DV ?', 'Nao')
        self.oHelper.SetValue('Aglutina seleção por CNPJ+IE ?', 'Nao')
        # self.oHelper.SetValue('Rest. ST Alteração Regime ?','')
        # self.oHelper.SetValue('Rest.ST Estoque/Nota Fiscal ?','')
        # self.oHelper.SetValue('Gera somente Reg. Rest.ST ?','')

        # CLICA NO BOTÃO OK PARA CONFIRMAR OS PARAMETROS E VOLTA PARA A TELA ANTERIOR
        self.oHelper.SetButton('OK')

        # CLICA NO OK E INICIA O PROCESSO DE Gerar Arquivo Magn�tico Layout SINTMG05 - Registro 55 (GNRE ICMS Antecipado - Documento de Entrada)
        self.oHelper.SetButton('Ok')

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
