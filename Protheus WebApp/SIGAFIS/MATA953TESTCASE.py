from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

class MATA953(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAFIS', DateSystem, 'T1', 'XIFIS26', '09')
        inst.oHelper.Program('MATA953')
    
    def test_MATA953_PRE001(self):

        self.oHelper.SetButton('Param.')
        self.oHelper.SetValue('Mes de Apuração ?', '11')
        self.oHelper.SetValue('Ano de Apuração ?', '2018')
        self.oHelper.SetValue('Livro Selecionado ?', '*')
        self.oHelper.SetValue('Apuração ?', 'Mensal')
        self.oHelper.SetValue('Período ?', '1o.')
        '''
        self.oHelper.SetValue('Arq. Período Anter. ?', '')
        self.oHelper.SetValue('Moeda do Título ?             ', '')
        '''
        self.oHelper.SetValue('Gera Título ?', 'Sim')
        self.oHelper.SetValue('Exibir Lanç.Contab. ?', 'Nao')
        self.oHelper.SetValue('Considera Filiais ?', 'Nao')
        self.oHelper.SetValue('Da Filial ?', '')
        self.oHelper.SetValue('Ate a Filial ?', '')
        self.oHelper.SetValue('Gera Guia de Recolhimento ?', 'Sim')
        self.oHelper.SetValue('Gera Cred.Estimulo ?', 'Nao')
        self.oHelper.SetValue('Imprime Credito ST ?', 'Nao')
        self.oHelper.SetValue('Consolidação na mesma UF ?', 'Nao')
        self.oHelper.SetValue('Gera Titulo ICMS Complem ?', 'Sim')
        self.oHelper.SetValue('Imprime Mapa Resumo ?', 'Nao')
        self.oHelper.SetValue('Seleciona filiais ?', 'Nao')
        self.oHelper.SetValue('Cred.Pres.MT ?', 'Não')
        self.oHelper.SetValue('Exclui GNR ?', 'Não')
        self.oHelper.SetValue('Aglutina por CNPJ+IE ?', 'Não')
        self.oHelper.SetValue('Processa Conv.139/06 ?', 'Não')
        self.oHelper.SetValue('GNRE/Título Conv.139/06 ?', 'Não')
        self.oHelper.SetValue('Inicial Sol.Aprov.Tit.Fluig ?', 'Nao')
        self.oHelper.SetValue('Título PROTEGE-GO ?', 'Não')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Ok')        

        # VERIFICAÇÃO DOS FOLDERS
        
        self.oHelper.ClickFolder('ICMS-Entradas')
        self.oHelper.ClickFolder('ICMS-Saidas')
        self.oHelper.ClickFolder('ST-Entradas')
        self.oHelper.ClickFolder('ST-Saidas')
        self.oHelper.ClickFolder('Apuracao-ICMS')
        self.oHelper.ClickFolder('Apuracao-ST')
        self.oHelper.ClickFolder('Informacoes Complementares')
        self.oHelper.ClickFolder('DIFAL/FECP')
        self.oHelper.ClickFolder('Créditos Extra Apuração')
        self.oHelper.ClickFolder('Débitos Especiais')

        self.oHelper.SetButton('Confirmar')     

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
