from fastapi import FastAPI
from env import MiniGrid

app = FastAPI()
env = MiniGrid()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: int):
    state, done, info = env.step(action)
    return {
        "state": state,
        "done": done, 
        "info": info
    }