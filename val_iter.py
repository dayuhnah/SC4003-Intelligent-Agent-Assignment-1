#=========================================================
# This file implements the Value Iteration (VI) algortihm for solving MDP
# and computes the optimal utility for each state and extracts the greedy policy
#=========================================================

try:
    from env_part2 import *
except ImportError:
    from env import *

def value_iteration(states, gamma = 0.99, epsilon = 1e-6):
    # This function runs VI until utilities converge 
    # with the respective factors such as states, gamma, epsilon and returns
    U = {s:0.0 for s in states}
    # records initial all-zero utilities so the plot starts from 0
    history = [U.copy()]
    iteration = 0

    while True:
        iteration += 1
        new_U = {}
        delta = 0


        for s in states:
            action_values = []

            for a in actions:
                expected_utility = 0
                for prob, s_next in get_transitions(s, a):
                    expected_utility += prob * U[s_next]
                action_values.append(expected_utility)

            # Bellman formula = reward + discounted best expected future utility
            best_action_value = max(action_values)
            new_U[s] = get_reward(s) + gamma * best_action_value
            # tracking the largest utility change across the states
            delta = max(delta, abs(new_U[s] - U[s]))

        U = new_U
        history.append(U.copy())

        # to check for convergence (stop when utilities have stabilised)
        if delta < epsilon:
            break

    print(f"Value Iteration converged in {iteration} iterations.")
    # U - dict mapping each state to its final utility value, history - list of U snapshots, one per iteration (starts at 0)
    return U, history

# function to extract the greey policy from a converged utility function
def extract_policy(U):
    policy = {}

    #each state picks the action with the highest expected utility
    for s in states:
        best_action = None
        best_value = float('-inf')

        #broken down by action list order
        for a in actions:
            #compute expected utility of taking action a from state s
            expected_utility = 0

            for prob, s_next in get_transitions(s, a):
                expected_utility += prob * U[s_next]

            if expected_utility > best_value:
                best_value = expected_utility
                best_action = a

        policy[s] = best_action

    #returns dict mapping each state to its optimal action string
    return policy