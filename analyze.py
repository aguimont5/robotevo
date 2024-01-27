import numpy as np
import matplotlib.pyplot as plt

# load sensor data
backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
# create plots
plt.plot(backLegSensorValues, label='Back Leg', linewidth=2)
plt.plot(frontLegSensorValues, label='Front Leg')
# show plot
plt.legend()
plt.show()