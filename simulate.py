# load libraries
import pyrosim.pyrosim as pyrosim
import pybullet as p
import time as t
import pybullet_data
import numpy as np
import random

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

# init motor variables
frontLeg_amplitude = np.pi/12
frontLeg_frequency = 12
frontLeg_phaseOffset = 0

backLeg_amplitude = np.pi/24
backLeg_frequency = 2
backLeg_phaseOffset = np.pi/2


# creating array to hold sensor values
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

#create sinuodusly varying values to send to motors
frontLeg_targetAngles = np.linspace(0, 2*np.pi, 1000, dtype='float')
for i in range(1000):
    frontLeg_targetAngles[i] = frontLeg_amplitude * np.sin(frontLeg_frequency * frontLeg_targetAngles[i] + frontLeg_phaseOffset)

backLeg_targetAngles = np.linspace(0, 2*np.pi, 1000, dtype='float')
for i in range(1000):
    backLeg_targetAngles[i] = backLeg_amplitude * np.sin(backLeg_frequency * backLeg_targetAngles[i] + backLeg_phaseOffset)


# simulation loop
for i in range(0, 1000):
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
                                maxForce=500)
    # add motor to robot Torso_FrontLeg
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId,
                                jointName=b'Torso_FrontLeg',
                                controlMode=p.POSITION_CONTROL,
                                targetPosition=random.uniform(frontLeg_targetAngles[i],
                                                              frontLeg_targetAngles[i]),
                                maxForce=500)
    t.sleep(1 / 60)
    #print(backLegSensorValues)

# save leg sensor values to numpy file
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)

#save motor values to np file
np.save('data/FrontLeg_MotorValues.npy', frontLeg_targetAngles)
np.save('data/BackLeg_MotorValues.npy', backLeg_targetAngles)

p.disconnect()
