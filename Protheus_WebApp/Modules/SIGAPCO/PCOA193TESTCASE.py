from tir import Webapp
#from selenium.webdriver.common.by 
import unittest
from datetime import datetime
import string
import random

class PCOA193(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '29/06/2020', 'T1', 'D MG 01 ')
        inst.oHelper.Program('PCOA193')
        
    # Inclusao
    #https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T344
    def test_PCOA193_CT001(self):

        sCodCubo    = 'TR'
        sDescrCubo  = 'TESTE TIR CUBO- INCLUSAO'
        #sMemo       = 'Teste inclusão TESTE TIR CUBO- INCLUSAO'

        #Acesso à rotina cubos gerenciais
        self.oHelper.WaitShow("Cubos Gerenciais")
        #Clique no botão incluir
        self.oHelper.ClickIcon("Incluir")
        #Clique no botão avançar, do wizzard
        self.oHelper.SetButton('Avançar')
        #Preencher Código e Descrição do cubo
        self.oHelper.SetValue('Cod. Cubo   ',sCodCubo)
        self.oHelper.SetValue('Descricao   ',sDescrCubo)
        #self.oHelper.SetValue('Memo        ',sMemo)
        #Clique no botão avançar do Wizzard
        self.oHelper.SetButton('Avançar')
        #Preencher niveis do Cubo
        self.oHelper.ClickIcon("Campos Pré-selecionados")
        #seleciona o primeiro item da tela: conta orçamentária
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Finalizar')
        #Validação de tipo de saldo
        self.oHelper.WaitShow("Atenção")
        self.oHelper.SetButton('Ok')
        #Abrir tela de níveis
        self.oHelper.ClickIcon("Campos Pré-selecionados")
        #selecionar radio buttom tipo de saldo (RADIO9003)
        self.oHelper.ClickLabel("Tipo de Saldo")
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Finalizar')
        self.oHelper.AssertTrue()
        

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    