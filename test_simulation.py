import sys
import gym
import rock_walk
import numpy as np
from time import sleep

from pylsl import StreamInfo, StreamOutlet, local_clock

from joystick import Joystick


class DataStream:

    def __init__(self):
        self.info = StreamInfo('rnw_sim', 'data', 3, 100, 'float32', 'myuid34234')
        self.outlet = StreamOutlet(self.info)

    def send(self, data):
        self.outlet.push_sample(data)


if __name__ == "__main__":
    js = Joystick()
    stream = DataStream()
    sim_hz = 240
    env = gym.make("MotionControlRnw-v0", env_config={
        'bullet_connection': 1,
        'step_freq': sim_hz,
        'frame_skip': 1,
        'episode_timeout': 1000.
    })
    env.reset()
    while True:
        sleep(1./sim_hz)
        action = np.array([js.y, js.x, -js.z])
        obs, rewards, done, info = env.step(action)
        if done:
            env.reset()
