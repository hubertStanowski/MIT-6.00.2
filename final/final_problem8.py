import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300


def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    for _ in range(CURRENTRABBITPOP):
        if CURRENTRABBITPOP < 10 or CURRENTRABBITPOP >= MAXRABBITPOP:
            return

        prob = 1 - (CURRENTRABBITPOP / MAXRABBITPOP)
        birth = random.random() <= prob
        if birth:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for _ in range(CURRENTFOXPOP):
        if CURRENTFOXPOP < 10:
            return

        prob = CURRENTRABBITPOP / MAXRABBITPOP
        eats = random.random() <= prob

        if eats and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            prob = 1 / 3
            birth = random.random() <= prob
            if birth:
                CURRENTFOXPOP += 1
        else:
            # PART A
            #prob = 1 / 10
            # PART B
            prob = 9 / 10
            dies = random.random() <= prob
            if dies and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations, fox_populations = [x for x in range(numSteps)], [
        x for x in range(numSteps)]
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations[i] = CURRENTRABBITPOP
        fox_populations[i] = CURRENTFOXPOP

    return rabbit_populations, fox_populations


numSteps = 1000
rabbit_populations, fox_populations = runSimulation(numSteps)
time = [y for y in range(numSteps)]
pylab.figure()

pylab.plot(time, rabbit_populations, "bo")
pylab.plot(time, fox_populations,  "r")
pylab.xlabel("time")

coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbit_populations))))

coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
pylab.plot(pylab.polyval(coeff, range(len(fox_populations))))
pylab.show()
