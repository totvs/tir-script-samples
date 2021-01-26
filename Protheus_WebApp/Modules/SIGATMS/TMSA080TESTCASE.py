from tir import Webapp
import unittest

class TMSA080(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','10/11/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA080')  		

    #Inclusão de registro
    def test_TMSA080_CT001(self):		

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.ClickBox("Descricao", "TABELA DE FRETE A RECEBER TMS", grid_number=1)
        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('DTF_TABTAR','FLP')
        self.oHelper.SetValue('DTF_KMDE','100,0')
        self.oHelper.SetValue('DTF_KMATE','200,0')

        self.oHelper.SetValue('Ate          (Peso Mercadoria)','100.000,0000',grid=True)
        self.oHelper.SetValue('Valor','117,00',grid=True, grid_number=1, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()

    #Exclusao 
    def test_TMSA080_CT002(self):
        self.oHelper.SearchBrowse("M SP    R00101FLP")

        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
                       
        self.oHelper.AssertTrue()
    
    #Copia de registro
    def test_TMSA080_CT003(self):

        self.oHelper.SetButton("Outras Ações", "Copiar")
        self.oHelper.SetValue('Para Tabela','FLP')
        self.oHelper.SetValue('Km De','51.000,0')
        self.oHelper.SetValue('Km Ate','52.000,0')

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Confirma")

        self.oHelper.SearchBrowse("M SP    R00101FLP")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
                       
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

