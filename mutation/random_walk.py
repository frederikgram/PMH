""" Random walk mutation on integer vectors """

from typing import List


def random_walk(vector: List[int], p: float = None, b: float=None) -> List[int]:
    """

    :param vector: n len list of boolean objects as 0 or 1
    :param p: chance for each entry in list to mutate, 0 -> 1
    :param b: coin flip probability
    :return:
    """
    import random

    if p is None:
        p = 1 / len(vector)
    if b is None:
        b = 0.5

    for i in range(1, len(vector)):
        if p > random.uniform(0, 1):
            while True:
                n = random.choice([-1, 1])
                if random.randint(0, 1) == 0:
                    vector[i] += n
                else:
                    vector[i] -= n

                if b < random.uniform(0, 1):
                    break
    return vector


# print(random_walk([1, 1, 2, 4, 5]))
