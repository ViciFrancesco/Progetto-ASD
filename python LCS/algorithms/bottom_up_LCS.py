import time
import numpy as np

class BottomUpLCS:
    def __init__(self, iterations, maxSize):
        self.iterations=iterations
        self.maxSizeAllowed = maxSize  
        self.results = np.full((self.iterations, self.maxSizeAllowed), np.nan)
    
    def bottom_up_LCS(self, X, Y):
        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    def execute(self, stringsList, testSize):
        if(testSize <= self.maxSizeAllowed):
            resultsAverage = 0
            for iteration in range(0, self.iterations, 1):
                X = stringsList[(2**iteration)-1]
                Y = stringsList[2**iteration]
                start = time.time()
                self.bottom_up_LCS(X, Y)
                end=time.time()
                self.results[iteration][testSize-1]=end-start
                resultsAverage += end-start
            return resultsAverage/self.iterations
        else:
            return np.nan
        
    def print_results(self):
        print(self.results)