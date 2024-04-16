# Genetic algorithm
import numpy as np
import random

# define costs
costs = np.array([130, 150, 140, 120, 140, 130])

# define returns
returns = np.array([0.10, 0.15, 0.05, 0.07, 0.12, 0.09])

# define budget
budget = 500

# define population size
pop_size = 4

# define number of generations
n_gen = 100

# define mutation rate
mutation_rate = 0.1


# define fitness function
def fitness(portfolio, costs, returns, budget):
    if np.dot(portfolio, costs) > budget:
        return 0
    else:
        return np.dot(portfolio, returns)


# initialize population
population = np.random.randint(2, size=(pop_size, 6))

# iterate over generations
for gen in range(n_gen):
    # calculate fitness
    fitness_values = np.array([fitness(pop, costs, returns, budget) for pop in population])

    # select parents
    parents = population[np.argsort(-fitness_values)[:2]]

    # create children, first the parents
    children = np.array([parents[0], parents[1]])
    for i in range(6):
        if random.random() < mutation_rate:
            children[:, i] = 1 - children[:, i]

    # add children to population
    population = np.vstack([population, children])

    # remove duplicates
    population = np.unique(population, axis=0)

    # select the best population
    fitness_values = np.array([fitness(pop, costs, returns, budget) for pop in population])
    population = population[np.argsort(-fitness_values)[:pop_size]]

# print the best portfolio
print(population[0])