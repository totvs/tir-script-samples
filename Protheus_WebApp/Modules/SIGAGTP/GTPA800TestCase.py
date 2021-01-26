from tir import Webapp
import unittest
import time


class GTPA800(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '09/10/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA800')

    def test_GTPA800_CT001(self):
        print("test_GTPA800_CT001 - Visualizar")
        self.oHelper.ClickLabel("+ Visualização")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()  

    def test_GTPA800_CT002(self):
        print("test_GTPA800_CT002 - Incluir")  
        self.oHelper.AddParameter("MV_ESPECIE", "", "122=CTE; ", "122=CTE; ", "122=CTE;")      
        self.oHelper.ClickLabel('+ Inclusão')
        self.oHelper.SetValue('Remetente', 'GTP011')
        self.oHelper.SetValue('Destinatario', 'GTP010')
        self.oHelper.SetValue('Emissor', '000009')
        self.oHelper.SetValue('Recebedor', '000010')
        self.oHelper.SetValue('Cod. Produto', 'GTP000000000000')
        self.oHelper.SetValue('Qtd.Volumes', '1')
        #self.oHelper.SetValue('G99_KMFRET', '100.00')        
        #self.oHelper.SetValue('G99_VALOR ', '1000.00')
        self.oHelper.SetValue('G99_DTPREV', '07102020')
        self.oHelper.SetValue('G99_HRPREV', '10:00')

        #self.oHelper.ClickFolder("Declarações")
        #self.oHelper.SetValue('Descrição', "Declaracao 1", grid=True)        
        #self.oHelper.LoadGrid()

        #self.oHelper.ClickFolder("Serviços")
        #self.oHelper.SetValue('Linha', "000003", grid=True)
        #self.oHelper.SetValue('Loc Inicial', "LOC002", grid=True)  
        #self.oHelper.SetValue('Loc. Final', "LOC001", grid=True) 
        #self.oHelper.LoadGrid()

        #self.oHelper.ClickFolder("Conhecimento")
        #self.oHelper.SetValue('Tipo Saída', '527')
        #self.oHelper.SetValue('CFOP', '5933')
        #self.oHelper.SetValue('Nr Documento', '000000003')
        #self.oHelper.LoadGrid()
        
        #self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AssertTrue()       

   
    def test_GTPA800_CT003(self):
        print("test_GTPA800_CT003 - Excluir")
        self.oHelper.ClickLabel('+ Exclusão')
        #self.oHelper.SetButton('Confirmar')
        #time.sleep(2)
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA800_CT004(self):
        print("test_GTPA800_CT004 - Atualiza Monitor")
        self.oHelper.ClickLabel('+ Atualizar Monitor')
        self.oHelper.AssertTrue()

    def test_GTPA800_CT005(self):
        print("test_GTPA800_CT005 - Retirada")
        self.oHelper.ClickLabel('+ Retirada')      
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA800_CT006(self):
        print("test_GTPA800_CT006 - Retirada")
        self.oHelper.ClickLabel('+ Recebimento')     
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()    

    def test_GTPA800_CT007(self):
        print("test_GTPA800_CT007 - Retirada")
        self.oHelper.ClickLabel('+ Automação')      
        self.oHelper.ClickLabel('+ Anulação') 
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AssertTrue()   

    def test_GTPA800_CT008(self):
        print("test_GTPA800_CT008 - Complemento")   
        self.oHelper.ClickLabel('+ Automação')            
        self.oHelper.ClickLabel('+ Complemento') 
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AssertTrue()       

    def test_GTPA800_CT009(self):
        print("test_GTPA800_CT009 - Cancelamento")   
        self.oHelper.ClickLabel('+ Automação')            
        self.oHelper.ClickLabel('+ Cancelamento') 
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AsserFalse()      

    def test_GTPA800_CT010(self):
        print("test_GTPA800_CT010 - Substituição")   
        self.oHelper.ClickLabel('+ AutomaAnul')            
        self.oHelper.ClickLabel('+ Substituição') 
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AssertTrue()  

    def test_GTPA800_CT011(self):
        print("test_GTPA800_CT011 - Averbação ENVIO")   
        self.oHelper.ClickLabel('+ AutomaAnul')            
        self.oHelper.ClickLabel('+ Envio Av') 
        self.oHelper.SetButton('Sim')
        self.oHelper.SetValue('Dt Inicial', '01012020')
        self.oHelper.SetValue('Dt Final', '01012021')
        self.oHelper.SetKey('F5')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AsserFalse() 

    def test_GTPA800_CT012(self):
        print("test_GTPA800_CT011 - Averbação cONSULTA")   
        self.oHelper.ClickLabel('+ AutomaAnul')            
        self.oHelper.ClickLabel('+ Consulta Av') 
        self.oHelper.SetValue('Ag. Emissora', '000001')
        self.oHelper.SetValue('Dt Inicial', '01012020')
        self.oHelper.SetValue('Dt Final', '01012021')
        self.oHelper.SetButton('Filtrar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair da página')
        self.oHelper.AsserFalse()     

        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
