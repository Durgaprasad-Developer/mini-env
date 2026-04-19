import random

class MiniGrid:
    def __init__(self, size=5):
        self.size = size

    def reset(self):
        self.agent = [0,0]
        self.goal = [self.size-1, self.size-1]
        self.step = 0
        return self.state
    
    def state(self):
        return {
            "agent": self.agent,
            "goal": self.goal
        }
    
    def step(self, action):
        if action == 0: self.agent[0] -= 1
        if action == 1: self.agent[0] += 1
        if action == 2: self.agent[1] -= 1
        if action == 3: self.agent[1] += 1

        self.steps += 1

        reached = self.agent == self.goal
        done = reached or self.steps > 20

        return self.state(), done, {"reached": reached}