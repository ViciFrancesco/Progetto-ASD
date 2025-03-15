from algorithms.recursive_LCS import RecursiveLCS
from algorithms.brute_force_LCS import BruteForceLCS
from test_algorithm import TestLCS
from enum import Enum
import time

class LCS(Enum):
    Recursive = RecursiveLCS
    BruteForce = BruteForceLCS
    Memoization = None
    BottomUp = None  

#==================================================================================================
#                                  Parametri del test
#==================================================================================================
    #
    # PARAM. 1) Lunghezza massima delle stringhe su cui effettuare il test
    #
maxStringLenght = 500

    #
    # PARAM. 2) Algoritmo su cui si desidera eseguire il test
    #
selectedAlgorithm = LCS.BruteForce

#==================================================================================================
#                                   Main del programma
#==================================================================================================
def main():
    # Ottenimento del fattore di scala della funzione dei tempi attesi
    scale = TestLCS.GET_scaling_factor()

    # Inizializzazione del test 
    test = TestLCS(scale, maxStringLenght, selectedAlgorithm.value)
    
    # Ottenimento orario di partenza del test
    startTest = time.time()

    # Esecuzione del test
    test.test_algorithm()

    # Ottenimento orario di fine del test
    endTest = time.time()

    # Stampa del tempo complessivo
    print("Tempo di esecuzione totale:", endTest-startTest, "secondi")

    # Stampa del grafico dei risultati del test
    test.plot_results()
    return True

if __name__ == "__main__":
    main()
