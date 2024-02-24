import pyrosim.pyrosim as pyrosim

# set L,W,H
length = 1.0
width = 1.0
height = 1.0

# position variables
x = 0.0
y=0.0
z=.5

def Generate_Body():
    # create robot body file
    pyrosim.Start_URDF("body.urdf")

    # create robot (absolute position)
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
    # create joint for robot torso <-> back leg (absolute position)
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1.0, 0, 1.0])
    # create back robot leg (relative position to Torso_BackLeg joint)
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[length, width, height])

    # create joint for robot torso <-> front leg (absolute position)
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2.0, 0, 1.0])
    # create robot front leg (relative position to Torso_FrontLeg joint)
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[length, width, height])

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
    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=1.0)

    # close robot
    pyrosim.End()


def Create_World():
    # open world in box.sdf
    pyrosim.Start_SDF("world.sdf")
    #create cube away from robot)
    pyrosim.Send_Cube(name="Box", pos=[x - 2, y + 2, z], size=[length, width, height])
    # close world
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()