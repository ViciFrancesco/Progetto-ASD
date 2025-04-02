import time
import numpy as np

class MemoizationLCS:
    #==================================================================================================
    #                                  Costruttore della classe 
    #==================================================================================================
    def __init__(self, scalingFactor):
        # Matrice dei risultati
        self.results = {
            "Memoization LCS": [],
            "Expected Times Function" : []}
        
        # Massima lunghezza delle stringhe in input
        self.maxSizeAllowed = 900

        # Fattore di scala (uguale per tutti gli algoritmi)
        self.scalingFactor = scalingFactor

        # Dizionario per la memoization
        self.memo = {} 
        
    #==================================================================================================
    #                                       Algoritmo principale 
    #==================================================================================================   
    def memoization_LCS(self, X, Y, m, n):
        if m == 0 or n == 0:
            return 0
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        
        if X[m - 1] == Y[n - 1]:
            self.memo[(m, n)] = 1 + self.memoization_LCS(X, Y, m - 1, n - 1)
        else:
            self.memo[(m, n)] = max(
                self.memoization_LCS(X, Y, m, n - 1),
                self.memoization_LCS(X, Y, m - 1, n)
            )
        return self.memo[(m, n)]

    #==================================================================================================
    #                                     Funzioni di environment
    #==================================================================================================

    # Funzione wrapper che esegue l'algoritmo e salva i tempi di esecuzione nella matrice dei risultati
    def execute(self, X, Y):
        if(len(X) <= self.maxSizeAllowed and len(X) <= self.maxSizeAllowed):
            start = time.time()
            self.memoization_LCS(X, Y, len(X), len(Y))
            end=time.time()
            self.results["Memoization LCS"].append(end-start)
            self.set_expected_time((len(X)+len(Y))/2)
        else:
            self.set_no_results()

    # Crea la funzione dell'andamento dell'algoritmo
    def set_expected_time(self, size):
        self.results["Expected Times Function"].append((size ** 2) * self.scalingFactor)

    # Imposta a NaN i tempi di esecuzione dell'algoritmo e del suo andamento
    def set_no_results(self):
        self.results["Memoization LCS"].append(np.nan)
        self.results["Expected Times Function"].append(np.nan)

    # Stampa il dizionario per la memoization
    def print_memo(self):
        print("Memoization Table:")
        for key, value in sorted(self.memo.items()):  
            print(f"LCS({key[0]}, {key[1]}) = {value}")