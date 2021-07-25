import os
import pybullet as bullet
import numpy as np


class Cargo:

    def __init__(self, client):
        bullet.setAdditionalSearchPath(
            os.path.join(os.path.dirname(__file__), 'models')
        )
        self.clientID = client
        self.coneID = bullet.loadURDF(
            fileName='large_cone.urdf',
            basePosition=[0, 0, 1],
            baseOrientation=bullet.getQuaternionFromEuler([0, 0, 0]),
            physicsClientId=client
        )

    def get_dynamics_info(self):
        print(bullet.getDynamicsInfo(self.coneID, -1, physicsClientId=self.clientID))

    def set_lateral_friction(self, value):
        bullet.changeDynamics(self.coneID, -1, lateralFriction=value, physicsClientId=self.clientID)

    def get_observation(self):
        pass