# OCI InLab - Pipeline de Dados Aplicado a Eventos

* [OCI Object Storage](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/tree/master#oci-object-storage)
* OCI Data Integration
* OCI Functions
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

### Step 1
<i>Pré Requisitos: Ter Compartimento Criado, VCN, Aplicar as [Policies](https://github.com/heloisaescobar/InLab-Pipeline-Dados-Aplicado-Eventos/blob/master/scripts_apoio/policies_anexo.txt)</i>.

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
