import ray
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
from ray.rllib.agents.sac import SACTrainer
from rock_walk.envs.rock_walk_env import RockWalkEnv
import ray
from ray import tune

if __name__ == "__main__":

    ellipse_params = [0.35, 0.35]
    apex_coordinates = [0, -0.35, 1.5]
    object_param = ellipse_params + apex_coordinates

    with open('training_objects_params.txt', 'w') as f:
        f.write("ellipse_a,ellipse_b,apex_x,apex_y,apex_z\n")
        f.write(str(0) + "," + str(0) + "," + str(0) + "," + str(0) + "," + str(0) + "\n")
        f.write(str(object_param[0]) + "," + str(object_param[1]) + "," + str(object_param[2]) + "," + str(
            object_param[3]) + "," + str(object_param[4]) + "\n")

    ray.init()

    config = ray.rllib.agents.sac.DEFAULT_CONFIG.copy()
    config.update({
            "framework": "torch",
            "env": RockWalkEnv,
            "rollout_fragment_length": 100,
            "learning_starts": 2000,
            "num_gpus": 0,
            "num_workers": 0,
            "env_config": {
                'bullet_connection': 1,
                'step_freq': 240,
                'frame_skip': 1,
                'isTrain': True
            }
    })

    trainer = SACTrainer(config=config)
    trainer.restore('./results/test_experiment/SAC_RockWalkEnv_1d353_00000_0_2021-07-31_01-53-58/checkpoint_000305/checkpoint-305')

    while True:
        trainer.step()

    # tune.run(
    #     "SAC",
    #     stop={"timesteps_total": 1e6},
    #     config=config,
    #     local_dir="./results",
    #     name="test_experiment",
    #     keep_checkpoints_num=10,
    #     checkpoint_freq=5,
    #     checkpoint_at_end=True,
    # )
