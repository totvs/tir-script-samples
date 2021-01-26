from tir import Webapp
import unittest
import time


class GTPA815(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '19/11/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA815')

    def test_GTPA815_CT001(self):
        print("test_GTPA815_CT001 - Visualizar")
        self.oHelper.ClickLabel("+ Visualização")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()  

    def test_GTPA815_CT002(self):
        print("test_GTPA815_CT002 - Incluir")              
        self.oHelper.ClickLabel('+ Inclusao')
        self.oHelper.SetValue('Código da Agência', '000010')
        self.oHelper.SetValue('Data Encomenda De', '01112020')
        self.oHelper.SetValue('Data Encomenda Até', '30112020')
        self.oHelper.SetValue('Data Viagem De', '01112020')
        self.oHelper.SetValue('Data Viagem Até', '30112020')
        self.oHelper.SetButton("Outras Ações", "Pesquisar")        
        #self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()       

   
    def test_GTPA815_CT003(self):
        print("test_GTPA815_CT003 - Alteração")
        self.oHelper.ClickLabel('+ Alteração')
        self.oHelper.SetValue('Tara', '1') 
        self.oHelper.SetButton('Confirmar')        
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA815_CT004(self):
        print("test_GTPA815_CT004 - Encerramento")
        self.oHelper.ClickLabel('+ Encerramento')
        self.oHelper.SetValue('Agência', '000001') 
        self.oHelper.SetButton('Confirmar')        
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA815_CT005(self):
        print("test_GTPA815_CT005 - Visualização Evento")
        self.oHelper.ClickLabel('+ Visualização Evento')
        time.sleep(2)
        self.oHelper.SetKey("ESC", grid=False)
        self.oHelper.AssertTrue()

    def test_GTPA815_CT006(self):
        print("test_GTPA815_CT006 - Incluir")              
        self.oHelper.ClickLabel('+ Inclusao')
        self.oHelper.SetValue('Código da Agência', '000010')
        self.oHelper.SetValue('Data Encomenda De', '01112020')
        self.oHelper.SetValue('Data Encomenda Até', '30112020')
        self.oHelper.SetValue('Data Viagem De', '01112020')
        self.oHelper.SetValue('Data Viagem Até', '30112020')
        self.oHelper.SetButton("Outras Ações", "Pesquisar")        
        #self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()           
    
    def test_GTPA815_CT007(self):
        print("test_GTPA815_CT007 - Envio")
        self.oHelper.ClickLabel('+ Envio')
        time.sleep(15)
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('OK')
        self.oHelper.AssertTrue()
        
    def test_GTPA815_CT008(self):
        print("test_GTPA815_CT008 - + Recebimento")
        self.oHelper.ClickLabel('+ Recebimento')
        self.oHelper.SetValue('Cód.Agencia', '000010')
        self.oHelper.SetValue('Data De', '01112020')
        self.oHelper.SetValue('Data Ate', '30112020')
        self.oHelper.SetButton("Outras Ações", "Pesquisar")        
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()  
        
    def test_GTPA815_CT009(self):
        print("test_GTPA815_CT009 - EVENTO CTE")
        self.oHelper.ClickLabel('EVENTO CTE')
        time.sleep(2)
        self.oHelper.SetKey("ESC", grid=False)
        self.oHelper.AssertTrue()   
        
    def test_GTPA815_CT010(self):
        print("test_GTPA815_CT010 - + Inclusão do Condutor")
        self.oHelper.ClickLabel('+ Inclusão do Condutor')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair da página')      
        self.oHelper.AssertTrue()

        

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
