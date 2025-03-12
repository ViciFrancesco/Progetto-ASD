from algorithms.recursive_LCS import RecursiveLCS
from test_algorithm import TestLCS
from test_algorithm import TestLCS
from enum import Enum

class LCS(Enum):
    Recursive = RecursiveLCS
    BruteForce = None
    Memoization = None
    BottomUp = None  

maxStringLenght = 500
selectedAlgorithm = LCS.Recursive.value

def main():
    scale = TestLCS.GET_scaling_factor()

    test = TestLCS(scale, maxStringLenght, selectedAlgorithm)
    test.test_algorithm()

    return True

if __name__ == "__main__":
    main()
