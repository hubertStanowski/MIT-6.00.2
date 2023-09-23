def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    remainder = s
    x1 = remainder // 25
    remainder -= 25 * x1
    x2 = remainder // 10
    remainder -= 10 * x2
    x3 = remainder // 5
    remainder -= 5 * x3
    x4 = remainder

    return [x1, x2, x3, x4]


print(solve(1))
