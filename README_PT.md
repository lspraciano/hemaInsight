# Hemato Insight

Este projeto tem dois objetivos, que são demonstrar a possibilidade de
aplicação de inteligência artificial na saúde e demonstra como podemos usar
um modelo YOLO como ferramenta para um modelo de LLM. Por linguagem natural e através
do terminal o usuário poderá manter uma conversa com o agente. Este agente possui
3 ferramentas, uma para realizar detecções, onde usamos um
modelo YOLOv10 treinado para detectar leucócitos, outra para listar as imagens
em uma determinada pasta, e a última que permite exibir imagens na tela para
usuário.

![compiled_graph.png](compiled_graph.png)

## 🗂️ Índice

- [☑️ Status do Projeto](#-status-do-projeto)
- [☄️ Versão Atual](#-versão-atual)
- [📁️ Estrutura do Projeto](#-estrutura-do-projeto)
    - [📂database](#database)
    - [📂images](#images)
    - [📂machine_learning](#machine_learning)
- [📋 Arquivo main.py](#-arquivo-mainpy)
- [🌠 Clonando Projeto](#-clonando-projeto)
- [✈️ Instalação](#-instalação)
- [🔧 Configurando](#-configurando)
    - [Criando ".env"](#criando-env)
- [🚀 Executando Aplicação](#-executando-aplicação)
- [🔭 Exemplo de Uso](#-exemplo-de-uso)
- [⚠️ Notas](#-notas)

## ☑️ Status do Projeto

- Em Desenvolvimento

### ☄️ Versão Atual

- 0.1.0

## 📁️ Estrutura do Projeto

### 📂database

Pasta destinada a receber os arquivos de conexão com banco
de dados sqlite, que será usado para persistência da memória.

### 📂images

Esta pasta é destinada a receber as imagens de entrada e saída
deste projeto. Nela podemos encontrar duas outras que são:

1. detections
2. originals

A pasta detections é destinada a receber as predições realizadas
pelo modelo YOLO, enquanto a pasta originals é destinada a receber
as imagens originais pela qual o agente irá usar para realizar
suas inferências.

### 📂machine_learning

Nesta pasta encontramos o core da aplicação. Ela se divide em duas
outras, que são:

1. cnn
2. llm

Na pasta cnn encontramos o código voltado para dar suporte as
funcionalidades que envolvem detecção em imagens. Nela você
vai encontrar, por exemplo, o modelo treinado para detecção
de leucócitos, que vai estar localizado dentro de cnn_models.
Já na pasta llm, vamos encontrar toda estrutura do graph. Separamos
o graph em seus principais componentes, como, por exemplo: Edges, Nodes,
etc.

### 📋 Arquivo main.py

Este é o arquivo principal e contém as seguintes funcionalidades:

- **`main()`**:
    - Um loop que captura a entrada do usuário.
    - Processa as mensagens usando o `compiled_graph`.
    - Exibe a resposta gerada no console.

## 🌠 Clonando Projeto

### Clonando Repositório Principal

Para clonar o projeto você pode seguir o comando abaixo.

```bash
git clone https://github.com/lspraciano/hemaInsight.git
```

## ✈️ Instalação

Com projeto clonado e dentro da raiz, agora você pode instalar
as dependências.

### Instalando

```bash
poetry install
poetry shell
```

## 🔧 Configurando

Antes de rodarmos o projeto, vamos precisar configurá-lo. Para
isso devemos criar um arquivo '.env' dentro da raiz do projeto.

### Criando ".env"

No Windows:

```bash
echo. > .env
```

No Linux:

```bash
touch .env
```

Com este arquivo criado você deve informar sua chave da OPENAI

```
OPENAI_API_KEY=...
```

## 🚀 Executando Aplicação

Para executar a aplicação podemos usar o comando abaixo

```bash
python main.py
```

### 🔭 Exemplo de Uso

```
- User: Olá
- Agente: Olá! Como posso ajudar você hoje?

- User: Quais células foram identificadas?
- Agente: Para identificar as células, preciso acessar as imagens onde
          elas estão localizadas. Por favor, forneça o caminho da pasta que 
          contém as imagens para que eu possa analisá-las.

- User: Ocaminho onde as imagens estão é ./images/originals
- Agente: Aqui estão as células identificadas nas imagens fornecidas:

1. **Imagem 1**:
   - Linfócito
   - Linfócito

...

```

### ⚠️ Notas

- O caminho padrão onde você deve colocar as imagens é `./images/originals`
- O agente pode fornecer informações adicionais, como áreas das células,
  tipos e sugestões de ações para células que necessitam de revisão e até
  abrir as imagens na sua tela