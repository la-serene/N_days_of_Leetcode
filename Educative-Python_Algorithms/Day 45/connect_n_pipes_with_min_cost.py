# Connecting n Pipes With Minimum Cost
# https://www.educative.io/courses/algorithms-coding-interviews-python/challenge-connecting-n-pipes-with-minimum-cost

"""
Implement a function that connects n pipes of different lengths, into one pipe. You can assume that the cost to connect
two pipes is equal to the sum of their lengths. We need to connect the pipes with minimum cost.
"""


def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """

    pipes = sorted(pipes)
    total_cost, last_cost = 0, pipes[0]
    for i in range(len(pipes) - 1):
        cur_cost = pipes[i + 1] + last_cost
        total_cost = last_cost + cur_cost

    return total_cost
