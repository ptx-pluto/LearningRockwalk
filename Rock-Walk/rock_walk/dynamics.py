import pybullet
from rock_walk.pybullet_enum import *


class Dynamics(object):

    def __init__(self, body, link, client):
        self.body = body
        self.link = link
        self.client = client

    @property
    def lateral_friction(self):
        return pybullet.getDynamicsInfo(self.body, self.link, physicsClientId=self.client)[DYNAMICS_LATERAL_FRICTION]

    @lateral_friction.setter
    def lateral_friction(self, value):
        pybullet.changeDynamics(self.body, self.link, lateralFriction=value, physicsClientId=self.client)

    @property
    def rolling_friction(self):
        return pybullet.getDynamicsInfo(self.body, self.link, physicsClientId=self.client)[DYNAMICS_ROLLING_FRICTION]

    @rolling_friction.setter
    def rolling_friction(self, value):
        pybullet.changeDynamics(self.body, self.link, rollingFriction=value, physicsClientId=self.client)

    @property
    def spinning_friction(self):
        return pybullet.getDynamicsInfo(self.body, self.link, physicsClientId=self.client)[DYNAMICS_SPINNING_FRICTION]

    @spinning_friction.setter
    def spinning_friction(self, value):
        pybullet.changeDynamics(self.body, self.link, spinningFriction=value, physicsClientId=self.client)

    @property
    def contact_damping(self):
        return pybullet.getDynamicsInfo(self.body, self.link, physicsClientId=self.client)[DYNAMICS_CONTACT_DAMPING]

    @contact_damping.setter
    def contact_damping(self, value):
        pybullet.changeDynamics(self.body, self.link, contactDamping=value, physicsClientId=self.client)

    @property
    def contact_stiffness(self):
        return pybullet.getDynamicsInfo(self.body, self.link, physicsClientId=self.client)[DYNAMICS_CONTACT_STIFFNESS]

    @contact_stiffness.setter
    def contact_stiffness(self, value):
        pybullet.changeDynamics(self.body, self.link, contactStiffness=value, physicsClientId=self.client)

    @property
    def mass(self):
        return pybullet.getDynamicsInfo(self.body, self.link, physicsClientId=self.client)[DYNAMICS_MASS]

    @mass.setter
    def mass(self, value):
        pybullet.changeDynamics(self.body, self.link, mass=value, physicsClientId=self.client)
