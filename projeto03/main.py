from embeddings import carregar_conhecimento
from rag import gerar_prompt_rag
from llm_client import gerar_resposta
from security import detectar_prompt_injection, resposta_bloqueada

base = carregar_conhecimento()

def responder(pergunta):

    if detectar_prompt_injection(pergunta):
        return resposta_bloqueada()

    prompt = gerar_prompt_rag(pergunta, base)

    resposta = gerar_resposta(prompt)

    return resposta


if __name__ == "__main__":

    pergunta = input("Pergunta: ")
    print(responder(pergunta))