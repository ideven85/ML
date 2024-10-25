class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise TypeError("name must be a string")
        else:
            self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be less than zero")
        else:
            self._age = age

    def __repr__(self):
        raise TypeError("Must be implemented by base class")

    def __str__(self):
        raise TypeError("Must be implemented by base class")


class Student(Person):
    def __init__(self, grade):
        # self.name=super(self.name)
        # self.age=super(self.age)
        self._grade = grade

    def __repr__(self):
        return "Student is in grade " + str(self._grade)

    def __str__(self):
        return f"{self.name} of {self.age} is in {self._grade} class"
