from tir import Webapp
import time
import unittest

class TMKA250(unittest.TestCase):

    @classmethod
    def setUpClass(inst):   
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMK','03/09/2019','T1','D MG 01 ','13')
        inst.oHelper.Program('TMKA250')

    def test_TMKA250_002(self):
      
        self.oHelper.SetButton("Incluir")
                
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetButton("Adiciona Ocorrencia")
        self.oHelper.SetValue("Código", "000007")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Adiciona Ação")
        self.oHelper.SetValue("Código", "000001")
        self.oHelper.SetButton("OK")
        
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_TMKA250_003(self):
      
        self.oHelper.SearchBrowse("D MG    000003")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetButton("Adiciona Ação")
        self.oHelper.SetValue("Código", "000005")
        self.oHelper.SetButton("OK")

        self.oHelper.ClickTree("TMK003")
        self.oHelper.ClickTree("ALTERAR ACAO")
        self.oHelper.SetButton("Move para baixo")
        self.oHelper.SetButton("Move para cima")
        self.oHelper.ClickTree("Excluir ACAO")
        self.oHelper.SetButton("Remover item")
        self.oHelper.SetButton("Sim")
        
        self.oHelper.SetButton("Adiciona Ação")
        self.oHelper.SetValue("Código", "000002")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()

    def test_TMKA250_004(self):
      
        self.oHelper.SearchBrowse("D MG    000008")
        self.oHelper.SetButton("Outras Ações","Excluir")
                
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        
        self.oHelper.AssertTrue()

    def test_TMKA250_005(self):
      
        self.oHelper.SearchBrowse("D MG    000004")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.WaitShow("Atualização da Relação Ocorrencia x Ação - VISUALIZAR")

        self.oHelper.ClickTree("TMK004")
        self.oHelper.ClickTree("EXCLUIR ACAO")
        
        self.oHelper.SetButton("Confirmar")
                
        self.oHelper.AssertTrue()

    '''def test_TMKA250_006(self):
      
        self.oHelper.SetButton("Incluir")
                
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetButton("Adiciona Ocorrencia")
        self.oHelper.SetValue("Código", "000003")

        self.oHelper.CheckHelp("TK250CADRE Problema: Essa reclamação já foi informada anteriormente nesse cadastro de relacionamento.", "Fechar")

        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()'''

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 