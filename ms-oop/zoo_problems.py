
class Animal(object):
    population = 0
    def __init__(self, name, favoriteFood):
        self.name = name
        self.favoriteFood = favoriteFood
        Animal.population += 1

    def populationCount():
        return population

    def sleep(self):
        print(self.name + " sleeps for 8 hours")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)

class Tiger(Animal):
    # Implement the initializer method here
    def __init__(self, name):
        Animal.__init__(self, name, "meat")

class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "fish")

    def sleep(self):
        print(self.name + " hibernates for 4 months")

# Implement the Unicorn class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep method
class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "marshmallows")

    def sleep(self):
        print(self.name + " sleeps in a cloud")


# Implement the Giraffe class here as a subclass of Animal
# Hint: Implement the initializer method and override the eat method
class Giraffe(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "leaves")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
        else:
            print("YUCK! " + self.name + " spits out " + food)


# Implement the Bee class here as a subclass of Animal
# Hint: Implement the initializer method and override the sleep and eat methods
class Bee(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, "pollen")

    def sleep(self):
        print(self.name + " never sleeps")

    def eat(self, food):
        print(self.name + " eats " + food)
        if food == self.favoriteFood:
            print("YUM! " + self.name + " wants more " + food)
        else:
            print("YUCK! " + self.name + " spits out " + food)

# Implement the Zookeeper class here
class Zookeeper(object):
    # Implement the initializer method here
    def __init__(self, name):
        self.name = name

    # Implement the feedAnimals method here
    def feedAnimals(self, animals, food):
        print( self.name + " is feeding " + food + " to " + str(len(animals)) + " of " + str(Animal.population) + " total animals")
        for animal in animals:
            animal.eat(food)
            animal.sleep()
