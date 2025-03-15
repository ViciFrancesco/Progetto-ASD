import time
import random
import string
import numpy as np
import matplotlib.pyplot as plt

from LCS_types import LCS

class TestLCS:
    ####################################################################################################
    #                                  Costruttore della classe 
    ####################################################################################################
    def __init__(self, scalingFactor, size, classToTest, printMemo = False):
        # Creazione dell'istanza della classe da creare
        self.instance = classToTest(scalingFactor)

        # Massima lunghezza delle stringhe da generare
        self.size = size   

        # Determina se il dizionario di MemoizationLCS viene stampato
        self.printMemo = printMemo     

    ####################################################################################################
    #                             Funzioni di test per gli algoritmi
    ####################################################################################################

    # Genera due stringhe randomiche della lunghezza data in input
    def generate_random_strings(self, size):
        return ''.join(random.choices(string.ascii_uppercase, k=size)), ''.join(random.choices(string.ascii_uppercase, k=size))

    # Genera gli input e richiama l'algoritmo da testare       
    def test_algorithm(self):
        for index in range(self.size-1):
            if index <= self.instance.maxSizeAllowed:
                X, Y= self.generate_random_strings(index+1)
                print("Esecuzione test con stringa di", index+1, "caratteri")
                self.instance.execute(X, Y)

        # Stampa il dizionario 'memo' della MemoizationLCS
        if(isinstance(self.instance, LCS.Memoization.value) and self.printMemo == True):
            self.instance.print_memo()
    
    ####################################################################################################
    #                                   Generazione del grafico
    ####################################################################################################

    # Genera un fattore di scala per la funzione di andamento dell'algoritmo da testare
    def GET_scaling_factor():
        # N = 10**6
        # start = time.perf_counter()
        # x = 0
        # for _ in range(N):
        #     x += 1  # Operazione semplice
        # end = time.perf_counter()

        # tempo_per_istruzione = (end - start)
        # print(f"Tempo medio per istruzione: {tempo_per_istruzione:.10f} secondi")
        # return tempo_per_istruzione
        return 0.0000001
    
    # Stampa il grafico dei risultati dell'algoritmo testato
    def plot_results(self):
        # Ottieni le chiavi dinamicamente
        keys = list(self.instance.results.keys())  
        # Ottieni i dati come liste
        values = list(self.instance.results.values())  
        
        if len(values) < 2:
            raise ValueError("Il dizionario deve contenere almeno due serie di dati!")
        if (len(values[0]) != len(values[1])):
            raise ValueError("I due array devono avere la stessa lunghezza")

        x = range(len(values[0]))  # Asse x (indice)

        plt.figure(figsize=(8, 5))  # Imposta dimensioni del grafico

        # Plot dinamico per ogni serie nel dizionario
        plt.plot(x, values[0], marker='o', linestyle='', label=keys[0], color='blue')
        plt.plot(x, values[1], linestyle='-', label=keys[1], color='red')

        # Miglioramenti estetici
        plt.title("Confronto Algoritmi")
        plt.xlabel("Lunghezza delle stringhe")
        plt.ylabel("Tempo di esecuzione")
        plt.legend()
        plt.grid(True)

        plt.show()

        plt.show()
    
