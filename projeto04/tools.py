from datetime import datetime
import random
import string


def data_atual():
    return datetime.now().strftime("%d/%m/%Y")


def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha