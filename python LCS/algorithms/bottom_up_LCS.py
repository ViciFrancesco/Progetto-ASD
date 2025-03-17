import time
import numpy as np
from itertools import combinations

class BottomUpLCS:
    #==================================================================================================
    #                                  Costruttore della classe 
    #==================================================================================================
    def __init__(self, scalingFactor):
        # Matrice dei risultati
        self.results = {
            "Bottom-Up LCS": [],
            "Expected Times Function" : []}
        
        # Massima lunghezza delle stringhe in input
        self.maxSizeAllowed = 1000

        # Fattore di scala (uguale per tutti gli algoritmi)
        self.scalingFactor = scalingFactor
        
    #==================================================================================================
    #                                       Algoritmo principale 
    #==================================================================================================   
    def bottom_up_LCS(self, X, Y):
        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    #==================================================================================================
    #                                     Funzioni di environment
    #==================================================================================================

    # Funzione wrapper che esegue l'algoritmo e salva i tempi di esecuzione nella matrice dei risultati
    def execute(self, X, Y):
        if(len(X) <= self.maxSizeAllowed and len(X) <= self.maxSizeAllowed):
            start = time.time()
            self.bottom_up_LCS(X, Y)
            end=time.time()
            self.results["Bottom-Up LCS"].append(end-start)
            self.set_expected_time(len(X))
        else:
            self.set_no_results()

    # Crea la funzione dell'andamento dell'algoritmo
    def set_expected_time(self, size):
        self.results["Expected Times Function"].append((size ** 2) * self.scalingFactor)

    # Imposta a NaN i tempi di esecuzione dell'algoritmo e del suo andamento
    def set_no_results(self):
        self.results["Bottom-Up LCS"].append(np.nan)
        self.results["Expected Times Function"].append(np.nan)