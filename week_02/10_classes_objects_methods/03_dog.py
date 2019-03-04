'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.

2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.

'''

#1


class Dog:

    def __init__(self, name, color, age, is_hungry=False, percent_full=100):
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = is_hungry
        self.percent_full = percent_full
#3

    def sleep(self):
        self.is_hungry = True
        self.percent_full = 0.8 * self.percent_full
#4

    def eat(self):
        self.is_hungry = False
        self.percent_full = 100
#5

    def __str__(self):
        print(self.name)
        print(self.color)
        print(self.age)
        print(self.is_hungry)
        print(self.percent_full)
#6


dog1 = Dog("Dante", "Ginger", "15", True)
dog2 = Dog("Bobo", "Black", "3", True)







