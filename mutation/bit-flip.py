""" Bit flip mutation on boolean vectors """

from typing import List


def flip(vector: List[bool], probability: float = None) -> List[bool]:
    """

    :param vector: n len list of boolean objects as 0 or 1
    :param probability: chance for each entry in list to mutate, 0 -> 1
    :return:
    """
    import random

    if probability is None:
        probability = 1 / len(vector)

    vector = [
        entry * -1 if random.uniform(0, 1) < probability else entry for entry in vector
    ]

    return vector


# print(flip([True, True, True], 0.1))
