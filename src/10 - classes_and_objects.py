"""
Classes and Objects
"""
# encapsulate variables and functions into one entity
# classes are templates to create objects

# 1. basic class


class MyClass:
    variable = "what is up?"

    def function(self):
        print("This is a message from inside the class.")

# 2. assign instance to object


class MyClass:
    variable = "what is up?"

    def function(self):
        print("This is a message from inside the class.")


my_first_object = MyClass()

# 3. accessing object variables


class MyClass:
    variable = "what is up?"

    def function(self):
        print("This is a message from inside the class.")


my_first_object = MyClass()

print(my_first_object.variable)

# 4. multiple instances


class MyClass:
    variable = "what is up?"

    def function(self):
        print("This is a message from inside the class.")


my_first_object = MyClass()
my_second_object = MyClass()

my_second_object.variable = "nothing much."

# Then print out both values
print(my_first_object.variable)
print(my_second_object.variable)

# 5. accessing object functions


class MyClass:
    variable = "what is up?"

    def function(self):
        print("This is a message from inside the class.")


my_first_object = MyClass()

my_first_object.function()


"""
YOU DO
4 minute timer
"""
# create a Vehicle class that has properties for
# name(str), kind(str), color(str), and value(float)

# add a method called "description" that returns a readable string providing the name, color, kind, and value.

# create two instances of the Vehicle class

# set the properties of each instance for a different vehicles

# call description method on each instance to test that your class worked as you expected
