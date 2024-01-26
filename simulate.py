# load libraries
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t
import pybullet_data

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

# simulation loop
for i in range(0, 5000):
    # step simulation
    p.stepSimulation()
    # add touch sensor for back leg
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    t.sleep(1 / 60)
    print(i)

p.disconnect()
