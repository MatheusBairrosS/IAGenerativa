from test_runner import TestRunner

mensagem_teste = "Quero cancelar meu plano imediatamente"

temperaturas = [0.0, 0.5, 1.0]

teste = TestRunner(
    mensagem=mensagem_teste,
    temperaturas=temperaturas,
    repeticoes=10
)

teste.executar()