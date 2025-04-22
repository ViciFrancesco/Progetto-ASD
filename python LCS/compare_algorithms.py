import numpy as np
import matplotlib.pyplot as plt

from constants import LCS, Functions, fit_function
from test_algorithm import TestLCS

# Classe per confrontare tutti gli algoritmi LCS
class CompareLCS:
    def __init__(self, size, iterations, mustFit):
        """
        Inizializza la classe eseguendo i test per tutti gli algoritmi LCS
        e memorizzando i risultati.

        Args:
            size: Massima lunghezza delle stringhe da testare.
            iterations: Numero di iterazioni per ogni test.
            mustFit: Flag per attivare il fitting sui dati raccolti.
        """
        self.results = {}
        self.size = size
        self.fitToCurve = mustFit

        # Esegue i test su tutti gli algoritmi definiti nell'enum LCS
        for alg in LCS:
            test = TestLCS(alg, self.size, iterations)
            test.test_algorithm()

            # Salva i risultati ottenuti per ciascun algoritmo
            self.results[alg.label] = test.results[alg.label]

            # Aggiunge anche le curve teoriche di riferimento (una sola volta)
            if alg == LCS.BruteForce:
                self.results[Functions.Exponential.label] = test.results[Functions.Exponential.label]
            if alg == LCS.BottomUp:
                self.results[Functions.Quadratic.label] = test.results[Functions.Quadratic.label]

        # Standardizza la lunghezza dei risultati per tutti gli algoritmi
        maxLength = self.standardize_results_length()

        # Mostra il grafico comparativo finale
        self.plot_results(maxLength)

    def standardize_results_length(self):
        """
        Uniforma la lunghezza delle liste di risultati tra tutti gli algoritmi,
        riempiendo con NaN dove necessario.

        Returns:
            La lunghezza massima tra le liste di risultati.
        """
        maxLength = 0

        # Trova la lunghezza massima tra tutti i risultati degli algoritmi
        for alg in LCS:
            rawLength = len(self.results[alg.label])
            if rawLength > maxLength:
                maxLength = rawLength

        # Riempi le liste più corte con NaN per uniformare la lunghezza
        for alg in LCS:
            rawLength = len(self.results[alg.label])
            if rawLength < maxLength:
                nan_tail = np.full(maxLength - rawLength, np.nan)
                self.results[alg.label] = self.results[alg.label] + nan_tail

        for func in Functions:
            rawLength = len(self.results[func.label])
            if rawLength < maxLength:
                nan_tail = np.full(maxLength - rawLength, np.nan)
                self.results[func.label] = self.results[func.label] + nan_tail

        return maxLength

    def plot_results(self, maxLength):
        """
        Crea un grafico che confronta i risultati dei vari algoritmi LCS
        e li confronta con le curve teoriche.

        Args:
            maxLength: Lunghezza massima dei dati da plottare.
        """
        plt.figure(figsize=(8, 5))

        # Plotta i risultati (con o senza fitting) per ogni algoritmo
        for alg in LCS:
            x_data = range(maxLength)
            y_data = self.results[alg.label]

            if self.fitToCurve:
                y_fit = fit_function(x_data, y_data, alg)
                plt.plot(x_data, y_fit, label=alg.label, linestyle='--', color=alg.color)
            else:
                plt.plot(x_data, y_data, label=alg.label, marker='o', linestyle='', color=alg.color)

        # Plotta anche le curve teoriche di riferimento
        for func in Functions:
            x_data = range(maxLength)
            y_data = self.results[func.label]

            plt.plot(x_data, y_data, linestyle='-', label=func.label, color='red')

        plt.title("Confronto Algoritmi LCS")
        plt.xlabel("Lunghezza delle stringhe")
        plt.ylabel("Tempo di esecuzione")
        plt.legend()
        plt.grid(True)
        plt.show()

 

