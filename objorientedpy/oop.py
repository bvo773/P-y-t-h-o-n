# Instance variable: Datas are unique for each instance
# Class variable: variables(Datas) that are shared among all instances of a class
class Employee:
    raiseAmount = 1.04 # class var

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName # instance var
        self.lastName = lastName # instance var
        self.salary = salary # instance var

    def printFullName(self):
        return (f'{self.firstName} {self.lastName}')

    def raiseSalary(self):
        self.pay = int(self.pay * Employee.raiseAmount)

emp1 = Employee('Binh', 'Vo', '$65000')

# Both ways are ==,
print(emp1.printFullName()) # Using an instance to call a method
print(Employee.printFullName(emp1)) # Using a Class and pass in the instance for it to reference it-'self'
# Getting all attributes of an instance or a class
print(emp1.__dict__)