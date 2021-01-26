from tir import Webapp
import unittest


class PCOC340(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "01/10/2020", "T1", "M SP 01", "57")

        inst.oHelper.Program("PCOC340")

   
    def test_PCOC340_001(self):
        # Caso de teste PCOC340 com movimento do periodo e PROCNIV falso
        self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        #self.oHelper.AddParameter("MV_PCOTPGR","","1")  # Tipo de Grafico utilizado nas consultas
        #self.oHelper.AddParameter("MV_PCOMCHV","","1") #Montar as chaves para processamento do saldo    
        self.oHelper.AddParameter("MV_PCOCPRC","","1")

        self.oHelper.SetParameters()

        self.oHelper.SearchBrowse("M SP 01 SP") 
        

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01102020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "1 - Linha")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR08", "50")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "50")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "050001")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "050001")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "ZZ")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")


        #self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Consultar")  

        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("X")

        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar"),
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("X")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    
    def test_PCOC340_002(self): 
    
        # Caso de teste PCOC340 MV_PCOTPGR","","2" E "MV_PCOMCHV","","2"
        self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        self.oHelper.AddParameter("MV_PCOTPGR","","2")  # Tipo de Grafico utilizado nas consultas
        #self.oHelper.AddParameter("MV_PCOGRAF", "", "F") #Pergunta nome do grafico para salvar  
        self.oHelper.AddParameter("MV_PCOMCHV","","2") #Montar as chaves para processamento do saldo    
       

        self.oHelper.SetParameters()

        self.oHelper.SearchBrowse("M SP 01 SP") 
        

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01102020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "1 - Linha")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Nao")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Nao")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Saldo final do periodo")
        self.oHelper.SetButton("Ok")


        self.oHelper.SetValue("MV_PAR08", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "zzzzzzzzzzzz")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "ZZ")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")


        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Ok")
        
        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()


       
    def test_PCOC340_003(self):
        # Caso de teste PCOC341 com movimento do periodo e PROCNIV TRUE
        self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        #self.oHelper.AddParameter("MV_PCOTPGR","","1")  # Tipo de Grafico utilizado nas consultas
        #self.oHelper.AddParameter("MV_PCOGRAF", "", "F") #Pergunta nome do grafico para salvar  
        #self.oHelper.AddParameter("MV_PCOMCHV","","1") #Montar as chaves para processamento do saldo    
       

        self.oHelper.SetParameters()

        self.oHelper.SearchBrowse("M SP 01 SP") 
        

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01102020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("Tipo do Grafico ?", "2 - Barra")
        self.oHelper.SetValue("MV_PAR06", "2")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        
        self.oHelper.SetValue("MV_PAR05", "RE")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "REALIZAD")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.SetValue("Movimento do periodo", True)
        self.oHelper.SetButton("Ok")        

       
        #FILTRO ORÇADO
        self.oHelper.SetValue("MV_PAR08", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "zzzzzzzzzzzz")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "ZZ")  # TP.SALDO ate ?
         
        self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")

        
        self.oHelper.SetButton("Ok")


        #FILTRO REALIZADO
        self.oHelper.SetValue("CO de ?", "")  # CO de ?
        self.oHelper.SetValue("CO Ate ?", "zzzzzzzzzzzz")  # Co ate ?
        self.oHelper.SetValue("Centro de Custo de ?", "")  # Centro de Custo de ?
        self.oHelper.SetValue("Centro de Custo Ate ?", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("PLANILHA de ?", "")  # planilha de  ?
        self.oHelper.SetValue("PLANILHA Ate ?", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        self.oHelper.SetValue("Item Contab de ?", "")  # Item de ?
        self.oHelper.SetValue("Item Contab Ate ?", "zzzzzzzzz")  # item  ate ?
        self.oHelper.SetValue("Cod Cl Valor de ? ", "")  # Cod Classe Vlr de ?
        self.oHelper.SetValue("Cod Cl Valor Ate ?", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("ENTIDADE 05 - CT CTBXSAL de", "")  # Entidade05 de ?
        #self.oHelper.SetValue("ENTIDADE 05 - CT CTBXSAL Ate", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("TP.SALDO de ?", "")  # TP.SALDO de ?
        self.oHelper.SetValue("TP.SALDO Ate ?", "ZZ")  # TP.SALDO ate ?

          
        self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")


        self.oHelper.SetButton("Ok")


        #self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("OK")  

        
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()



    
    def test_PCOC340_004(self):
        # Caso de teste PCOC341 com movimento do periodo e PROCNIV TRUE
        # Saldo final do periodo
        #self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        #self.oHelper.AddParameter("MV_PCOTPGR","","1")  # Tipo de Grafico utilizado nas consultas
        #self.oHelper.AddParameter("MV_PCOGRAF", "", "F") #Pergunta nome do grafico para salvar  
        #self.oHelper.AddParameter("MV_PCOMCHV","","1") #Montar as chaves para processamento do saldo    
       

        #self.oHelper.SetParameters()

        self.oHelper.SearchBrowse("M SP 01 SP") 
        

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01102020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("Tipo do Grafico ?", "10 - Pizza")
        self.oHelper.SetValue("MV_PAR06", "2")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Saldo final do periodo")
        
        self.oHelper.SetValue("MV_PAR05", "RE")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "REALIZAD")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        #self.oHelper.ClickLabel("Saldo final do periodo")
        self.oHelper.SetValue("Saldo final do periodo", True)
        self.oHelper.SetButton("Ok")        

       
        #FILTRO ORÇADO
        self.oHelper.SetValue("MV_PAR08", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "zzzzzzzzzzzz")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "ZZ")  # TP.SALDO ate ?
         
        self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")

        
        self.oHelper.SetButton("Ok")


        #FILTRO REALIZADO
        self.oHelper.SetValue("CO de ?", "")  # CO de ?
        self.oHelper.SetValue("CO Ate ?", "zzzzzzzzzzzz")  # Co ate ?
        self.oHelper.SetValue("Centro de Custo de ?", "")  # Centro de Custo de ?
        self.oHelper.SetValue("Centro de Custo Ate ?", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("PLANILHA de ?", "")  # planilha de  ?
        self.oHelper.SetValue("PLANILHA Ate ?", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        self.oHelper.SetValue("Item Contab de ?", "")  # Item de ?
        self.oHelper.SetValue("Item Contab Ate ?", "zzzzzzzzz")  # item  ate ?
        self.oHelper.SetValue("Cod Cl Valor de ? ", "")  # Cod Classe Vlr de ?
        self.oHelper.SetValue("Cod Cl Valor Ate ?", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("ENTIDADE 05 - CT CTBXSAL de", "")  # Entidade05 de ?
        #self.oHelper.SetValue("ENTIDADE 05 - CT CTBXSAL Ate", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("TP.SALDO de ?", "")  # TP.SALDO de ?
        self.oHelper.SetValue("TP.SALDO Ate ?", "ZZ")  # TP.SALDO ate ?

          
        self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")


        self.oHelper.SetButton("Ok")



        #self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Outras Ações", "Drilldown")
        self.oHelper.SetButton("Ok")
                
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Confirmar")

        #self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    
    def test_PCOC340_032(self): # Caso de teste gerado a partir da PCOA100 para cobertura

        #Posiciona no elemento



        #vERIFICAR ESSES 2 ABAIXO
        self.oHelper.SetButton('X')
        self.oHelper.Program('PCOA100')



        codigoCT005 = 'TIRPCOC340     '

        self.oHelper.WaitShow("Planilha Orcamentaria")
        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ? ", step = 6 )
        self.oHelper.SetValue("Tipo Exibição ? ? ","1 - Completa")
        self.oHelper.SetButton("Ok")

        #Reposiciona no elemento
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')
                        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=2)
        self.oHelper.ClickGridCell("Descricao", row=4, grid_number=1)

        self.oHelper.SetButton('Outras Ações', 'Consultas') 
        self.oHelper.ClickMenuPopUpItem("Cubo SP - PCO SQUAD CONTROL")
        self.oHelper.SetButton('Cancelar') 
       
        self.oHelper.SetButton('Outras Ações', 'Consultas')
        self.oHelper.ClickMenuPopUpItem("Cubo SP - PCO SQUAD CONTROL",position=2)
        
        self.oHelper.SetValue("MV_PAR01", "01112020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("Tipo do Grafico ?", "2 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")

        #self.oHelper.ClickCheckBox("Considerar saldos zerados")
        #self.oHelper.SetFocus("Considerar saldos zerados", grid_cell=False)

        #self.oHelper.SetButton("Ok")

        
        #self.oHelper.SetValue("MV_PAR06", "RE")  # Config.Cubo Serie 1 ?
        #self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        #self.oHelper.SetValue("MV_PAR08", "REALIZAD")  # Descrição Série ?
        #self.oHelper.SetValue("Descrição Série ?", "REALIZAD")  # Descrição Série ?

        # Considerar  ? Saldo final do periodo/Movimento do periodo
        #self.oHelper.SetValue("Movimento do periodo", True)
           

       
        #FILTRO ORÇADO
        self.oHelper.SetValue("MV_PAR08", "340001")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "340001")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "PCOC340")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "PCOC340")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "TIRPCOC340     0001")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "TIRPCOC340     0001")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "OR")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "OR")  # TP.SALDO ate ?
         
        self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")
      
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitProcessing("Gerando Cubos...")
        self.oHelper.WaitProcessing("Verificando saldos...")

        #self.oHelper.WaitProcessing("Processando...")
        #self.oHelper.Waitshow("Consulta Saldos por Periodos - Cubos")


        #FILTRO REALIZADO
        #self.oHelper.SetValue("CO de ?", "")  # CO de ?
        #self.oHelper.SetValue("CO Ate ?", "zzzzzzzzzzzz")  # Co ate ?
        #self.oHelper.SetValue("Centro de Custo de ?", "")  # Centro de Custo de ?
        #self.oHelper.SetValue("Centro de Custo Ate ?", "zzzzzzzzz")  # Centro de Custo de ?
        #self.oHelper.SetValue("PLANILHA de ?", "")  # planilha de  ?
        #self.oHelper.SetValue("PLANILHA Ate ?", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        #self.oHelper.SetValue("Item Contab de ?", "")  # Item de ?
        #self.oHelper.SetValue("Item Contab Ate ?", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("Cod Cl Valor de ? ", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("Cod Cl Valor Ate ?", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("ENTIDADE 05 - CT CTBXSAL de", "")  # Entidade05 de ?
        #self.oHelper.SetValue("ENTIDADE 05 - CT CTBXSAL Ate", "zzzzzzzzz")  # Entidade 05 ate ?        
        #self.oHelper.SetValue("TP.SALDO de ?", "")  # TP.SALDO de ?
        #self.oHelper.SetValue("TP.SALDO Ate ?", "ZZ")  # TP.SALDO ate ?

          
        #self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        #self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")


        #self.oHelper.SetButton("Ok")


        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Cancelar")
        
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
        #self.oHelper.SetButton("OK")  
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
        #self.oHelper.SetButton("OK")  
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
        #self.oHelper.SetButton("OK")  
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
        #self.oHelper.SetButton("OK")  
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
        #self.oHelper.SetButton("OK")  
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
        #self.oHelper.SetButton("OK")  
        #self.oHelper.SetButton("Outras Ações", "Drilldown")
       
        #self.oHelper.SetButton("OK")  

        
        #self.oHelper.SetButton("Cancelar")
        #self.oHelper.SetButton("Cancelar")
        #self.oHelper.SetButton("Cancelar")
        #self.oHelper.SetButton("Cancelar")
        #self.oHelper.SetButton("Cancelar")
        #self.oHelper.SetButton("Cancelar")
        #self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

        ##ANALISAR AQUI SE DEIXOU NO PCOC340 PARA EXECUÇÃO DO P´ROXIMO TESTECASE
        self.oHelper.SetButton('X')
        self.oHelper.Program('PCOC340')

    def test_PCOC340_033(self):
        self.oHelper.SetButton('X')
        self.oHelper.Program('PCOA100')



        codigoCT005 = 'TIRPCOC340     '

        self.oHelper.WaitShow("Planilha Orcamentaria")
        self.oHelper.SetKey( key = "F12", wait_show="Tipo Exibição ? ? ", step = 6 )
        self.oHelper.SetValue("Tipo Exibição ? ? ","1 - Completa")
        self.oHelper.SetButton("Ok")

        #Reposiciona no elemento
        self.oHelper.SearchBrowse(f'M SP 01 {codigoCT005}0001')
                        
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetFocus("Descricao", grid_cell=True, row_number=2)
        self.oHelper.ClickGridCell("Descricao", row=4, grid_number=1)

        self.oHelper.SetButton('Outras Ações', 'Consultas') 
        self.oHelper.ClickMenuPopUpItem("Cubo SP - PCO SQUAD CONTROL")
        self.oHelper.SetButton('Cancelar') 
       
        self.oHelper.SetButton('Outras Ações', 'Consultas')
        self.oHelper.ClickMenuPopUpItem("Cubo SP - PCO SQUAD CONTROL",position=2)
        
        self.oHelper.SetValue("MV_PAR01", "01112020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("Tipo do Grafico ?", "2 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")

        #self.oHelper.ClickCheckBox("Considerar saldos zerados")
        #self.oHelper.SetFocus("Considerar saldos zerados", grid_cell=False)

        #self.oHelper.SetButton("Ok")

        
        #self.oHelper.SetValue("MV_PAR06", "RE")  # Config.Cubo Serie 1 ?
        #self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        #self.oHelper.SetValue("MV_PAR08", "REALIZAD")  # Descrição Série ?
        #self.oHelper.SetValue("Descrição Série ?", "REALIZAD")  # Descrição Série ?

        # Considerar  ? Saldo final do periodo/Movimento do periodo
        #self.oHelper.SetValue("Movimento do periodo", True)
           

       
        #FILTRO ORÇADO
        self.oHelper.SetValue("MV_PAR08", "340001")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "340001")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "PCOC340")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "PCOC340")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "TIRPCOC340     0001")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "TIRPCOC340     0001")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "OR")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "OR")  # TP.SALDO ate ?
         
        self.oHelper.ClickCheckBox("Processar resultados de valores zerados ")
        self.oHelper.ClickCheckBox("Mostrar resultados sintéticos a partir do segundo nivel ")
      
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitProcessing("Gerando Cubos...")
        self.oHelper.WaitProcessing("Verificando saldos...")

        self.oHelper.SetButton("Outras Ações", "Grafico")
        self.oHelper.SetButton("Outras Ações", "Grafico")
        self.oHelper.SetButton("Outras Ações", "Salva/BMP")

        self.oHelper.SetButton("Fechar")
       
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Cancelar")
        

        ##ANALISAR AQUI SE DEIXOU NO PCOC340 PARA EXECUÇÃO DO P´ROXIMO TESTECASE
        self.oHelper.SetButton('X')
        self.oHelper.Program('PCOC340')

        self.oHelper.AssertTrue()

    def test_PCOC340_034(self):

        self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        self.oHelper.AddParameter("MV_PCOCPRC","","1")

        self.oHelper.SetParameters()

        self.oHelper.SearchBrowse("M SP 01 SP") 
        

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01102020")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122020")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "1 - Linha")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Exibe total nas series? Sim/Nao
             
        self.oHelper.ClickLabel("Sim")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR08", "50")  # CO de ?
        self.oHelper.SetValue("MV_PAR09", "50")  # Co ate ?
        self.oHelper.SetValue("MV_PAR11", "050001")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR12", "050001")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR14", "")  # planilha de  ?
        self.oHelper.SetValue("MV_PAR15", "zzzzzzzzzzzzzzzzzzz")  #  planilha ate ?
        #self.oHelper.SetValue("MV_PAR07", "")  # Item de ?
        #self.oHelper.SetValue("MV_PAR08", "zzzzzzzzz")  # item  ate ?
        #self.oHelper.SetValue("MV_PAR09", "")  # Cod Classe Vlr de ?
        #self.oHelper.SetValue("MV_PAR10", "zzzzzzzzz")  # Cod. Classe de Vlr ate ?
        #self.oHelper.SetValue("MV_PAR11", "")  # Entidade05 de ?
        #self.oHelper.SetValue("MV_PAR12", "zzzzzzzzz")  # Entidade 05 ate ?        
        self.oHelper.SetValue("MV_PAR26", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR27", "ZZ")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")


        #self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Outras Ações", "Pesquisar")

        self.oHelper.SetValue("Pesquisar texto ?", "teste") 

        self.oHelper.ClickLabel("Utilizar pesquisa exata")   
        self.oHelper.ClickLabel("Pesquisar a partir do inicio")
        self.oHelper.ClickLabel("Coincidir maiusculas e minusculas")        
         

        
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Cancelar")
      
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()

    
        

   



        





