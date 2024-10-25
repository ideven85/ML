# #############
# Combinations
# #############
#
# ..  contents::
#
# Definition
# ==========
#
# For some deeper statistical calculations,
# we need the number of combinations of *n* things
# taken *k* at a time, :math:`\binom{n}{k}`.
#
# ..  math::
#
#     \binom{n}{k} = \dfrac{n!}{k!(n-k)!}
#
# The function will use an internal ``fact()`` function because
# we don't need factorial anywhere else in the application.
#
# We'll rely on a simplistic factorial function without memoization.
#
# Test Case
# =========
#
# Here are two simple unit tests for this function provided
# as doctest examples.
#
# >>> from combo import combinations
# >>> combinations(4,2)
# 6
# >>> combinations(8,4)
# 70
#
# Implementation
# ===============
#
# Here's the essential function definition, with docstring:
# ::


def combinations(n: int, k: int) -> int:
    """Compute :math:`\binom{n}{k}`, the number of
    combinations of *n* things taken *k* at a time.

    :param n: integer size of population
    :param k: groups within the population
    :returns: :math:`\binom{n}{k}`
    """

    # An important consideration here is that someone hasn't confused
    # the two argument values.
    # ::

    assert k <= n

    # Here's the embedded factorial function. It's recursive. The Python
    # stack limit is a limitation on the size of numbers we can use.
    # ::

    def fact(a: int) -> int:
        if a == 0:
            return 1
        return a * fact(a - 1)

    # Here's the final calculation. Note that we're using integer division.
    # Otherwise, we'd get an unexpected conversion to float.
    # ::

    return fact(n) // (fact(k) * fact(n - k))


# We can make this more efficient by treating the factorial product
# as a *Multiset* of individual integer values. The product updates the
# multiset. The division removes items from the multiset. Once the final
# set of factors is available, the final product can be computed more efficiently.
