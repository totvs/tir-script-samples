from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class TMKC010(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGATMK", DateSystem, "T1", "D MG 01 ", "73")
        self.oHelper.Program("TMKC010") 

    def test_TMKC010_CT001(self):
        self.oHelper.SearchBrowse("D MG    000001","Filial+contato + Id Exchange")
        self.oHelper.WaitShow("Informacoes gerencias das entidades")
        self.oHelper.SetButton("Consulta")
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickTree("Perfil do Cliente") 
        self.oHelper.ClickTree("Contato")  
        self.oHelper.ClickTree("Telemarketing > Encerramentos")
        self.oHelper.ClickTree("Ativos")
        self.oHelper.ClickTree("Receptivos")
        self.oHelper.ClickTree("Follow Up")
        self.oHelper.ClickTree("Pendências")
        self.oHelper.ClickTree("Chamado Técnico")
        self.oHelper.ClickTree("Atendimentos")
        self.oHelper.ClickTree("Campanha > Detalhado")
        self.oHelper.ClickTree("Análise Scripts")
        self.oHelper.ClickTree("Script Resp.")
        self.oHelper.SetKey("F10")
        self.oHelper.SetButton("Consulta")
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickTree("Perfil do Cliente") 
        self.oHelper.ClickTree("Empresa") 
        self.oHelper.ClickTree("Televendas > Orçamentos")
        self.oHelper.ClickTree("Faturamento")
        self.oHelper.ClickTree("Cancelamentos")
        self.oHelper.ClickTree("Vendas SigaLoja")
        self.oHelper.ClickTree("Mais Comprados")
        self.oHelper.ClickTree("Conhecimento > Análise Banco")
        self.oHelper.ClickTree("Telecobrança > Cobranças")
        self.oHelper.ClickTree("Negociação")
        self.oHelper.ClickTree("Ocorrências")
        self.oHelper.ClickTree("Cobr. Vencida")
        self.oHelper.ClickTree("Cobr. a Realizar")
        self.oHelper.ClickTree("Análise Financeira > Vencidos")
        self.oHelper.ClickTree("A vencer")
        self.oHelper.ClickTree("Pagto c/ Atraso")
        self.oHelper.ClickTree("Pagto Cartório")
        self.oHelper.ClickTree("Protestados")
        self.oHelper.ClickTree("Posição Financ.")
        self.oHelper.ClickTree("NCC's em aberto")
        self.oHelper.ClickTree("Vendas > Loja")
        self.oHelper.ClickTree("Faturamento")
        self.oHelper.ClickTree("Entregas agendadas")
        self.oHelper.ClickTree("Devoluções")
        self.oHelper.ClickTree("Ticket Médio")
        self.oHelper.ClickTree("Categoria Produto")
        self.oHelper.ClickTree("Marketing > Lista de Contato")
        self.oHelper.ClickTree("Resultado")
        self.oHelper.ClickTree("Serviço > Chamado Técnico")
        self.oHelper.ClickTree("Ordem de Serviço")
        self.oHelper.ClickTree("Agendamentos")
        self.oHelper.ClickTree("Varejo > Regra Desconto")
        self.oHelper.ClickTree("Venda Perdida")
        self.oHelper.ClickTree("Cartão Fidelidade")
        self.oHelper.SetKey("F10")
        self.oHelper.WaitShow("Informacoes gerencias das entidades")
        self.oHelper.SetButton("X")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()