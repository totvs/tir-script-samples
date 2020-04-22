import unittest

from tir.technologies.apw_internal import ApwInternal


class PPLPRORINTTESTCASE(unittest.TestCase):


# test_PPLPRORINT_CT001 - Prorrogação de Internação Autorizada com Impressão
# test_PPLPRORINT_CT002 - Prorrogação de Internação Pacialmente Autorizada com Impressão
# test_PPLPRORINT_CT003 - Prorrogação de Internação Negada
# test_PPLPRORINT_CT004 - Prorrogação de Internação em Auditoria


    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Configuração de inicialização dos Casos de Teste
        '''
        # Endereco do webapp e o nome do Browser
        inst.oHelper = ApwInternal("config.json")

        inst.oHelper.Setup()

    # Prorrogação de Internação Autorizada com Impressão
    def test_PPLPRORINT_CT001(self):
        
        self.oHelper.ClickMenu("Principal > Guia de Prorrogação")
        self.oHelper.SetValue("003 - Numero da Guia de So", "000120180900000010")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("003 - Numero da Guia de So", "add")
        self.oHelper.SetButton("011 - Nome Profissional So", "search")
        self.oHelper.SearchValue("Código", "000008")
        self.oHelper.SetValue("018 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("019 - Tabela", "search")
        self.oHelper.SearchValue("Código", "22")   
        self.oHelper.SetButton("020 - Codigo Procedimento", "search")
        self.oHelper.SearchValue("Código", "40303136", True)
        self.oHelper.SetValue("022 - Qtd Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Autorizada")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("imprimir")
        self.oHelper.SwitchWindow()
        self.oHelper.CheckLink("Clique aqui.")
        self.oHelper.CloseWindow()
        self.oHelper.SwitchWindow()
        self.oHelper.EndCase()


# Prorrogação de Internação Parcialmente Autorizada com Impressão
    def test_PPLPRORINT_CT002(self):
        
        self.oHelper.ClickMenu("Principal > Guia de Prorrogação")
        self.oHelper.SetValue("003 - Numero da Guia de So", "000120180800000010")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("003 - Numero da Guia de So", "add")
        self.oHelper.SetButton("011 - Nome Profissional So", "search")
        self.oHelper.SearchValue("Código", "000008")
        self.oHelper.SetValue("018 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("019 - Tabela", "search")
        self.oHelper.SearchValue("Código", "22")   
        self.oHelper.SetButton("020 - Codigo Procedimento", "search")
        self.oHelper.SearchValue("Código", "40303136", True)
        self.oHelper.SetValue("022 - Qtd Sol.", "2", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("019 - Tabela", "search")
        self.oHelper.SearchValue("Código", "22")   
        self.oHelper.SetButton("020 - Codigo Procedimento", "search")
        self.oHelper.SearchValue("Código", "40311236", True)
        self.oHelper.SetValue("022 - Qtd Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Autorizada")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("imprimir")
        self.oHelper.SwitchWindow()
        self.oHelper.CheckLink("Clique aqui.")
        self.oHelper.CloseWindow()
        self.oHelper.SwitchWindow()
        self.oHelper.EndCase()

# test_PPLPRORINT_CT003 - Prorrogação de Internação Negada
    def test_PPLPRORINT_CT003(self):
        
        self.oHelper.ClickMenu("Principal > Guia de Prorrogação")
        self.oHelper.SetValue("003 - Numero da Guia de So", "000120180800000010")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("003 - Numero da Guia de So", "add")
        self.oHelper.SetButton("011 - Nome Profissional So", "search")
        self.oHelper.SearchValue("Código", "000008")
        self.oHelper.SetValue("018 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("019 - Tabela", "search")
        self.oHelper.SearchValue("Código", "22")   
        self.oHelper.SetButton("020 - Codigo Procedimento", "search")
        self.oHelper.SearchValue("Código", "40311236", True)
        self.oHelper.SetValue("022 - Qtd Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Nao Autorizada")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("imprimir")
        self.oHelper.SwitchWindow()
        self.oHelper.CheckLink("Clique aqui.")
        self.oHelper.CloseWindow()
        self.oHelper.SwitchWindow()
        self.oHelper.EndCase()

# test_PPLPRORINT_CT004 - Prorrogação de Internação em Auditoria
    def test_PPLPRORINT_CT004(self):
        
        self.oHelper.ClickMenu("Principal > Guia de Prorrogação")
        self.oHelper.SetValue("003 - Numero da Guia de So", "000120180800000010")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("003 - Numero da Guia de So", "add")
        self.oHelper.SetButton("011 - Nome Profissional So", "search")
        self.oHelper.SearchValue("Código", "000008")
        self.oHelper.SetValue("018 - Indicacao Clinica", "Teste")
        self.oHelper.SetButton("019 - Tabela", "search")
        self.oHelper.SearchValue("Código", "22")   
        self.oHelper.SetButton("020 - Codigo Procedimento", "search")
        self.oHelper.SearchValue("Código", "30101018", True)
        self.oHelper.SetValue("022 - Qtd Sol.", "1", True)
        self.oHelper.SetGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitModal("Em Análise")
        self.oHelper.SwitchModal("Fechar")
        self.oHelper.SetButton("imprimir")
        self.oHelper.SwitchWindow()
        self.oHelper.CheckLink("Clique aqui.")
        self.oHelper.CloseWindow()
        self.oHelper.SwitchWindow()
        self.oHelper.EndCase()

            

    @classmethod
    def tearDownClass(inst):
        '''
        Método que finaliza o TestCase
        '''
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
