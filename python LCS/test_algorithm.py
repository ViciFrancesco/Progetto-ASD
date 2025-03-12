import time
import random
import string
import numpy as np

from algorithms.recursive_LCS import RecursiveLCS

class TestLCS:
    ####################################################################################################
    #                                  Costruttore della classe 
    ####################################################################################################
    def __init__(self, scalingFactor, size, classToTest):
        self.instance = classToTest(scalingFactor)
        self.size = size        

    ####################################################################################################
    #                             Funzioni di test per gli algoritmi
    ####################################################################################################
    def generate_random_strings(self, size):
        return ''.join(random.choices(string.ascii_uppercase, k=size)), ''.join(random.choices(string.ascii_uppercase, k=size))

    def test_algorithm(self):
        for index in range(self.size-1):
            if index <= self.instance.maxSizeAllowed:
                X, Y= self.generate_random_strings(index+1)
                print("Esecuzione test con stringa di", index+1, "caratteri")
                self.instance.execute(X, Y)
    
    ####################################################################################################
    #                                   Generazione del grafico
    ####################################################################################################
    def GET_scaling_factor():
        start=time.time()
        x=1+5
        end=time.time()
        return end-start

    def plot_results():
        print("test")

    
