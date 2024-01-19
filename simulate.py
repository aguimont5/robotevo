#load libraries
import pybullet as p
import time as t

#create physics client
physicsClient = p.connect(p.GUI)

#simulation loop
for i in range(0,1000):
    p.stepSimulation()
    t.sleep(1/60)
    print(i)

p.disconnect()