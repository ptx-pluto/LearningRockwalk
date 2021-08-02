import os
import gym
import numpy as np
import rock_walk
import time
import pybullet as bullet
import matplotlib.pyplot as plt

from stable_baselines3 import TD3, SAC, PPO
from stable_baselines3.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback, CheckpointCallback, CallbackList
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize, VecVideoRecorder

from custom_callback import GenerateObjectCallback


if __name__ == "__main__":
    freq = 50
    frame_skip = 10

    ellipse_params = [0.35, 0.35]
    apex_coordinates = [0, -0.35, 1.5]
    object_param = ellipse_params + apex_coordinates

    with open('training_objects_params.txt', 'w') as f:
        f.write("ellipse_a,ellipse_b,apex_x,apex_y,apex_z\n")
        f.write(str(0) + "," + str(0) + "," + str(0) + "," + str(0) + "," + str(0) + "\n")
        f.write(str(object_param[0]) + "," + str(object_param[1]) + "," + str(object_param[2]) + "," + str(
            object_param[3]) + "," + str(object_param[4]) + "\n")

    env = gym.make("RockWalk-v0", bullet_connection=0, step_freq=freq, frame_skip=frame_skip, isTrain=True)
    env = Monitor(env, "./log")

    n_actions = env.action_space.shape[-1]
    action_noise = OrnsteinUhlenbeckActionNoise(mean=0 * np.ones(n_actions), sigma=1.5 * np.ones(n_actions))  # 5 prev
    # self._model.set_random_seed(seed=999)

    model = SAC("MlpPolicy",
                env,
                action_noise=action_noise,
                batch_size=128,
                train_freq=64,
                gradient_steps=64,
                learning_starts=20000,
                verbose=1,
                tensorboard_log="./rockwalk_tb/"
                )

    object_callback = GenerateObjectCallback(check_freq=1000000)

    checkpoint_callback = CheckpointCallback(save_freq=20000, save_path='./save/', name_prefix='rw_model')

    callback_list = CallbackList([object_callback, checkpoint_callback])

    model.learn(total_timesteps=500000, log_interval=10, callback=callback_list)
    model.save_replay_buffer('./save/buffer')
    env.close()

