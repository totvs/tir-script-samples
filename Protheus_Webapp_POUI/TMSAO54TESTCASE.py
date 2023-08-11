from tir import Poui
from tir import Webapp
import unittest
from datetime import datetime

class TMSAO54(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        #Instancia do objeto Poui
        inst.oHelper_Poui = Poui()
        #Instancia do objeto Webapp
        inst.oHelper_Webapp = Webapp(autostart=False)
        #Método Setup do objeto Webapp
        inst.oHelper_Webapp.Setup("SIGATMS", datetime.today().strftime('%d/%m/%Y'), "T1", "D MG 01 ", '02')
        #Método Program do objeto Webapp
        inst.oHelper_Webapp.Program('TMSAO54')

    def test_TMSAO54_001(self):
        #Após abrir a tela do POUI, iniciamos o uso dos métodos do POUI que interagem com os componentes do POUI
        #Efetua o click no menu do componente do POUI
        self.oHelper_Poui.ClickMenu('Home')
        #Efetuar o click no componente po-select 
        self.oHelper_Poui.ClickSelect('Visão', 'Compras')
        #Efetua o click no componente po-widget, usando o titulo como referencia do widget e clica no action usando a label como referencia
        self.oHelper_Poui.ClickWidget(title='Lead Time SC x PC', action='Detalhes')
        #Efetua o click no componente po-button usando a label como referencia
        self.oHelper_Poui.ClickButton('Fechar')
        self.oHelper_Poui.ClickMenu('Cards')
        #Efetua o preenchimento no campo de pesquisa do componente po-search e efetua a busca
        self.oHelper_Poui.POSearch('Lotes Vencidos')
        #Efetua o click em uma célula do componente po-table usando como referencia as colunas e valores para identificar uma célula
        self.oHelper_Poui.ClickTable(first_column='Código', first_content='000008', click_cell='Editar')
        #Efetua o preenchimento de um valor no componente po-input
        self.oHelper_Poui.InputValue('Título', 'Lotes')
        #Método utilizado para verificar o conteudo de uma valor no componente po-input(Em breve será implementado a conferencia de valor em outros componentes)
        self.oHelper_Poui.CheckResult('Título', 'Lotes')
        self.oHelper_Poui.ClickButton('Cancelar')
        self.oHelper_Poui.ClickMenu('Gráficos')
        self.oHelper_Poui.ClickMenu('Visão')
        self.oHelper_Poui.ClickMenu('Sair')
        #Tela com botão do componente do Webapp, nesse caso usamos o método Setbutton para interagir
        self.oHelper_Webapp.SetButton('Sim')
        self.oHelper_Poui.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper_Poui.TearDown()


if __name__ == "__main__":
    unittest.main()
