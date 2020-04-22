from tir import Webapp
import unittest

class ATFA380(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "M SP 01 ", "01")

        inst.oHelper.Program("ATFA380")

    def test_ATFA380_001(self):
        #INCLUI UM REGISTRO, OBS: A NUMERAÇÃO É AUTOMATICA.
        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        
        #Parâmetros de perguntes
        self.oHelper.SetValue("MV_PAR01","ATF11001", name_attr=True) #Bem de
        self.oHelper.SetValue("MV_PAR02","ATF11001", name_attr=True) #Bem até

        self.oHelper.SetValue("MV_PAR03","", name_attr=True) #Grupo de
        self.oHelper.SetValue("MV_PAR04","ZZZZ", name_attr=True) #Grupo até

        self.oHelper.SetValue("MV_PAR05","", name_attr=True) #Centro de Custo de
        self.oHelper.SetValue("MV_PAR06","ZZZZZZZZZ",name_attr=True) #Centro de Custo até

        self.oHelper.SetValue("MV_PAR07","101010200005",name_attr=True ) #Conta de 
        self.oHelper.SetValue("MV_PAR08","101010200005",name_attr=True ) #Conta até
        
        self.oHelper.SetValue("MV_PAR11" , "" , name_attr=True ) #Item de
        self.oHelper.SetValue("MV_PAR12" , "ZZZZ" , name_attr=True ) #Item até
        
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Simular", True)
        self.oHelper.SetButton("Finalizar")

        self.oHelper.CheckResult("NJ_ITEM","000001", grid=True, line=1)#NJ_ITEM
        self.oHelper.CheckResult("NJ_BEM","ATF11001  ", grid=True, line=1)#NJ_BEM
        self.oHelper.CheckResult("NJ_TIPO","01", grid=True, line=1)#NJ_TIPO

        self.oHelper.CheckResult("NJ_VLREC01","100,00", grid=True, line=1)#NJ_VLREC01
        self.oHelper.CheckResult("NJ_VLTAX01","10,00", grid=True, line=1)#NJ_VLTAX01
        self.oHelper.CheckResult("NJ_VLORI01","100,00", grid=True, line=1)#NJ_VLORI01        
        self.oHelper.CheckResult("NJ_TPDEPR","Linear", grid=True, line=1)#NJ_TPDEPR

        #Carrega a grid com as atualizações alteradas e/ou para checar
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()
        
    def test_ATFA380_002(self):

            process = '00000000000000000008'

            self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")

            self.oHelper.SetButton("Alterar")

            self.oHelper.SetButton("Avançar")

            self.oHelper.SetButton("Avançar")
           
            self.oHelper.SetButton("Avançar")

            self.oHelper.SetValue("Simular", True)

            self.oHelper.SetButton("Finalizar") 
            
            self.oHelper.SetValue("Valor", "100,00", grid=True,row=1)#NJ_VLREC01   Valor
            self.oHelper.SetValue("Taxa", "99,00", grid=True,row=1)#NJ_VLTAX01      Taxa
            self.oHelper.SetValue("Venda","125,00", grid=True,row=1)#NJ_VLACMD01  Venda
            self.oHelper.LoadGrid()

            self.oHelper.CheckResult("NJ_VLREC01", "100,00", grid=True,line=1)#NJ_VLREC01
            self.oHelper.CheckResult("NJ_VLTAX01", "99,00", grid=True,line=1)#NJ_VLTAX01
            self.oHelper.CheckResult("NJ_VLVEN01", "125,00", grid=True,line=1)#NJ_VLVEN01
            self.oHelper.LoadGrid()

            self.oHelper.SetButton("Salvar")
            
            self.oHelper.AssertTrue()

    def test_ATFA380_003(self):
            
            process = '00000000000000000007'

            self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
            
            self.oHelper.SetButton("Visualizar")

            self.oHelper.SetButton("Avançar")
            self.oHelper.SetButton("Avançar")            
            self.oHelper.SetButton("Avançar")

            self.oHelper.SetButton("Finalizar")      

            self.oHelper.CheckResult("NJ_ITEM","000001", grid=True, line=1)
            self.oHelper.CheckResult("NJ_BEM","ATF11003", grid=True, line=1)
            self.oHelper.CheckResult("NJ_TIPO","01", grid=True, line=1)
            self.oHelper.CheckResult("NJ_VLREC01","50,00", grid=True, line=1)
            self.oHelper.CheckResult("NJ_VLTAX01","10,00", grid=True, line=1)       
            self.oHelper.CheckResult("NJ_TPDEPR","Linear", grid=True, line=1)
            self.oHelper.CheckResult("NJ_VLORI01","100,00", grid=True, line=1)

            self.oHelper.LoadGrid()
            
            self.oHelper.SetButton("Confirmar")

            self.oHelper.AssertTrue()

    def test_ATFA380_004(self):
       
        process = '00000000000000000009' #Alteração de simulação de Redução ao valor recuperavel de um Ativo/bem

        self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
        self.oHelper.SetButton("Outras ações", "Excluir")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Finalizar")

        self.oHelper.SetButton("Confirmar")
    
        self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
        self.oHelper.AssertFalse()

    def test_ATFA380_005(self):
        ##Efetivação de um registro de simulaçao de Redução ao Valor Recuperavel de um Ativo/Bem
        ##Parametros de ultima depreciação para poder efetivar o registro, use caso nao tenha feito na base manualmente, se não comente
        self.oHelper.AddParameter("MV_ULTDEPR","M SP 01","20160331","20160331","20160331")
        self.oHelper.SetParameters()

        process = '00000000000000000010' 

        self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
        self.oHelper.SetButton("Outras ações", "Efetivar")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Finalizar")

        self.oHelper.SetButton("Confirmar")
    
        self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Avançar")

        self.oHelper.CheckResult("NI_STATUS", "2 - Efetivação",grid=False)
        self.oHelper.SetButton("Avançar")

        self.oHelper.SetButton("Finalizar")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()
        self.oHelper.RestoreParameters()
    def test_ATFA380_006(self):  #Validar Helps 
        ##Validação de Helps de um registro de efetivação ja efetuada e nem que pode ser excluida pois ja foi efetuada.

        process = '00000000000000000010' #mudar depois na base congelada o registro

        self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
        self.oHelper.SetButton("Outras ações", "Efetivar")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Outras ações", "Excluir")
        self.oHelper.SetButton("OK")        

        self.oHelper.AssertFalse()

    def test_ATFA380_007(self):
           
        process = '00000000000000000010'
        self.oHelper.SearchBrowse(f"M SP 01 {process}", "Filial+processo")
        self.oHelper.SetButton("Outras ações", "Exportar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")

                                    ####
        self.oHelper.SetValue("MV_PAR01","ATF380EXPORT",grid=False)
        #self.oHelper.SetValue("MV_PAR02",r"C:\ProtheusT\\Base_congeladaSistemico\\exports\\",) ###Aguardando retorno para 
        #self.oHelper.SetFilePath(r"C:\\ProtheusT\\Base_congeladaSistemico\\exports\\")         ###
                                    ####

        self.oHelper.SetButton("Finalizar")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckView("Exportacao gerada com sucesso",element_type=help)
        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()

    def test_ATFA380_008(self):
         #INCLUI UM REGISTRO efetivado, mesmos registros do de inclusao de simulação 001
        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("MV_PAR01","ATF11001", name_attr=True) #Bem de
        self.oHelper.SetValue("MV_PAR02","ATF11001", name_attr=True) #Bem até
        self.oHelper.SetValue("MV_PAR03","", name_attr=True) #Grupo de
        self.oHelper.SetValue("MV_PAR04","ZZZZ", name_attr=True) #Grupo até
        self.oHelper.SetValue("MV_PAR05","", name_attr=True) #Centro de Custo de
        self.oHelper.SetValue("MV_PAR06","ZZZZZZZZZ",name_attr=True) #Centro de Custo até

        self.oHelper.SetValue("MV_PAR07","101010200005",name_attr=True ) #Conta de 
        self.oHelper.SetValue("MV_PAR08","101010200005",name_attr=True ) #Conta até
        
        self.oHelper.SetValue("MV_PAR11" , "" , name_attr=True ) #Item de
        self.oHelper.SetValue("MV_PAR12" , "ZZZZ" , name_attr=True ) #Item até
        
        self.oHelper.SetButton("Avançar")
        self.oHelper.SetValue("Simular", False)
        self.oHelper.SetButton("Finalizar")

        self.oHelper.CheckResult("NJ_ITEM","000001", grid=True, line=1)#NJ_ITEM
        self.oHelper.CheckResult("NJ_BEM","ATF11001  ", grid=True, line=1)#NJ_BEM
        self.oHelper.CheckResult("NJ_TIPO","01", grid=True, line=1)#NJ_TIPO

        self.oHelper.CheckResult("NJ_VLREC01","100,00", grid=True, line=1)#NJ_VLREC01
        self.oHelper.CheckResult("NJ_VLTAX01","10,00", grid=True, line=1)#NJ_VLTAX01
        self.oHelper.CheckResult("NJ_VLORI01","100,00", grid=True, line=1)#NJ_VLORI01        
        self.oHelper.CheckResult("NJ_TPDEPR","Linear", grid=True, line=1)#NJ_TPDEPR

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()