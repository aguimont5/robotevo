import os
import parallelHillClimber

#for i in range(0,5):
#    os.system("python generate.py")
#    os.system("python simulate.py")
phc = parallelHillClimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()