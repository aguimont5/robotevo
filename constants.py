import numpy as np

# simulation vars
STEPS = 1000
SIM_SPEED = 1/60

# gravity
GRAVITY_X = 0
GRAVITY_Y = 0
GRAVITY_A = -9.8

# motors
MAX_FORCE = 500

FRONTLEG_AMP = np.pi/12
FRONTLEG_FREQ = 12
FRONTLEG_OFFSET = 0

BACKLEG_AMP = np.pi/24
BACKLEG_FREQ = 2
BACKLEG_OFFSET = np.pi/2