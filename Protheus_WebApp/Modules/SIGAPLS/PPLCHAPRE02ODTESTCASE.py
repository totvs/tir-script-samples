import unittest

from tir.technologies.apw_internal import ApwInternal


class PPLCHAPRE02ODTESTCASE(unittest.TestCase):

    # test_PPLCHAPRE02OD_CT001 - Atendimento guia Odontológica Autorizada com impressão
    # test_PPLCHAPRE02OD_CT002 - Atendimento guia Odontológica Pacialmente Autorizada com Impressão
    # test_PPLCHAPRE02OD_CT003 - Atendimento guia Odontológica SADT Negada
    # test_PPLCHAPRE02OD_CT004 - Atendimento guia Odontológica Em Auditoria com inclusão de documentos

    @classmethod
    def setUpClass(inst):

        inst.oHelper = ApwInternal("config.json")

        inst.oHelper.Setup()

    # Solicitação Odontológica autorizada
    def test_PPLCHAPRE02OD_CT001(self):

        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.ClickLink("Trocar para matrícula")
        self.oHelper.SetValue("Selecione o prestador, local de Atendimento e regime de atendimento que irá atender o beneficiário", "PRODE ODONTOLOGIA - CONSULTORIO ODONTOLOGICO PART. - NORMAL")
        self.oHelper.SetValue("Matrícula", "00010013000001003")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetValue("Tipo de Atendimento:", "Odontologico")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|PRODE ODONTOLOGIA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("016 - Rn?", "Nao")
        self.oHelper.SetButton("017 - Nome do Profissional Solicitante", "search")
        self.oHelper.SearchValue("Numero C.R.", "321987")
        self.oHelper.SetValue("020 - Cod. Cbos", "CIRURGIAO DENTISTA EM GERAL")
        self.oHelper.SetButton("031 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "82000026", True)
        self.oHelper.SetButton("033 - Dente/Região", "search")
        self.oHelper.SearchValue("Código", "11", True)
        self.oHelper.SetButton("034 - Face", "search")
        self.oHelper.SearchValue("Código", "D", True)
        self.oHelper.SetValue("035 - Qtd", "1", True)
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
        self.oHelper.driver.refresh()

    def test_PPLCHAPRE02OD_CT002(self):

        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.SetValue("Tipo de Atendimento:", "Odontologico")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|PRODE ODONTOLOGIA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("016 - Rn?", "Nao")
        self.oHelper.SetButton("017 - Nome do Profissional Solicitante", "search")
        self.oHelper.SearchValue("Numero C.R.", "321987")
        self.oHelper.SetValue("020 - Cod. Cbos", "CIRURGIAO DENTISTA EM GERAL")
        self.oHelper.SetButton("031 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "82000026", True)
        self.oHelper.SetButton("033 - Dente/Região", "search")
        self.oHelper.SearchValue("Código", "11", True)
        self.oHelper.SetButton("034 - Face", "search")
        self.oHelper.SearchValue("Código", "D", True)
        self.oHelper.SetValue("035 - Qtd", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("031 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "81000030", True)
        self.oHelper.SetButton("033 - Dente/Região", "search")
        self.oHelper.SearchValue("Código", "11", True)
        self.oHelper.SetButton("034 - Face", "search")
        self.oHelper.SearchValue("Código", "D", True)
        self.oHelper.SetValue("035 - Qtd", "1", True)
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
        self.oHelper.driver.refresh()

    def test_PPLCHAPRE02OD_CT003(self):

        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.SetValue("Tipo de Atendimento:", "Odontologico")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|PRODE ODONTOLOGIA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("016 - Rn?", "Nao")
        self.oHelper.SetButton("017 - Nome do Profissional Solicitante", "search")
        self.oHelper.SearchValue("Numero C.R.", "321987")
        self.oHelper.SetValue("020 - Cod. Cbos", "CIRURGIAO DENTISTA EM GERAL")
        self.oHelper.SetButton("031 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "81000030", True)
        self.oHelper.SetButton("033 - Dente/Região", "search")
        self.oHelper.SearchValue("Código", "11", True)
        self.oHelper.SetButton("034 - Face", "search")
        self.oHelper.SearchValue("Código", "D", True)
        self.oHelper.SetValue("035 - Qtd", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Nao Autorizada")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Anexar documento")
        self.oHelper.SetValue("Selecione o Arquivo:", "C:\\Totvs\\Automacao\\UPLOAD_GEN.txt")
        self.oHelper.SetButton("Anexar")
        self.oHelper.CheckBrowse("UPLOAD_GEN")
        self.oHelper.driver.refresh()

    def test_PPLCHAPRE02OD_CT004(self):
        
        self.oHelper.ClickMenu("Principal > Atendimento")
        self.oHelper.SetValue("Tipo de Atendimento:", "Odontologico")
        self.oHelper.SelectBrowse("CARLOS ROBERTO|PRODE ODONTOLOGIA")
        self.oHelper.SetButton("Atendimento")
        self.oHelper.SwitchModal("Sim")
        self.oHelper.SetButton("000 - Protocolo", "add")
        self.oHelper.SetValue("016 - Rn?", "Nao")
        self.oHelper.SetButton("017 - Nome do Profissional Solicitante", "search")
        self.oHelper.SearchValue("Numero C.R.", "321987")
        self.oHelper.SetValue("020 - Cod. Cbos", "CIRURGIAO DENTISTA EM GERAL")
        self.oHelper.SetButton("031 - Cod. Procedimento", "search")
        self.oHelper.SearchValue("Código", "82000026", True)
        self.oHelper.SetButton("033 - Dente/Região", "search")
        self.oHelper.SearchValue("Código", "12", True)
        self.oHelper.SetValue("035 - Qtd", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Em Análise")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("Anexar documento")
        self.oHelper.SetValue("Selecione o Arquivo:", "C:\\Totvs\\Automacao\\UPLOAD_GEN.txt")
        self.oHelper.SetButton("Anexar")
        self.oHelper.CheckBrowse("UPLOAD_GEN")
        self.oHelper.driver.refresh()

    @classmethod
    def tearDownClass(inst):
        '''
        Método que finaliza o TestCase
        '''
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
