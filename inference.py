from env import MiniGrid
from agent import get_action
from grader import grader

env = MiniGrid()

state = env.reset()

done = False
steps = 0
reached = False

while not done:
    action = get_action(state)
    state, done, info = env.step(action)
    steps += 1
    reached = info["reached"]

score = grader(reached, steps)

print("Final Score:", score)
