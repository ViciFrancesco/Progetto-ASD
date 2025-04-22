import time
import numpy as np
from itertools import combinations

class BruteForceLCS:
    """
    Classe per calcolare la Longest Common Subsequence (LCS) tra due stringhe 
    utilizzando l'approccio brute-force, e misurare il tempo medio di esecuzione
    su più iterazioni.
    """

    def __init__(self, iterations, maxSize):
        """
        Inizializza un oggetto BruteForceLCS.

        Parametri:
        iterations (int): Numero di iterazioni da eseguire per ogni test.
        maxSize (int): Dimensione massima consentita per le stringhe da testare.
        """
        self.iterations = iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)

    def brute_force_LCS(self, X, Y):
        """
        Calcola la LCS tra due stringhe generando tutte le possibili sottosequenze 
        e confrontando quelle comuni.

        Parametri:
        X (str): Prima stringa.
        Y (str): Seconda stringa.

        Ritorna:
        int: Lunghezza della LCS tra X e Y.
        """
        subseq_X = self.subsequences(X)
        subseq_Y = self.subsequences(Y)
        common = subseq_X.intersection(subseq_Y)
        return max(map(len, common)) if common else 0

    def subsequences(self, s):
        """
        Genera tutte le sottosequenze non vuote di una stringa.

        Parametri:
        s (str): Stringa da cui generare le sottosequenze.

        Ritorna:
        set: Insieme delle sottosequenze generate.
        """
        subseqs = set()
        for i in range(1, len(s) + 1):
            for combo in combinations(s, i):
                subseqs.add("".join(combo))
        return subseqs

    def execute(self, stringsList, testSize):
        """
        Esegue il calcolo della LCS su una lista di coppie di stringhe e misura
        il tempo medio di esecuzione.

        Parametri:
        stringsList (list of str): Lista contenente le stringhe da confrontare.
                                   Ogni due stringhe consecutive formano una coppia da testare.
        testSize (int): Dimensione della stringa da testare (usata come indice per salvare i risultati).

        Ritorna:
        float: Tempo medio di esecuzione sulle iterazioni, oppure NaN se testSize supera maxSizeAllowed.
        """
        if testSize <= self.maxSizeAllowed:
            resultsAverage = 0
            for iteration in range(0, self.iterations, 1):
                X = stringsList[(2 * iteration)]
                Y = stringsList[(2 * iteration) + 1]
                start = time.time()
                self.brute_force_LCS(X, Y)
                end = time.time()
                self.results[iteration][testSize - 1] = end - start
                resultsAverage += end - start
            return resultsAverage / self.iterations
        else:
            return np.nan

    def print_results(self):
        """
        Stampa la matrice dei risultati contenente i tempi di esecuzione per ogni test.
        """
        print(self.results)
