from env import *

def init_policy():
    return {s: 'Up' for s in states}

def policy_evaluation(policy, gamma = 0.99, epsilon = 1e-6):
    U = {s: 0.0 for s in states}

    while True:
        new_U = {}
        delta = 0

        for s in states:
            a = policy[s]
            expected_utility = 0
            for prob, s_next in get_transitions(s, a):
                expected_utility += prob * U[s_next]

            new_U[s] = get_reward(s) + gamma * expected_utility
            delta = max(delta, abs(new_U[s] - U[s]))

        U = new_U

        if delta < epsilon:
            break

    return U

def policy_iteration(gamma = 0.99, epsilon = 1e-6):
    policy = init_policy()
    history = []
    iteration = 0

    while True:
        iteration += 1
        U = policy_evaluation(policy, gamma, epsilon)
        history.append(U.copy())

        stable = True

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

            if best_action != old_action:
                stable = False

        if stable:
            print(f"Policy Iteration converged in {iteration} improvement rounds.")
            return policy, U, history
    