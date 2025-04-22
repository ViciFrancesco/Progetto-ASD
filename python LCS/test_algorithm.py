import random
import string
import matplotlib.pyplot as plt
import math
import numpy as np
import time

from constants import LCS, Functions, fit_function

class TestLCS:
    def __init__(self,  lscType, size, iterations,  mustFit=False, printMemo=False):
        """
        Inizializza un test per un algoritmo LCS (Longest Common Subsequence).

        Args:
            lscType: Tipo di algoritmo LCS da testare.
            size: Dimensione massima delle stringhe da utilizzare nel test.
            iterations: Numero di coppie di stringhe da testare per ogni dimensione.
            mustFit: Indica se si desidera effettuare il fit dei risultati.
            printMemo: Indica se stampare la tabella memoization (se applicabile).
        """
        self.lcsType = lscType
        self.size = size
        self.iterations = iterations

        self.fitToCurve = mustFit
        self.printMemo = printMemo 
        self.instance = lscType.clss(self.iterations, self.lcsType.maxSizeAllowed) 

        # Associa la funzione di crescita teorica attesa in base all'algoritmo
        if(self.lcsType == LCS.Recursive or self.lcsType == LCS.BruteForce):
            self.expectedTimes = Functions.Exponential
        elif(self.lcsType == LCS.Memoization or self.lcsType == LCS.BottomUp):
            self.expectedTimes = Functions.Quadratic

        # Struttura per salvare i risultati ottenuti e quelli attesi
        self.results={
            self.lcsType.label : [],
            self.expectedTimes.label : []
        }
   
    def test_algorithm(self):
        """
        Esegue il test dell'algoritmo LCS per tutte le dimensioni fino a `size`,
        salvando i tempi di esecuzione reali e teorici.
        """
        startTests = time.time() 

        for currentSize in range(1, self.size+1):
            strings = self.generate_random_strings(currentSize)
            
            if(self.meet_requirements(strings, currentSize)):
                print("[", self.lcsType.label,"] -> Test size:", currentSize)
                result = self.instance.execute(strings, currentSize) 
                self.results[self.lcsType.label].append(result)
                self.results[self.expectedTimes.label].append(self.expectedTimes.formula(currentSize))
            else:
                self.results[self.lcsType.label].append(np.nan)
                self.results[self.expectedTimes.label].append(np.nan)

        endTests = time.time()
        print(f"Esecuzione del test di {self.lcsType.label} ({self.iterations} iterazioni, fino a {self.size} caratteri) -> Durata: {endTests - startTests} secondi")

        if self.lcsType == LCS.Memoization and self.printMemo:
            self.instance.print_memo()

    def meet_requirements(self, strings, size):
        """
        Controlla che le stringhe generate rispettino i requisiti del test.

        Args:
            strings: Lista di stringhe generate.
            size: Dimensione attesa delle stringhe.

        Returns:
            True se i requisiti sono rispettati, False altrimenti.
        """
        if(len(strings) == 0):
            print('Non ci sono stringhe nella lista')
            return False
        if(len(strings)%2 != 0):
            print('Il numero di stringhe non è pari')
            return False
        if(len(strings)/2 != self.iterations):
            print('Il numero di stringhe non è il doppio del numero di iterazioni del test')
            return False
        if(size > self.instance.maxSizeAllowed):
            return False
        return True
        
    def generate_random_strings(self, lenghtAvg):
        """
        Genera coppie di stringhe casuali con lunghezze variabili attorno alla media specificata.

        Args:
            lenghtAvg: Lunghezza media delle stringhe.

        Returns:
            Lista contenente le stringhe generate.
        """
        strings = [] 
        for iteration in range(self.iterations):
            size1 = self.random_variation(lenghtAvg)
            strings.append(''.join(random.choices(string.ascii_uppercase, k=size1)))
            size2 = (2 * lenghtAvg) - size1
            strings.append(''.join(random.choices(string.ascii_uppercase, k=size2)))
        return strings
    
    def random_variation(self, number):
        """
        Applica una variazione casuale fino al 20% a un numero.

        Args:
            number: Numero su cui applicare la variazione.

        Returns:
            Numero intero modificato con una variazione casuale.
        """
        percentage = random.uniform(0, 0.2) 
        result = number * (1 + percentage) if random.choice([True, False]) else number * (1 - percentage)
        return math.floor(result)  

    def plot_results(self):
        """
        Mostra un grafico dei risultati ottenuti rispetto ai valori teorici attesi.
        Se richiesto, aggiunge anche il fit ai dati sperimentali.
        """
        x_data = range(self.size) 
        y_data = self.results[self.lcsType.label]

        plt.figure(figsize=(8, 5))

        if(self.fitToCurve == True):
            y_fit = fit_function(x_data, y_data, self.lcsType)   
            plt.plot(x_data, y_fit, label=f"Fit esponenziale", linestyle='--', color='green')
        else:
            plt.plot(x_data, y_data, label=self.lcsType.label, marker='o', linestyle='', color='blue')

        plt.plot(x_data, self.results[self.expectedTimes.label], label=self.expectedTimes.label, linestyle='-', color='red')
        
        plt.title("Confronto Algoritmi con Fit Esponenziale")
        plt.xlabel("Lunghezza delle stringhe")
        plt.ylabel("Tempo di esecuzione")
        plt.legend()
        plt.grid(True)
        plt.show()

   