class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_details(self):
        print(f"employee name: {self.name}")
        print(f"employee salary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def display_total_salary(self):
        total=self.salary+self.bonus
        print(f"total salary:{total}")
m=Manager("sravs",50000,10000)
m.display_details()
m.display_total_salary()
