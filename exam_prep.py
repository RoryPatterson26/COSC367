def select(population, error, max_error, r):
    j = 0
    fitnesses = []
    normal_fitness = []
    for i in population:
        fitness = max_error - error(i)
        fitnesses.append(fitness)
    total_fitness = sum(fitnesses)
    for i in fitnesses:
        normal_fitness.append(i/total_fitness)
    for i, item in enumerate(normal_fitness):
        if item + j >= r:
            return population[i]
        j += item

population = ['a', 'b']

def error(x):
    return {'a': 14,
            'b': 12}[x]

max_error = 15

for r in [0, 0.1, 0.24, 0.26, 0.5, 0.9]:
    print(select(population, error, max_error, r))
