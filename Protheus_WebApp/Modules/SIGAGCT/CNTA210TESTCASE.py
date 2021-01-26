from cawebhelper import CAWebHelper
import unittest

class CNTA210(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Configuração de inicialização dos Casos de Teste
        '''
        #Endereço do webapp e o nome do Browser
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")
        
        #Parametros de inicializaçao
        inst.oHelper.SetUp("SIGAGCT","P12_CONGELADA","ADMIN","","","T1","D MG 01 ")

        #Nome da rotina do Caso de Teste
        inst.oHelper.UTProgram("CNTA210")

    def test_CNTA210_004(self):
        '''
        Caso de Teste 004
        '''
        #Aciona os botões do TOTVS SmartClient HTML.
        self.oHelper.SetButton('Incluir', 'D MG 01')

        #Preenche os campos do Cabeçalho e/ou Grid do TOTVS: SmartClient HTML.
        self.oHelper.UTSetValue("aCab","CNJ_SITUAC","09")
     
        self.oHelper.UTSetValue("aItens","CNJ_TPDOC","004")

        # confirma a gravação da inclusão do pedido de venda.
        self.oHelper.SetButton("Salvar")
        # após a gravação, o TOTVS: SmartClient HTML volta para a tela de inclusão, então eu cancelo essa tela para voltar para o mbrowse.
        self.oHelper.SetButton("Cancelar")
      
        # na tela do mbrowse, posicionado no pedido de venda desejado, seleciono o botão Alterar.
        self.oHelper.SetButton("Visualizar")

        #Com o pedido sendo apresentado na tela, efetuo a conferencia dos dados da interface com o resultado esperado pelo usuário.
        self.oHelper.UTCheckResult("aCab","CNJ_SITUAC","09")

        self.oHelper.UTCheckResult("aItens","CNJ_TPDOC","004")
        self.oHelper.UTCheckResult("aItens","CNJ_TPCTO", "   ")
        self.oHelper.UTCheckResult("aItens","CNJ_DESCTD","GCT MATA210 002")

        self.oHelper.SetButton("Cancelar")

        #Define que o teste espera uma retorno verdadeiro para passar.
        self.oHelper.AssertTrue()

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

