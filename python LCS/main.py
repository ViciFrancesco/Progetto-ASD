from test_algorithm import TestLCS
from compare_algorithms import CompareLCS
import time

from LCS_types import LCS

#==================================================================================================
#                                  Parametri del test
#==================================================================================================
    #
    # PARAM. 1) Variabile che consente di testare tutti gli algoritmi e stampare i risultati in un unico grafico
    #
testAllAlgorithms = True

    #
    # PARAM. 2) Lunghezza massima delle stringhe su cui effettuare il test
    #
testSize = 600

    #
    # PARAM. 3) Algoritmo su cui si desidera eseguire il test
    #
selectedAlgorithm = LCS.Memoization

    #
    # PARAM. 4) Variabile che consente di stampare il dizionario per la memoization
    #
printMemoDictionary = False

#==================================================================================================
#                                   Main del programma
#==================================================================================================
def main():
    # Ottenimento del fattore di scala della funzione dei tempi attesi
    scale = TestLCS.get_scaling_factor()

    if(testAllAlgorithms):
        compare = CompareLCS(testSize, scale)

        # Ottenimento orario di partenza del test
        startTest = time.time()

        # Uniforma la lunghezza dei risultati
        resultLength = compare.standardize_results_length()  

        # Ottenimento orario di fine del test
        endTest = time.time()

        # Stampa del tempo complessivo
        print("Tempo di esecuzione totale:", endTest-startTest, "secondi")

        # Stampa del grafico dei risultati del test
        compare.plot_results(resultLength)  
    else:
        # Inizializzazione del test 
        test = TestLCS(scale, testSize, selectedAlgorithm.value, printMemoDictionary)
        
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
