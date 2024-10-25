import math


class VectorException(Exception):
    """
    Just ignores the exception
    """

    pass


class Vector:
    def __init__(self, ndim):
        self._vector = [0 for _ in range(ndim)]

    def __len__(self):
        return len(self._vector)

    def __getitem__(self, dimension):
        if -len(self) <= dimension < len(self):
            return self._vector[dimension]
        return VectorException("Index out of bounds")

    def __add__(self, other):
        if type(other) == Vector and len(self) == len(other):
            return [(x + y) for x, y in zip(self._vector, other)]
        return VectorException("Some Error Occurred")

    def __setitem__(self, key, value):
        self._vector[key] = value


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def match_vector(v):
    pass
