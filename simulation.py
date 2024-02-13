from world import WORLD
from robot import ROBOT
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c
import time as t
import random
class SIMULATION:
    def __init__(self):
        # create physics client
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # Adds gravity
        p.setGravity(c.grav_x, c.grav_y, c.grav_acc)

        self.world = WORLD()
        self.robot = ROBOT()

        self.Run()


    def __del__(self):
        p.disconnect()

    def Run(self):
        # simulation loop
        for i in range(0, c.steps):
            # step simulation
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            t.sleep(c.sim_speed)
