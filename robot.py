import pyrosim.pyrosim as pyrosim
import pybullet as p
import sensor
import motor
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.nn = NEURAL_NETWORK("brain.nndf")
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
            joint = str(jointName).lstrip("'b").rstrip("'")
            self.motors[joint] = motor.MOTOR(jointName)

    def Sense(self, t):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(t)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self, desiredAngle)
                print(neuronName + ',' + jointName + '  val = ' + str(desiredAngle))

        #for motor in self.motors:
            #self.motors[motor].Set_Value(self, t)