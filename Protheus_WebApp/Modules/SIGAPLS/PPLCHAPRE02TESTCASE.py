import unittest

from tir.technologies.apw_internal import ApwInternal


class PPLCHAPRE02TESTCASE(unittest.TestCase):


# test_PPLCHAPRE02_CT001 - Atendimento guia SADT Autorizada com impressão
# test_PPLCHAPRE02_CT002 - Atendimento guia SADT Pacialmente Autorizada com Impressão
# test_PPLCHAPRE02_CT003 - Atendimento guia SADT Negada
# test_PPLCHAPRE02_CT004 - Atendimento guia Em Auditoria com inclusão de documentos

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Configuração de inicialização dos Casos de Teste
        '''
        # Endereco do webapp e o nome do Browser
        inst.oHelper = ApwInternal("config.json")

        inst.oHelper.Setup()

    # Atendimento guia SADT Autorizada com impressao
    def test_PPLCHAPRE02_CT001(self):
        
        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.ClickLink("Trocar para matrícula")
        self.oHelper.SetValue("Selecione o prestador, local de Atendimento e regime de atendimento que irá atender o beneficiário", "HOSPITAL BOM CLIMA - HOSPITAIS - NORMAL")
        self.oHelper.SetValue("Matrícula", "00010013000001003")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetValue("Tipo de Atendimento:", "SADT")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|HOSPITAL BOM CLIMA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("012 - Rn?", "Nao")
        self.oHelper.SetButton("015 - Nome Prof. Sol.", "search")
        self.oHelper.SearchValue("Numero C.R.", "654987")
        self.oHelper.SetValue("019 - Cod. Cbos", "MEDICO EM GERAL (CLINICO GERAL)")
        self.oHelper.SetButton("021 - Carater Atend.", "search")
        self.oHelper.SearchValue("Código", "1")
        self.oHelper.SetValue("023 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("025 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "40303136", True)
        self.oHelper.SetValue("027 - Qtd. Sol.", "5", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("025 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "40201120", True)
        self.oHelper.SetValue("027 - Qtd. Sol.", "10", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Autorizada")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("imprimir")
        self.oHelper.SwitchWindow()
        self.oHelper.CheckLink("Clique aqui.")
        self.oHelper.CloseWindow()
        self.oHelper.SwitchWindow()
        self.oHelper.SetButton("Anexar documento")
        self.oHelper.SetValue("Selecione o Arquivo:", "C:\\Totvs\\Automacao\\UPLOAD_GEN.txt")
        self.oHelper.SetButton("Anexar")
        self.oHelper.CheckBrowse("UPLOAD_GEN")
        self.oHelper.EndCase()

    # Atendimento guia SADT Pacialmente Autorizada com Impressao
    def test_PPLCHAPRE02_CT002(self):

        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.SetValue("Tipo de Atendimento:", "SADT")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|HOSPITAL BOM CLIMA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("012 - Rn?", "Nao")
        self.oHelper.SetButton("015 - Nome Prof. Sol.", "search")
        self.oHelper.SearchValue("Numero C.R.", "654987")
        self.oHelper.SetValue("019 - Cod. Cbos", "MEDICO EM GERAL (CLINICO GERAL)")
        self.oHelper.SetButton("021 - Carater Atend.", "search")
        self.oHelper.SearchValue("Código", "1")
        self.oHelper.SetValue("023 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("025 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "40303136", True)
        self.oHelper.SetValue("027 - Qtd. Sol.", "5", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("025 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "40311236", True)
        self.oHelper.SetValue("027 - Qtd. Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Autorizada Parcialmente")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("imprimir")
        self.oHelper.SwitchWindow()
        self.oHelper.CheckLink("Clique aqui.")
        self.oHelper.CloseWindow()
        self.oHelper.SwitchWindow()
        self.oHelper.SetButton("Anexar documento")
        self.oHelper.SetValue("Selecione o Arquivo:", "C:\\Totvs\\Automacao\\UPLOAD_GEN.txt")
        self.oHelper.SetButton("Anexar")
        self.oHelper.CheckBrowse("UPLOAD_GEN") 
        self.oHelper.EndCase() 

    # Atendimento guia SADT Negada
    def test_PPLCHAPRE02_CT003(self):
 
        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.SetValue("Tipo de Atendimento:", "SADT")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|HOSPITAL BOM CLIMA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("012 - Rn?", "Nao")
        self.oHelper.SetButton("015 - Nome Prof. Sol.", "search")
        self.oHelper.SearchValue("Numero C.R.", "654987")
        self.oHelper.SetValue("019 - Cod. Cbos", "MEDICO EM GERAL (CLINICO GERAL)")
        self.oHelper.SetButton("021 - Carater Atend.", "search")
        self.oHelper.SearchValue("Código", "1")
        self.oHelper.SetValue("023 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("025 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "40311236", True)
        self.oHelper.SetValue("027 - Qtd. Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Nao Autorizada")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Anexar documento")
        self.oHelper.SetValue("Selecione o Arquivo:", "C:\\Totvs\\Automacao\\UPLOAD_GEN.txt")
        self.oHelper.SetButton("Anexar")
        self.oHelper.CheckBrowse("UPLOAD_GEN")
        self.oHelper.EndCase()

    # Atendimento guia Em Auditoria com inclusao de documentos
    def test_PPLCHAPRE02_CT004(self):
        

        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.SetValue("Tipo de Atendimento:", "SADT")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|HOSPITAL BOM CLIMA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("012 - Rn?", "Nao")
        self.oHelper.SetButton("015 - Nome Prof. Sol.", "search")
        self.oHelper.SearchValue("Numero C.R.", "654987")
        self.oHelper.SetValue("019 - Cod. Cbos", "MEDICO EM GERAL (CLINICO GERAL)")
        self.oHelper.SetButton("021 - Carater Atend.", "search")
        self.oHelper.SearchValue("Código", "1")
        self.oHelper.SetValue("023 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("025 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "30101018", True)
        self.oHelper.SetValue("027 - Qtd. Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Em Análise")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Anexar documento")
        self.oHelper.SetValue("Selecione o Arquivo:", "C:\\Totvs\\Automacao\\UPLOAD_GEN.txt")
        self.oHelper.SetButton("Anexar")
        self.oHelper.CheckBrowse("UPLOAD_GEN")
        self.oHelper.EndCase()


    @classmethod
    def tearDownClass(inst):
        '''
        Método que finaliza o TestCase
        '''
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
