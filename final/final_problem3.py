import random
# helper function


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


def guessfood_sim(num_trials, probs, cost, get):
    """
    num_trials: integer, number of trials to run
    probs: list of probabilities of guessing correctly for 
           the ith food, in each trial
    cost: float, how much to pay for each food guess
    get: float, how much you get for a correct guess

    Runs a Monte Carlo simulation, 'num_trials' times. In each trial 
    you guess what each food is, the ith food has 'prob[i]' probability 
    to get it right. For every food you guess, you pay 'cost' dollars.
    If you guess correctly, you get 'get' dollars. 

    Returns: a tuple of the mean and standard deviation over 
    'num_trials' trials of the net money earned 
    when making len(probs) guesses
    """

    result = []
    for _ in range(num_trials):
        earned = 0
        for i in range(len(probs)):
            guessed = random.random() <= probs[i]
            if guessed:
                earned += get
            earned -= cost
        result.append(earned)
    return getMeanAndStd(result)


print("###################")
print(guessfood_sim(100, [1, 1, 1], 1, 0))
