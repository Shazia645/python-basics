# =====================================================
# OOP practice file
# Part 1: The @property decorator
# Part 2: Polymorphism (one operator, different meanings)
# Part 3: Operator overloading with a Complex number class
# =====================================================


# -----------------------------------------------------
# PART 1: The @property decorator
# -----------------------------------------------------
class Student:
    def __init__(self, phy, math, bio):
        self.phy = phy
        self.math = math
        self.bio = bio

    # @property lets us use a method like a normal attribute:
    # stu1.percentage (no brackets).
    @property
    def percentage(self):
        # Calculated every time we ask for it, so it always
        # uses the latest marks.
        return f"{(self.phy + self.math + self.bio) / 3:.2f}%"


stu1 = Student(87, 77, 99)
print("Percentage:", stu1.percentage)

# If we change a subject's marks...
stu1.phy = 80

# ...the percentage updates by itself. Without @property we would have
# stored the percentage once in __init__, and it would stay old after
# the marks changed.
print("Percentage after changing physics marks:", stu1.percentage)

# HOMEWORK: add a getter and a setter (@percentage.setter or a private
# attribute like self._phy) to the Student class.


# -----------------------------------------------------
# PART 2: Polymorphism
# -----------------------------------------------------
# The + operator does a different job depending on the data type.
# This idea (one thing, many forms) is called polymorphism.
print(1 + 2)                                       # numbers: addition -> 3
print("hy i am shazia" + " thank u for joining me")  # strings: joining
print([1, 2, 3] + [4, 5, 6])                       # lists: merging -> [1, 2, 3, 4, 5, 6]

# Python already does this for its built-in types (this is called
# implicit operator overloading). We can do the same for our own
# classes with dunder methods, which we do next.


# -----------------------------------------------------
# PART 3: Operator overloading with a Complex number class
# -----------------------------------------------------
# Dunder methods (double underscore methods) like __add__ and __sub__
# tell Python what + and - should do for our class.
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumbers(self):
        # Shows the number like 3 + 4i or 3 - 4i
        if self.img < 0:
            print(f"{self.real} - {abs(self.img)}i")
        else:
            print(f"{self.real} + {self.img}i")

    # Runs when we write num1 + num2
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)

    # Runs when we write num1 - num2
    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal, newimg)


num1 = Complex(1, 3)
num1.showNumbers()      # 1 + 3i

num2 = Complex(7, 7)
num2.showNumbers()      # 7 + 7i

# Because of __add__ and __sub__, we can use + and - directly.
# Without them we would need our own method, like num1.add(num2).
num3 = num1 + num2
num3.showNumbers()      # 8 + 10i

num4 = num1 - num2
num4.showNumbers()      # -6 - 4i


# -----------------------------------------------------
# PRACTICE
# -----------------------------------------------------
# Try adding a __mul__ method to the Complex class.
# Formula: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i