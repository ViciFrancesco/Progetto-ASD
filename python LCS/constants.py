from enum import Enum

from algorithms.recursive_LCS import RecursiveLCS
from algorithms.brute_force_LCS import BruteForceLCS
from algorithms.memoization_LCS import MemoizationLCS
from algorithms.bottom_up_LCS import BottomUpLCS

scale:float = 1e-4

def exponential(x):
    return (2 ** x) * scale

def quadratic(x):
    return (x ** 2) * scale

class Functions(Enum):
    Exponential = ("Andamento esponenziale", exponential)
    Quadratic = ("Andamento quadratico", quadratic)

    def __init__(self, label: str, formula: callable):
        self.label = label
        self.formula = formula

class LCS(Enum):
    Recursive = ("Recursive", RecursiveLCS, 15)
    BruteForce = ("Brute Force", BruteForceLCS, 25)
    Memoization = ("Memoization", MemoizationLCS, 600)
    BottomUp = ("Bottom-Up", BottomUpLCS, 900)

    def __init__(self, label: str, clss: type, max_size: int):
        self.label = label
        self.clss = clss
        self.maxSizeAllowed = max_size