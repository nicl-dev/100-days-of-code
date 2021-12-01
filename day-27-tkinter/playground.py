# Positional arguments
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# print(add(5, 6, 9, 10))


# Keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.doors = kw.get("doors")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan")
print(my_car.make)
