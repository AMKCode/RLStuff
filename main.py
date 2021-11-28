import gym
import pygame
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

from maze import Player
from control import maze

env = maze()

episodes = 2

log_path = os.path.join('Training', 'Logs')
model = A2C('MlpPolicy', env, verbose=1, tensorboard_log=log_path)

model.learn(total_timesteps=50000)

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

pygame.quit()
env.close()

