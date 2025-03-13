# Versione con memoization
def memoization_LCS(X, Y, m, n, memo):
    # Caso base: se una delle due stringhe è vuota, la LCS è 0
    if m == 0 or n == 0:
        return 0

    # Se il valore è già stato calcolato, restituiscilo
    if (m, n) in memo:
        return memo[(m, n)]

    # Se gli ultimi caratteri coincidono, aggiungiamo 1 alla LCS
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + memoization_LCS(X, Y, m - 1, n - 1, memo)
    else:
        # Altrimenti, prendiamo il massimo tra le due possibilità
        memo[(m, n)] = max(
            memoization_LCS(X, Y, m, n - 1, memo),
            memoization_LCS(X, Y, m - 1, n, memo)
        )

    return memo[(m, n)]