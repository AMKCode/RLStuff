import gym
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
import numpy as np
import random
import os
import stable_baselines3
from stable_baselines3 import SAC, PPO, DQN, A2C, TD3
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy
import numpy as np
import matplotlib.pyplot as plt

from env_file3 import sine_wave_env

env = sine_wave_env()

log_path = os.path.join('Training', 'Logs')
model = SAC('MlpPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=1000)

plt.axis([-12, 12, -1.5, 1.5])

episodes = 2
for episode in range(1, episodes + 1):
    obs = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action, _ = model.predict(np.array(obs))
        obs, reward, done, info = env.step(action)
        score += reward
    print('Episode:{}, score: {}'.format(episode, score))

plt.show()
env.close()

# save_sine_model = os.path.join('Training', 'Saved Models', 'sine_Model_PPO')
# model.save(save_sine_model)

