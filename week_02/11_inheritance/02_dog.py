'''

Building on the dog class from the previous example, create a subclass of the dog class
with at least one additional attribute. Also, override the sleep() and eat() methods to act
slightly different.

Create and object of this class and demonstrate it's functionality.

'''


class Dog:

    def __init__(self, name, color, age, is_hungry=False, percent_full=100):
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = is_hungry
        self.percent_full = percent_full


class Pugs(Dog):

    def __init__(self, name, color, age, is_hungry=False, percent_full=100, ears="Floppy"):
        super().__init__(name, color, age, is_hungry, percent_full)
        self.ears = ears


puggy = Pugs("Rex", "brown", 8, True, 40, "Spiky")

print(puggy.name, puggy.ears)


