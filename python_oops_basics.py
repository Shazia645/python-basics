# ==========================================
# Python Object-Oriented Programming (OOP)
# Fundamentals & Examples
# ==========================================

# ------------------------------------------
# 1. Basic Class & Instance Variables
# ------------------------------------------
# 'self' represent karta hai instance ko. Jab bhi har object ka
# data alag store karna ho, hum 'self.variable_name' use karte hain.

class Student:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

# Objects (Instances) Creation
s1 = Student("maths", 90) 
print(s1.subject, s1.marks) 

s2 = Student("phy", 90) 
print(s2.subject, s2.marks)

s3 = Student("english", 90) 
print(s3.subject, s3.marks)

s4 = Student("chy", 90) 
print(s4.subject, s4.marks)

s5 = Student("urdu", 90) 
print(s5.subject, s5.marks)

s6 = Student("computer", 90) 
print(s6.subject, s6.marks)


# ------------------------------------------
# 2. Calculating Average Marks using Method
# ------------------------------------------
class StudentAverage:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total_sum = 0
        for val in self.marks:
            total_sum += val
        
        # Average calculate loop ke bahar hoga taakay sahi average aaye
        avg_score = total_sum / len(self.marks)
        print(f"Hi {self.name}, your average score is: {avg_score:.2f}")

# Example Usage
s1_avg = StudentAverage("Shazia", [98, 97, 99])
s1_avg.get_avg()


# ------------------------------------------
# 3. Class Attributes vs Object Attributes
# ------------------------------------------
class CarAttributes:
    # Class Attributes (Shared by all instances)
    color = "red"
    brand = "mercedes"

car1 = CarAttributes()
print("Car Color:", car1.color)
print("Car Brand:", car1.brand)


# ------------------------------------------
# 4. Abstraction, Encapsulation & Methods
# ------------------------------------------
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started successfully!")

    # Static method (Doesn't need 'self')
    @staticmethod
    def hello():
        print("Welcome to the Car Application")

# Example Usage
Car.hello()
car1 = Car()
car1.start()


# ------------------------------------------
# 5. Practical Example: Bank Account System
# ------------------------------------------
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_no = acc_no

    # Debit Method (Withdraw Money)
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs. {amount} was debited.")
        else:
            print("Insufficient Balance!")
        print("Total Balance =", self.get_balance())

    # Credit Method (Deposit Money)
    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited.")
        print("Total Balance =", self.get_balance())

    # Get Current Balance
    def get_balance(self):
        return self.balance

# Example Usage
print("\n--- Bank Account Transaction ---")
acc1 = Account(1000, 12345)
acc1.debit(1000)
acc1.credit(5000)
acc1.credit(10000)

