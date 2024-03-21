import solution
import pyrosim.pyrosim as pyrosim
import constants
import random

class HILL_CLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()

    def Evolve(self):
        self.parent.Evalute()

