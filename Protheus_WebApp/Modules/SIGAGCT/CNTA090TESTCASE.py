from tir import Webapp
import unittest

class CNTA090(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGCT","11/12/2020","","D MG 02","69")
        inst.oHelper.Program("CNTA090")
    
    def test_CNTA090_001(self):
        # Configuração parametro
        self.oHelper.AddParameter("MV_CAUCNAT", "", "001", ".F.", ".F.")
        
        # Inclusão caução mov financeira
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SearchBrowse("D MG 02")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Tipo de Caução", "003")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("CN8_CONTRA","CNTA090TIRCT001")
        self.oHelper.SetValue("CN8_REVISA","")
        self.oHelper.SetValue("CN8_FORNEC","FHOND1")
        self.oHelper.SetValue("CN8_LOJA","01")
        self.oHelper.SetValue("CN8_DTENT","11/12/2020")
        self.oHelper.SetValue("CN8_BANCO","001")
        self.oHelper.SetValue("CN8_AGENCI","00001")
        self.oHelper.SetValue("CN8_CONTA","0000000001")
        self.oHelper.SetValue("CN8_VLEFET","1.000,00")
        self.oHelper.SetValue("CN8_TPABAT", "1 - Caucao")
        self.oHelper.SetValue("CN8_PERCAB","10,00")
        self.oHelper.SetValue("CN8_MOEDA","1")
        self.oHelper.SetValue("CN8_TPDOC","R$")
        self.oHelper.SetButton("Salvar")
        
        # Inclusão caução sem mov financeira. Testar validações datas
        self.oHelper.SetValue("Tipo de Caução", "002")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("CN8_CONTRA","CNTA090TIRCT001")
        self.oHelper.SetValue("CN8_REVISA","")
        self.oHelper.SetValue("CN8_FORNEC","FHOND1")
        self.oHelper.SetValue("CN8_LOJA","01")
        self.oHelper.SetValue("CN8_NUMDOC","TESTE")
        self.oHelper.SetValue("CN8_DTENT","11/12/2020")
        
        # Valida data inicio. Help CNTA090_07
        self.oHelper.SetValue("CN8_DTINVI","11/12/2030")
        self.oHelper.CheckHelp(text_help="CNTA090_07", button="Fechar")
        self.oHelper.SetValue("CN8_DTINVI","11/12/2020")

        # Valida data FIM. Help CNTA090_08
        self.oHelper.SetValue("CN8_DTFIVI","01/01/2000")
        self.oHelper.CheckHelp(text_help="CNTA090_08", button="Fechar")
        self.oHelper.SetValue("CN8_DTFIVI","11/12/2021")
        
        # confirmando a inclusão
        self.oHelper.SetValue("CN8_VLEFET","1.000,00")
        self.oHelper.SetValue("CN8_TPDOC","R$")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        
        # Pesquisa da caução inclusa para o contrato
        self.oHelper.SearchBrowse("D MG 02", key=2, index=True)
        self.oHelper.SearchBrowse("D MG 02 CNTA090TIRCT001")

        # Visualizando caução
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        
        # Alterando caução
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetValue("CN8_VLEFET","2.000,00")
        self.oHelper.SetButton("Salvar")

        # Alterando caução com valor acima do permitido. Testando help CNTA090_10
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetValue("CN8_VLEFET","50.000,00")
        self.oHelper.SetButton("Salvar")     
        self.oHelper.CheckHelp(text_help="CNTA090_10", button="Fechar")
        self.oHelper.SetValue("CN8_VLEFET","2.000,00")
        
        # Validação fornecedor. Help CNTA090_04
        self.oHelper.SetValue("CN8_FORNEC","FHOND2")
        self.oHelper.SetValue("CN8_LOJA","01")
        self.oHelper.SetButton("Salvar")
        self.oHelper.CheckHelp(text_help="CNTA090_04", button="Fechar")

        self.oHelper.SetValue("CN8_LOJA","01")
        self.oHelper.SetValue("CN8_FORNEC","FHOND1")
        
        # Validação data entrega. Help CNTA090_07
        self.oHelper.SetValue("CN8_DTENT","01/12/2000")
        self.oHelper.CheckHelp(text_help="CNTA090_07", button="Fechar")

        self.oHelper.SetValue("CN8_DTENT","11/12/2020")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()     

    ###################################################
    # CT002 - Testes das validações da rotina         #
    ###################################################
    def test_CNTA090_002(self):

        # Pesquisa da caução inclusa para o contrato
        self.oHelper.SearchBrowse("D MG 02", key=2, index=True)
        self.oHelper.SearchBrowse("D MG 02 CNTA090TIRCT002")

        # Teste exclusão. Help CNTA090_03
        self.oHelper.SetButton('Outras Ações', sub_item='Excluir')
        self.oHelper.CheckHelp(text_help="CNTA090_03", button="Fechar")

        # Teste estorno. Help CNTA090BXC
        self.oHelper.SetButton('Outras Ações', sub_item='Estorno Baixa')
        self.oHelper.CheckHelp(text_help="CNTA090BXC", button="Fechar")

        # Teste baixa. 
        self.oHelper.SetButton('Outras Ações', sub_item='Baixar')
        self.oHelper.SetButton('Sim')

        # Teste exclusão com caução baixada. Help CNTA090_01
        self.oHelper.SetButton('Outras Ações', sub_item='Excluir')
        self.oHelper.CheckHelp(text_help="CNTA090BXC", button="Fechar")

        self.oHelper.SetButton('Outras Ações', sub_item='Estorno Baixa')
        self.oHelper.SetButton('Ok')

        # Teste alteração com caução baixada. Help CNTA_03
        self.oHelper.SetButton('Alterar')
        self.oHelper.CheckHelp(text_help="CNTA090_03", button="Fechar")

        # Teste inclusão para contrato vigente
        self.oHelper.SetButton('Incluir')
        self.oHelper.SearchBrowse("D MG 02")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Tipo de Caução", "003")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("CN8_CONTRA","CNTA090TIRCT002")
        self.oHelper.CheckHelp(text_help="CNTA090_03", button="Fechar")
        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()     
                 
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()