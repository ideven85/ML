"""
A Vector module
"""


class VectorException(Exception):
    """
    Just ignores the exception
    """

    pass


class Vector:
    """
    An n dimensional Vector class
    """

    def __init__(self, dim):
        self._vector = [0 for _ in range(dim)]
        self._index = -1

    def __len__(self):
        return len(self._vector)

    def __contains__(self, item):
        return -len(self) <= item < len(self)

    def __getitem__(self, item):
        if item not in self:
            return VectorException("Out of range")

        return self._vector[item]

    def __setitem__(self, key, value):
        if key not in self:
            raise VectorException("Co ordinate not in dimensions")

        self._vector[key] = value

    def __eq__(self, other):
        return bool(
            len(self) == len(other) and [x == y for x, y in zip(self._vector, other)]
        )

    def set(self, values):
        """

        :param values: sets our vector with same values as vector
        :return: None
        """
        for index, val in enumerate(values):
            self._vector[index] = val

    def __next__(self):
        self._index += 1
        if self._index <= len(self):
            raise StopIteration
        return self._vector[self._index]

    def __iter__(self):
        for index in range(len(self._vector)):
            yield self._vector[index]

    def __add__(self, other):
        if len(self) != len(other):
            return VectorException("Dimensions do not agree")

        x = [(x + y) for x, y in zip(self._vector, other)]

        return " ".join(str(a) for a in x)

    def __repr__(self):
        return " ".join(str(x) for x in self._vector)

    def __str__(self):
        x = " ".join(str(x) for x in self._vector)
        # print(x)
        return x


def main():
    """

    Main method
    """
    v1 = Vector(2)
    v1[0] = 1
    v1[1] = 2

    # print(list(v1))
    print(v1)
    v2 = Vector(2)
    print(len(v2))
    v2[0] = 1
    v2[-1] = 100
    print(v1 + v2)
    v = v1 + v2
    print(v)
    vector = Vector(5)
    a = list(range(5))
    vector.set(a)
    print(len(vector))
    print(vector)
    vector[-3] = 100
    print(vector[2])
    v3 = Vector(2)
    print("V1 state is now", v1)
    v3[0] = 1
    v3[-1] = 2
    print(v3)
    print(v3 == v1)
    # v1[3] = 3
    print(v1)
    print(type(v1 + vector))


if __name__ == "__main__":
    main()
