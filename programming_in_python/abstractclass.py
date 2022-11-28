from abc import ABC, abstractmethod # 1. Import ABC and method

class Employee(ABC): # 2. Define ABC method, ABC inside parentheses 

    @abstractmethod
    def donate(self):
        pass

class Donation(Employee): # 3. Create sub class
    def donate(self):
        a = input("How much would you like to donate: ") # implementation for the donate function, which takes a user inputs, stores it in variable a, and returns it
        return a

amounts = []
john = Donation() # create two employee instances called John and Peter and call the function over each of them
j = john.donate()
amounts.append(j) # Create a list amounts, to which the returned values will be appended

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)