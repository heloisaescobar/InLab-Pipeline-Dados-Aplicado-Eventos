# OCI InLab - Pipeline de Dados Aplicado a Eventos

* [OCI Object Storage](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/tree/master#oci-object-storage)
* [OCI Functions](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/README.md#oci-functions)
* [OCI Data Integration](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#oci-data-integration)
* [Autonomous Data Warehouse](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#autonomous-data-warehouse)
* [OCI Events](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#oci-events)
* [Tópico Bônus - Execução do Fluxo](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#t%C3%B3pico-b%C3%B4nus---execu%C3%A7%C3%A3o-do-fluxo)

## OCI Object Storage

<i>Pré Requisitos: Ter Compartimento Criado</i>

Vamos iniciar com a criação dos buckets dentro do Object Storage, onde irá nos permitir armazenar nossos dados de trabalho.
Expanda a lista de serviços da OCI utilizando o menu de hamburguer, no canto superior esquerdo. Em seguida, selecione Storage e clique em buckets.

![image](https://user-images.githubusercontent.com/46925501/155425296-ad145c2c-a006-4b20-b7a9-9ccefc2b9532.png)

Verifique se você está no compartimento correto e clique em <i>Create Bucket</i>:

![image](https://user-images.githubusercontent.com/46925501/155425373-439e0582-c1dc-4535-960c-c462777e10d8.png)

Atribua um nome para o seu bucket, habilite a opção <i>Emit Object Events</i> e clique em <i>Create</i> para que seu bucket seja provisionado.

![image](https://user-images.githubusercontent.com/46925501/155425463-0c344700-484c-4f81-aeb6-b1e444fda5d1.png)

Após a criação do bucket, vamos realizar upload do arquivo <i>[Personagens.xlsx](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/Personagens.csv)</i>.

Para fazer upload do arquivo, acesse o buckets criado no passo anterior e clique em Upload:

![image](https://user-images.githubusercontent.com/46925501/155425587-e44a2c7d-399a-49ea-af3d-1d01907f63f4.png)

Irá abrir uma caixa para que você possa selecionar o arquivo que deseja fazer upload:

![image](https://user-images.githubusercontent.com/46925501/155425638-7a9f1901-e30a-4eff-902d-c2a0f0186c46.png)

<b>Realizei novamente os passos anteriores e crie um bucket vazio.</b>


## OCI Functions

<i>Pré Requisitos: Ter Compartimento Criado, VCN, Aplicar as [Policies](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/policies_anexo.txt)</i>.

### Step 1

Vamos iniciar criando a estrutura do functions, onde vamos montar e fazer o deploy dos nossos scripts.

Expanda a lista de serviços da OCI utilizando o menu de hamburguer, no canto superior esquerdo. Em seguida, selecione <i>Developer Services</i> e clique em <i>Applications</i>.

![image](https://user-images.githubusercontent.com/46925501/155426553-2023a968-3f4a-4400-83bc-635c9432e94b.png)

Clique em <i>Create Application</i>

![image](https://user-images.githubusercontent.com/46925501/155426593-050c5b2f-1e34-44f8-b06b-d0e413b8ffef.png)

Informar o nome da sua aplicação, a VCN na qual deseja criar sua aplicação e a subnet de escolha e clique em criar:

![image](https://user-images.githubusercontent.com/46925501/155426670-10b26cec-5daa-485d-a56c-ca1ca2d2a7f3.png)

Após a Criação, acesse a Functions que você criou clique em <i>Getting Started</i>

![image](https://user-images.githubusercontent.com/46925501/155426941-f4b67189-4370-4a53-a655-deddc7608fd8.png)

Vamos escolher a opção de configuração através do <i>Cloud Shell Setup</i>

![image](https://user-images.githubusercontent.com/46925501/155427083-86e47860-842e-400e-b18a-628f71d1b07b.png)

<b>Seguir com o procedimento em tela até o passo 7</b>

### Step 2

Nesse passo vamos configurar os dois functions que vamos utilizar nessa dinâmica:

* O Primeiro [Function](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/tree/master/scripts_apoio/functions/fn_getApi) é um script para coletar informações de uma API.
* O Segundo [Function](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/tree/master/scripts_apoio/functions/fn_execute_task), vamos utilizar para chamar uma tarefa no OCI Data Integration para execução.

<b>Para criar o primeiro functions, vamos seguir os comandos abaixo:</b>

> fn init --runtime python fn_getApi

Será criado uma estrutura com três arquivos (func.py, func.yaml e requirements.txt), copiar o conteúdo dos arquivos [func.py](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/functions/fn_getApi/func.py) e [requirements.txt](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/functions/fn_getApi/requirements.txt)

Após a configuração dos dois arquivos do passo anterior, executar o comando abaixo:

> fn -v deploy --app App_InLab

Se finalizar com mensagem de sucesso, foi realizado o deploy com sucesso do seu código. Reserver que vamos utilizar ele mais a frente.

<b>Para o segundo Function, realize primeiro a configuração do OCI Data Integration e depois retorne nesse ponto para finalizarmos a configuração </b>

Após a configuração do OCI Data Integration, vamos seguir com a configuração do segundo Function:

> fn init --runtime python fn_execute_task

Será criado uma estrutura com três arquivos (func.py, func.yaml e requirements.txt), copiar o conteúdo dos arquivos [func.py](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/functions/fn_execute_task/func.py) e [requirements.txt](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/functions/fn_execute_task/requirements.txt)

Para o arquivo [func.py](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/functions/fn_execute_task/func.py), será necessário obter algumas informações do OCI Data Integration e do Object Storage. Para coletar essas informações, [clique aqui](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/README.md#fn_execute_task---coletando-par%C3%A2metros).

Configurado o código no passo acima, siga com a execução do próximo comando:

> fn -v deploy --app App_InLab

Se finalizar com mensagem de sucesso, foi realizado o deploy com sucesso do seu código. Reserver que vamos utilizar ele mais a frente.

## OCI Data Integration

<i>Pré Requisitos: Ter Compartimento Criado, VCN, Aplicar as [Policies](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/policies_anexo.txt)</i>.

### Criação do Workspace

<b>Provisionamento do Workspace</b>

Expanda a lista de serviços da OCI utilizando o menu de hambúrguer, no canto superior esquerdo. Em seguida, selecione Oracle Database e clique em Analytics & AI e clique me Data Integration

![image](https://user-images.githubusercontent.com/46925501/155429984-23074dfd-a568-4474-bd97-fbb84aa25f3f.png)

Clique em <i>Create Workspace</i>

![image](https://user-images.githubusercontent.com/46925501/155430011-cf283564-089c-4f5c-96f4-09b26182f8aa.png)

Dê um nome ao Workspace, Descrição, clique em ‘Enable private Networking’ e selcione uma VCN e uma Subnet <i>PRIVADA</i>. Em seguida clique em <i>Create</i>.

![image](https://user-images.githubusercontent.com/46925501/155430061-25807ea8-98bf-4958-be52-860675de0c4b.png)

Após alguns minutos você verá seu workspace listado como <i>Active</i>.

![image](https://user-images.githubusercontent.com/46925501/155430098-223d7788-d99e-4c73-8a50-3199a3302ecd.png)

### Criação dos Data Assets

<b>Criando o Data Asset do Autonomous Data Warehouse</b>

Pré-requisito: Ter um Autonomous Data Warehouse provisionado, ter um usuário com privilégios DBMS_CLOUD e DWROLE. Para provisionar o Autonomous [clique aqui](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#autonomous-data-warehouse)

Antes começarmos a criação do Data Asset do Oracle Autonomous Data Warehouse nós precisamos salvar a Wallet de acesso ao banco. Para isso siga os passos abaixo:
Expanda a lista de serviços da OCI utilizando o menu de hambúrguer, no canto superior esquerdo. Em seguida, selecione Oracle Database e clique em Autonomous Data Warehouse.

![image](https://user-images.githubusercontent.com/46925501/155430296-1fc6b6be-c5a3-47e8-9108-c4cb1776f376.png)

Em seguida, clique sobre o nome da instância de Autonomous Data Warehouse que você tenha disponível (pré-requisito)

![image](https://user-images.githubusercontent.com/46925501/155430313-ddc907a0-e375-42c4-9328-48dec42212ee.png)

Você será redirecionado para uma janela com os detalhes da instância de Autonomous Data Warehouse. Nesta tela clique sobre o botão DB Connection.

![image](https://user-images.githubusercontent.com/46925501/155430331-200b01a7-c21d-4a74-a72a-f0c4d664affc.png)

Uma caixa de diálogo será exibida. Nesta, clique em Download Wallet.

![image](https://user-images.githubusercontent.com/46925501/155430342-6432977a-da15-45ec-aecc-a902c17bf714.png)

Digite uma senha de sua preferência, clique em Download e salve o arquivo .zip em uma pasta desejada.

![image](https://user-images.githubusercontent.com/46925501/155430352-6ca40330-33c3-42ee-9a30-4a02befa546f.png)

Acesse a aba do OCI Data Integration:

![image](https://user-images.githubusercontent.com/46925501/155430369-d5144133-97da-4d7b-be95-7cdb96556074.png)

E selecione o Workspace que foi criado durante a parte de preparação do ambiente:

![image](https://user-images.githubusercontent.com/46925501/155430413-d5c13497-26d4-4a64-877c-2abc02b7368e.png)

Clique no sinal de <b>+</b> e em seguida clique em Data Assets

![image](https://user-images.githubusercontent.com/46925501/155430452-cbc4d61f-d6f9-4dd3-96e8-f19c10457026.png)

Clique em Create Data Asset, você pode observar que uma nova aba chamada Create Data Asset foi aberta.

![image](https://user-images.githubusercontent.com/46925501/155430469-201cf816-1e80-4441-a219-72976c0b40eb.png)

Dê o nome ao Data Asset <i>DA_ADW01</i> (como na imagem) e selecione o Type como Oracle Autonomous Data Warehouse.

![image](https://user-images.githubusercontent.com/46925501/155430490-75e71c87-ae4b-4444-9224-6c2f87f27f46.png)

Mais abaixo, na mesma página mantenha o botão de rádio Upload Wallet selecionado., clique em Select File e localize o arquivo .zip que você fez o download anteriormente. Faça a carga do arquivo .zip, insira a senha do .zip e escolha o Service Name <b>(<nome_do_ADW>.medium)</b>

![image](https://user-images.githubusercontent.com/46925501/155430535-0d260919-2398-44e5-832c-75601b5f8655.png)

Deixe a opção Default Connection no Name e Identifier. Em seguida coloque o User name e Password fornecido (em caso de dúvida informe ao palestrante que ele te fornecerá as credenciais).
  
Clique em Teste Connection, se a conexão for bem sucedida clique no botão <i>Create</i>.

![image](https://user-images.githubusercontent.com/46925501/155430632-78dc0791-c3e1-4fb5-84f6-34d01e263b0e.png)

Pronto você criou um Data Asset do Oracle Autonomous Data Warehouse.

<b>Criando o Data Asset do Object Storage</b>
  
Retorne para a aba do OCI Data Integration

![image](https://user-images.githubusercontent.com/46925501/155430849-aaadbef9-866c-4234-aa3b-bee93b6c806e.png)

E selecione o Workspace que foi criado durante a parte de preparação do ambiente.
  
![image](https://user-images.githubusercontent.com/46925501/155430872-c9f90037-e421-4cee-af6f-b2f823998f77.png)

Clique no sinal de <b>+</b> e em seguida clique em Data Assets

![image](https://user-images.githubusercontent.com/46925501/155430906-238282a3-7fea-4829-8ded-626827d63679.png)

Clique em Create Data Asset, você pode observar que uma nova aba chamada Create Data Asset foi aberta.

![image](https://user-images.githubusercontent.com/46925501/155430929-cc3e81d7-0641-459f-88a0-81a69a70bde6.png)

Dê o nome ao Data Asset “DA_OBJstorage” (como na imagem) e selecione o Type como Oracle Object storage

![image](https://user-images.githubusercontent.com/46925501/155430952-90c03e17-a0bb-420d-8760-279dbd0ce87d.png)

Nesta fase, necessitamos de algumas informações que estão distribuídas na console da OCI. Duplique a aba do seu navegador para navegar pelas próximas páginas. Primeiro precisaremos da “tenancy OCID” em seguida o Namespace do Object Storage.

Na aba duplicada, no o canto superior direito clique na figura humana e, em seguida, clique em Tenancy.
  
![image](https://user-images.githubusercontent.com/46925501/155431013-f407c853-719f-4012-abd9-88abe3af021e.png)

Uma tela com os detalhes da Tenancy será exibida. Localize o campo OCID e clique em Copy.
  
![image](https://user-images.githubusercontent.com/46925501/155431039-2c5f3b51-e925-46c7-bb98-94fd731547e1.png)

Reserve esse ID da tenancy, em seguida copie e reserve o identificador do Namespace do Object Storage (indicado em azul na imagem acima).

Retorne à aba do OCI Data Integration em que está criando o data asset do Object Storage e insira os valores copiados no campo Tenant OCID e Namespace. (Geralmente o campo Namespace é preenchido automaticamente após você colocar o OCID da tenancy, mas caso isso não ocorra cole o Namespace que você salvou no passo anterior)
A ultima informação necessário para configurarmos o Data Asset do Object Storage é o identificador da sua Region, você vai encontra-lo em sua URL como representado no imagem abaixo

![image](https://user-images.githubusercontent.com/46925501/155431089-7885a910-d1db-4b0d-a0b9-8139baa736f8.png)
  
Agora preencha as informações conforme a imagem abaixo:

![image](https://user-images.githubusercontent.com/46925501/155431113-1920ab63-c9a8-44d8-9b48-1fbaef95406b.png)

Mantenha as opções de Connection como estão e clique em Test Connection.
Se conexão for bem sucedida clique em Create:
![image](https://user-images.githubusercontent.com/46925501/155431192-ee12bbbf-6093-495a-8bd6-f9ca5c430ad2.png)

Você finalizou a criação dos Data Assets!

### Criação e Configuração do DataFlow Designer

<b>Criação do DataFlow</b>
Acesse a aba do OCI Data Integration

![image](https://user-images.githubusercontent.com/46925501/155432024-efe8aa55-967f-4201-99f9-fd123e481a8f.png)

E selecione o Workspace que criamos nos passos anteriores

![image](https://user-images.githubusercontent.com/46925501/155432080-749e96f2-2ac0-4229-8773-b247b7deb1d5.png)

Clique no sinal de <b>+</b> e em seguida clique em Projects

![image](https://user-images.githubusercontent.com/46925501/155432105-6fd3dfde-3242-4eb4-9a22-18b90b7464c2.png)

Selecione o projeto existente no Workspace - My First Project

![image](https://user-images.githubusercontent.com/46925501/155432118-5315eab4-6d67-4c92-98a8-1c614e56cf7d.png)

Selecione a guia Data Flow na lateral esquerda e em seguida clique em Create Data Flow.

![image](https://user-images.githubusercontent.com/46925501/155432135-e03b52a2-0cbd-4751-b424-b02d1a2037c1.png)

<b>Configurando o Data Flow</b>

Com os canvas do data flow aberto vamos fazer o desenho do fluxo de dados e configurar cada um dos operadores.
Na tela do Data Flow desing, no painel de Properties, dê um nome ao Data Flow e verifique se o projeto correto está selecionado.

![image](https://user-images.githubusercontent.com/46925501/155432175-eda23ed5-3ded-49cc-94b7-ee7b7493979d.png)

DICA: para facilitar a visualização você pode clicar nas setas na lateral superior direita para expandir e diminuir o tamanho do Painel properties:
![image](https://user-images.githubusercontent.com/46925501/155432193-c375620d-0d5c-4080-a599-a2da8fa3fb65.png)

<b>Configurando os Operadores</b>

Em seguida vamos começar a criação do Fluxo de Dados
Clique no Painel Operators e arraste um Operador de Source (Fonte) e um de Target (Destino)
![image](https://user-images.githubusercontent.com/46925501/155432273-a19c65ff-6ba7-4388-bf17-e0ca8ed926dd.png)

Clique no Operador Source que você arrastou até o Canvas do Data Flow, em seguida no Painel Properties dê um nome ao Operator (SOURCE_PERSONAGENS)
  
![image](https://user-images.githubusercontent.com/46925501/155432385-f5280bcc-db45-4706-bdbf-b00c60df4f7a.png)

Agora nós vamos configurar cada propriedade indicada no Painel Properties: Data Asset, Connection, Schema e Data Entity, conforme abaixo:

![image](https://user-images.githubusercontent.com/46925501/155432475-ac240cbb-9439-4b18-9267-39df0845f550.png)

<b>Agora arraste coloque outro Operador Source no Canvas, ele será configurado para ser a Source do arquivo que vem do function, conforme abaixo:</b>
![image](https://user-images.githubusercontent.com/46925501/155432585-a1c7eaac-e8f9-4758-96cd-b54f6641f99b.png)

### Configurando o Operador Target

Clique no Operador Target que você arrastou até o Canvas do Data Flow, em seguida no Painel Properties dê um nome ao Operator ‘TARGET_ADW’. Em Integration Strategy selecione a opção Insert:

![image](https://user-images.githubusercontent.com/46925501/155432705-599b4d60-cf35-4193-ba01-ee1b3c7d628b.png)

Agora nós vamos configurar cada propriedade indicada no Painel Properties: Data Asset, Connection, Schema, Data Entity e Staging Location. O processo é muito semelhante a configuração do Source Operator.
* Vamos Utilizar o Schema ADMIN para fins didáticos, o ideal é que você tenha outro usuário disponível no seu ADW (Autonomous Data Warehouse) que você possa usar. 
Faça a configuração com base no nome que você a cada item demonstrado. Lembre-se de dar um nome ao seu Operador Target e marcar a opção Create New Data Entity

![image](https://user-images.githubusercontent.com/46925501/155432770-fdb7ac7b-2634-4fc9-8375-3fa7267693d8.png)

Agora vamos selecionar a Staging Location. Clique em Select em frente a Staging Location e preencha as informações conforme a imagem abaixo:
  
![image](https://user-images.githubusercontent.com/46925501/155432804-1cbbf851-526b-4f49-8a66-4002ade74301.png)

### Configurando os Shaping Operators

Coloque no canvas um Operator Join e um Operator Filter
Após arrastar os Operadores conecte cada um dele conforme a Imagem Abaixo: 
  
![image](https://user-images.githubusercontent.com/46925501/155432915-ee017a01-7571-4682-90d6-0c1737ea78c3.png)

-> Para conectar os Operadores basta descansar o mouse sobre o operador até que uma bolinha apareça no lado direito do operador, após isso basta clicar na bolinha e arrastas a linha até o operador que você deseja fazer a conexão:
  
![image](https://user-images.githubusercontent.com/46925501/155432937-743f2d1d-3dc9-41bb-a9fc-02c2a740e641.png)

<b>Configurando o Operador Join</b>
Clique no Operador Join que você arrastou até o Canvas do Data Flow, em seguida no Painel Properties dê um nome ao Operator:
  
![image](https://user-images.githubusercontent.com/46925501/155433055-1e53e9d5-da6c-4a36-9127-0b96d8f7ca38.png)

Em seguinda, vamos selecionar o Join Type e criar uma condição, conforme abaixo:
  
![image](https://user-images.githubusercontent.com/46925501/155433126-0a75493c-6f57-4478-9693-5e0da673b903.png)

<b>Configurando o Operador Filter</b>

Clique no Operador Filter que você arrastou até o Canvas do Data Flow, em seguida no Painel Properties dê um nome ao Operator. Clique em Filter Condition e informe a condição conforme abaixo:

![image](https://user-images.githubusercontent.com/46925501/155433256-624b5a68-be3f-4598-aab7-482501481635.png)

Pronto! Todos os Operadores do Data Flow Designer estão configurados
Agora Clique em Save and Close 

### Criação e Execução da Integration Tasks
  
Nessa seção vamos criar e configurar uma Integration Task
Clique no sinal de + e selecione Application

![image](https://user-images.githubusercontent.com/46925501/155433320-daee7bca-13ed-4123-9d28-fb29204768a8.png)

Acesse a Default Application que estará disponível no seu Workspace
  
![image](https://user-images.githubusercontent.com/46925501/155433335-a089780f-e8f7-4cfc-bbf5-ced95b42d85a.png)

Toda Integration Task deverá ser publicada aqui nessa Application. Agora continue para a próxima sessão “Criando Integration Task”
  
<b>Criando Integration Task</b>

Clique no sinal de + e em seguida clique em Projects
  
![image](https://user-images.githubusercontent.com/46925501/155433383-babeeae7-4300-4a9f-a2bc-32c1b1c0d8c0.png)

Selecione o projeto existente no Workspace - My First Project

![image](https://user-images.githubusercontent.com/46925501/155433402-facda9a3-8063-43c0-a5b7-e600da9350e8.png)

Em seguida clique em Task na parte esquerda da tela. Clique em Create Task e escolha a Opção Integration

![image](https://user-images.githubusercontent.com/46925501/155433415-8ee61caf-c603-4498-8ef2-a344d3eb341c.png)

Dê um nome a Integration Task e verifique se o seu Projeto está selecionado, em seguida clique no botão Select para selecionar o Data Flow que será usado na Task

![image](https://user-images.githubusercontent.com/46925501/155433433-a9ba9716-fe13-4208-8f53-dac5abfac994.png)

Selecione o Data Flow que criamos na seção anterior e clique em Select
  
![image](https://user-images.githubusercontent.com/46925501/155433451-7cb0534a-3055-49c6-a98e-b251a634365c.png)

Aguarde a Validação e clique em Create and Close

![image](https://user-images.githubusercontent.com/46925501/155433469-ea17c92f-70c6-4163-a1db-9662c5c41638.png)

<b>Executando a Task Integration</b>
Clique no sinal de + e em seguida clique em Projects
  
![image](https://user-images.githubusercontent.com/46925501/155433493-74268f04-0aa1-4829-bca4-fa75ba617fc2.png)

Selecione o projeto existente no Workspace - My First Project
 
![image](https://user-images.githubusercontent.com/46925501/155433506-11bcd9bd-3bc8-49aa-a101-b6064e610bd2.png)

Clique na aba Tasks e localize a Integration Task que criamos na seção anterior. Clique no menu de ação no lado direito da integration task (representado por 3 pontinhos como indicado na imagem)

![image](https://user-images.githubusercontent.com/46925501/155433528-b7767650-8b6e-4c28-ab97-19cd45398410.png)

Clique em Publish to Application

![image](https://user-images.githubusercontent.com/46925501/155433538-2e727621-e96b-46f5-b351-4ef36cfffc91.png)

Selecione a Default Application e clique em Publish
  
![image](https://user-images.githubusercontent.com/46925501/155433550-bcb2e853-51b8-4b88-967e-54417295832e.png)

Agora clique no sinal de + e selecione Application
  
![image](https://user-images.githubusercontent.com/46925501/155433565-93a62506-9e10-45d5-b037-96ff9927f5f5.png)

Acesse a Default Application que estará disponível no seu Workspace
  
![image](https://user-images.githubusercontent.com/46925501/155433586-ab7ae1ce-ad9a-4817-9ff6-3f8b2668e302.png)

Ao acessar a Application você vai localizar a Integration Task que publicamos na seção anterior 
 
![image](https://user-images.githubusercontent.com/46925501/155433610-2ed87d93-435b-4492-aa7b-10b57c029314.png)

Clique no menu de ação no lado direito da integration task (representado por 3 pontinhos como indicado na imagem) e selecione a opção Run

![image](https://user-images.githubusercontent.com/46925501/155433625-bfd45547-35e3-4896-8391-83178df3d00e.png)
  
A execução da integration task vai começar e você será direcionado para a aba Runs (ainda dentro de Applications)
Você pode utilizar o botão Refresh para visualizar o progresso da integration task

![image](https://user-images.githubusercontent.com/46925501/155433642-e82cf5b1-b8e2-4cf5-abcf-a9a158244de9.png)

Após o Status aparecer como ‘Sucess’ a integration task estará concluída com sucesso! 
Os arquivos .CSV que estavam no Oracle Object Storage foram extraídos, transformados (Data Flow designer) e carregados no Oracle Autonomous Data Warehouse.

# Autonomous Data Warehouse

## Criando uma instância do Autonomous Data Warehouse

Clicar no Hambúrguer superior esquerdo, <i>Oracle Database</i> e <i>Autonomous Data Warehouse</i>
  
![image](https://user-images.githubusercontent.com/46925501/155531068-e823c84f-3210-46b5-8777-121221267337.png)

Verifique se o compartimento está correto e clique em <i>Create Autonomous Database</i>
  
![image](https://user-images.githubusercontent.com/46925501/155531442-d1aab77d-acd2-4d0a-8d2b-85beda0d63dd.png)

Informar as informações de <i>Display Name</i>, <i>Database Name</i>

![image](https://user-images.githubusercontent.com/46925501/155531754-eaa11f9e-abf7-4469-b88b-77de1be498ac.png)

Escolher a opção <i>Data Warehouse</i> em Workload Type e <i>Shared Infrastructure</i> em Deployment Type
  
![image](https://user-images.githubusercontent.com/46925501/155531853-ed62f919-91df-4f71-8c89-f5e74efc0ade.png)

Para fins de laboratório, vamos utilizar o Autonomous na versão free. Habilite a flag conforme abaixo:
  
![image](https://user-images.githubusercontent.com/46925501/155532160-00d419e2-bfc7-464f-adc3-899448ed1cd4.png)

Inserir o password para o usuário ADMIN e após clicar em <i>Create Autonomous Database</i>

![image](https://user-images.githubusercontent.com/46925501/155532347-1a68151d-bc96-4040-b794-a7674cbdd77b.png)

Aguardar o Provisionamento da instância

![image](https://user-images.githubusercontent.com/46925501/155532515-a38c5be1-068d-4914-a8cb-e72d7a3043af.png)


## Acessando a Instância do Autonomous Data Warehouse

Clique na instância que você criou no passo anterior:

![image](https://user-images.githubusercontent.com/46925501/155532791-4564ee1e-ddd1-46a6-9ec5-e2879a0fc32b.png)

Selecione a opção <i>Database Actions</i>

![image](https://user-images.githubusercontent.com/46925501/155532956-4c69d5f8-9162-4465-a43b-54a0b32db171.png)

Será Aberta uma console com diversas ações que você poderá executar no Autonomous:
  
![image](https://user-images.githubusercontent.com/46925501/155533098-59b93530-fbea-47d4-b517-17b7159d4b18.png)

Para fazer consultas SQL ou executar outras queries, você pode acessar a opção <i>SQL</i>
 
![image](https://user-images.githubusercontent.com/46925501/155533555-3db18700-0df8-4980-9f90-51591a0e64ac.png)

Irá aparecer Like SQL Developer para que você possa executar as suas funções.

![image](https://user-images.githubusercontent.com/46925501/155533857-2da752dc-9f50-40e3-8c6f-3926dc57c7bd.png)

## OCI Events
  
Pré Requisitos: Ter Compartimento Criado, VCN, Aplicar as Policies, Criação dos Functions, Autonomous Data Warehouse e OCI Data Integration.
  
Após seguir todos os passos anteriores, vamos criar o evento de integração com as funções criadas.
Para acessar o Event Service, seguir pelo menu de hamburguer, <i>Observability & Management</i> e em Events Services acesse <i>Rules</i>

![image](https://user-images.githubusercontent.com/46925501/155534943-a20745b6-c9b0-42ac-b0c9-ef755fce2ad9.png)

Clique em <i>Create Rule</i>

![image](https://user-images.githubusercontent.com/46925501/155535238-4fb97711-9404-4b2c-9352-0e50e97e0303.png)

Informe o <i>Display Name</i> e uma <i>Description</i> de identificação da Regra:
  
![image](https://user-images.githubusercontent.com/46925501/155535730-76d4b980-90a7-47f0-a00b-a34f85410ece.png)

Agora, vamos começar a brincadeira, pois vamos começar a preencher as condições da Regra.
  
Primeiramente, vamos informar o tipo de evento. No nosso caso toda vez que um object for criado em um bucket (No Bucket especificado), será gerado um evento.

![image](https://user-images.githubusercontent.com/46925501/155536005-cfa8ae80-74d4-497d-a0d2-8f66540db400.png)

Agora, vamos informar os atributos desse evento. Os atributos que vamos preencher são <i>compartmentId</i>, <i>bucketName</i> e <i>namespace</i>

![image](https://user-images.githubusercontent.com/46925501/155536541-1223434a-ae3d-42a9-9983-5a0cf0cf3d25.png)
Obs. Para saber como coletar essas informações, [clique aqui](a)
  
Por fim e não menos importante, vamos informar a ação que esse evento irá ativar, no nosso caso vamos ativar a função criada para fazer a chamada do OCI Data Integration.

![image](https://user-images.githubusercontent.com/46925501/155536928-7b469269-29a4-4d1c-90f8-d41638f1ea1f.png)

Após preencher as informações como a imagem anterior, clique em <i>Create Rule</i>
Criação da Regra criado com sucesso!
  
## Tópico Bônus - Execução do Fluxo

Após criação de toda a arquitura apresentada durante esse documento, vamos seguir com a execução do nosso fluxo.
  
Para isso, primeiramente vamos acessar o <i>Cloud Shell</i>

![image](https://user-images.githubusercontent.com/46925501/155538829-b7c5ab7d-fa1c-49ed-aee8-9ff5d3c032a9.png)

Para invocarmos nosso function, vamos utilizar o seguinte comando:
> fn invoke App_InLab fn_getapi
  
Ao invocarmos o nosso function, será retornada uma mensagem de sucesso, conforme abaixo:
  
![image](https://user-images.githubusercontent.com/46925501/155539864-f98c993d-ac40-4768-9e6c-71e2eab14edd.png)

Na imagem acima, temos o nome do arquivo que foi gerado <i>stranger_api20220224-140757.csv</i>. Podemos consultar ele no bucket bucket-raw-data:
  
![image](https://user-images.githubusercontent.com/46925501/155540119-5d9d93d2-08cf-43a1-b24d-dde4233d1d49.png)

Para acompanharmos a evolução do nosso fluxo, podemos também acessar a Tarefa que foi criada no OCI Data Integration, seguindo o fluxo abaixo:

No workpace do OCI Data Integration, acesse <i>Applications</i>

![image](https://user-images.githubusercontent.com/46925501/155540537-dd747f1d-e10f-44d1-9f06-8e5aaa8bc56b.png)

Clique na sua aplicação:

![image](https://user-images.githubusercontent.com/46925501/155540826-bc04587d-c117-4077-a72b-8d501c49a184.png)

Em <i>Runs</i>, conseguimos acompanhar e obter informações de todas as execuções:
  
![image](https://user-images.githubusercontent.com/46925501/155541153-419f11e4-0834-4a09-8dc1-6a382c6cb5dc.png)

Por fim, você pode acessar os dados inseridos no Autonomous Data Warehouse conforme apresentado no tópico do [Autonomous](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#autonomous-data-warehouse).

## fn_execute_task - Coletando parâmetros
  
Para esse function, será necessário coletar alguns parâmetros para adicionar ao código.
Os parâmetros são:
  * wsid
  * application
  * task
  * connection
  * bucketName
  * namespace
  
<b>wsid</b>
Para Coletar o wsid, vamos acessar nosso workspace do OCI Data Integration e clique nos três pontinhos:

![image](https://user-images.githubusercontent.com/46925501/155544410-ed0d996e-bc03-4978-9237-672c6c67f4cf.png)

Nos três pontinhos, escolha a opção <i>Copy OCID</i>

![image](https://user-images.githubusercontent.com/46925501/155544756-4d972b4d-7b01-4c83-acc7-e5790612c516.png)

Adicione o conteúdo no código do function.
  
<b>application</b>
Para coletar o application, vamos acessar nosso workspace do OCI Data Integration:

![image](https://user-images.githubusercontent.com/46925501/155545057-46ce2d22-e3df-4cf5-b0bf-4dacb258d442.png)

Clique em <i>applications</i>
  
![image](https://user-images.githubusercontent.com/46925501/155545234-61b118a5-05c5-4cd7-a2e8-39b50b7b8924.png)

Clique nos três pontinhos:

![image](https://user-images.githubusercontent.com/46925501/155545393-04d368f6-94e4-4793-9f49-b4e9d9e78cbe.png)

Nos três pontinhos, escolha a opção <i>Copy Application Key</i>

![image](https://user-images.githubusercontent.com/46925501/155545563-a103227f-9134-4de0-a704-2d032a357243.png)

Adicione o conteúdo no código do function.

<b>Task</b>
Para coletar a task, vamos acessar o nosso application da nossa workspace no OCI Data Integration:

![image](https://user-images.githubusercontent.com/46925501/155546554-af82b925-5579-431a-b0f0-e7589edcfb3b.png)

Em <i>Tasks</i>, clique nos três pontinhos da tarefa:
  
![image](https://user-images.githubusercontent.com/46925501/155546860-d79dd8d2-e82d-46b4-ba89-25ff5bc89c53.png)

Nos três pontinhos, escolha a opção <i>Copy Task Key</i>:
![image](https://user-images.githubusercontent.com/46925501/155547058-9b150389-3e3f-45b5-8764-cf2161a94e04.png)

Adicione o conteúdo no código do function.
  
<b>Connection, Namespace e BucketName</b>

Para os outros três atributos, vamos acessar o bucket que criamos para armazenar os dados. Acessando o bucket, vamos acessar as demais informações necessárias:
 
![image](https://user-images.githubusercontent.com/46925501/155547971-e8fcfb7b-f04b-4d2d-a6e7-886154673ac6.png)

Adicione o conteúdo no código do function.
  
## Events Services - Coletando parâmetros
Para esse Events Services, será necessário coletar alguns parâmetros para adicionar a regra.
Os parâmetros são:
* CompartmentID
* namespace
  
<b>CompartmentID</b>
  
Para coletar o CompartmentID, vamos ao menu de hamburguer, <i>Identity & Security</i> e <i>Compartments</i>

![image](https://user-images.githubusercontent.com/46925501/155551107-a0cd066e-efcd-4952-ae1b-0ef61f4542b3.png)

Localize seu compartimento, clique nele e colete o OCID conforme abaixo:
  
![image](https://user-images.githubusercontent.com/46925501/155551354-b4044177-734b-4ef4-8df0-a7c5af22f9a9.png)

Preencher a informação no campo necessário.
  
<b>Namespace</b>
  
Para coletar o namespace, [clique aqui](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos#fn_execute_task---coletando-par%C3%A2metros).
Preencher a informação no campo necessário.
