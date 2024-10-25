x = "dog"


class Cat:
    x = "cat"

    def __init__(self, y):
        self.x = self.x


class TigerCat(Cat):
    x = "ferret"

    def __init__(self):
        # Cat.__init__(self,self.x)
        super().__init__(self.x)

    # def __init__(self):
    #     # nonlocal x Error not for classes
    #     self.x=self.x #Will assign tiger
    #     self.x=x # Now will look in the global scope # To Reference Local use self.x
    #     #pass  # Now will not look in this method

    def log(self):
        print(self.x)  # Prints Global x if __init__ is not used

    @classmethod
    def log1(cls):
        print(cls.x)  # Still prints Global x


tiger = TigerCat()
print(tiger.x)
tiger.log()
tiger.log1()
print(TigerCat.x)
