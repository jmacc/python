#Ejemplo de error TypeError: __init__() missing 1 required positional argument
'''
class Person():
    def __init__(self,name):
        self.name = name


class Employee(Person):
    # 👇️ takes `name` arg
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary = salary

emp1 = Employee("lUIS ",1000)
print(emp1.name)
print(emp1.salary)
'''
class Employee():
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return "Mi nombre es " + self.name
    
empl = Employee("Mario")
print(empl)
