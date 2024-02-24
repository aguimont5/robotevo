import numpy as np

# simulation vars
steps = 1200
sim_speed = 1/60

# gravity
grav_x = 0
grav_y = 0
grav_acc = -9.8

# motors
max_force = 500

frontleg_amp = np.pi/4
frontleg_freq = 16
frontleg_offset = 0

backleg_amp = np.pi/4
backleg_freq = 8
backleg_offset = 0