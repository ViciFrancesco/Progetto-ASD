import random
import string
import matplotlib.pyplot as plt
import math

from LCS_types import LCS

class TestLCS:
    #==================================================================================================
    #                                  Costruttore della classe 
    #==================================================================================================
    def __init__(self, scalingFactor, size, classToTest, printMemo=False):
        self.instance = classToTest(scalingFactor)  # Creazione dell'istanza della classe
        self.size = size  # Lunghezza massima delle stringhe
        self.printMemo = printMemo  # Flag per stampare la memoization
    
    #==================================================================================================
    #                             Funzioni di test per gli algoritmi
    #==================================================================================================

    def generate_random_strings(self, size):
        size1 = self.random_variation(size)
        size2 = (2 * size) - size1
        return (
            ''.join(random.choices(string.ascii_uppercase, k=size1)),
            ''.join(random.choices(string.ascii_uppercase, k=size2))
        )
    
    def random_variation(self, number):
        percentage = random.uniform(0, 0.2)  # Percentuale tra 0% e 20%
        result = number * (1 + percentage) if random.choice([True, False]) else number * (1 - percentage)
        return math.floor(result)  # Arrotonda per difetto
    
    def test_algorithm(self):
        for index in range(1, self.size):
            if index <= self.instance.maxSizeAllowed:
                X, Y = self.generate_random_strings(index)
                self.instance.execute(X, Y)  # Esegui l'algoritmo con le stringhe generate
        
        # Stampa la tabella di memoizzazione se richiesto
        if isinstance(self.instance, LCS.Memoization.value) and self.printMemo:
            self.instance.print_memo()
    
    #==================================================================================================
    #                                   Generazione del grafico
    #==================================================================================================
    
    @staticmethod
    def get_scaling_factor():
        return 1e-7
    
    def plot_results(self):
        keys = list(self.instance.results.keys())  # Estrai le chiavi (nomi delle serie di dati)
        values = list(self.instance.results.values())  # Estrai i valori (serie di dati)
        
        # Controlli di validità
        if len(values) < 2:
            raise ValueError("Il dizionario deve contenere almeno due serie di dati!")
        if len(values[0]) != len(values[1]):
            raise ValueError("I due array devono avere la stessa lunghezza")
        
        x = range(len(values[0]))  # Asse X: indice delle misurazioni
        
        plt.figure(figsize=(8, 5))  # Imposta dimensioni del grafico
        
        # Grafico delle due serie di dati
        plt.plot(x, values[0], marker='o', linestyle='', label=keys[0], color='blue')
        plt.plot(x, values[1], linestyle='-', label=keys[1], color='red')
        
        # Miglioramenti estetici del grafico
        plt.title("Confronto Algoritmi")
        plt.xlabel("Lunghezza delle stringhe")
        plt.ylabel("Tempo di esecuzione")
        plt.legend()
        plt.grid(True)
        
        plt.show()