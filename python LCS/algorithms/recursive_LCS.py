import time
import numpy as np

class RecursiveLCS:
    ####################################################################################################
    #                                  Costruttore della classe 
    ####################################################################################################
    def __init__(self, scalingFactor):
        # Definizione della matrice dei risultati
        self.results = {
            "Recursive": [],
            "Expected Times Function" : []}
        
        # Definizione della massima lunghezza delle stringhe in input
        self.maxSizeAllowed = 24

        # Fattore di scala uguale per tutti gli algoritmi
        self.scalingFactor = scalingFactor

        # Creazione della funzione di riferimento
        self.create_exponential_curve()
        
    ####################################################################################################
    #                                       Algoritmo principale 
    ####################################################################################################  
    def execute(self, X, Y):
        if(len(X) <= self.maxSizeAllowed and len(X) <= self.maxSizeAllowed):
            start = time.time()
            self.recursive_LCS(X, Y, len(X), len(Y))
            end=time.time()
            self.results["Recursive_LCS"].append(end-start)
            self.set_expected_time(len(X))
        else:
            self.set_no_results()
        
    def recursive_LCS(self, X, Y, m, n):
        if m == 0 or n == 0:
            return 0
        elif X[m - 1] == Y[n - 1]:
            return 1 + self.recursive_LCS(X, Y, m - 1, n - 1)
        else:
            return max(self.recursive_LCS(X, Y, m, n - 1), self.recursive_LCS(X, Y, m - 1, n))
    
    ####################################################################################################
    #                                      Funzione di riferimento
    #################################################################################################### 
    def set_expected_time(self, size):
        self.results["Expected Times Function"].append((2 ** size)* self.scalingFactor)

    def set_no_results(self):
        self.results["Recursive_LCS"].append(np.nan)
        self.results["Expected Times Function"].append(np.nan)




    