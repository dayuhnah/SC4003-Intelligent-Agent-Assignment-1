import numpy as np

rows = 12
cols = 12

walls = {
    (0, 5), (0, 6), (1, 2), (1, 8),
    (2, 2), (2, 5), (2, 6), (2, 9),
    (3, 2), (3, 9), (4, 4), (4, 5),
    (4, 7), (4, 8), (5, 0), (5, 1),
    (5, 4), (5, 7), (6, 4), (6, 7),
    (6, 10), (6, 11),(7, 1), (7, 2),
    (7, 7), (8, 4), (8, 5), (8, 8),
    (8, 9), (9, 2), (9, 6), (10, 6),
    (10, 9), (11, 3), (11, 4)}

green_states = {
    (0, 0), (0, 11), (2, 4), (2, 11),
    (4, 0),(4, 10), (6, 2),(6, 6),
    (8, 0), (8, 11), (10, 4), (10, 11)
}

brown_states = {
    (0, 3), (0, 9), (3, 5), (3, 7),
    (5, 6), (5, 9),(7, 4), (7, 9),
    (9, 4), (9, 9), (11, 7), (11, 10)
}

assert not (green_states & brown_states), "Overlap green brown"
assert not (green_states & walls), "Overlap green wall"
assert not (brown_states & walls), "Overlap brown wall"

start_state = (5, 5)

# --- actions available to move around the map ---
actions = ['Up', 'Down', 'Left', 'Right']

# --- reward given for states ---
reward_map = {
    'white' : -0.05,
    'green' : 1.0,
    'brown' : -1.0
}

# --- building the 6x6 grid map ---
states = []
for r in range(rows):
    for c in range(cols):
        if (r, c) not in walls:
            states.append((r,c))

# --- reward function for robot landing on different states ---
def get_reward(state):
    if state in green_states:
        return reward_map["green"]
    elif state in brown_states:
        return reward_map["brown"]
    else:
        return reward_map["white"]

# --- function to change coordinates according to actions Up, Down, Left, Right ---
def move(state, action):
    # take in current coordinates of the robot
    r, c = state 

    # change coordinates accordingly - Row changes for Up/Down, Column changes for Left/Right
    if action == 'Up':
        nr, nc = r - 1, c
    elif action == "Down":
        nr, nc = r + 1, c
    elif action == "Left":
        nr, nc = r, c - 1
    elif action == "Right":
        nr, nc = r,  c + 1
    else:
        # default safety check for invalid actions
        raise ValueError(f"Invalid Action: {action}")
    
    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in walls:
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
    else:
        raise ValueError(f"Invalid Action: {action}")

    transitions = []
    for a, prob in candidates:
        next_state = move(state, a)
        transitions.append((prob, next_state))

    return transitions
