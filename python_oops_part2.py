# ==========================================
# Python Object-Oriented Programming (Part 2)
# ==========================================

# ------------------------------------------
# 1. The 'del' Keyword
# ------------------------------------------
class Student:
    def __init__(self, name):
        self.name = name  # Public attribute

s1 = Student("Shazia")
print("Student Name:", s1.name)

# Deleting the attribute
del s1.name
# print(s1.name)  # Uncommenting this line will raise an AttributeError

# ------------------------------------------
# 2. Private Attributes (Encapsulation)
# ------------------------------------------
class PrivateStudent:
    def __init__(self, name):
        self.__name = name  # Private attribute (prefixed with double underscore)

    # Getter method to access private variable safely
    def get_name(self):
        return self.__name

s2 = PrivateStudent("Shazia")
print("Private Student Name (via Getter):", s2.get_name())

# ------------------------------------------
# 3A. Single Inheritance
# ------------------------------------------
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
print("\nCar Name:", car1.name)
car1.start()  # Calling inherited method


# ------------------------------------------
# 3B. Multilevel Inheritance
# ------------------------------------------
class MultilevelCar(Car):
    def __init__(self, brand):
        self.brand = brand

class FortunerModel(MultilevelCar):
    def __init__(self, fuel_type, brand="Toyota"):
        super().__init__(brand)
        self.fuel_type = fuel_type

fortuner_car = FortunerModel("Diesel")
print("\nMultilevel - Brand:", fortuner_car.brand)
print("Multilevel - Fuel Type:", fortuner_car.fuel_type)
fortuner_car.start()
# 3C. Multiple Inheritance
# ------------------------------------------
class ClassA:
    var_a = "Welcome to Class A"

class ClassB:
    var_b = "Welcome to Class B"

class ClassC(ClassA, ClassB):
    var_c = "Welcome to Class C"

c1 = ClassC()
print("\nMultiple Inheritance Outputs:")
print(c1.var_c)
print(c1.var_b)
print(c1.var_a)


# ------------------------------------------
# 4. The super() Method
# ------------------------------------------
class Dress:
    def __init__(self, color):
        self.color = color
    @staticmethod
    def show_black():
        print("Color is black.")

class Trouser(Dress):
    def __init__(self, name, color):
        self.name = name
        super().__init__(color)  # Calling parent class constructor

dress1 = Trouser("Cargo Trouser", "Black")
print("\nSuper Method - Name:", dress1.name)
print("Super Method - Color:", dress1.color)
dress1.show_black()
        