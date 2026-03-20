from env import *
from val_iter import *
from pol_iter import *
from plot import *

def print_utilities(U):
    for r in range(rows):
        row_vals = []
        for c in range(cols):
            if (r, c) in walls:
                row_vals.append('#####')
            else:
                row_vals.append(f'{U[(r, c)]:6.2f}')
        print(" ".join(row_vals))

U_vi, vi_history = value_iteration(states)
policy_vi = extract_policy(U_vi)

print("~"*40)
print("VALUE ITERATION UTILITIES")
print_utilities(U_vi)
print("\nVALUE ITERATION POLICY")
print_utilities(policy_vi)

plot_history(vi_history, [(0,0), (0,1), (1,2)], "VI Utility Estimates")
plot_history(pi_history, [(0,0), (0,1), (1,2)], "PI Utility Estimates")
