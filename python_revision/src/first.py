from collections import abc

x = 100


class A:
    x = 10

    def __init__(self):
        self.x = self.x


class B(A):
    x = 30
    # def __init__(self):
    #     """
    #     Remember that when we make a new instance of a class,
    #      Python will look up the name __init__ in that new instance according to our normal attribute-lookup rules;
    #       and if it finds a method called __init__, it will implicitly call that method with our new instance passed in as the first argument.
    #     """
    #     self.x=x


class C(B):
    x = "fish"


class D(A):
    x = "d"

    def __init__(self):
        self.x = self.x


class Shapes:
    def __init__(self):
        pass


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return self._radius * self._radius


if __name__ == "__main__":
    b = B()
    print(b.x)
    print(dir(b))
    c = C()
    print(c.x)
    print(B.x)
    print(A.x)
    print(C.x)
    print(D.x)
    d = D()
    print(d.x)
    print(dir(D))
    print(dir(D()))
