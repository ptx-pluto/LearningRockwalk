import pybullet
import os

from rock_walk.dynamics import Dynamics


class Plane:
    def __init__(self, client):
        pybullet.setAdditionalSearchPath(
            os.path.join(os.path.dirname(__file__), 'models')
        )
        self.clientID = client
        self.bodyID = pybullet.loadURDF(
            'plane.urdf',
            [0, 0, 0],
            physicsClientId=self.clientID
        )
        self.textureID = pybullet.loadTexture('checker_blue.png')
        pybullet.changeVisualShape(self.bodyID, -1, textureUniqueId=self.textureID, physicsClientId=self.clientID)
        self.dynamics = Dynamics(self.bodyID, -1, self.clientID)
