import json
import re
from llm_client import gerar_resposta
from validator import validar_resposta

CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]

def classificar_mensagem(mensagem, temperature=0.2):

    prompt = f"""
    Classifique a mensagem abaixo em uma das seguintes categorias: {', '.join(CATEGORIAS)}.

    Responda APENAS com um JSON válido no formato:
    {{
        "categoria": "nome_categoria"
    }}

    Mensagem: "{mensagem}"
    """

    resposta = gerar_resposta(prompt, temperature)

    if not resposta:
        return fallback()

    try:
        # Extrai JSON mesmo que venha texto junto
        match = re.search(r'\{.*\}', resposta, re.DOTALL)

        if not match:
            raise ValueError("Nenhum JSON encontrado")

        json_text = match.group()
        dados = json.loads(json_text)

        if dados["categoria"] not in CATEGORIAS:
            raise ValueError("Categoria inválida")

        return dados

    except Exception as e:
        print("Erro de validação:", e)
        return fallback()


def fallback():
    return {"categoria": "Geral"}