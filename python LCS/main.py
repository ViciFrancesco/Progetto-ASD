from constants import LCS
from test_algorithm import TestLCS

def main():
    test = TestLCS(LCS.Recursive, 11, 3)
    test.test_algorithm()
    test.plot_results()

if __name__ == "__main__":
    main()
