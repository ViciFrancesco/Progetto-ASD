from itertools import combinations

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