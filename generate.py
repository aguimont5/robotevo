import pyrosim.pyrosim as pyrosim

# open world in box.sdf
pyrosim.Start_SDF("boxes.sdf")

# set L,W,H
length = 1.0
width = 1.0
height = 1.0

# position variables
x = 0.0
y=0.0
z=.5

# creates twenty five towers
for row in range(0,5):
    for col in range(0,5):
        for i in range(0,10):
            pyrosim.Send_Cube(name="Box2", pos=[x+row, y+col, z + i], size=[length*(.9**i), width*(.9**i), height*(.9**i)])

# close world
pyrosim.End()
