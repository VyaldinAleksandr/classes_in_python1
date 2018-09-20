class Animal(object):


    def __init__(self, tail, paw, wool):
        self.tail = 1
        self.paw = 4
        self.wool = True


class Dog(Animal):

    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)

    def say_woof(self):
        return 'Woof Woof'


class Cat(Animal):

    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)

    def say_meow(self):
        return 'Meow meow'


class SphynxCat(Cat):

    def __init__(self, tail, paw, wool):
        Cat.__init__(self, tail, paw, wool)
        self.wool = False

    def say_murr(self):
        return 'murr-murr'


class Rooster(Animal):

    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)
        self.paw = 2
        self.wool = False

    def say_Cocorico(self):
        return "Cocorico"

print(SphynxCat.say_meow(Cat))
print(SphynxCat.say_murr(Cat))
print(Cat.say_meow(Animal))
print(Dog.say_woof(Animal))
print(Rooster.say_Cocorico(Animal))
