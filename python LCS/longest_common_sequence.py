from itertools import combinations

# Versione ricorsiva senza ottimizzazione
def recursive_LCS(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + recursive_LCS(X, Y, m - 1, n - 1)
    else:
        return max(recursive_LCS(X, Y, m, n - 1), recursive_LCS(X, Y, m - 1, n))



# Versione forza bruta (controlla tutte le sottosequenze)
def subsequences(s):
    subseqs = set()
    for i in range(1, len(s) + 1):
        for combo in combinations(s, i):
            subseqs.add("".join(combo))
    return subseqs

def brute_force_LCS(X, Y):
    subseq_X = subsequences(X)
    subseq_Y = subsequences(Y)
    common = subseq_X.intersection(subseq_Y)
    return max(map(len, common)) if common else 0



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



# Versione bottom-up
def bottom_up_LCS(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]