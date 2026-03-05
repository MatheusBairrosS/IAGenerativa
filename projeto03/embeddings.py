import numpy as np
from sentence_transformers import SentenceTransformer
import os

# Modelo leve e eficiente
model = SentenceTransformer("all-MiniLM-L6-v2")


def gerar_embedding(texto):
    return model.encode(texto).tolist()


def carregar_conhecimento(caminho="conhecimento/conhecimento.txt"):

    caminho_base = os.path.dirname(__file__)
    caminho_completo = os.path.join(caminho_base, caminho)

    with open(caminho_completo, "r", encoding="utf-8") as f:
        texto = f.read()

    partes = texto.split("\n\n")

    base = []

    for parte in partes:
        embedding = gerar_embedding(parte)
        base.append({
            "texto": parte,
            "embedding": embedding
        })

    return base


def similaridade(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def buscar_contexto(pergunta, base, top_k=2):
    emb_pergunta = gerar_embedding(pergunta)

    resultados = []

    for item in base:
        score = similaridade(emb_pergunta, item["embedding"])
        resultados.append((score, item["texto"]))

    resultados.sort(reverse=True)

    return [texto for _, texto in resultados[:top_k]]