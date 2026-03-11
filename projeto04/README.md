# 🤖 Assistente Inteligente com Memória – Projeto 04

## 📖 Descrição

Este projeto implementa um **chatbot em Python** capaz de interagir com o usuário utilizando um **modelo de linguagem (LLM)**.
O sistema mantém **memória da conversa**, executa **funções específicas em Python** e salva o histórico em **arquivo JSON**, permitindo que o contexto seja preservado entre diferentes execuções do programa.

O objetivo do projeto é demonstrar, na prática, como integrar **modelos de IA, lógica em Python e armazenamento de dados** para criar um assistente simples e funcional.

---

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

* Python
* Groq API (modelo de linguagem)
* python-dotenv
* JSON (armazenamento do histórico)

---

## ⚙️ Instalação e Execução

### 1. Instalar as dependências

No terminal, dentro da pasta do projeto:

```bash
python -m pip install groq python-dotenv
```

---

### 2. Configurar a chave da API

Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave da Groq:

```
GROQ_API_KEY=sua_chave_aqui
```

---

### 3. Executar o chatbot

No terminal:

```bash
python main.py
```

Após executar o comando, o chatbot será iniciado no terminal.

---

## 🧩 Funcionalidades

### 🧠 Memória de Conversa

O assistente armazena as mensagens trocadas com o usuário para manter o **contexto da conversa**.

Também foi implementado o comando:

```
/limpar
```

Esse comando remove todo o histórico da conversa.

---

### 🎭 Personalidade do Assistente

Foi definida uma mensagem de sistema (*system prompt*) que faz o assistente responder de forma:

* educada
* objetiva
* focada em ajudar estudantes

---

### 📉 Controle de Histórico

Para evitar que o histórico fique muito grande, o sistema mantém **apenas as últimas 10 mensagens**.

Quando o limite é ultrapassado, as mensagens mais antigas são removidas automaticamente.

---

### 🧩 Integração com Funções Python

Algumas tarefas são executadas diretamente em Python, garantindo maior precisão.

Exemplos de funções implementadas:

* 📅 Mostrar a **data atual**
* 🔐 **Gerar senha aleatória**

---

### 💾 Persistência de Dados

O histórico das conversas é salvo automaticamente no arquivo:

```
memoria.json
```

Quando o programa é iniciado novamente, o histórico é carregado e a conversa pode continuar.

---

## 💡 Reflexões

### 📚 Problemas de um histórico muito grande

Se o histórico da conversa crescer demais, alguns problemas podem ocorrer:

* respostas mais lentas
* aumento do custo da API
* limite de contexto do modelo pode ser atingido
* mensagens antigas podem deixar de ser consideradas

Por isso é importante limitar o tamanho da memória.

---

### 🧠 Por que usar Python para algumas tarefas?

Algumas tarefas são mais adequadas para serem executadas diretamente em Python, principalmente aquelas que exigem **precisão**, como cálculos ou geração de valores.

Enquanto o modelo de linguagem pode cometer erros, o Python executa essas operações de forma **exata e rápida**.

---

### ⚠️ Riscos de deixar o LLM decidir quando usar funções

Permitir que o modelo decida sozinho quando utilizar funções pode gerar alguns problemas:

* escolher a função errada
* executar funções desnecessariamente
* gerar comportamentos inesperados

Por isso, muitos sistemas utilizam **regras definidas para controlar essas chamadas**.

---

## 🚧 Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram encontradas:

* configuração da API do modelo de linguagem
* controle do histórico da conversa
* salvar e carregar dados utilizando JSON
* ajustes na integração com a plataforma Groq

Esses desafios ajudaram a compreender melhor o funcionamento de **LLMs em aplicações Python**.

---

## ✅ Conclusão

Este projeto permitiu aprender na prática como criar um **assistente inteligente com memória**, integrar **funções em Python** e trabalhar com **modelos de linguagem** em uma aplicação real.

Além disso, possibilitou entender melhor conceitos importantes como:

* gerenciamento de contexto
* persistência de dados
* integração entre IA e lógica de programação
