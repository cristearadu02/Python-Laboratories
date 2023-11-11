
# Exercitiul 1 - Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle, Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape

import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def __str__(self):
        return f"Shape: {self.__class__.__name__} - Area: {self.area()} - Perimeter: {self.perimeter()}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Exercitiul 2 - Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount.
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"Account: {self.__class__.__name__} - Account number: {self.account_number} - Balance: {self.balance}"
    
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def interest_calculation(self):
        return self.balance * self.interest_rate

    def __str__(self):
        return super().__str__() + f" - Interest rate: {self.interest_rate}"
    
class CheckingAccount(Account):
    def __init__(self, account_number, balance, limit):
        super().__init__(account_number, balance)
        self.limit = limit

    def withdrawal(self, amount):
        if self.balance - amount < self.limit:
            print("You don't have enough money!")
        else:
            self.balance -= amount

    def __str__(self):
        return super().__str__() + f" - Overdraft limit: {self.limit}"


# Exercitiul 3 - Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types of vehicles like
# Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        if self.fuel_efficiency * 50 < distance:
            return "You don't have enough fuel!"
        else:
            return "You can ran the distance!"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self, distance):
        if self.year < 2010:
            return distance / 40
        else:
            return distance / 60

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"{self.towing_capacity} tons"


# Exercitiul 4 - Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like
# Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their roles.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"{self.name} - {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus, people_managed):
        super().__init__(name, salary)
        self.bonus = bonus
        self.people_managed = people_managed

    def display_info(self):
        return super().display_info() + f" - {self.bonus}" + f" - {self.people_managed}"

    def verify_people_managed(self):
        if self.people_managed > 10:
            return "This manager has too many people to manage!"
        else:
            return "This manager has a good number of people to manage!"

class Engineer(Employee):
    def __init__(self, name, salary, degree, department):
        super().__init__(name, salary)
        self.degree = degree
        self.department = department

    def display_info(self):
        return super().display_info() + f" - {self.degree}" + f" - {self.department}"

    def calculate_performance_bonus(self):
        if self.department == "IT":
            if self.degree == "Bachelor":
                return self.salary * 0.3
            elif self.degree == "Master":
                return self.salary * 0.35
            else:
                return self.salary * 0.1
        else:
            return self.salary * 0.05

class Salesperson(Employee):
    def __init__(self, name, salary, sales, target):
        super().__init__(name, salary)
        self.sales = sales
        self.target = target


    def display_info(self):
        return super().display_info() + f" - {self.sales}" + f" - {self.target}"

    def calculate_performance_bonus(self):
        if self.sales > self.target:
            return self.salary * 0.35
        else:
            return self.salary * 0.15


# Exercitiul 5 - Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird, and Fish.
# Add properties and methods to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def display_info(self):
        return f"{self.name} - {self.age} - {self.weight}"

class Mammal(Animal):
    def __init__(self, name, age, weight, hair_color):
        super().__init__(name, age, weight)
        self.hair_color = hair_color

    def display_info(self):
        return super().display_info() + f" - {self.hair_color}"

    def how_they_give_birth(self):
        return "Mammals give birth to miniature versions of themselves and feed them with milk."

    def how_they_move(self):
        return "Mammals move by walking, running, hopping, crawling, swimming, climbing"

class Bird(Animal):
    def __init__(self, name, age, weight, feather_color):
        super().__init__(name, age, weight)
        self.feather_color = feather_color

    def display_info(self):
        return super().display_info() + f" - {self.feather_color}"

    def how_they_give_birth(self):
        return "Birds lay eggs."

class Fish(Animal):
    def __init__(self, name, age, weight, scale_color):
        super().__init__(name, age, weight)
        self.scale_color = scale_color

    def display_info(self):
        return super().display_info() + f" - {self.scale_color}"

    def how_they_give_birth(self):
        return "Fish lay eggs."


# Exercitiul 6 - Design a library catalog system with a base class LibraryItem and subclasses for different types of items like
# Book, DVD, and Magazine. Include methods to check out, return, and display information about each item

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def display_info(self):
        status = "checked out" if self.checked_out else "available"
        return f"{self.title} by {self.author} (ID: {self.item_id}) - {status}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        return super().display_info() + f" - Genre: {self.genre}"

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return super().display_info() + f" - Director: {self.director}, Duration: {self.duration} minutes"

class Magazine(LibraryItem):
    def __init__(self, title, issue_number, item_id):
        super().__init__(title, "Unknown", item_id)
        self.issue_number = issue_number

    def display_info(self):
        return super().display_info() + f" - Issue Number: {self.issue_number}"



if __name__ == '__main__':

    # Exercitiul 1
    print("Exercitiul 1")
    circle = Circle(5)
    rectangle = Rectangle(5, 10)
    triangle = Triangle(3, 4, 5)

    print(circle)
    print(rectangle)
    print(triangle)

    # Exercitiul 2
    print("\nExercitiul 2")
    savings_account = SavingsAccount(123456789, 1000, 0.1)
    checking_account = CheckingAccount(987654321, 500, 100)

    savings_account.deposit(100)
    checking_account.deposit(100)
    savings_account.withdrawal(200)
    checking_account.withdrawal(200)
    savings_account.interest_calculation()

    print(savings_account)
    print(checking_account)

    # Exercitiul 3
    print("\nExercitiul 3")
    best_car_in_the_world = Car("Opel", "Astra", 2011, 5)
    motorcycle = Motorcycle("Honda", "CBR", 2005)
    truck = Truck("Volvo", "FH", 2015, 20)

    print(best_car_in_the_world.display_info())
    print(motorcycle.display_info())
    print(truck.display_info())

    print("Calculate mileage opel:", best_car_in_the_world.calculate_mileage(100))
    print(motorcycle.calculate_mileage(100))
    print(truck.calculate_towing_capacity())

    # Exercitiul 4
    print("\nExercitiul 4")
    manager = Manager("John", 1000, 200, 10)
    engineer = Engineer("Mike", 500, "Bachelor", "IT")
    salesperson = Salesperson("Anna", 300, 200, 100)

    print(manager.display_info())
    print(engineer.display_info())
    print(salesperson.display_info())

    print(" IT Engineer bonus:",engineer.calculate_performance_bonus())
    print(" Salesperson bonus",salesperson.calculate_performance_bonus())
    print(" Manger verify:",manager.verify_people_managed())

    # Exercitiul 5
    print("\nExercitiul 5")
    dog = Mammal("Dog", 5, 10, "Brown")
    eagle = Bird("Eagle", 10, 5, "Black")
    shark = Fish("Shark", 2, 100, "Grey")

    print(dog.display_info())
    print(eagle.display_info())
    print(shark.display_info())

    print("How they give birth:")
    print("Dog:", dog.how_they_give_birth())
    print("Eagle:", eagle.how_they_give_birth())
    print("Shark:", shark.how_they_give_birth())

    print("Dog: ", dog.how_they_move())

    # Exercitiul 6
    print("\nExercitiul 6")
    book = Book("Singur pe lume", "Hector Malot", 1, "Nuvela")
    dvd = DVD("Inception", "Christopher Nolan", 2, 148)
    magazine = Magazine("National Geographic", 202, 3)

    print(book.display_info())
    print(book.check_out())
    print(book.display_info())
    print(book.return_item())
    print(book.display_info())

    print(dvd.display_info())
    print(dvd.check_out())
    print(dvd.display_info())

    print(magazine.display_info())















