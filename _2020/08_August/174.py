"""
Describe and give an example of each of the following types of polymorphism:

    Ad-hoc polymorphism
    Parametric polymorphism
    Subtype polymorphism

"""

# Ad hoc polymorphism
#  - Apply functions to different types
#  - e.g. Operator overloading [1] + [2] = [1, 2], 1 + 2 = 3

# Parametric polymorphism
# - Handles values independent of their type
# e.g. v = [] v.append(1), v.append([1, 2, 3])
# The append function does the same thing with different types

# Subtype polymorphism
# - classic polymorphism
# class Animal:
# class Duck(Animal)
# e.g. Class Number
# class Integer(Number)
# class float(Number)
# Can call max() or both integer and float
