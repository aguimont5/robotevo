import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import random

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.frontleg_amp
        self.frequency = c.frontleg_freq
        self.offset = c.frontleg_offset
        # create sinuodusly varying values to send to motors
        self.targetAngles = np.linspace(0, 2 * np.pi, c.steps, dtype='float')
        #separate loops for front and back leg joints
        if str(self.jointName).find('Front') != -1:
            for i in range(c.steps):
                self.targetAngles[i] = self.amplitude * np.sin(
                        self.frequency * self.targetAngles[i] + self.offset)
        else:
            for i in range(c.steps):
                self.targetAngles[i] = self.amplitude * np.sin(
                        self.frequency/2 * self.targetAngles[i] + self.offset)

    def Set_Value(self, robot, t):
        # add motor to robot Torso_BackLeg
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot.robotId,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=random.uniform(self.targetAngles[t],
                                                                  self.targetAngles[t]),
                                    maxForce=c.max_force)

    def Save_Values(self):
        # save motor values to numpy file
        np.save(f'data/{self.jointName}SensorValues.npy', self.targetAngles)
