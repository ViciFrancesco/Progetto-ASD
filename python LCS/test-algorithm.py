import time
import random
import string
import numpy as np

from algorithms.recursive_LCS import RecursiveLCS

class TestLCS:
    def __init__(self, scalingFactor, size, classToTest):
        self.instance = classToTest(scalingFactor)
        self.size = size        

    def generate_random_strings(self, size):
        return ''.join(random.choices(string.ascii_uppercase, k=size)), ''.join(random.choices(string.ascii_uppercase, k=size))

    def test_algorithm(self):
        for index in range(self.size):
            if index <= self.instance.maxSizeAllowed:
                X, Y= self.generate_random_strings(20)
                self.instance.execute(X, Y)
    
    def plot_results():
        print("test")

    
