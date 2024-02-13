import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import random

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName


    def Set_Value(self, robot, desiredAngle):
        # add motor to robot Torso_BackLeg
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot.robotId,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=random.uniform(desiredAngle,
                                                                  desiredAngle),
                                    maxForce=c.max_force)

