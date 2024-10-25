# class range:
#     def __init__(self, start=0, stop=1, step=1):
#         self._list = [0] * (abs(stop - start + step - 1) // step)
#         l = start
#         for key, index in enumerate(self._list):
#
#             self._list[key] = l
#             l += step
#         # print(self._list)
#         self._index = -1
#
#     def __len__(self):
#         return len(self._list)
#
#     def __getitem__(self, index):
#         return self._list[index]
#
#     def __setitem__(self, key, value):
#         self._list[key] = value
#
#     def __next__(self):
#         self._index += 1
#         if self._index < len(self):
#             return self._list[self._index]
#         raise StopIteration
#
#     def __iter__(self):
#         return self


# Better, not creating a list
class Range:
    def __init__(self, start=0, stop=None, step=None):
        if not stop:
            start, stop = 0, start
        if not step:
            step = 1
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._stop = stop
        self._step = step
        self._index = self._start

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if k > len(self):
            raise IndexError("Index out of bounds")
        return self._start + k * self._step

    def __iter__(self):
        # self._length=self._step
        # print(self._length,self._index,self._step)
        i = 0
        while i < self._length:

            yield self._index

            self._index += self._step
            i += 1


def main():
    r = range(-10, 45, 5)
    r[0] = 1
    r[-1] = 2
    print(list(r))
    # print(r)
    r1 = Range(-20, -2, 3)
    l = [1, 2, 3]
    for i in Range(len(l)):
        print(l[i], end=" ")
    print()

    print(len(r1))
    print(list(r1))
    print(r1[-3])


if __name__ == "__main__":
    main()
