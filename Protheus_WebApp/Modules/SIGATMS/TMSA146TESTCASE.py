from tir import Webapp
import unittest
import datetime

class TMSA146(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA146')

        inst.oHelper.AddParameter("MV_TMSRRE", "", "")
        inst.oHelper.SetParameters()

    def test_TMA146_CT015(self):
        self.oHelper.SearchBrowse("M SP    M SP 03 000002")

        self.oHelper.SetButton("Outras Ações", "Efetivar, Efetivar")

        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()
    
    # Inclusão básica de registro. M SP    15/10/2020    
    def test_TMA146_CT016(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.SetValue("Data Previsão Entrega De ?", "01/01/2020")
        self.oHelper.SetValue("Data Previsão Entrega Até ?", "01/12/2020")
        self.oHelper.SetValue("Data Emissão De ?", "01/01/2020")
        self.oHelper.SetValue("Data Emissão Até ?", "01/12/2020")
        self.oHelper.SetValue("Prioridade De ?", "")
        self.oHelper.SetValue("Prioridade Até ?", "Z")
        self.oHelper.SetValue("Cliente De ?", "")
        self.oHelper.SetValue("Loja De ?", "")
        self.oHelper.SetValue("Cliente Até ?", "ZZZZZZ")
        self.oHelper.SetValue("Loja Até ?", "ZZ")
        self.oHelper.SetValue("Tipo de Cliente ?", "Devedor")
        self.oHelper.SetValue("Região Origem De ?", "")
        self.oHelper.SetValue("Região Origem Ate ?", "ZZZZZZ")
        self.oHelper.SetValue("Região Destino De ?", "")
        self.oHelper.SetValue("Região Destino Até ?", "ZZZZZZ")
        self.oHelper.SetValue("Exibir Veiculos ?", "Todos")
        self.oHelper.SetValue("Rota De ?", "")
        self.oHelper.SetValue("Rota Ate ?", "ZZZZZZ")
        self.oHelper.SetValue("Listar Doctos Bloqueados ?", "Ambos")
        self.oHelper.SetValue("Filiais de Destino ?", "")
        self.oHelper.SetValue("Selecionar Documentos Por: ?", "Todos")
        self.oHelper.SetValue("Tipo de Agendamento De ?", "Priori. Cliente")
        self.oHelper.SetValue("Tipo de Agendamento Até ?", "Aguardando Agd.")
        self.oHelper.SetValue("Prioridade Ag. Entrega De ?", "")
        self.oHelper.SetValue("Prioridade Ag. Entrega Até ?", "ZZZ")
        self.oHelper.SetValue("Serviço de Transporte De ?", "3")
        self.oHelper.SetValue("Serviço de Transporte Até ?", "3")
        self.oHelper.SetValue("Tipo de Transporte ?", "1")
       
        self.oHelper.SetButton('OK')  # Confirmação da janela dos Parâmetros

        self.oHelper.ClickBox("No.Docto.","000000195", grid_number=1)	#Selecionar o documento       

        self.oHelper.ClickBox("Veiculo", "TMS003", grid_number=2)
        self.oHelper.SetFocus("C", grid_cell = True) 

        self.oHelper.SetValue('DF8_ROTA','ENTCLI',grid=True,grid_number=3,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Veículos")
        self.oHelper.ClickFolder("Motoristas")

        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        
        self.oHelper.AssertTrue()
    
    # Exclusão de registro.    
    def test_TMA146_CT017(self):
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        self.oHelper.SearchBrowse('M SP    ' + dataAtual, key='Filial+data Geração + Hora Geração')
        
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
    
    # Estorno da efetivação
    def test_TMA146_CT018(self):
        self.oHelper.SearchBrowse("M SP    M SP 03 000002")

        self.oHelper.SetButton("Outras ações", "Efetivar, Estornar")
        
        self.oHelper.SetButton("Sim")
       
        self.oHelper.AssertTrue()

    # Alteração de registro.    
    def test_TMA146_CT019(self):
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        self.oHelper.SearchBrowse('M SP    ' + dataAtual, key='Filial+data Geração + Hora Geração')
        
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue('DF8_ROTA','ENTSP3',grid=True,grid_number=3,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
