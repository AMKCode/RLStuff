from maze import *
import time
import numpy as np
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete

class maze(Env):
    def __init__(self):
        self.action_space = Discrete(4) # 4 directions, 0=up, 1=down, 2=left, 3=right
        self.observation_space = Box(0, 23, shape=(2,)) # the maximum distance is 22.627 steps, we use 1 step = 16 pixels
        self.state = np.array([2, 2]) # the starting position is 32, 32, but we use 2, 2 here
        self.num_steps = 0 # we set a maximum step as 20
        self.prev_pos = [] # the list with previous positions

    def step(self, action):
        last_distance = ((self.state[0]*16)**2 + (self.state[1]*16)**2)**0.5
        append_to_list = True

        for pos in self.prev_pos:
            if pos[0] == (self.state[0]*16) and pos[1] == (self.state[1]*16):
                append_to_list = False

        if append_to_list:
            self.prev_pos.append([self.state[0]*16, self.state[1]*16])

        if action == 0:
            player.move(0, -16)
        elif action == 1:
            player.move(0, 16)
        elif action == 2:
            player.move(-16, 0)
        else:
            player.move(16, 0)

        # update the states
        self.state[0] = player.rect.x / 16
        self.state[1] = player.rect.y / 16

        curr_distance = ((self.state[0]*16)**2 + (self.state[1]*16)**2)**0.5

        # reward function
        is_repeat = False
        for pos in self.prev_pos:
            if pos[0] == (self.state[0]*16) and pos[1] == (self.state[1]*16):
                is_repeat = True

        if is_repeat:
            reward = -5;
            self.num_steps += 1
        else:
            if curr_distance == 0:
                reward = 100
                self.num_steps = 20
            elif curr_distance > last_distance:
                reward = -2
                self.num_steps += 1
            elif curr_distance < last_distance:
                reward = 1
                self.num_steps += 1
            elif curr_distance == last_distance:
                reward = -2
                self.num_steps += 1

        # # reward function
        # if curr_distance == 0:
        #     reward = 100
        #     self.num_steps = 20
        # elif curr_distance > last_distance:
        #     reward = -5
        #     self.num_steps += 1
        # elif curr_distance < last_distance:
        #     reward = -1
        #     self.num_steps += 1
        # elif curr_distance == last_distance:
        #     reward = -3
        #     self.num_steps += 1

        if self.num_steps == 20:
            done = True
        else:
            done = False

        info = {}

        return self.state, reward, done, info

    def render(self):
        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
        pygame.display.flip()
        time.sleep(1)

        # pygame.quit()

    def reset(self):
        self.state = np.array([2, 2])
        self.num_steps = 0
        return self.state



