from tir import Webapp
import unittest

class TMKA061(unittest.TestCase):

    @classmethod
    def setUpClass(inst):   
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMK','13/04/2020','T1','D MG 01 ','13')
        inst.oHelper.Program('TMKA061')

    def test_TMKA061_001(self):
        self.oHelper.SetButton("Outras Ações","Assistente")
        self.oHelper.SetButton("OK")
        self.oHelper.ClickLabel("Lista de Contato")
        self.oHelper.SetButton("Avançar")
        self.oHelper.ClickLabel("Vendas")
        self.oHelper.SetButton("Avançar")
        self.oHelper.ClickLabel("1 - Clientes")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Data Ultima Compra ?", "")
        self.oHelper.SetValue("Data Ultima Visita ?", "")
        self.oHelper.SetButton("OK")
        self.oHelper.ClickLabel("Detalhada")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Nível do Contato ?", "")
        self.oHelper.SetValue("Perfil do Contato ?", "Nao Avalia")
        self.oHelper.SetValue("Ligacões não executadas ?", "Nao Considera")
        self.oHelper.SetValue("A partir de quando ?", "31/12/2004")
        self.oHelper.SetValue("Ignora os dias da semana ?", "")
        self.oHelper.SetButton("OK")
        self.oHelper.ClickLabel("Voz")
        self.oHelper.SetButton("Avançar")
        self.oHelper.ClickLabel("Comercial 1")
        self.oHelper.SetButton("Avançar")
        self.oHelper.ClickLabel("Lista Aberta")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Nome Lista", "Lista Contatos Vendas- TIR")
        self.oHelper.SetValue("Servico SLA", "")
        self.oHelper.SetKey("TAB")
        self.oHelper.SetValue("Número máximo de Itens por Lista:", "000999")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Finalizar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("OK")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 