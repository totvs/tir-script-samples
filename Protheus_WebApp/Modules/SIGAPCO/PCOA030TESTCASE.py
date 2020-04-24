from tir import Webapp
import unittest

class PCOA030(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "10/03/2017", "T1", "M SP 01 ", "01")
        inst.oHelper.Program("PCOA030")

    def test_PCOA030_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01 ")
        codigo = "900002"
        self.oHelper.SetValue("AK8_CODIGO",f"{codigo}", name_attr=True) #Código
        self.oHelper.SetValue("AK8_DESCRI","TESTE PCOA030 TIR", name_attr=True) #Descrição
        self.oHelper.SetValue("AK8_FUNCAO","PCOXRES", name_attr=True) #Função
        self.oHelper.SetValue("AK8_VISUAL","2", name_attr=True) #Exibe Lancto
        self.oHelper.LoadGrid()
        self.oHelper.ClickFolder("Pontos de Lançamento")
        self.oHelper.SetValue("Descricao","TESTE LINHA 1  ", grid=True)
        self.oHelper.SetValue("Entidade","FO6", grid=True)
        self.oHelper.SetValue("Indice","1", grid=True) 
        self.oHelper.LoadGrid()
        self.oHelper.SetKey("DOWN", grid=True)
        self.oHelper.SetValue("Descricao","TESTE LINHA 2  ", grid=True)
        self.oHelper.SetValue("Entidade","FO6", grid=True)
        self.oHelper.SetValue("Indice","1", grid=True) 
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.LoadGrid()
        self.oHelper.SearchBrowse(f"M SP    {codigo}", "Filial+codigo")        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.ClickFolder("Pontos de Lançamento")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SearchBrowse(f"M SP    {codigo}", "Filial+codigo")        
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.SetButton("Excluir")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
