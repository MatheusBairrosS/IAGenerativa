import json
import re

CATEGORIAS_PERMITIDAS = ["Suporte", "Vendas", "Financeiro", "Geral"]


def extrair_json(texto):
    match = re.search(r'\{.*\}', texto, re.DOTALL)
    if not match:
        raise ValueError("Nenhum JSON encontrado")
    return match.group()


def parse_json(texto):
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        raise ValueError("JSON inválido")


def validar_categoria(dados):
    if dados.get("categoria") not in CATEGORIAS_PERMITIDAS:
        raise ValueError("Categoria inválida")
    return True


def fallback():
    return {"categoria": "Geral"}


def validar_resposta(resposta_llm):
    try:
        json_texto = extrair_json(resposta_llm)
        dados = parse_json(json_texto)
        validar_categoria(dados)
        return dados
    except Exception as e:
        print("Erro de validação:", e)
        return fallback()
