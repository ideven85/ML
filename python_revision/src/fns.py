import copy

x = 1000


def foo(y):
    return x + y


z = foo(308)


print(f"{z}")
print(f"{foo}")


def bar(x):
    x = 500
    return foo(308)


def fib(n):
    a, b = 0, 1
    x = []
    y = []
    for _ in range(n + 1):
        yield a
        """
        # Here the evaluation is not like C/Java
        First the whole right hand side expression is evaluated and stored in memory 
        Then assigned right to left to left side variables
        So the equation is:
        c=a+b
        
        a=b
        b=c
        
        """
        a, b = b, a + b

        """
                c = a + b
               
                a = b
                b = c
        """
    # print(y)
    # return x


w = bar(349)
print(f"{w}")
print(f"{x}")
print(list(fib(10)))
a = [1, 2, 3, 4]
b = [a, a]  # Creates a new list in what time?
print(id(a), id(b))
c = b[:]  # Shallow Copy Containing the same references as b...
d = copy.deepcopy(b)  # As the name suggests...
c[0][0] = 100
print(a, b, c)
print(d)
x = [9, 8, 7, 6, 5, 4, 3, 2]
print(x[::2])  # x[start:stop:step]
# b.extend(a) # you know
# print(b)
# b.append(a) # you know
print(b)
# This i did not know, creates  copy...Overloaded extends returns a new list
z = b + a
b += a  # At the same memory location Overloaded hai plus
print(f"{z}\n{b}")
# print(id(z))
# print(id(b))
# z[0][0]=-1
# print(z,a)
# print(id(z[0])==id(b))
