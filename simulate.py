# load libraries
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

p.loadSDF("boxes.sdf")

# simulation loop
for i in range(0, 5000):
    p.stepSimulation()
    t.sleep(1 / 60)
    print(i)

p.disconnect()
