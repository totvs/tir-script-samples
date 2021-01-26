from tir import Webapp
import unittest

class TMSA200A(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','06/11/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA200')  		

    def test_TMSA200A_CT001(self):

        self.oHelper.WaitShow('Calculo de Frete')
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Exibe Preview do Frete ?", "Não")
        self.oHelper.SetButton("Ok")		
            
        self.oHelper.SetButton('Outras Ações', "Selecionar Lotes")

        self.oHelper.SetValue('Tipo Lote ?','Normal')
        self.oHelper.SetValue('Numero do Lote De ?','000184')
        self.oHelper.SetValue('Numero do Lote Ate ?','000185')
        self.oHelper.SetValue('Data do Lote De ?','05/11/2020')
        self.oHelper.SetValue('Data do Lote Ate ?', '06/11/2020')
        self.oHelper.SetValue('Status do Lote ?', 'Digitado')
        self.oHelper.SetValue('Lote de Rateio ?', 'Não')
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickLabel('Marca/Desmarca Todos')

        self.oHelper.SetButton('Legenda')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Calcular')
        self.oHelper.SetButton('Ok')

        self.oHelper.WaitProcessing('Gerando Documentos...')

        self.oHelper.SetButton("Sair")

        self.oHelper.AssertTrue()
	
		
    def test_TMSA200A_CT002(self):

        self.oHelper.SetButton('Outras Ações', "Selecionar Lotes")

        self.oHelper.SetValue('Status do Lote ?', 'Calculado')
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickLabel('Marca/Desmarca Todos')

        self.oHelper.SetButton('Estornar')
        self.oHelper.SetButton('Ok')

        self.oHelper.WaitProcessing('Estornando conhecimento de frete...')

        self.oHelper.SetButton("Sair")
        
        self.oHelper.AssertTrue()

    def test_TMSA200A_CT003(self):

        self.oHelper.SetButton('Outras Ações', "Selecionar Lotes")

        self.oHelper.SetValue('Status do Lote ?', 'Digitado')
        self.oHelper.SetButton('Ok')

        self.oHelper.ClickLabel('Marca/Desmarca Todos')

        self.oHelper.SetButton('Aglutinar')
        self.oHelper.SetButton('Sim')

        self.oHelper.SetButton("Sair")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

