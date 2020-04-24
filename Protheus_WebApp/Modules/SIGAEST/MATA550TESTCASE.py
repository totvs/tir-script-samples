from tir import Webapp
import unittest

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","20/09/2019","T1","D MG 01 ","04")
        inst.oHelper.Program("MATA550")

    def test_MATA550_001(self):
        cod     =  'ESTSEGRADE01'
        desc    =  'MATA550TIR'
        tipo    =  'PA'
        unidade =  'UN'
        armazem =  '01'
        linha   =  '12'
        coluna  =  '13'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Codigo", cod)
        self.oHelper.SetValue("Descricao", desc)
        self.oHelper.SetValue("Tipo", tipo)
        self.oHelper.SetValue("Unidade", unidade)
        self.oHelper.SetValue("Armazem Pad.", armazem)
        self.oHelper.SetValue("Tabela Linha", linha)
        self.oHelper.SetValue("Tabela Colun", coluna)
        self.oHelper.ClickFolder("E-Commerce")
        self.oHelper.SetValue("Título ", desc)           
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetKey("RIGHT", grid=True)        
        self.oHelper.SetValue("[01] PRETO", "X", grid=True,row=1)
        self.oHelper.LoadGrid() 
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()