import matplotlib.pyplot as plt
from env import *

arrow_map = {
    'Up' : '↑',
    'Down' : '↓',
    'Left' : '←',
    'Right' : '→'
}

def print_policy(policy):
    for r in range(rows):
        row_vals = []
        for c in range(cols):
            if (r, c) in walls:
                row_vals.append("■")
            else:
                row_vals.append(arrow_map[policy[(r, c)]])
        print(" ".join(row_vals))

def plot_history(history, tracked_states, title):
    plt.figure()
    for s in tracked_states:
        values = [U[s] for U in history]
        plt.plot(values, label=str(s))

    plt.xlabel("Iteration")
    plt.ylabel("Utility Estimate")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()