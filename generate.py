import constants
import pyrosim.pyrosim as pyrosim
import random



def Generate_Body():
    # create robot body file
    pyrosim.Start_URDF("body.urdf")

    # create robot (absolute position)
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[constants.length, constants.width, constants.height])
    # create joint for robot torso <-> back leg (absolute position)
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1.0, 0, 1.0])
    # create back robot leg (relative position to Torso_BackLeg joint)
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[constants.length, constants.width, constants.height])

    # create joint for robot torso <-> front leg (absolute position)
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2.0, 0, 1.0])
    # create robot front leg (relative position to Torso_FrontLeg joint)
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[constants.length, constants.width, constants.height])

    # close robot
    pyrosim.End()

def Generate_Brain():
    # create robot brain file
    pyrosim.Start_NeuralNetwork("brain.nndf")


    # create sensor neurons
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    # create motor neurons
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    # create synapses
    for sensor in range(0,3):
        for motor in range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=motor, weight=random.uniform(-1,1))

    # torso sensor -> torso_backleg motor
    #pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=0)


    # close robot
    pyrosim.End()


def Create_World():
    # open world in box.sdf
    pyrosim.Start_SDF("world.sdf")
    #create cube away from robot)
    #pyrosim.Send_Cube(name="Box", pos=[x - 2, y + 2, z], size=[constants.length, constants.width, constants.height])
    # close world
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()