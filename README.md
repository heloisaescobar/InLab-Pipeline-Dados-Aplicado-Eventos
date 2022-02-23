# OCI InLab - Pipeline de Dados Aplicado a Eventos

* [OCI Object Storage](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/tree/master#oci-object-storage)
* [OCI Functions](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/README.md#oci-functions)
* OCI Data Integration
* Autonomous Data Warehouse
* OCI Events

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

Para o arquivo [func.py](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/functions/fn_execute_task/func.py), será necessário obter algumas informações do OCI Data Integration e do Object Storage. Para coletar essas informações, [clique aqui](a).

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

Pré-requisito: Ter um Autonomous Data Warehouse provisionado, ter um usuário com privilégios DBMS_CLOUD e DWROLE. Para provisionar o Autonomous [clique aqui](a)

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
