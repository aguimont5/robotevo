import pyrosim.pyrosim as pyrosim

# set L,W,H
length = 1.0
width = 1.0
height = 1.0

# position variables
x = 0.0
y=0.0
z=.5

def Create_Robot():
    # create robot body file
    pyrosim.Start_URDF("body.urdf")

    # create robot torso
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, .5], size=[length, width, height])
    #create joint for robot torso <-> leg
    pyrosim.Send_Joint(name="Torso_Leg1", parent="Torso", child="Leg1", type="revolute", position=[0, 0, 1.0])
    # create robot leg
    pyrosim.Send_Cube(name="Leg1", pos=[0.0, 0, .5], size=[length, width, height])

    #second joint
    pyrosim.Send_Joint(name="Leg1_Leg2", parent="Leg1", child="Leg2", type="revolute", position=[0, 0, 1.0])
    #second leg
    pyrosim.Send_Cube(name="Leg2", pos=[0.0, 0, .5], size=[length, width, height])

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
Create_Robot()