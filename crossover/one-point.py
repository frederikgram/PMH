""" One point vector crossover """

from typing import List, Tuple


def one_point(vector_a: List, vector_b: List) -> Tuple[List, List]:
    """

    :param vector_a: n len list of objects
    :param vector_b: n len list of objects
    :return: (vector_a, vector_b) swapped at random indexes
    """

    import random

    point = random.randint(0, len(vector_a))

    if not point == 1:
        for i in range(point, len(vector_a)):
            vector_a[i], vector_b[i] = vector_b[i] + vector_a[i]

    return vector_a, vector_b


# print(one_point([1, 1, 2, 6, 5], [7, 6, 4, 4, 3]))
