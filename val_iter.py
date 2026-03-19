from env import *

gamma = 0.99
epsilon = 1e-6

def value_iteration(states, gamma = 0.99, epsilon = 1e-6):
    U = {s:0.0 for s in states}
    history = [ ]
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

            best_action_value = max(action_values)
            new_U[s] = get_reward(s) + gamma * best_action_value
            delta = max(delta, abs(new_U[s] - U[s]))

        U = new_U
        history.append(U.copy())

        if delta < epsilon:
            break

    print(f"Value Iteration converged in {iteration} iterations.")
    return U, history

def extract_policy(U):
    policy = {}

    for s in states:
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

    return policy

