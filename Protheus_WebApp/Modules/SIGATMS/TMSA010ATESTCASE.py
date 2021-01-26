from tir import Webapp
import unittest

class TMSA010A(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','15/10/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA010')  		

    #Inclusão de registro
    def test_TMA010A_CT003(self):		

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.ClickBox("Descricao", "TABELA DE FRETE A RECEBER TMS", grid_number=1)

        self.oHelper.SetButton('Ok')

        self.oHelper.SetValue('DT0_CDRORI','Q57204')
        self.oHelper.SetValue('DT0_CDRDES','Q57204')
        self.oHelper.SetValue('DT0_TABTAR','0001')
        self.oHelper.SetValue('DT0_CODPRO','TMS-001-PERIGOSO')

        self.oHelper.ClickFolder("Complemento Tabela de Frete")
        self.oHelper.ClickGridCell("Produto", row=1, grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True)
        self.oHelper.SetValue('DTK_EXCMIN','10,0000',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTK_VALMIN','101,33',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTK_VALMAX','200,19',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Base Componente Taxa de Dificil Acesso")
        self.oHelper.ClickGridCell("Componente", row=1, grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True)
        self.oHelper.SetValue('DVY_VLBASE','140,00',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()

    #Esrutura 
    def test_TMA010A_CT004(self):
        self.oHelper.SearchBrowse("M SP    R00101Q57204")

        self.oHelper.SetButton("Outras ações", "Estrutura")
        self.oHelper.SetButton("Cancelar")
                       
        self.oHelper.AssertTrue()
    
    #Exclusão de registro
    def test_TMA010A_CT005(self):
        self.oHelper.SearchBrowse("M SP    R00101Q57204")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
                       
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

