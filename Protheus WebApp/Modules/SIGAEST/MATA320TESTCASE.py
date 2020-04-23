from tir import Webapp
import unittest

class MATA320(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","16/10/2019","T1","D MG 01 ","04")
        inst.oHelper.Program("MATA320")

    def test_MATA320_001(self):
        Cod   = 'ESTSE0000000000000000000000565'
        Custo = 0

        self.oHelper.SetButton("Parâmetros")     
        self.oHelper.SetValue("Utilizar Qual Moeda ?", 'Nenhuma')
        self.oHelper.SetValue("Utilizar Taxa ?", 'Mensal')       
        self.oHelper.SetValue('Calcular os Custos Por ?',"Estrutura")
        self.oHelper.SetValue('Considerar Ult. Preco Compra ?',"Sim")
        self.oHelper.SetValue('Dt.Final Ref.Taxa ?',"16/10/2019")
        self.oHelper.SetValue('Do Tipo do Produto',"")
        self.oHelper.SetValue('Ate o Tipo do Produto',"ZZ")      
        self.oHelper.SetValue('Do Grupo do Produto',"EST1") 
        self.oHelper.SetValue('Ate o Grupo do Produto',"EST1") 
        self.oHelper.SetValue("Considerar Qtdes. Negativa ?", 'Sim')
        self.oHelper.SetValue("Avisar Divergencia ?", 'Atualizar')
        self.oHelper.SetValue("Seleciona filiais ?", 'Nao')
        self.oHelper.SetValue("Considera Mão de Obra?", 'Ambos')
        self.oHelper.SetValue("Considera Tipo Dec. OP ?", 'Sim')              
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetLateralMenu("Atualizações > Cadastros > Produto > Produtos")
        self.oHelper.SearchBrowse(f"D MG 01 {Cod}", "Filial+codigo")
        self.oHelper.SetButton("Visualizar")
      
        Custo = float(self.oHelper.GetValue("B1_CUSTD").replace(",","."))
        
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetKey("ESC")
        self.oHelper.Program('MATA320')    
        Custo > 0
        self.oHelper.AssertTrue()     

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()