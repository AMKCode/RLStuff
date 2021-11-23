from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
import matplotlib.pyplot as plt
import math
import numpy as np
import random


class sine_wave_env(Env):
    def __init__(self):
        self.action_space = Box(-10.0, 10.0, shape=(2,))
        self.observation_space = Box(-10.0, 10.0, shape=[2,])
        x = random.uniform(-10, 10)
        y = math.sin(x)
        self.state = np.array([x,y])
        self.num_points = 0

    def step(self, action):
        self.state = action

        self.num_points += 1

        if abs((self.state[1] / 10) - math.sin(self.state[0])) < 0.1:
            reward = 1
        else:
            reward = -1

        if self.num_points >= 100:
            done = True
        else:
            done = False

        info = {}

        return self.state, reward, done, info

    def render(self):
        plt.scatter(self.state[0], (self.state[1] / 10))

    def reset(self):
        x = random.uniform(-10, 10)
        y = math.sin(x)
        self.state = np.array([x, y])
        self.num_points = 0
        return self.state
