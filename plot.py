#=========================================================
# This file provides visualization utilities for the MDP results
#=========================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from env import *


# try:
#     from env_part2 import *
# except ImportError:
#     from env import *

# maps action strings to unicode arrow characters for display
arrow_map = {
    'Up' : '↑',
    'Down' : '↓',
    'Left' : '←',
    'Right' : '→'
}

# function prints the policy to the console as a grid of arrow
def print_policy(policy):
    # reverse rows only so top of printed output matches top of maze figure
    for r in range(rows):
        row_vals = []
        for c in range(cols):
            if (r, c) in walls:
                row_vals.append("■")
            else:
                row_vals.append(arrow_map[policy[(r, c)]])
        print(" ".join(row_vals))

# function prints the utility values to the console as a grid
def print_utilities(U):
    for r in range(rows):
        row_vals = []
        for c in range(cols):
            if (r, c) in walls:
                row_vals.append('#####')
            else:
                row_vals.append(f"{U[(r, c)]:6.2f}")
        print(" ".join(row_vals))

#function renders the maze with colour as shown in the assignment document
def plot_grid(U, policy, title):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.axis('off')

    for r in range(rows):
        display_r = rows - 1 - r

        for c in range(cols):
            x, y = c, display_r

            if (r, c) in walls:
                color = '#888888'
                ax.add_patch(mpatches.FancyBboxPatch(
                    (x + 0.02, y + 0.02), 0.96, 0.96, 
                    boxstyle="round,pad=0.02", color=color))
                ax.text(x + 0.5, y + 0.5, 'Wall',
                        ha='center', va='center',
                        fontsize = 9, color = 'white', fontweight='bold')
                
            elif (r, c) in green_states:
                color = '#7ec87e'
                ax.add_patch(mpatches.FancyBboxPatch(
                    (x + 0.02, y + 0.02), 0.96, 0.96,
                    boxstyle="round,pad=0.02", color=color))
                ax.text(x + 0.5, y + 0.72, f"{U[(r, c)]:.2f}",
                        ha='center', va='center', fontsize=9, color='#1a4a1a')
                ax.text(x + 0.5, y + 0.35, arrow_map[policy[(r, c)]],
                        ha='center', va='center', fontsize=18, color='#1a4a1a')
                if (r, c) == start_state:
                    ax.text(x + 0.5, y + 0.15, '* start',
                            ha='center', va='center', fontsize=7, color='#1a4a1a')
                    
            elif (r, c) in brown_states:
                color = '#c97c5d'
                ax.add_patch(mpatches.FancyBboxPatch(
                    (x + 0.02, y + 0.02), 0.96, 0.96,
                    boxstyle="round,pad=0.02", color=color))
                ax.text(x + 0.5, y + 0.72, f"{U[(r, c)]:.2f}",
                        ha='center', va='center', fontsize = 9, color='#3a1a0a')
                ax.text(x + 0.5, y + 0.35, arrow_map[policy[(r, c)]],
                        ha='center', va='center', fontsize = 18, color='#3a1a0a')
                if (r, c) == start_state:
                    ax.text(x + 0.5, y + 0.5, '* start',
                            ha = 'center', va = 'center', fontsize=7, color='#3a1a0a')
            
            else:
                color = '#f5f5f0'
                ax.add_patch(mpatches.FancyBboxPatch(
                    (x+0.02, y+0.02), 0.96, 0.96,
                    boxstyle="round, pad=0.02", color=color,
                    linewidth=0.5, edgecolor='#aaaaaa'))
                ax.text(x+0.5, y+0.72, f"{U[(r, c)]:.2f}",
                        ha = 'center', va='center', fontsize=9, color='#333333')
                ax.text(x+0.5, y+0.35, arrow_map[policy[(r, c)]],
                        ha='center', va='center', fontsize=18, color='#333333')
                if(r, c) == start_state:
                    ax.text(x+0.5, y+0.15, '* start',
                            ha='center', va='center', fontsize=7, color='#555555')

    # column index labelling        
    for c in range(cols):
        ax.text(c + 0.5, -0.3, str(c),
                ha='center', va='center', fontsize = 9, color='#555555')
    # row index labelling
    for r in range(rows):
        display_r = rows - 1 - r
        ax.text(-0.15, display_r + 0.5, str(r),
                ha='center', va='center', fontsize=9, color='#555555')
    
    #legend making
    legend_elements = [
        mpatches.Patch(color='#7ec87e', label='Green (+1)'),
        mpatches.Patch(color='#c97c5d', label='Brown (-1)'),
        mpatches.Patch(color='#f5f5f0', label = 'White (-0.05)', linewidth=0.5, edgecolor='#aaaaaa'),
        mpatches.Patch(color='#888888', label='Wall')
    ]

    ax.legend(handles = legend_elements, loc = 'upper right',
              bbox_to_anchor=(1.18, 1.0), fontsize=9)
    
    plt.tight_layout()
    plt.show()

# function that plots utility estimates as a function of iteration number
def plot_history(history, tracked_states, title):
    plt.figure(figsize=(9, 5))
    for s in tracked_states:
        if s not in states:
            print(f"Skipping invalid tracked state: {s}")
            continue

        # collects this state's utility value at every iteration
        values = [U[s] for U in history]

        # label each line with state type
        label = f'{s}'
        if s in green_states:
            label += " (green)"
        elif s in brown_states:
            label += ' (brown)'
        else: 
            label += ' (white)'
        plt.plot(values, label=label, linewidth=1.8)

    plt.xlabel("Iteration")
    plt.ylabel("Utility Estimate")
    plt.title(title)
    plt.legend()
    plt.grid(True, linestyle='--', alpha = 0.5)
    plt.tight_layout()
    plt.show()