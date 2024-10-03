# Parent class
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


# Dog class (inherits from Animal)
class Dog(Animal):
    def sound(self):
        return "Bark"


# Cat class (inherits from Animal)
class Cat(Animal):
    def sound(self):
        # super().sound()
        # super().__init__()
        return "Meow"


# Cow class (inherits from Animal)
class Cow(Animal):
    def sound(self):
        return "Moo"


# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.sound())


# Create objects for Dog, Cat, and Cow
dog = Dog()
cat = Cat()
cow = Cow()

# Demonstrating polymorphism using the same method name `sound()`
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
animal_sound(cow)  # Output: Moo


# method overloading
class Calculator:
    # Method with default arguments to simulate overloading
    def add(self, a=0, b=0, c=0):
        return a + b + c


# Create an object of the Calculator class
calc = Calculator()

# Call the method with different numbers of arguments
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9
print(calc.add())  # Output: 0 (no arguments, default values are used)


# method overrding


class Shape:
    def area(self):
        return "Undefined area"


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth


# Create objects of Circle and Rectangle
circle = Circle()
rectangle = Rectangle()

# Polymorphism in action
print(circle.area(5))  # Output: 78.5
print(rectangle.area(4, 5))  # Output: 20
