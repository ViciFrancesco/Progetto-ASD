import time
import numpy as np


class RecursiveLCS:
    def __init__(self, iterations, maxSize):
        self.iterations=iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)
    
    def recursive_LCS(self, X, Y, m, n):
        if m == 0 or n == 0:
            return 0
        elif X[m - 1] == Y[n - 1]:
            return 1 + self.recursive_LCS(X, Y, m - 1, n - 1)
        else:
            return max(self.recursive_LCS(X, Y, m, n - 1), self.recursive_LCS(X, Y, m - 1, n))

    def execute(self, stringsList, testSize):
        if(testSize <= self.maxSizeAllowed):
            resultsAverage = 0
            for iteration in range(0, self.iterations, 1):
                X = stringsList[(2**iteration)-1]
                Y = stringsList[2**iteration]
                start = time.time()
                self.recursive_LCS(X, Y, len(X), len(Y))
                end=time.time()
                self.results[iteration][testSize-1]=end-start
                resultsAverage += end-start
            return resultsAverage/self.iterations
        else:
            return np.nan
        
    def print_results(self):
        print(self.results)

























    