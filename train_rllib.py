import ray
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
from ray.rllib.agents.sac import SACTrainer
from rock_walk.envs.motion_control_rnw_env import MotionControlRnwEnv


if __name__ == "__main__":
    ray.init()  # Skip or set to ignore if already called
    config = {
        "framework": "torch",
        'simple_optimizer': True,
        # 'gamma': 0.9,
        # 'lr': 1e-2,
        'num_workers': 4,
        # 'train_batch_size': 1000,
        #'model': {'fcnet_hiddens': [128, 128]}
    }
    trainer = SACTrainer(env=MotionControlRnwEnv, config=config)
    results = trainer.train()
    print(results)
    #tune.run(PPOTrainer, config={"env": , })
