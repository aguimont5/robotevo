import numpy as np

# simulation vars
steps = 1000
sim_speed = 1/45

# gravity
grav_x = 0
grav_y = 0
grav_acc = -9.8

# motors
max_force = 500

frontleg_amp = np.pi/12
frontleg_freq = 10
frontleg_offset = 0

backleg_amp = np.pi/12
backleg_freq = 2
backleg_offset = 0