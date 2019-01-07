""" One point vector mutation """

from typing import List


def one_point(vector: List) -> List:
    """

    :param vector: n len list of objects
    :return: vector swapped at random index
    """

    import random

    point = random.randint(0, len(vector))

    if point != 1:
        vector = vector[point:] + vector[:point]

    return vector


#print(one_point([1, 1, 2, 6, 5]))
