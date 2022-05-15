import random


def n_queens_neighbours(state):
    help = set()
    output = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j:
                help.add(tuple(sorted((i,j))))
    for i in help:
        a = i[0]
        b = i[1]
        potential = list(state[:])
        temp = potential[a]
        potential[a] = potential[b]
        potential[b] = temp
        output.append(tuple(potential))
    return sorted(output)


def n_queens_cost(state):
    conflicts = 0
    for i, item in enumerate(state):
        for j, jtem in enumerate(state):
            if i != j and item != jtem:
                if abs(i-j) == abs(item - jtem):
                    conflicts += 1
    return int(conflicts/2)


def greedy_descent(initial_state, neighbours, cost):
    results = [initial_state]
    all_costs = [cost(initial_state)]
    finished = False
    current_state = initial_state
    while not finished:
        new_neighbour, new_cost = best_neighbour(current_state, neighbours, cost)
        if new_cost in all_costs or new_neighbour in results:
            finished = True
        else:
            results.append(new_neighbour)
            all_costs.append(new_cost)
        current_state = new_neighbour
    return results

            
def best_neighbour(state, neighbours, cost):

    all_neighbours = neighbours(state)
    all_costs = [cost(i) for i in all_neighbours]
    if len(all_costs) > 0:
        best_neighbour = all_neighbours[all_costs.index(min(all_costs))]
        best_neighbour_cost = min(all_costs)
        return best_neighbour, best_neighbour_cost
    else:
        return state, 100000000


def roulette_wheel_select(population, fitness, r):
    pop_fitness = [fitness(i) for i in population]
    num = 0
    fitness_percentage = []
    total_fitness = sum(pop_fitness)
    for i in pop_fitness:
        fitness_percentage.append(i/total_fitness)
    for i, item in enumerate(fitness_percentage):
        num += item
        if num >= r:
            return population[i]



population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))