from oops.person import Student


def main():
    student1 = Student(10)
    student1.age = 24
    student1.name = "Deven"
    print(student1)
    print(repr(student1))


if __name__ == "__main__":
    main()
