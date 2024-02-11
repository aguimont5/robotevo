import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkname):
        self.values = np.zeros(c.steps)
        self.linkName = linkname

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #if t == c.steps:
            #print(self.values)

    def Save_Values(self):
        # save leg sensor values to numpy file
        np.save(f'data/{self.linkName}SensorValues.npy', self.values)
