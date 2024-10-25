class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, val):
        self.series.append(val)
        total = sum(self.series)
        return total / len(self.series)


def calc_avg_functional():

    count = 1
    total = 1
    x = "Hi"

    # series = []
    def make_averager(val):
        nonlocal total, x
        nonlocal count
        x += " deven"
        total += val
        count += 1
        # series.append(val)
        # return sum(series)/len(series)
        return total / count

    return make_averager


def memo_wrapper(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


@memo_wrapper
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def main():
    avg = Averager()
    print(callable(avg))
    print(avg(10))
    print(avg(11))
    print(avg(12))
    # print(avg.__code__.co_varnames)
    avg_functional = calc_avg_functional()
    print(avg_functional(10))
    print(avg_functional(11))
    print(avg_functional(12))
    print(callable(avg_functional(13)))
    # print(avg_functional(0))
    # First is value of count, second is value of total,3rd is value of x, all values referenced inside the closure
    print(
        avg_functional.__closure__[0].cell_contents,
        avg_functional.__closure__[1].cell_contents,
        avg_functional.__closure__[2].cell_contents,
    )  # 10+11+12+13
    # print(avg_functional.__closure__[0].cell_contents)
    print(avg_functional.__code__.co_varnames)
    print(avg_functional.__code__.co_freevars)
    print([fib(i) for i in range(30)])


if __name__ == "__main__":
    main()
