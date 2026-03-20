from env import *
from val_iter import *
from pol_iter import *
from plot import *

tracked_states = [(2, 0), (1, 1), (5, 5)]

U_vi, vi_history = value_iteration(states)
policy_vi = extract_policy(U_vi)

print("~"*40)
print("VALUE ITERATION UTILITIES")
print_utilities(U_vi)
print("\nVALUE ITERATION POLICY")
print_policy(policy_vi)

plot_grid(U_vi, policy_vi, "VI Optimal policy and Utilities")
plot_history(vi_history, tracked_states, "VI Utility Estimates per Iteration")

policy_pi, U_pi, pi_history = policy_iteration()

print("~"*40)
print("\nPOLICY ITERATION UTILITIES")
print_utilities(U_pi)
print("\nPOLICY ITERATION POLICY")
print_policy(policy_pi)

plot_grid(U_pi, policy_pi, "PI Optimal policy and Utilities")
plot_history(pi_history, tracked_states, "PI Utility Estimates per Iteration")
