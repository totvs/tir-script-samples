# Pré requisito
- Possuir o python instalado
- Ter configurado em 'Variáveis de Ambiente'

# Instalação do WebApp
- Baixar o webapp, o mesmo deve ser descompactado na mesma pasta que se encontra o appserver.ini
- Caminho = http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclienthtml_webapp/
- Dentro do ini deve criar uma tag como a apresentado:
    [WEBAPP]
    port=<port>
    Ex: port=9095

# config.json
- Na documentação possui o passo a passo para a configuração.
- O arquivo .json deve inserir em sua área de trabalho ou passar seu caminho como um parâmetro de qualquer inicialização dd classe.
- Dentro do .json da tag "Url" deve ser informado o IP e porta que foi configurado no INI do WebApp:
    "Url": "http://localhost:9095/"

# Documentação do TIR
- https://github.com/totvs/tir

# Definição das áreas para extração (BIXLink)
- O processo exige que seja seleciona uma área para prosseguir
- A primeira área que deva ser selecionada é a "Comercial"

# Processo do TesteCase (BIXLink)
- Será desmarcado a área anterior
- Será marcado a proxima área
- Isso tudo ocorre em ordem crescente
     
    1. Comercial
    2. Controladoria
    3. Financeiro
    4. Materiais
    5. Produção
    6. RH
    8. DL
    9. Serviços
    10. Varejo
    11. CRM
    12. Juridico

# OBSERVAÇÃO (BIXLink)
- A área PCO não possui TestCase, porém ela é apresentada no Wizard pois não foi possível retirar do configurador.

