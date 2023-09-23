import random
import pylab

# You are given this function


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class


class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.figure()
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO

    trials = []
    for _ in range(numTrials):
        rolls = []
        for i in range(numRolls):
            rolls.append(die.roll())
        longest, current = 0, 0
        for i in range(numRolls):
            try:
                if rolls[i] == rolls[i-1]:
                    current += 1

                else:
                    if current > longest:
                        longest = current
                    current = 1
            except IndexError:
                pass
            # print(current)
        if current > longest:
            longest = current
        trials.append(longest)

   # print(trials)
    mean, std = getMeanAndStd(trials)
    makeHistogram(trials, 10, "TrialNumber", "Longest", "PROBLEM 4")
    return round(mean, 3)


print(getAverage(Die([1]), 10, 1000))
