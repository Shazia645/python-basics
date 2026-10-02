# =====================================================
# OOP practice questions
# Q1: Circle class (area and perimeter)
# Q2: Employee class
# Q3: Engineer class (inheritance)
# Q4: Order class (comparing objects with __gt__)
# =====================================================


# -----------------------------------------------------
# Q1: Circle class
# -----------------------------------------------------
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Formula: pi * r * r.  Here we use 22/7 for pi.
        # Note: ** (power) runs before * and /, so we write
        # self.radius ** 2 and multiply it by (22/7).
        return (22 / 7) * self.radius ** 2

    def perimeter(self):
        # Formula: 2 * pi * r
        return 2 * (22 / 7) * self.radius


c1 = Circle(21)
print("Area:", round(c1.area(), 2))            # 1386.0
print("Perimeter:", round(c1.perimeter(), 2))  # 132.0


# -----------------------------------------------------
# Q2: Employee class
# -----------------------------------------------------
class Employee:
    def __init__(self, role, dep, salary):
        self.role = role
        self.dep = dep
        self.salary = salary    # salary is a number, not a string

    def showDetails(self):
        print("role =", self.role, "| dep =", self.dep, "| salary =", self.salary)


e1 = Employee("accountant", "finance", 10000)
e1.showDetails()


# -----------------------------------------------------
# Q3: Engineer class (inheritance)
# -----------------------------------------------------
# Engineer is a child of Employee, so it gets showDetails() for free.
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # super() calls the parent class (Employee) constructor.
        # Every engineer gets the same role, department and salary.
        super().__init__("Engineer", "IT", 75000)


engg1 = Engineer("shazia", 40)
engg1.showDetails()     # method inherited from Employee


# -----------------------------------------------------
# Q4: Order class (operator overloading with __gt__)
# -----------------------------------------------------
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # __gt__ is the dunder method for the "greater than" (>) operator.
    # It runs when we write odr1 > odr2.
    # self = the left object (odr1), order2 = the right object (odr2).
    def __gt__(self, order2):
        return self.price > order2.price

    def showDetails(self):
        print("item:", self.item, "| price:", self.price)


odr1 = Order("lipstick", 50)
odr1.showDetails()

odr2 = Order("mascara", 590)
odr2.showDetails()

print(odr1 > odr2)      # False, because 50 is not greater than 590
print(odr2 > odr1)      # True


# -----------------------------------------------------
# PRACTICE
# -----------------------------------------------------
# Try adding __lt__ (less than) and __eq__ (equal to) to the Order class.