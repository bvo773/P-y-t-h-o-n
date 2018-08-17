# Instance variable: Datas are unique for each instance
# Class variable: variables(Datas) that are shared among all instances of a class
# Class method is declared by adding a decorator and uses a cls argument -> Usually to create an instance
# Static method doesn't have cls and self as arguments
class Employee:
    raiseAmount = 1.04 # class var
    numOfEmployees = 0

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName # instance var
        self.lastName = lastName # instance var
        self.salary = salary # instance var
        Employee.numOfEmployees += 1 # class var

    def printFullName(self):
        return (f'{self.firstName} {self.lastName}')

    def raiseSalary(self):
        self.salary = int(self.salary * Employee.raiseAmount)

  
    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount
 
    @classmethod
    def fromStringCreateEmployee(cls, string):
        first, last, pay = string.split('-')  
        return cls(first, last, pay) 

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 6 or day.weekday() == 7:
            return False
        return True

class Developer(Employee):
    raiseAmount = 1.10
    pass

emp1 = Developer('Binh', 'Vo', 65000)
emp1.raiseSalary()
print(emp1.salary)


emp2 = Employee('Trash', 'Bin', 40000)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

emp_str_3 = 'David-Lee-90000'
emp3 = Employee.fromStringCreateEmployee(emp_str_3)

# print(help(Developer))
Employee.setRaiseAmount(1.05)

# Both ways are ==, Using an instance to call a method
# Using a Class and pass in the instance for it to reference it-'self'
print(emp1.printFullName())  
print(Employee.printFullName(emp1))
print(emp2.__dict__) # Getting all attributes of an instance or a class

import datetime
day_off = datetime.date(2018, 8, 17)
print(Employee.isWorkday(day_off))
