from tir import Webapp
import unittest

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","17/09/2019","T1","D MG 01 ","04")
        inst.oHelper.Program("MATA260")

    def test_MATA260_001(self):
        prod        =  'ESTSE0000000000000000000000557'
        armazemOri  =  '02'       
        Qtd         =  "10,00"      

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("ok")
        self.oHelper.SetValue("Produto", prod)
        self.oHelper.SetValue("Armazem  /  Endereco",armazemOri)       
        self.oHelper.SetValue('Quantidade Primaria',Qtd)        
        self.oHelper.SetButton("Salvar")        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()