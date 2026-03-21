#=========================================================
# This file is to build up the 6x6 grid maze environment for Part 1
# It contains the state, actions available, reward function, movement logic
# and stochastic transition model
#=========================================================

import numpy as np

# --- building the grip map env ---
rows = 6
cols = 6
walls = {(0, 1),(1, 4),(4, 1),(4, 2),(4, 3)}

# --- terminal reward states and starting position ---
green_states = {(0, 0), (0, 2), (0, 5), (1, 3), (2, 4), (3, 5)}
brown_states = {(1, 1), (1, 5), (2, 2), (3, 3), (4, 4)}
start_state = (3, 2)

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
    
    #if the resulting cell is out of bounds or a wall, remain original spot
    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in walls:
        return state
    
    # returns new (row, col) tuple of next state
    return (nr, nc)

# --- function to return stochastic transition distribution for a given state and action ---
def get_transitions(state, action):
    # intended actions have 0.8 probability of occuring, else, slips to either perpendicular direction with 0.1 probability
    if action == "Up":
        candidates = [('Up', 0.8), ("Left", 0.1), ("Right", 0.1)]
    elif action == "Down":
        candidates = [("Down", 0.8), ("Left", 0.1), ("Right", 0.1)]
    elif action == "Left":
        candidates = [("Left", 0.8), ("Up", 0.1), ("Down", 0.1)]
    elif action == "Right":
        candidates = [("Right", 0.8), ("Up", 0.1), ("Down", 0.1)]
    else:
        # catch any invalid actions if any
        raise ValueError(f"Invalid Action: {action}")

    transitions = []
    for a, prob in candidates:
        next_state = move(state, a)
        transitions.append((prob, next_state))
    
    #returns list of (probability, next_state) tuples
    return transitions