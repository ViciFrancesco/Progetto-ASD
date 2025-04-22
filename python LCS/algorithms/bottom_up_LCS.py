import time
import numpy as np

class BottomUpLCS:
    """
    Classe per calcolare la Longest Common Subsequence (LCS) tra due stringhe 
    utilizzando l'approccio bottom-up (programmazione dinamica), e misurare il 
    tempo medio di esecuzione su più iterazioni.
    """

    def __init__(self, iterations, maxSize):
        """
        Inizializza un oggetto BottomUpLCS.

        Parametri:
        iterations (int): Numero di iterazioni da eseguire per ogni test.
        maxSize (int): Dimensione massima consentita per le stringhe da testare.
        """
        self.iterations = iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)

    def bottom_up_LCS(self, X, Y):
        """
        Calcola la LCS tra due stringhe utilizzando l'approccio bottom-up
        (tabulazione) della programmazione dinamica.

        Parametri:
        X (str): Prima stringa.
        Y (str): Seconda stringa.

        Ritorna:
        int: Lunghezza della LCS tra X e Y.
        """
        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

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
                self.bottom_up_LCS(X, Y)
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