import pyrosim.pyrosim as pyrosim
import pybullet as p
import sensor
import motor

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        # Adds robot to world
        self.robotId = p.loadURDF("body.urdf")
        # init sensors
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = sensor.SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = motor.MOTOR(jointName)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Act(self, t):
        for motor in self.motors:
            self.motors[motor].Set_Value(self, t)