from classifier import classificar_mensagem
from collections import Counter


class TestRunner:

    def __init__(self, mensagem, temperaturas, repeticoes=10):
        self.mensagem = mensagem
        self.temperaturas = temperaturas
        self.repeticoes = repeticoes

    def executar(self):
        print("\nINÍCIO DOS TESTES\n")

        for temp in self.temperaturas:
            print(f"\n Temperatura: {temp} ")

            resultados = []

            for i in range(self.repeticoes):
                resultado = classificar_mensagem(
                    self.mensagem,
                    temperature=temp
                )

                categoria = resultado["categoria"]
                resultados.append(categoria)

                print(f"Execução {i+1}: {resultado}")

            distribuicao = Counter(resultados)

            print("\nDistribuição final:")
            print(distribuicao)

        print("\n FIM DOS TESTES \n")