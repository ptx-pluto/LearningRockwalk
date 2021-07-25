import pybullet
import os


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

    @property
    def lateral_friction(self):
        return pybullet.getDynamicsInfo(self.bodyID, -1, physicsClientId=self.clientID)[1]

    @lateral_friction.setter
    def lateral_friction(self, value):
        pybullet.changeDynamics(self.bodyID, -1, lateralFriction=value, physicsClientId=self.clientID)