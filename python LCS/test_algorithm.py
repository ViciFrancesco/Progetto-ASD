# import random
# import string
# import matplotlib.pyplot as plt
# import random
# import math

# from LCS_types import LCS

# class TestLCS:
#     #==================================================================================================
#     #                                  Costruttore della classe 
#     #==================================================================================================
#     def __init__(self, scalingFactor, size, classToTest, printMemo = False):
#         # Creazione dell'istanza della classe da creare
#         self.instance = classToTest(scalingFactor)

#         # Massima lunghezza delle stringhe da generare
#         self.size = size   

#         # Determina se il dizionario di MemoizationLCS viene stampato
#         self.printMemo = printMemo     

#     #==================================================================================================
#     #                             Funzioni di test per gli algoritmi
#     #==================================================================================================

#     # Genera due stringhe randomiche della lunghezza data in input
#     def generate_random_strings(self, size):
        
#         size1 = self.random_variation(size)
#         size2 = (2 * size) - size1

#         return ''.join(random.choices(string.ascii_uppercase, k=size1)), ''.join(random.choices(string.ascii_uppercase, k=size2))


#     def random_variation(self, number):
#         # Genera una percentuale casuale tra 0% e 20%
#         percentage = random.uniform(0, 0.2)
#         # Decide casualmente se aggiungere o sottrarre
#         if random.choice([True, False]):
#             result = number * (1 + percentage)  # Aggiunge la percentuale
#         else:
#             result = number * (1 - percentage)  # Sottrae la percentuale

#         # Arrotonda per difetto
#         return math.floor(result)



#     # Genera gli input e richiama l'algoritmo da testare       
#     def test_algorithm(self):
#         for index in range(self.size-1):
#             if index <= self.instance.maxSizeAllowed:
#                 X, Y= self.generate_random_strings(index+1)
#                 # print("Esecuzione test con stringa di", index+1, "caratteri")
#                 self.instance.execute(X, Y)

#         # Stampa il dizionario 'memo' della MemoizationLCS
#         if(isinstance(self.instance, LCS.Memoization.value) and self.printMemo == True):
#             self.instance.print_memo()
    
#     #==================================================================================================
#     #                                   Generazione del grafico
#     #==================================================================================================

#     # Genera un fattore di scala per la funzione di andamento dell'algoritmo da testare
#     def get_scaling_factor():
#         return 1e-7
    
#     # Stampa il grafico dei risultati dell'algoritmo testato
#     def plot_results(self):
#         # Ottieni le chiavi dinamicamente
#         keys = list(self.instance.results.keys())  
#         # Ottieni i dati come liste
#         values = list(self.instance.results.values())  
        
#         if len(values) < 2:
#             raise ValueError("Il dizionario deve contenere almeno due serie di dati!")
#         if (len(values[0]) != len(values[1])):
#             raise ValueError("I due array devono avere la stessa lunghezza")

#         x = range(len(values[0]))  # Asse x (indice)

#         plt.figure(figsize=(8, 5))  # Imposta dimensioni del grafico

#         # Plot dinamico per ogni serie nel dizionario
#         plt.plot(x, values[0], marker='o', linestyle='', label=keys[0], color='blue')
#         plt.plot(x, values[1], linestyle='-', label=keys[1], color='red')

#         # Miglioramenti estetici
#         plt.title("Confronto Algoritmi")
#         plt.xlabel("Lunghezza delle stringhe")
#         plt.ylabel("Tempo di esecuzione")
#         plt.legend()
#         plt.grid(True)

#         plt.show()

#         plt.show()
    

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
        """
        Inizializza un'istanza della classe TestLCS per testare un algoritmo di LCS.
        
        :param scalingFactor: Fattore di scala per l'algoritmo
        :param size: Massima lunghezza delle stringhe da generare
        :param classToTest: Classe dell'algoritmo da testare
        :param printMemo: Se True, stampa la tabella di memoizzazione
        """
        self.instance = classToTest(scalingFactor)  # Creazione dell'istanza della classe
        self.size = size  # Lunghezza massima delle stringhe
        self.printMemo = printMemo  # Flag per stampare la memoization
    
    #==================================================================================================
    #                             Funzioni di test per gli algoritmi
    #==================================================================================================

    def generate_random_strings(self, size):
        """
        Genera due stringhe casuali con variazione di lunghezza.
        
        :param size: Lunghezza base delle stringhe
        :return: Due stringhe casuali con lunghezze variabili
        """
        size1 = self.random_variation(size)
        size2 = (2 * size) - size1
        return (
            ''.join(random.choices(string.ascii_uppercase, k=size1)),
            ''.join(random.choices(string.ascii_uppercase, k=size2))
        )
    
    def random_variation(self, number):
        """
        Applica una variazione casuale del 20% alla lunghezza della stringa.
        
        :param number: Numero di riferimento
        :return: Valore modificato con una variazione casuale
        """
        percentage = random.uniform(0, 0.2)  # Percentuale tra 0% e 20%
        result = number * (1 + percentage) if random.choice([True, False]) else number * (1 - percentage)
        return math.floor(result)  # Arrotonda per difetto
    
    def test_algorithm(self):
        """
        Esegue i test sull'algoritmo generando stringhe casuali di lunghezze variabili.
        """
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
        """
        Restituisce un fattore di scala predefinito per la funzione di andamento.
        """
        return 1e-7
    
    def plot_results(self):
        """
        Genera un grafico per confrontare i risultati dell'algoritmo testato.
        """
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