from tir import Webapp
import unittest


class CTBR560P(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "31/12/2018", "T1", "M PR 02 ", "01")

        inst.oHelper.Program("CTBR560P")

    def test_CTBR560P_001(self):
        
        if self.oHelper.GetRelease() >= "12.1.30":
            self.oHelper.SetValue("Exercicio Contabil ?          ", "218")           
            self.oHelper.SetValue("Cod. Config. Livros ?         ", "001")            
            self.oHelper.SetValue("Moeda ?                       ", "01")            
            self.oHelper.SetValue("Posicao Anterior L/P ?        ", "Nao")            
            self.oHelper.SetValue("Data Lucros/Perdas ?          ", "")               
            self.oHelper.SetValue("Dem. Variação ?               ", "Nao")           
            self.oHelper.SetValue("Folha Inicial ?               ", "1")              
            self.oHelper.SetValue("Data de Referencia ?          ", "31/12/2018")      
            self.oHelper.SetValue("Periodo ?                     ", "Calendario")     
            self.oHelper.SetValue("Imp. Arq. Termo Aux. ?        ", "Nao")            
            self.oHelper.SetValue("Termo Aux. a ser imp. ?       ", "")               
            self.oHelper.SetValue("Saldos Zerados ?              ", "Nao")            
            self.oHelper.SetValue("Considerar ?                  ", "Mov. Periodo")   
            self.oHelper.SetValue("Descricao na Moeda ?          ", "01")            
            self.oHelper.SetValue("Consolidar Saldo ?            ", "Sim")            
            self.oHelper.SetValue("Saldos a Consolidar ?         ", "1")              
            self.oHelper.SetValue("Tipo de Saldo ?               ", "1")              
            self.oHelper.SetValue("Metodo ?                      ", "Direto")         
            self.oHelper.SetValue("Resultado do Exercicio ?      ", "Composto")       
            self.oHelper.SetValue("Saldo do Exercício ?          ", "0,00")             
            self.oHelper.SetValue("Saldo do Exercício Anterior ? ", "0,00")              
            self.oHelper.SetValue("Titulo como nome da visão ?   ", "Sim")           
            self.oHelper.SetValue("Seleciona Filiais ?           ", "Nao")           

            self.oHelper.SetButton("Ok")
            self.oHelper.SetButton("x",)

            self.oHelper.AssertTrue()

    def test_CTBR560P_002(self):
        
        if self.oHelper.GetRelease() >= "12.1.30":
            self.oHelper.Program("CTBR560P")

            self.oHelper.SetValue("Exercicio Contabil ?          ", "218")           
            self.oHelper.SetValue("Cod. Config. Livros ?         ", "001")            
            self.oHelper.SetValue("Moeda ?                       ", "01")            
            self.oHelper.SetValue("Posicao Anterior L/P ?        ", "Nao")            
            self.oHelper.SetValue("Data Lucros/Perdas ?          ", "")               
            self.oHelper.SetValue("Dem. Variação ?               ", "Sim")           
            self.oHelper.SetValue("Folha Inicial ?               ", "1")              
            self.oHelper.SetValue("Data de Referencia ?          ", "31/12/2018")      
            self.oHelper.SetValue("Periodo ?                     ", "Calendario")     
            self.oHelper.SetValue("Imp. Arq. Termo Aux. ?        ", "Nao")            
            self.oHelper.SetValue("Termo Aux. a ser imp. ?       ", "")               
            self.oHelper.SetValue("Saldos Zerados ?              ", "Nao")            
            self.oHelper.SetValue("Considerar ?                  ", "Mov. Periodo")   
            self.oHelper.SetValue("Descricao na Moeda ?          ", "01")            
            self.oHelper.SetValue("Consolidar Saldo ?            ", "Sim")            
            self.oHelper.SetValue("Saldos a Consolidar ?         ", "1")              
            self.oHelper.SetValue("Tipo de Saldo ?               ", "1")              
            self.oHelper.SetValue("Metodo ?                      ", "Direto")         
            self.oHelper.SetValue("Resultado do Exercicio ?      ", "Composto")       
            self.oHelper.SetValue("Saldo do Exercício ?          ", "0,00")             
            self.oHelper.SetValue("Saldo do Exercício Anterior ? ", "0,00")              
            self.oHelper.SetValue("Titulo como nome da visão ?   ", "Sim")           
            self.oHelper.SetValue("Seleciona Filiais ?           ", "Nao")           

            self.oHelper.SetButton("Ok")
            self.oHelper.SetButton("x",)
            
            self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
