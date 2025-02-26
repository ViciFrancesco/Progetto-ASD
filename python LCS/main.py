from longest_common_sequence import *

def main():
    X = "AGGTAB"
    Y = "GXTXAYB"
    memo={}

    print("Versione ricorsiva ->" , recursive_LCS(X, Y, len(X), len(Y)))
    print("Versione forza bruta ->" , brute_force_LCS(X, Y))
    print("Versione memoization ->" , memoization_LCS(X, Y, len(X), len(Y), memo))
    print("Versione bottom-up ->" , bottom_up_LCS(X, Y))

if __name__ == "__main__":
    main()