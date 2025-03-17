from enum import Enum

from algorithms.recursive_LCS import RecursiveLCS
from algorithms.brute_force_LCS import BruteForceLCS
from algorithms.memoization_LCS import MemoizationLCS
from algorithms.bottom_up_LCS import BottomUpLCS

class LCS(Enum):
    Recursive = RecursiveLCS
    BruteForce = BruteForceLCS
    Memoization = MemoizationLCS
    BottomUp = BottomUpLCS  

 