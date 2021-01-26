from tir import Webapp
import unittest


class TMSA145(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()

        inst.oHelper.Setup('SIGATMS', '06/10/2020', 'T1', 'M SP 04 ', '43')
        inst.oHelper.Program('TMSA145')
    
    # Operações basicas no gestão de viagens.
    def test_TMA145_CT001(self):

        self.oHelper.SetValue("Exibição ?", "Por Veículo")
        self.oHelper.SetValue("Veículo ?", "")
        self.oHelper.SetValue("Refresh ?", "Manual")        
        self.oHelper.SetValue("Parâmentros abaixo ?", "Considerar")
        self.oHelper.SetValue("Tipo de Frota ?", "Todos")
        self.oHelper.SetValue("Status do Veículo ?", "Todos")
        self.oHelper.SetValue("Filial Base De ?", "")
        self.oHelper.SetValue("Filial Base Ate ?", "ZZZZZZZZ")
        self.oHelper.SetValue("Serviço de Transporte ?", "3")
        self.oHelper.SetValue("Tipo de Transporte ?", "1")
        self.oHelper.SetValue("Região Origem ?", "")
        self.oHelper.SetValue("Região Destino ?", "ZZZZZZ")
        self.oHelper.SetValue("Status da Viagem ?", "Todos")
        self.oHelper.SetValue("Data Viagem De ?", "01/01/2020")
        self.oHelper.SetValue("Data Viagem Ate ?", "20/01/2021")
        self.oHelper.SetValue("Veiculos sem Alocação ?", "Considerar")
       
        self.oHelper.SetButton('OK')  # Confirmação da janela dos Parâmetros

        self.oHelper.ClickLabel("Qtde. Viagens:")
        self.oHelper.SetKey('F4') #Legenda 
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetKey('F6') #Legenda 
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetKey('F5') #Refresh
        self.oHelper.SetValue("Exibição ?", "Por Documento")
        self.oHelper.SetButton('OK')

        self.oHelper.ClickLabel("Qtde. Viagens:")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
