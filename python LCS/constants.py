from enum import Enum
import numpy as np
from scipy.optimize import curve_fit

from algorithms.recursive_LCS import RecursiveLCS
from algorithms.brute_force_LCS import BruteForceLCS
from algorithms.memoization_LCS import MemoizationLCS
from algorithms.bottom_up_LCS import BottomUpLCS

# Funzione esponenziale personalizzata per uso teorico o di fitting
def exponential(x):
    """
    Funzione esponenziale modificata, usata come riferimento teorico.

    Args:
        x: Valori dell'asse x.

    Returns:
        Valori calcolati con la funzione esponenziale.
    """
    return (2 ** x) * np.power(np.e, -13)

# Funzione quadratica personalizzata per uso teorico o di fitting
def quadratic(x):
    """
    Funzione quadratica modificata, usata come riferimento teorico.

    Args:
        x: Valori dell'asse x.

    Returns:
        Valori calcolati con la funzione quadratica.
    """
    return (x ** 2) * np.power(np.e, -15)

# Enum per rappresentare funzioni teoriche con etichetta e formula associata
class Functions(Enum):
    """
    Enum per le funzioni teoriche di riferimento (esponenziale, quadratica).
    Ogni elemento ha una label e una funzione matematica associata.
    """
    Exponential = ("Andamento esponenziale", exponential)
    Quadratic = ("Andamento quadratico", quadratic)

    def __init__(self, label: str, formula: callable):
        self.label = label
        self.formula = formula

# Enum per rappresentare gli algoritmi LCS con metadati utili (etichetta, classe, dimensione massima, colore)
class LCS(Enum):
    """
    Enum per i vari algoritmi LCS testabili.
    Ogni elemento ha:
        - label: nome descrittivo
        - clss: classe dell'algoritmo
        - maxSizeAllowed: dimensione massima gestibile
        - color: colore associato per i grafici
    """
    Recursive = ("Recursive", RecursiveLCS, 13, "b")
    BruteForce = ("Brute Force", BruteForceLCS, 19, "m")
    Memoization = ("Memoization", MemoizationLCS, 1000, "g")
    BottomUp = ("Bottom-Up", BottomUpLCS, 2000, "c")

    def __init__(self, label: str, clss: type, max_size: int, color: str):
        self.label = label
        self.clss = clss
        self.maxSizeAllowed = max_size
        self.color = color

# Funzione generica quadratica da usare per il fitting
def quadratic_function(x, a, b, c):
    """
    Funzione quadratica generica usata per il curve fitting.

    Args:
        x: Dati indipendenti.
        a, b, c: Parametri della funzione.

    Returns:
        Risultato della funzione quadratica.
    """
    return a * np.power(x, 2) + b * x + c

# Funzione generica esponenziale da usare per il fitting
def exponential_function(x, a, b, c):
    """
    Funzione esponenziale generica usata per il curve fitting.

    Args:
        x: Dati indipendenti.
        a, b, c: Parametri della funzione.

    Returns:
        Risultato della funzione esponenziale.
    """
    return a * np.exp(b * x) + c

# Funzione per eseguire il fitting dei dati x, y secondo il tipo di algoritmo LCS
def fit_function(x, y, alg):
    """
    Esegue il fitting dei dati y rispetto a x usando la funzione appropriata
    (esponenziale o quadratica) in base all'algoritmo LCS.

    Args:
        x: Dati sull'asse x (dimensioni delle stringhe).
        y: Tempi osservati corrispondenti.
        alg: Algoritmo LCS da cui determinare la funzione da usare.

    Returns:
        Lista di valori fitted della stessa lunghezza di y, con NaN dove non è stato possibile fit.
    """
    # Seleziona la funzione di fitting in base all'algoritmo
    if alg == LCS.Recursive or alg == LCS.BruteForce:
        func = exponential_function
    elif alg == LCS.Memoization or  alg == LCS.BottomUp:
        func = quadratic_function
    else:
        raise ValueError("Funzione di fitting non supportata")

    # Considera solo la parte di y senza NaN
    valid_length = np.argmax(np.isnan(y)) if np.isnan(y).any() else len(y)
    x_valid = x[:valid_length]
    y_valid = y[:valid_length]

    # Esegue il fitting con vincoli sui parametri
    bounds = ([0, 0, 0], [np.inf, np.inf, np.inf])
    popt, _ = curve_fit(func, x_valid, y_valid, maxfev=10000, bounds=bounds)

    # Calcola i valori previsti dalla funzione fitted
    y_fit_valid = func(x_valid, *popt)

    # Riempie il resto dell'array con NaN per mantenere la lunghezza originale
    nan_tail = [np.nan] * (len(y) - valid_length)
    y_fit_full = np.concatenate([y_fit_valid, nan_tail])

    return y_fit_full
