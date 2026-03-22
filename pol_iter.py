#=========================================================
# This file implements Policy Iteration algortihm for solving the MDP.
# It alternates between the two steps until the policy stops changing:
# 1. Policy Evaluation - compute utilities for the current policy
# 2. Policy Improvement - update each state's action to the greedy best
#=========================================================
from env import *

# function that initialises a default policy action for every state
def init_policy():
    return {s: 'Up' for s in states}

# function to evaluate a fixed policy by iterating the Bellman formula until utilities converge:
# U(s) = R(s) + gamma * sum over s' of P(s'|s, policy(s)) * U(s')
# gamma -> discount factor, epsilon -> convergence threshold
def policy_evaluation(policy, gamma = 0.99, epsilon = 1e-6):
    U = {s: 0.0 for s in states}

    while True:
        new_U = {}
        delta = 0

        for s in states:
            # follow policy - no max, just evaluate this action
            a = policy[s]
            expected_utility = 0
            for prob, s_next in get_transitions(s, a):
                expected_utility += prob * U[s_next]

            new_U[s] = get_reward(s) + gamma * expected_utility
            delta = max(delta, abs(new_U[s] - U[s]))

        U = new_U

        #stop when utilities have stabilised under this policy
        if delta < epsilon:
            break

    # returns dict mapping each state to it utility under the given policy
    return U

# function to run policy iteration until the policy stops changing between rounds.
def policy_iteration(gamma = 0.99, epsilon = 1e-6):
    policy = init_policy()
    U = policy_evaluation(policy, gamma, epsilon)
    history = [U.copy()]

    #each round will fully evaluate the current policy then improve it greedily
    iteration = 0

    while True:
        iteration += 1
        stable = True # assuming plicy is stable until a change is found

        # policy improvement -> updating each state to its greedy best action
        for s in states:
            old_action = policy[s]

            best_action = None
            best_value = float('-inf')

            for a in actions:
                expected_utility = 0 
                for prob, s_next in get_transitions(s, a):
                    expected_utility += prob * U[s_next]

                if expected_utility > best_value:
                    best_value = expected_utility
                    best_action = a

            policy[s] = best_action

            # if any state changeed its action, the policy is not stable yet
            if best_action != old_action:
                stable = False

        # if no state changed, policy has converged -> stop
        if stable:
            print(f"Policy Iteration converged in {iteration} improvement rounds.")
            return policy, U, history
        
        #policy changed so need to re-evaluate and record new utilities
        U = policy_evaluation(policy, gamma, epsilon)
        history.append(U.copy())