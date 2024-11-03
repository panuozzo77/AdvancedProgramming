def dec(type):
    def quanti(cls):
        def func(self):
            counter = 0
            for item, value in cls.__dict__.items():
                if isinstance(value, type):
                    counter += 1
            return counter

        cls.conta = func
        return cls
    return quanti

@dec(int)
class C:
    pass

C.a = 10
C.b = 5
C.d = 1


@dec(int)
class C:
    pass


# Adding attributes to the class
C.a = 10
C.b = 5
C.d = 1

# Testing the conta method
c_instance = C()
print(c_instance.conta())  # Output: 3
