from tir import Webapp
import unittest
import datetime

class TMSA018(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA018')
    
    # Inclusão básica de registro. M SP    15/10/2020    
    def test_TMA018_CT001(self):

        self.oHelper.SetValue("Filial de Origem de ?", "")
        self.oHelper.SetValue("Filial de Origem até ?", "ZZZZZZZZ")
        self.oHelper.SetValue("Filial de Destino de ?", "")
        self.oHelper.SetValue("Filial de Destino até ?", "ZZZZZZZZ")
        self.oHelper.SetValue("Data de Emissão de ?", "01/01/2020")
        self.oHelper.SetValue("Data de Emissão até ?", "01/12/2020")
        self.oHelper.SetValue("Status Agendamento de ?", "1")
        self.oHelper.SetValue("Status Agendamento até ?", "6")
        self.oHelper.SetValue("Cliente Remetente de ?", "")
        self.oHelper.SetValue("Loja de ?", "")
        self.oHelper.SetValue("Cliente Remetente até ?", "ZZZZZZ")
        self.oHelper.SetValue("Loja até ?", "ZZ")
        self.oHelper.SetValue("Cliente Destinatário de ?", "")
        self.oHelper.SetValue("Loja de ?", "")
        self.oHelper.SetValue("Cliente Destinatário até ?", "ZZZZZZ")
        self.oHelper.SetValue("MV_PAR16", "ZZ", name_attr=True)
        self.oHelper.SetButton('OK')  # Confirmação da janela dos Parâmetros

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.SetFocus("DYD_FILDOC")
        self.oHelper.SetKey("F3")

        self.oHelper.SearchBrowse("M SP 03 000000003A01")
        self.oHelper.SetButton('OK') 

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        
        self.oHelper.AssertTrue()
    
    # Exclusão de registro.    
    def test_TMA018_CT002(self):
        self.oHelper.SetButton('OK') 

        self.oHelper.SearchBrowse("M SP   M SP 03 000000003A01", 'Filial+fil. Docto + No.docto. + Serie Docto. + Agendament')
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Outras Ações","Cancelar")        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetValue("Digite um motivo para o cancelamento:", "TESTE TMS")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()  
    
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
