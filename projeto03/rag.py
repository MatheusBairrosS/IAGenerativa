from embeddings import buscar_contexto

def gerar_prompt_rag(pergunta, base):

    contextos = buscar_contexto(pergunta, base)

    contexto_formatado = "\n\n".join(contextos)

    prompt = f"""
    Use o contexto abaixo para responder a pergunta.

    CONTEXTO:
    {contexto_formatado}

    PERGUNTA:
    {pergunta}
    """

    return prompt