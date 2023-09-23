import numpy as np
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    result = []
    current = [0 for i in range(len(choices))]
    sumCurrent = 0
    for i in range(len(choices)):
        if sumCurrent + choices[i] <= total:
            current[i] = 1
            sumCurrent += choices[i]
        if sumCurrent == total:
            return np.array(current)

    return np.array(current)


print(find_combination([1, 1, 1, 9], 5))

# GREEDY 16/20
