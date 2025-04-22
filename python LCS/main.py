from constants import LCS
from test_algorithm import TestLCS
from compare_algorithms import CompareLCS



#====================================================================================================
#   PARAM. 1)   Determina se verrà testato un solo algoritmo o tutti.
#               (Nel secondo caso 'PARAM. 2' è irrilevante)
#====================================================================================================
test_all_algorithms : bool = True


#====================================================================================================
#   PARAM. 2)   Determina l'algoritmo che verrà testato.
#               (Usando l'oggetto LCS è possibile selezionare l'algoritmo)
#====================================================================================================
algorithm_to_test : LCS = LCS.BottomUp


#====================================================================================================
#   PARAM. 3)   Determina se i risultati del test saranno riassunti con le rispettive funzioni.
#               (Se si testano tutti gli algoritmi verranno mostrate soltanto le curve ottenute)
#====================================================================================================
fit_results_into_curve : bool = False


#====================================================================================================
#   PARAM. 4)   Determina la lunghezza media delle stringhe per il test.
#               (Il test verrà effettuato da stringhe lunghe 1 carattere fino alla lunghezza inserita)
#====================================================================================================
test_size : int= 100


#====================================================================================================
#   PARAM. 5)   Determina quante volte i test saranno ripetuti.
#               (Ripeterà il test fino alla lunghezza del 'PARAM. 4' ad ogni iterazione)
#====================================================================================================
test_iterations : int= 1


#====================================================================================================
#   PARAM. 6)   Permette di stampare il vettore delle soluzioni parziali 
#               (Viene considerato solo nell'esecuzione singola di LCS.Memoization)
#====================================================================================================
print_memo_saved_solutions : bool= False



def main():
    if(test_all_algorithms):
        CompareLCS(test_size, test_iterations, fit_results_into_curve)
    else:
        test=TestLCS(algorithm_to_test, test_size, test_iterations, fit_results_into_curve, print_memo_saved_solutions)

        test.test_algorithm()
        test.plot_results()
        
if __name__ == "__main__":
    main()
