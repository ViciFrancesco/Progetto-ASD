import time
import numpy as np
from itertools import combinations

class BruteForceLCS:
    def __init__(self, iterations, maxSize):
        self.iterations=iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)
    
    def brute_force_LCS(self, X, Y):
        subseq_X = self.subsequences(X)
        subseq_Y = self.subsequences(Y)
        common = subseq_X.intersection(subseq_Y)
        return max(map(len, common)) if common else 0
    
    def subsequences(self, s):
        subseqs = set()
        for i in range(1, len(s) + 1):
            for combo in combinations(s, i):
                subseqs.add("".join(combo))
        return subseqs

    def execute(self, stringsList, testSize):
        if(testSize <= self.maxSizeAllowed):
            resultsAverage = 0
            for iteration in range(0, self.iterations, 1):
                X = stringsList[(2**iteration)-1]
                Y = stringsList[2**iteration]
                start = time.time()
                self.brute_force_LCS(X, Y)
                end=time.time()
                self.results[iteration][testSize-1]=end-start
                resultsAverage += end-start
            return resultsAverage/self.iterations
        else:
            return np.nan
        
    def print_results(self):
        print(self.results)