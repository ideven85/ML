from configparser import ConfigParser


def memoization_wrapper(func):
    cache = {}

    def inner(*args):
        pass

    pass


def my_func(*args):
    """
    Just concatenate the args to a list
    Args:
        *args: variable arguments

    Returns: list

    """
    n = len(args)
    result = []
    for i in range(n):
        result.append(args[i])
    return result


# Way too confusing..
def debug_this(n):
    functions = []
    for i in range(n):

        def func(*x):
            nonlocal functions
            # breakpoint() # here functions is not defined?
            print(functions)
            print(n)
            return x

        functions.append(func)  # Closure...
    # breakpoint()
    # print(func(12), end=' ')

    return functions

    # breakpoint()
    # return functions


def main():
    a, *b = 1, 2, 3

    print(my_func(a, *b))
    config = ConfigParser()

    x = debug_this(2)
    print()
    print(x)
    for f in x:
        print(f([1, 2]))


if __name__ == "__main__":
    main()
