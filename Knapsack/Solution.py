def Mochila(capacidade, pesos, valores):
    n = len(pesos)
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(
                    valores[i - 1] + dp[i - 1][w - pesos[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

pesos = [6, 3, 4, 2, 3]
valores = [30, 14, 16, 9, 102]
capacidade = 10

resultado = Mochila(capacidade, pesos, valores)
print(f"Valor máximo que pode ser carregado: {resultado}")
