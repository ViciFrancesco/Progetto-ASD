import time
import numpy as np

class MemoizationLCS:
    def __init__(self, iterations, maxSize):
        self.iterations=iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)
        self.memo = {}
    
    def memoization_LCS(self, X, Y, m, n):
        if m == 0 or n == 0:
            return 0
        if (m, n) in self.memo:
            return self.memo[(m, n)]
        
        if X[m - 1] == Y[n - 1]:
            self.memo[(m, n)] = 1 + self.memoization_LCS(X, Y, m - 1, n - 1)
        else:
            self.memo[(m, n)] = max(
                self.memoization_LCS(X, Y, m, n - 1),
                self.memoization_LCS(X, Y, m - 1, n)
            )
        return self.memo[(m, n)]

    def execute(self, stringsList, testSize):
        if(testSize <= self.maxSizeAllowed):
            resultsAverage = 0
            for iteration in range(0, self.iterations, 1):
                X = stringsList[(2**iteration)-1]
                Y = stringsList[2**iteration]
                start = time.time()
                self.memoization_LCS(X, Y, len(X), len(Y))
                end=time.time()
                self.results[iteration][testSize-1]=end-start
                resultsAverage += end-start
            return resultsAverage/self.iterations
        else:
            return np.nan
        
    def print_results(self):
        print(self.results)

    def print_memo(self):
        print("Memoization Table:")
        for key, value in sorted(self.memo.items()):  
            print(f"LCS({key[0]}, {key[1]}) = {value}")




