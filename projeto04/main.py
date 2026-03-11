from groq import Groq
from dotenv import load_dotenv
from tools import data_atual
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

ARQUIVO_MEMORIA = "memoria.json"
LIMITE_MEMORIA = 10


# Persona do assistente
persona = {
    "role": "system",
    "content": "Você é um assistente educado, objetivo e que ajuda estudantes a aprender programação."
}


# Carregar histórico do arquivo
def carregar_historico():
    try:
        with open(ARQUIVO_MEMORIA, "r") as f:
            return json.load(f)
    except:
        return [persona]


# Salvar histórico no arquivo
def salvar_arquivo():
    with open(ARQUIVO_MEMORIA, "w") as f:
        json.dump(historico_mensagens, f, indent=4)


# Histórico de mensagens
historico_mensagens = carregar_historico()


def salvar_historico(mensagem):
    historico_mensagens.append(mensagem)

    # Limite de memória
    if len(historico_mensagens) > LIMITE_MEMORIA:
        historico_mensagens.pop(1)

    salvar_arquivo()


def chat(pergunta):

    salvar_historico({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=historico_mensagens
    )

    resposta_conteudo = resposta.choices[0].message.content

    salvar_historico({
        "role": "assistant",
        "content": resposta_conteudo
    })

    return resposta_conteudo


while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break

    if pergunta == "/limpar":
        historico_mensagens.clear()
        historico_mensagens.append(persona)
        salvar_arquivo()
        print("Assistente: Memória da conversa apagada.")
        continue

    if "data" in pergunta.lower():
        resposta = "Hoje é " + str(data_atual())
        salvar_historico({"role": "user", "content": pergunta})
        salvar_historico({"role": "assistant", "content": resposta})
        print("Assistente:", resposta)
        continue

    # 🔹 FUNÇÃO PYTHON (GERAR SENHA)
    if "senha" in pergunta.lower():
        from tools import gerar_senha
        senha = gerar_senha()
        resposta = f"Sua senha gerada é: {senha}"
        salvar_historico({"role": "user", "content": pergunta})
        salvar_historico({"role": "assistant", "content": resposta})
        print("Assistente:", resposta)
        continue

    resposta = chat(pergunta)
    print("Assistente:", resposta)