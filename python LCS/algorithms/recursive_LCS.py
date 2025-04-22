import time
import numpy as np


class RecursiveLCS:
    """
    Classe per calcolare la Longest Common Subsequence (LCS) tra due stringhe 
    utilizzando l'algoritmo ricorsivo, e misurare il tempo medio di esecuzione
    su più iterazioni.
    """

    def __init__(self, iterations, maxSize):
        """
        Inizializza un oggetto RecursiveLCS.

        Parametri:
        iterations (int): Numero di iterazioni da eseguire per ogni test.
        maxSize (int): Dimensione massima consentita per le stringhe da testare.
        """
        self.iterations = iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)

    def recursive_LCS(self, X, Y, m, n):
        """
        Calcola la LCS tra due stringhe utilizzando un approccio ricorsivo.

        Parametri:
        X (str): Prima stringa.
        Y (str): Seconda stringa.
        m (int): Lunghezza della stringa X.
        n (int): Lunghezza della stringa Y.

        Ritorna:
        int: Lunghezza della LCS tra X e Y.
        """
        if m == 0 or n == 0:
            return 0
        elif X[m - 1] == Y[n - 1]:
            return 1 + self.recursive_LCS(X, Y, m - 1, n - 1)
        else:
            return max(self.recursive_LCS(X, Y, m, n - 1), self.recursive_LCS(X, Y, m - 1, n))

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
                self.recursive_LCS(X, Y, len(X), len(Y))
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
























    