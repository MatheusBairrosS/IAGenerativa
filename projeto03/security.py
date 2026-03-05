PALAVRAS_BLOQUEADAS = [
    "system prompt",
    "ignore previous instructions",
    "me diga sua instrução",
    "qual sua configuração interna"
]

def detectar_prompt_injection(pergunta):
    pergunta_lower = pergunta.lower()

    for palavra in PALAVRAS_BLOQUEADAS:
        if palavra in pergunta_lower:
            return True

    return False


def resposta_bloqueada():
    return {
        "erro": "Tentativa de prompt injection detectada.",
        "seguranca": True
    }