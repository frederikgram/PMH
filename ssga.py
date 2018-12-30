""" Incredibly simple Steady-State Genetic Algorithm Implementation """

from dataclasses import dataclass
from random import uniform, randint
from numpy import mean


@dataclass
class Genome:
    weights: list
    fitness: float


def assessment_function(weights: list) -> float:
    """ Returns a float based on the mean of the input weights"""
    return mean(weights)


def ssga() -> list:
    """ Preconfigured Steady-State GA"""
    # Configuration variables

    _population_size = 100
    _mutation_rate = 100    # A value of 100 means that each genome has a 1/100th chance of mutating
    _num_weights = 5
    _num_additions = 2  # How many children to create at a time

    # Evolutionary boundaries
    _max_score = 0.7

    # Store globally best solution
    _globally_fittest_genome = None

    # Initialize population

    population = [
        Genome(weights=[uniform(0, 1) for _ in range(_num_weights)], fitness=None)
        for _ in range(_population_size)
    ]

    while True:

        # Assess fitness for every genome
        for genome in population:
            genome.fitness = assessment_function(genome.weights)

        # Sort population by fitness
        population = sorted(population, key=lambda genome: genome.fitness, reverse=True)

        # Find the fittest genome
        fittest_genome = population[0]

        if _globally_fittest_genome is None:
            _globally_fittest_genome = fittest_genome

        # Assure globally best solution is stored
        if fittest_genome.fitness > _globally_fittest_genome.fitness:
            _globally_fittest_genome = fittest_genome

        # Return Logic
        if _globally_fittest_genome.fitness >= _max_score:
            return _globally_fittest_genome.weights

        # Remove the n worst genomes where n is equal to _num_additions
        population = population[:-_num_additions]

        # Mean Value Crossover
        for i in range(0, _num_additions + 1, 2):
            tmp_weights = [
                mean([a, b])
                for a, b in zip(*[population[i].weights, population[i + 1].weights])
            ]
            child = Genome(weights=tmp_weights, fitness=None)

            # Uniform Mutation
            if randint(0, _mutation_rate) == 1:
                idx = randint(0, _num_weights - 1)
                child.weights[idx] = uniform(0, 1)

            population.append(child)


weights = ssga()
print(weights)
