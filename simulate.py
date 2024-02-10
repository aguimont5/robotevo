# load libraries
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet as p
import time as t
import pybullet_data
import numpy as np
import random

# create physics client
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Adds gravity
p.setGravity(c.GRAVITY_X, c.GRAVITY_Y, c.GRAVITY_A)

# Adds a plane to serve as the floor
planeId = p.loadURDF("plane.urdf")

# Adds robot to world
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

# init sensors
pyrosim.Prepare_To_Simulate(robotId)

# creating array to hold sensor values
backLegSensorValues = np.zeros(c.STEPS)
frontLegSensorValues = np.zeros(c.STEPS)

#create sinuodusly varying values to send to motors
frontLeg_targetAngles = np.linspace(0, 2*np.pi, c.STEPS, dtype='float')
for i in range(c.STEPS):
    frontLeg_targetAngles[i] = c.FRONTLEG_AMP * np.sin(c.FRONTLEG_FREQ * frontLeg_targetAngles[i] + c.FRONTLEG_OFFSET)

backLeg_targetAngles = np.linspace(0, 2*np.pi, c.STEPS, dtype='float')
for i in range(c.STEPS):
    backLeg_targetAngles[i] = c.BACKLEG_AMP * np.sin(c.BACKLEG_FREQ * backLeg_targetAngles[i] + c.BACKLEG_OFFSET)


# simulation loop
for i in range(0, c.STEPS):
    # step simulation
    p.stepSimulation()

    # add touch sensor for back leg
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # add motor to robot Torso_BackLeg
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName=b'Torso_BackLeg',
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=random.uniform(backLeg_targetAngles[i],
                                                              backLeg_targetAngles[i]),
                                maxForce=c.MAX_FORCE)
    # add motor to robot Torso_FrontLeg
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName=b'Torso_FrontLeg',
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=random.uniform(frontLeg_targetAngles[i],
                                                              frontLeg_targetAngles[i]),
                                maxForce=c.MAX_FORCE)
    t.sleep(c.SIM_SPEED)
    #print(backLegSensorValues)

# save leg sensor values to numpy file
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

#save motor values to np file
np.save('data/FrontLeg_MotorValues.npy', frontLeg_targetAngles)
np.save('data/BackLeg_MotorValues.npy', backLeg_targetAngles)

p.disconnect()
