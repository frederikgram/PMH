""" Uniform vector crossover """

from typing import List, Tuple


def uniform(vector_a: List, vector_b: List, probability: float=None) -> Tuple[List, List]:
    """

    :param vector_a: n len list of objects
    :param vector_b: n len list of objects
    :param probability: chance of each index swapping
    :return: (vector_a, vector_b) swapped at random indexes
    """

    import random

    if probability is None:
        probability = 1 / len(vector_a)

    for i in range(1, len(vector_a)):
        if probability > random.uniform(0, 1):
            vector_a[i], vector_b[i] = vector_b[i], vector_a[i]

    return vector_a, vector_b


# print(uniform([1, 1, 2, 6, 5]))
