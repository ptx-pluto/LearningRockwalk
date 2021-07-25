from gym.envs.registration import register

register(
    id='RockWalk-v0',
    entry_point='rock_walk.envs:RockWalkEnv'
)

register(
    id='CableRockWalk-v0',
    entry_point='rock_walk.envs:RnwSingleCableEnv'
)

register(
    id='MotionControlRnw-v0',
    entry_point='rock_walk.envs:MotionControlRnwEnv'
)
