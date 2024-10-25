from functools import lru_cache


def fib(n):
    """
    :param n: Positive Integer
    :return: generator object of fibonacci series of n

    """
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b


def memoized(func):
    memo = {}

    def inner(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    print(memo)
    return inner


#
# @lru_cache(maxsize=None)
@memoized  # Decorator is executed as soon as the module is loaded...
def memoized_fib(n):
    return n if n < 2 else memoized_fib(n - 1) + memoized_fib(n - 2)


def main():
    print(list(fib(10)))
    print(memoized_fib(10))


if __name__ == "__main__":
    main()
