# 6.101 recitation 0
# subject introduction
# testing and debugging, some python "goodies" and style


############### EXAMPLE 0: ADDING ELEMENTS IN NESTED LISTS


def sum_lists(lists):
    """
    Given a list of lists, return a new list where each list is replaced by
    the sum of its elements.
    >>> input1 = [[1, 2], [3, 4]]
    >>> sum_lists(input1) == [3, 7]
    True
    """

    return [sum(lst) for lst in lists]


############### EXAMPLE 1: REVERSING NESTED LISTS


def reverse_all(inp):
    """
    given a list of lists, return a new list of lists
    but with all of the inner lists reversed, without
    modifying the input list

    example:
    >>> input1 = [[1, 2], [3, 4]];inp2 = input1[:]
    >>> reverse_all(input1)
    [[2, 1], [4, 3]]
    >>> input1 == inp2
    True
    """

    return [list(reversed(L)) for L in inp[:]]


############### EXAMPLE 2: SUBTRACTING CORRESPONDING ELEMENTS IN LISTS


def subtract_lists(l1, l2):
    """
    Given lists of numbers l1 and l2, return a new list where each position is
    the difference between that position in l1 and in l2.

    >>> subtract_lists([1,2],[3,4])
    [-2, -2]
    """
    return [x - y for x, y in zip(l1, l2)]
