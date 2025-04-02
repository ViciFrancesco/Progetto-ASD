import copy
import numpy as np
import matplotlib.pyplot as plt

from test_algorithm import TestLCS
from LCS_types import LCS

import pdb

class CompareLCS:
    #==================================================================================================
    #                                  Costruttore della classe 
    #==================================================================================================
    def __init__(self, size, scale):
        self.results = {}  # Dizionario per memorizzare i risultati dei test

        # Esecuzione del test per ogni tipo di LCS
        for index, lcs_type in enumerate(LCS):
            print('Indice:', index, '/ Chiave:', lcs_type.name, '/ Valore:', lcs_type.value)
            
            # Inizializzazione del test 
            test = TestLCS(scale, size, lcs_type.value, False)
            test.test_algorithm()  # Esecuzione del test
            
            keys = list(test.instance.results.keys()) 

            self.results[lcs_type.name] = copy.deepcopy(test.instance.results[keys[0]])
            if index % 2 == 1:
                if(index==1):
                    self.results['Exponential Curve'] = copy.deepcopy(test.instance.results[keys[1]])
                else: 
                    self.results['Quadratic Curve'] = copy.deepcopy(test.instance.results[keys[1]])

    #==================================================================================================
    #                                     Funzioni ausiliarie
    #==================================================================================================
    
    # Rende uniforme la lunghezza delle serie di risultati riempiendo con NaN gli array più corti.
    def standardize_results_length(self):
        maxLength = 0
        
        # Trova la lunghezza massima tra i risultati
        for index, lcs_type in enumerate(LCS):
            if len(self.results[lcs_type.name]) > maxLength:
                maxLength = len(self.results[lcs_type.name])
                print(maxLength)
        
        # Estende i risultati più corti con valori NaN
        for lcs_type in LCS:
            if len(self.results[lcs_type.name]) < maxLength:
                for index in range(len(self.results[lcs_type.name]), maxLength):
                    self.results[lcs_type.name].append(np.nan)
        
        if len(self.results['Exponential Curve']) < maxLength:
            for index in range(len(self.results['Exponential Curve']), maxLength):
                self.results['Exponential Curve'].append(np.nan)

        if len(self.results['Quadratic Curve']) < maxLength:
            for index in range(len(self.results['Quadratic Curve']), maxLength):
                self.results['Quadratic Curve'].append(np.nan)
        
        return maxLength
    
    # Genera e visualizza un grafico comparativo tra le varie implementazioni di LCS
    def plot_results(self, maxLength):
        keys = list(self.results.keys())  # Ottieni le chiavi dinamicamente
        values = list(self.results.values())  # Ottieni i dati come liste
        
        if len(values) < 6:
            raise ValueError("Il dizionario deve contenere almeno sei serie di dati!")
        
        # Controllo sulla lunghezza degli array
        for value_set in values:
            if len(value_set) != maxLength:
                raise ValueError("Tutti gli array devono avere la stessa lunghezza")
        
        x = range(len(values[0]))  # Asse x (indice)
        plt.figure(figsize=(8, 5))  # Imposta dimensioni del grafico
        
        # Plot dinamico per ogni serie nel dizionario
        for index, key in enumerate(keys):
            plt.plot(x, values[index], linestyle='-', label=key)
        
        # Miglioramenti estetici del grafico
        plt.title("Confronto Algoritmi")
        plt.xlabel("Lunghezza complessiva delle stringhe")
        plt.ylabel("Tempo di esecuzione")
        plt.legend()
        plt.grid(True)
        
        plt.show()
