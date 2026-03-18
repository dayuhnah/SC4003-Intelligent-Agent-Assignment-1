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




