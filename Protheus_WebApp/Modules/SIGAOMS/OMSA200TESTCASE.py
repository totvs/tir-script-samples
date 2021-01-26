from tir import Webapp
import unittest
import datetime

class OMSA200(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGAOMS',dataAtual,'T1','D MG 01 ','39')
        inst.oHelper.Program("OMSA200")

    #Inclusão de Montagem de Carga 
    def test_OMSA200_CT001(self):
        
        self.oHelper.SetValue("Carga de ?", "")
        self.oHelper.SetValue("Carga ate ?", "ZZZZZZ")
        self.oHelper.SetValue("Data geracao de ?", "01/01/2020")
        self.oHelper.SetValue("Data geracao ate ?", "15/12/2020")
        self.oHelper.SetValue("Filtra por ?", "Todas")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Carregamento","Montagem de Carga")      
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.ClickBox("Codigo","000001",grid_number = 1)

        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetValue("Pedido de ?", "")
        self.oHelper.SetValue("Pedido ate ?", "ZZZZZZ")
        self.oHelper.SetValue("Cliente de ?", "")
        self.oHelper.SetValue("Cliente ate ?", "ZZZZZZ")
        self.oHelper.SetValue("Aglutina por ?", "Pedido")
        self.oHelper.SetValue("Filial de ?", "")
        self.oHelper.SetValue("Filial ate ?", "ZZZZZZZZ")
        self.oHelper.SetValue("Data Liberacao de ?", "")
        self.oHelper.SetValue("Data Liberacao ate ?", "31/12/2020")
        self.oHelper.SetValue("Loja de ?", "")
        self.oHelper.SetValue("Loja ate ?", "ZZ")
        self.oHelper.SetValue("Data Entrega de ?", "")
        self.oHelper.SetValue("Data Entrega ate ?", "31/12/2020")
        self.oHelper.SetValue("Armazem de ?", "")
        self.oHelper.SetValue("Armazem até ?", "ZZ")
        self.oHelper.SetValue("Grupo Cliente De ?", "")
        self.oHelper.SetValue("Grupo Cliente Ate ?", "ZZZZZZ")
        self.oHelper.SetValue("Rota De ?", "")
        self.oHelper.SetValue("Rota Ate ?", "ZZZZZZ")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickBox("Pedido","OMS002",grid_number = 5)
        self.oHelper.ClickBox("Pedido","OMS003",grid_number = 5)

        self.oHelper.SetButton("Outras Ações","Seq. Ent.")
        self.oHelper.SetButton("Outras Ações","Sequencia anterior")
        self.oHelper.SetButton("Outras Ações","Sequencia posterior")
        self.oHelper.SetButton("Outras Ações","Hora inicial")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Veiculo")
        self.oHelper.SetValue("cVeiculo", "OMS-A120", name_attr=True)        
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Pedido")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações","Graficos")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Outras Ações","Transp.")
        self.oHelper.SetValue("cDakTransp", "TSSTR1", name_attr=True)   
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Outras Ações","Tipo Oper/ Class. Frete")
        self.oHelper.SetValue("cDAKTpOp", "3", name_attr=True)   
        self.oHelper.SetValue("cDAKClFr", "1", name_attr=True)   
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Outras Ações","Nova") 

        self.oHelper.SetButton("Cancelar") 

        self.oHelper.AssertTrue()

    #Manutenção
    def test_OMSA200_CT002(self): 

        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        self.oHelper.SearchBrowse("D MG 01 " + dataAtual, 'Filial+data + Hora + Cod. Carga + Seq. Carga  ')
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Carregamento","Manutencao")   

        self.oHelper.SetButton("Outras Ações","Est.Ped") 
        self.oHelper.ClickBox("Item","01", grid_number = 1)
        
        self.oHelper.SetButton("Editar")
        self.oHelper.SetValue("nQtdNew", "2,00", name_attr=True)  
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()
    
    #Agrupmamento
    def test_OMSA200_CT003(self): 

        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        self.oHelper.SearchBrowse("D MG 01 " + dataAtual, 'Filial+data + Hora + Cod. Carga + Seq. Carga  ')

        self.oHelper.SetButton("Carregamento","Agrupa")        
        
        self.oHelper.SetValue("cCodCarDes", "000017", name_attr=True)  
        self.oHelper.SetButton("Ok")
 
        self.oHelper.AssertTrue()   

    #Operaçãoes Gerais
    def test_OMSA200_CT004(self): 

        self.oHelper.SetButton("Outras Ações","Legenda") 
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Outras Ações","Entregas") 
        self.oHelper.SetButton("Sair")
        
        self.oHelper.SetButton("Carregamento","Montagem de Carga")      
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.ClickBox("Codigo","000001",grid_number = 1)
        self.oHelper.SetButton("Ok")
        
        self.oHelper.SetButton("Outras Ações","Refresh") 
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Outras Ações","Legenda") 
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Pesquisa") 
        self.oHelper.SetValue("xPesq", "000005", name_attr=True) 
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()   

    #Associa Motorista
    def test_OMSA200_CT005(self): 

        self.oHelper.SearchBrowse("D MG 01 000017", 'Filial+cod. Carga + Seq. Carga')

        self.oHelper.SetButton("Carregamento","Associar Veiculo") 

        self.oHelper.SetValue("cVeiculo", "OMS0001", name_attr=True)  
        self.oHelper.SetValue("cVeiculo2", "OMS0002", name_attr=True)  
        self.oHelper.SetValue("cMotorista", "OMS001", name_attr=True)  
        self.oHelper.SetValue("cAjuda1", "OMS001", name_attr=True)  
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()   
    
    #Bloqueio
    def test_OMSA200_CT006(self): 

        self.oHelper.SearchBrowse("D MG 01 000017", 'Filial+cod. Carga + Seq. Carga')

        self.oHelper.SetButton("Carregamento","Bloqueio")      
        self.oHelper.SetButton("Sim")
        
        self.oHelper.SetButton("Carregamento","Bloqueio")      
        self.oHelper.SetButton("Sim")
        
        self.oHelper.AssertTrue()  
    
    #Estorno
    def test_OMSA200_CT007(self): 

        self.oHelper.SearchBrowse("D MG 01 000017", 'Filial+cod. Carga + Seq. Carga')
        
        self.oHelper.SetButton("Carregamento","Estorno")        
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()  

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
