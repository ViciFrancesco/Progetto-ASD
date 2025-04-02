import time
import numpy as np
from itertools import combinations

class BruteForceLCS:
    #==================================================================================================
    #                                  Costruttore della classe 
    #==================================================================================================
    def __init__(self, scalingFactor):
        # Matrice dei risultati
        self.results = {
            "Brute Force LCS": [],
            "Expected Times Function" : []}
        
        # Massima lunghezza delle stringhe in input
        self.maxSizeAllowed = 20

        # Fattore di scala (uguale per tutti gli algoritmi)
        self.scalingFactor = scalingFactor
        
    #==================================================================================================
    #                                       Algoritmo principale 
    #==================================================================================================   
    def brute_force_LCS(self, X, Y):
        subseq_X = self.subsequences(X)
        subseq_Y = self.subsequences(Y)
        common = subseq_X.intersection(subseq_Y)
        return max(map(len, common)) if common else 0
    
    # Trova tutte le sottosequenze di una stringa data in input
    def subsequences(self, s):
        subseqs = set()
        for i in range(1, len(s) + 1):
            for combo in combinations(s, i):
                subseqs.add("".join(combo))
        return subseqs

    #==================================================================================================
    #                                     Funzioni di environment
    #==================================================================================================

    # Funzione wrapper che esegue l'algoritmo e salva i tempi di esecuzione nella matrice dei risultati
    def execute(self, X, Y):
        if(len(X) <= self.maxSizeAllowed and len(X) <= self.maxSizeAllowed):
            start = time.time()
            self.brute_force_LCS(X, Y)
            end=time.time()
            self.results["Brute Force LCS"].append(end-start)
            self.set_expected_time((len(X)+len(Y))/2)
        else:
            self.set_no_results()

    # Crea la funzione dell'andamento dell'algoritmo
    def set_expected_time(self, size):
        self.results["Expected Times Function"].append((2 ** size) * self.scalingFactor)

    # Imposta a NaN i tempi di esecuzione dell'algoritmo e del suo andamento
    def set_no_results(self):
        self.results["Brute Force LCS"].append(np.nan)
        self.results["Expected Times Function"].append(np.nan)