import pybullet as p
import pyrosim.pyrosim as pyrosim
class WORLD:
    def __init__(self):
        # Adds a plane to serve as the floor
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")