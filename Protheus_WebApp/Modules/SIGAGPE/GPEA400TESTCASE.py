from cawebhelper import CAWebHelper
import unittest

class GPEA400(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Configuração de inicialização dos Casos de Teste
        '''
        #Endereço do webapp e o nome do Browser
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")
        
        #Parametros de inicializaçao
        inst.oHelper.SetUp("SIGAGPE","P12117","ADMIN","","09/01/2018","T1","D MG 01 ")

        #Nome da rotina do Caso de Teste
        inst.oHelper.UTProgram("GPEA400")

    def test_GPEA400_001(self):
        codProcesso = "00001"
        cMes = "12"
        cAno = "2015"
        cDtini = "01/12/2015"
        cDtfim = "31/12/2015"

        #self.oHelper.SearchBrowse("Filial+cod Processo", "D MG    %s" %codProcesso, True)
        
        #Aciona os botões do TOTVS SmartClient HTML.
        self.oHelper.SetButton('Incluir', 'D MG 01 ')
        
        self.oHelper.ClickFolder("Cadastro de Período")

        self.oHelper.UTSetValue('aCab','RFQ_MES', cMes)
        self.oHelper.UTSetValue('aCab','RFQ_ANO', cAno)
        self.oHelper.UTSetValue('aCab','RFQ_DTINI', cDtini)
        self.oHelper.UTSetValue('aCab','RFQ_DTFIM', cDtfim)

        self.oHelper.UTSetValue('aItens','RCH_PROCES', codProcesso)
        self.oHelper.UTSetValue('aItens','RCH_ROTEIR', "FOL")
        self.oHelper.UTSetValue('aItens','RCH_DTPAGO', "05/01/2016")

        self.oHelper.UTAddLine()

        self.oHelper.UTSetValue('aItens','RCH_ROTEIR', "RES")
        self.oHelper.UTSetValue('aItens','RCH_DTPAGO', "31/12/2015")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.UTCheckResult('aCab','RFQ_MES', cMes)
        self.oHelper.UTCheckResult('aCab','RFQ_ANO', cAno)
        self.oHelper.UTCheckResult('aCab','RFQ_DTINI', cDtini)
        self.oHelper.UTCheckResult('aCab','RFQ_DTFIM', cDtfim)

        #Define que o teste espera um retorno verdadeiro de todos os pontos de verificação.
        self.oHelper.AssertTrue()
        
    
    @classmethod
    def tearDownClass(inst):
        '''
        Método que finaliza o TestCase
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()