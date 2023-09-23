def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """

    # IMPLEMENT THIS FUNCTION
    range = -100
    results = []
    while x <= abs(range):

        try:
            if test(x) == True:
                results.append(x)
        except:
            pass
        x += 1

    results.sort(key=abs)
    if len(results) > 1:
        if abs(results[0]) == abs(results[1]):
            return abs(results[0])
    return results[0]


def f(x):
    return x**2 + x + 0 == 0


print(solveit(f))
