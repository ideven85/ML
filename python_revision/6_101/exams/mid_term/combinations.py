from typing import List
from functools import cache, lru_cache

ops = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y,
]


def memo_wrapper(func):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return inner


# @lru_cache(maxsize=None)
def combinations(nums):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x // y,
    }

    @lru_cache(maxsize=None)
    def inner(temp):
        if len(temp) < 2:
            return temp
        # temp = list(temp)
        return {
            op(curr, temp[-1])
            for curr in inner(temp[:-1])
            for op in operations.values()
        }

    # if len(nums)<2:
    #     return nums
    # else:
    #     out = []
    #
    #     for _, operation in operations.items():
    #         out.extend(combinations([operation(nums[0],nums[1])]+nums[2:]))

    #    return out
    nums = tuple(nums[:])
    return inner(nums)


def main():
    print(combinations([5]))
    print(combinations([1, 2, 3]))  # {0, 1, 2, 3, 5, 6, 9, -4, -3, -1}
    print(combinations([1, 2]))
    # print(len(combinations(list(range(1,20))))) # 69,854,050


if __name__ == "__main__":
    main()
