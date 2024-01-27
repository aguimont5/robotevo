# load libraries
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t
import pybullet_data
import numpy as np

# create physics client
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Adds gravity
p.setGravity(0, 0, -9.8)

# Adds a plane to serve as the floor
planeId = p.loadURDF("plane.urdf")

# Adds robot to world
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

# init sensors
pyrosim.Prepare_To_Simulate(robotId)

# creating leg sensors
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

# simulation loop
for i in range(0, 1000):
    # step simulation
    p.stepSimulation()
    # add touch sensor for back leg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    t.sleep(1 / 60)
    #print(backLegSensorValues)

# save leg sensor values to numpy file
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()
