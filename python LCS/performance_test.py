import time
import random
import string
import matplotlib.pyplot as plt
from longest_common_sequence import *

class LCSTester:
    def __init__(self, sizes):
        self.sizes = sizes
        self.results = {"Recursive": [], "Brute Force": [], "Memoization": [], "Bottom-Up": []}
    
    def generate_random_strings(self, size):
        return ''.join(random.choices(string.ascii_uppercase, k=size)), ''.join(random.choices(string.ascii_uppercase, k=size))
    
    def run_test(self):
        for size in self.sizes:
            X, Y = self.generate_random_strings(size)
            print(f"Testing with strings of length {size}...")
            
            timeSum=0
            for i in range(5):
                # Recursive LCS
                start = time.time()
                if size <= 15:  
                    recursive_LCS(X, Y, len(X), len(Y))
                end = time.time()
                timeSum += end - start if size <= 15 else 0

            self.results["Recursive"].append(timeSum/5 if size <= 15 else None)
            
            # Brute Force LCS
            start = time.time()
            if size <= 24: 
                brute_force_LCS(X, Y)
            end = time.time()
            self.results["Brute Force"].append(end - start if size <= 24 else None)
            
            # Memoization LCS
            start = time.time()
            memoization_LCS(X, Y, len(X), len(Y), {})
            end = time.time()
            self.results["Memoization"].append(end - start)
            
            # Bottom-Up LCS
            start = time.time()
            bottom_up_LCS(X, Y)
            end = time.time()
            self.results["Bottom-Up"].append(end - start)
    
    def plot_results(self):
        plt.figure(figsize=(10, 6))
        for method, times in self.results.items():
            valid_sizes = [self.sizes[i] for i in range(len(times)) if times[i] is not None]
            valid_times = [t for t in times if t is not None]
            plt.plot(valid_sizes, valid_times, label=method)
        
        plt.xlabel("String Length")
        plt.ylabel("Execution Time (seconds)")
        plt.title("LCS Algorithm Performance Comparison")
        plt.legend()
        plt.grid()
        plt.show()


