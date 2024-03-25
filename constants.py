import numpy as np

# set L,W,H
length = 1.0
width = 1.0
height = 1.0

# position variables
x = 0.0
y=0.0
z=.5

# simulation vars
steps = 600
sim_speed = 1/60
number_of_generations = 10
populationSize = 2

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

sensors = ['Torso', 'BackLeg', 'FrontLeg']
motors = ['Torso_BackLeg', 'Torso_FrontLeg']