from dis import dis

registers = []


# Decorators are executed as soon as the module is loaded...
# Even if not executed, executed as many times as the decorator is used
def register_wrapper(func):
    # print(f"Register: {func}")
    # print("Hi")
    # registers.append(func)
    def inner():
        print(f"Register: {func()}")
        registers.append(func)

    return inner


@register_wrapper
def f1():
    return "f1"


@register_wrapper
def f2():
    return "f21"


@register_wrapper
def f3():
    return "f32"


def main():
    print("Hi")
    print(f1.__name__)
    print(dis(f1))
    f3()
    print([f.__name__ for f in registers])


if __name__ == "__main__":
    main()
    # Output Register: <function f1 at 0x104240cc0>
    # Hi
    # Register: <function f2 at 0x1043a76a0>
    # Hi
    # Register: <function f3 at 0x1095536a0>
    # Hi
    # Hi
    # f1
    # f2
    # [<function f1 at 0x104240cc0>, <function f2 at 0x1043a76a0>, <function f3 at 0x1095536a0>]
