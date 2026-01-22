# https://www.codewars.com/kata/5535572c1de94ba2db0000f6/train/python

# Pretty much just monkey patching

class Dog(object):
    def __init__(self, name, breed, sex, age):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = age


def bark(self) -> str:
    return "Woof!"


Dog.bark = bark


def test() -> None:
    dog = Dog("Nacho", "Pug", "Male", 3)
    print(dog.bark())


if __name__ == "__main__":
    test()
