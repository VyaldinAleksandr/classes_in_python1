class Animal():
    def  __init__(self, dog, cat, rooster):
        self.dog = dog
        self.cat = cat
        self.rooster = rooster

class Dog(Animal):
    def __init__(self,dog):
        self.dog = dog

class Cat(Animal):
    def __init__(self, cat, sphinxcat):
        self.sphinxcat = sphinxcat
        self.cat = cat

class SphynxCat(Cat):
    def __init__(self, sphinxcat):
        self.sphinxcat = sphinxcat

class Rooster(Animal):
    def __init__(self, rooster):
        self.rooster = rooster

    def my_sphinxcat(self):
        return self.woolkitty("No wool")

    def my_rooster(self):
        return (self.petya_paw("He has 2 paws, not 4, and he has no wool"))

say_something = Animal(" Woof - woof", "Meow - meow", "Cocorico")
say_something1 = SphynxCat("Murr-Murr")


print (say_something.cat, say_something.dog, say_something.rooster)
print (say_something1.sphinxcat)
