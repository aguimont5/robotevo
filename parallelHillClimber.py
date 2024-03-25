import solution
import pyrosim.pyrosim as pyrosim
import constants
import random
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        for parent in range(0,constants.populationSize):
            self.parents[parent] = solution.SOLUTION()
        self.child = solution.SOLUTION()


    def Evolve(self):
        #self.Show_Best()
        #for currentGeneration in range(0,constants.number_of_generations):
        #    self.Evolve_For_One_Generation()
        #self.Show_Best()
        for parent in range(0, constants.populationSize):
            self.parents[parent].Evaluate('GUI')
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate('DIRECT')
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child

    def Print(self):
        print("\nC: "+ str(self.parent.fitness) + "  P: " + str(self.child.fitness))

    def Show_Best(self):
        self.parent.Evaluate('GUI')