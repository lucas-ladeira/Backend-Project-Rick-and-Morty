# Projeto Full-Stack: Rick & Morty

Projeto desenvolvido sob a mentoria da [Eitree Academy](https://www.eitree.dev/academy/) com a finalidade de aprendizado e prática da programação Full-Stack.

## Introdução

O desenvolvimento do projeto é dividido em três etapas:
- <u>Aquisição de dados:</u> Extração de dados de documento JSON com psycopg2;
- <u>Backend:</u> Comunicação entre o frontend e o banco de dados utilizando Flask e SQLAlchemy;
- <u>Frontend:</u> Interface gráfica e requisições ao backend utilizando Vite+React.js.

## Pré-Requisitos
Para a utilização correta deste projeto é necessária a instalação de alguns pacotes.

### A. Aquisição de dados
Pacotes Python utilizados:

```
pip install psycopg2
pip install sqlalchemy
```

### B. Backend
Primeiro de tudo é necessário ter instalado o programa [Python](https://www.python.org/downloads/).

Para instalar os pacotes necessários pode-se executar os comandos abaixo:
```
pip install flask
pip install flask-cors
```

Ou ainda, é possível instalar os pacotes como o comando abaixo:
```
pip install -r requirements.txt
```

### C. Frontend
Para poder executar o frontend deste projeto é necessário ter instalado o programa [Node.js](https://nodejs.org/en/download/current).

Além disso, é necessário instalar o pacote abaixo:
```
npm install axios
```

## 1. Aquisição de dados
Script em linguagem Python desenvolvido com a lib psycopg2 (lib utilizada para extrair os dados de um documento JSON e com esses dados popular o banco de dados).

## 2. Backend
O backend recebe as requisições do frontend e faz a comunicação com o banco de dados para obter as informações requeridas.

As requisições podem chegar de três formas:
- string name: termo a ser pesquisa na base de dados na coluna name;
- int page: termo que representa página solicitada;
- vazia: por padrão, caso não seja fornecida informação serão solicitados os dados de 1 à 20 que compõe a primeira página (ou seja, page=1).

Para lidar com as requisições do frontend são utilizadas duas rotas:
- get_characters: recebe uma string que é a pesquisa realizada pelo usuário na interface gráfica feita com React.js. Utilizando essa string, pesquisa no banco de dados por dados que contenham essa string na coluna "name". Além disso, utiliza um atributo chamado "index", que é um número inteiro positivo referente ao número da página desejada (por exemplo, index=1 retorna os itens 1 a 20 dos resultados da pesquisa; index=2 retorna os itens de 21 a 40; e assim por diante). Por padrão, caso não seja informado index, subentendesse que index=1. E caso não haja a quantidade máxima na página para retornar, retorna apenas os disponíveis (por exemplo, index=1 possui apenas 4 itens, logo, retorna apenas 21, 22, 23, 24).
- get_by_id: retorna um item da lista selecionado pelo usuário. Possui apenas um atributo, este atributo se chama "id" e é um número inteiro positivo.

## 3. Frontend
O frontend do projeto é desenvolvido em React.js e possui quatro estado de exibição:
- Home: onde o usuário pode digitar sua pesquisa em uma caixa de texto, e ao clicar no botão “Search” é redirecionado para a próxima página.
- Loading: onde o usuário pode digitar sua pesquisa em uma caixa de texto, e ao clicar no botão “Search” é redirecionado para a próxima página.
- Search: são exibidos os resultados relacionados à pesquisa feita, sendo que os resultados são mostrados em uma lista de paginação e que cada página desta lista irá exibir no máximo 20 itens de resultados. O usuário poderá navegar para qualquer página da lista de paginação através de um navegador no rodapé da tela. Caso o usuário clique em algum item da pesquisa, ele é redirecionado para a próxima página.
- View: são exibidas as informações do resultado de busca selecionado na tela anterior. Caso o usuário clique no botão “Close”, ele é redirecionado novamente para o estado anterior (Search).
