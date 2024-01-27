import numpy as np
import matplotlib.pyplot as plt

# load sensor data
backLegSensorValues = np.load('data/backLegSensorValues.npy')
# create plot
plt.plot(backLegSensorValues)
# show plot
print(plt.show())