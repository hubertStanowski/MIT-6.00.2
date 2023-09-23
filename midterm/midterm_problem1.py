def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """

    remainder = s
    multi = []
    idx = 0
    while remainder != 0 and idx < len(L):
        m = 0
        while L[idx] * (m+1) <= remainder:
            m += 1

        remainder -= L[idx] * m
        multi.append(m)
        idx += 1

    if remainder == 0:
        return sum(multi)
    else:
        return "no solution"


print(greedySum([10, 5, 1], 14))
