import numpy as np
import matplotlib.pyplot as plt

# load sensor data
backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
frontLeg_MotorValues = np.load('data/FrontLeg_MotorValues.npy')
backLeg_MotorValues = np.load('data/BackLeg_MotorValues.npy')
# create plots
#plt.plot(backLegSensorValues, label='Back Leg', linewidth=2)
#plt.plot(frontLegSensorValues, label='Front Leg')
plt.plot(backLeg_MotorValues, label='Back Leg')
plt.plot(frontLeg_MotorValues, label='Front Leg')
# show plot
plt.legend()
plt.show()