def get_min(state, neighbours, cost):
    """Returns the min value of the given state."""
    min_value = 1000000000
    active = state
    for i in neighbours(state):
        state_cost = cost(i)
        if state_cost < min_value:
            active = i
            min_value = state_cost

    return active, min_value


def greedy_descent(initial_state, neighbours, cost):
    """Takes an initial state and two functions to compute the neighbours and cost of a state, and then iteratively 
    improves the state until a local minimum (which may be global) is reached. """
    results = []
    costs = []
    done = False
    new_cost = cost(initial_state)
    last_value = -10000
    current = initial_state
    while not done:
        if new_cost in costs:
            done = True
            break
        if current in results:
            done = True
            break
        costs.append(new_cost)
        results.append(current)
        new, new_cost = get_min(current, neighbours, cost)
        if last_value == new:
            done = True
            break
        last_value = current
        current = new
        
    return results

def cost(x):
    return -x**2

def neighbours(x):
    return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
    print(state)