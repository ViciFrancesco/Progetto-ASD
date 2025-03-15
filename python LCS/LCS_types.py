from enum import Enum

from algorithms.recursive_LCS import RecursiveLCS
from algorithms.brute_force_LCS import BruteForceLCS
from algorithms.memoization_LCS import MemoizationLCS

class LCS(Enum):
    Recursive = RecursiveLCS
    BruteForce = BruteForceLCS
    Memoization = MemoizationLCS
    BottomUp = None  