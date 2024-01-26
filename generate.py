import pyrosim.pyrosim as pyrosim

# open world in box.sdf
pyrosim.Start_SDF("world.sdf")

# set L,W,H
length = 1.0
width = 1.0
height = 1.0

# position variables
x = 0.0
y=0.0
z=.5

#create one box at the origin
pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

# close world
pyrosim.End()
