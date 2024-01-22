import pyrosim.pyrosim as pyrosim

#open world in box.sdf
pyrosim.Start_SDF("box.sdf")

#create a 1m cube
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])

#close world
pyrosim.End()