import numpy as np

# --- building the grip map env ---
rows = 6
col = 6

walls = {(1,1),(1,5),(2,1),(3,1),(4,4)}
green_states = {(0,5), (2,5), (3,4), (4,3), (2,2)}
brown_states = {(1,4), (2,3), (3,2), (4,1), (5,4)}

# --- actions available to move around the map ---
actions = ['Up', 'Down', 'Left', 'Right']

reward_map = {
    'white' : -0.05,
    'green' : 1.0,
    'brown' : -1.0
}

states = []
for r in range(rows):
    for c in range(col):
        if (r,c) not in walls:
            states.append((r,c))

def get_reward(state):
    if state in green_states:
        return 1.0
    elif state in brown_states:
        return -1.0
    else:
        return -0.05
    
def move(state, action):
    r, c = state

    if action == 'Up':
        nr, nc = r - 1, c
    elif action == "Down":
        nr, nc = r + 1, c
    elif action == "Left":
        nr, nc = r, c - 1
    elif action == "Right":
        nr, nc = r,  c + 1
    
    if nr < 0 or nr >= rows or nc < 0 or nc >= col or (nr, nc) in walls:
        return state
    
    return (nr, nc)

def get_transitions(state, action):
    if action == "Up":
        candidates = [('Up', 0.8), ("Left", 0.1), ("Right", 0.1)]
    elif action == "Down":
        candidates = [("Down", 0.8), ("Left", 0.1), ("Right", 0.1)]
    elif action == "Left":
        candidates = [("Left", 0.8), ("Up", 0.1), ("Down", 0.1)]
    elif action == "Right":
        candidates = [("Right", 0.8), ("Up", 0.1), ("Down", 0.1)]

    transitions = []
    for a, prob in candidates:
        next_state = move(state, a)
        transitions.append((prob, next_state))

    return transitions

