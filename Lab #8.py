class Dog_1:
    pass
dog1 = Dog_1()
dog2 = Dog_1()

print(dog1)
print(dog2)

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Buddy", 3)
print(cat1.name)
print(cat1.age)

class DogBehavoir:
    
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name, "says Woof!")

db1 = DogBehavoir("Buddy")
db1.bark()

class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(2, 3))
print(calc.multiply(4, 5))

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def display(self):
        print(self.owner, "has", self.balance)

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.display()

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

    def display(self):
        print(f"Count: {self.count}")

counter = Counter()
counter.increment()
counter.increment()
counter.display()

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10
    
    def brake(self):
        self.speed -= 5
    
    def display(self):
        print(f"Car brand: {self.brand}")
        print(f"Car speed: {str(self.speed)}")
               
    
car1 = Car("Toyota", 50)
car1.accelerate()
car1.brake()
car1.display()

# --Reflection--

# 1. A class is a template that can be used to make instances of objects

# 2. A object is a instance of a class that uses that class template and defines the varibles.

# 3. A method is a function that belongs to a class

# 4. The state of a object can change in multiple ways. Like in this code using the accelerate function changes the state of the object.
# Anything that modifies the orginal default values is a state change.

