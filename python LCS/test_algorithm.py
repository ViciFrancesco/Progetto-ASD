import random
import string
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit

from constants import LCS, Functions

def exponential_function(x, a, b):
        return a * np.exp(b * x)

def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

class TestLCS:
    def __init__(self,  lscType, size, iterations,  mustFit=False, printMemo=False):
        self.lcsType = lscType
        self.size = size  
        self.iterations = iterations

        self.fitToCurve = mustFit

        self.printMemo = printMemo 
        self.instance = lscType.clss(self.iterations, self.lcsType.maxSizeAllowed) 

        if(self.lcsType == LCS.Recursive or self.lcsType == LCS.BruteForce):
            self.expectedTimes = Functions.Exponential
        elif(self.lcsType == LCS.Memoization or self.lcsType == LCS.BottomUp):
            self.expectedTimes = Functions.Quadratic

        self.results={
            self.lcsType.label : [],
            self.expectedTimes.label : []
        }
   
    def test_algorithm(self):
        for currentSize in range(1, self.size+1):
            strings = self.generate_random_strings(currentSize)
            if(self.meet_requirements(strings)):
                result = self.instance.execute(strings, currentSize) 
                if(result != np.nan):
                    self.results[self.lcsType.label].append(result)
                    self.results[self.expectedTimes.label].append(self.expectedTimes.formula(currentSize))
                else:
                    self.results[self.lcsType.label].append(np.nan)
                    self.results[self.expectedTimes.label].append(np.nan)

        if self.lcsType == LCS.Memoization and self.printMemo:
            self.instance.print_memo()
    
    def meet_requirements(self, strings):
        if(len(strings) == 0):
            print('Non ci sono stringhe nella lista')
            return False
        if(len(strings)%2 != 0):
            print('Il numero di stringhe non è pari')
            return False
        if(len(strings)/2 != self.iterations):
            print('Il numero di stringhe non è il doppio del numero di iterazioni del test')
            return False
        return True
        
    def generate_random_strings(self, lenghtAvg):
        strings = [] 
        for iteration in range(self.iterations):
            size1 = self.random_variation(lenghtAvg)
            strings.append(''.join(random.choices(string.ascii_uppercase, k=size1)))
            size2 = (2 * lenghtAvg) - size1
            strings.append(''.join(random.choices(string.ascii_uppercase, k=size2)))
        return strings
    
    def random_variation(self, number):
        percentage = random.uniform(0, 0.2) 
        result = number * (1 + percentage) if random.choice([True, False]) else number * (1 - percentage)
        return math.floor(result)  

    def plot_results(self):
        x_data = range(self.size) 
        y_data = self.results[self.lcsType.label]

        y_fit = self.fit_function(x_data, y_data)   
      
        plt.figure(figsize=(8, 5))
        plt.plot(x_data, y_data, marker='o', linestyle='', label=self.lcsType.label, color='blue')
        plt.plot(x_data, y_fit, label=f"Fit esponenziale", color='green', linestyle='--')
        plt.plot(x_data, self.results[self.expectedTimes.label], linestyle='-', label=self.expectedTimes.label, color='red')
        
        plt.title("Confronto Algoritmi con Fit Esponenziale")
        plt.xlabel("Lunghezza delle stringhe")
        plt.ylabel("Tempo di esecuzione")
        plt.legend()
        plt.grid(True)
        plt.show() 

    def fit_function(self, x, y, func_type="exponential"):
        # Scegli la funzione di fitting
        if func_type == "exponential":
            func = exponential_function
        elif func_type == "quadratic":
            func = quadratic_function
        else:
            raise ValueError("Funzione di fitting non supportata")

        # Trova la parte valida di y (prima dei nan)
        valid_length = np.argmax(np.isnan(y)) if np.isnan(y).any() else len(y)
        x_valid = x[:valid_length]
        y_valid = y[:valid_length]

        # Esegui il fit sulla parte valida
        popt, _ = curve_fit(func, x_valid, y_valid)

        # Applica il modello alla parte valida
        y_fit_valid = func(x_valid, *popt)

        # Ricostruisci array completo con np.nan in coda
        nan_tail = [np.nan] * (len(y) - valid_length)
        y_fit_full = np.concatenate([y_fit_valid, nan_tail])

        return y_fit_full