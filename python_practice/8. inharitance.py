# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal makes a sound"


class Dog(Animal):  # Single Inheritance: Dog inherits from Animal
    def sound(self):
        return f"{self.name} barks"


# Multiple Inheritance
class Pet:
    def type(self):
        return "This is a pet"


class Cat(Animal, Pet):  # Multiple Inheritance: Cat inherits from Animal and Pet
    def sound(self):
        return f"{self.name} meows"


# Multilevel Inheritance
class Mammal(Animal):  # Multilevel Inheritance: Mammal inherits from Animal
    def warm_blooded(self):
        return "Mammals are warm-blooded"


class Cow(Mammal):  # Cow inherits from Mammal
    def sound(self):
        return f"{self.name} moos"


# Hierarchical Inheritance
class Bird(Animal):  # Hierarchical Inheritance: Bird inherits from Animal
    def sound(self):
        return f"{self.name} chirps"


class Eagle(Animal):  # Another Hierarchical Inheritance: Eagle inherits from Animal
    def sound(self):
        return f"{self.name} screeches"


# Hybrid Inheritance (Combination of Multiple and Multilevel Inheritance)
class Fish(Mammal, Pet):  # Hybrid Inheritance: Fish inherits from Mammal and Pet
    def sound(self):
        return f"{self.name} makes bubble sounds"


# Creating Objects to Demonstrate Different Types of Inheritance

# Single Inheritance
dog = Dog("Buddy")
print(dog.sound())  # Output: Buddy barks

# Multiple Inheritance
cat = Cat("Whiskers")
print(cat.sound())  # Output: Whiskers meows
print(cat.type())  # Output: This is a pet

# Multilevel Inheritance
cow = Cow("Daisy")
print(cow.sound())  # Output: Daisy moos
print(cow.warm_blooded())  # Output: Mammals are warm-blooded

# Hierarchical Inheritance
bird = Bird("Tweety")
eagle = Eagle("Hawkeye")
print(bird.sound())  # Output: Tweety chirps
print(eagle.sound())  # Output: Hawkeye screeches

# Hybrid Inheritance
fish = Fish("Goldie")
print(fish.sound())  # Output: Goldie makes bubble sounds
print(fish.warm_blooded())  # Output: Mammals are warm-blooded
print(fish.type())  # Output: This is a pet
