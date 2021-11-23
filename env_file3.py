from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
import matplotlib.pyplot as plt
import math
import numpy as np


class sine_wave_env(Env):
    def __init__(self):
        self.action_space = Box(-1, 1, shape=(1,))
        self.observation_space = Box(-10, 10.0, shape=[2,])
        self.state = np.array([-10, math.sin(-10)])
        self.num_points = 0

    def step(self, action):
        x = self.state[0] + 0.1
        self.state = np.array([x, action[0]])

        self.num_points += 1

        if abs((self.state[1]) - math.sin(self.state[0])) < 0.1:
            reward = 1
        else:
            reward = -1

        if self.num_points >= 200:
            done = True
        else:
            done = False

        info = {}

        return self.state, reward, done, info

    def render(self):
        plt.scatter(self.state[0], self.state[1])

    def reset(self):
        self.state = np.array([-10, math.sin(-10)])
        self.num_points = 0
        return self.state
