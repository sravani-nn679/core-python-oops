class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_marks(self):
        print(f"name:{self.name}")
        print(f"marks:{self.marks}")
class Result(Student):
    def check_result(self):
        if self.marks>=35:
            print("passed")
        else:
            print("failed")
s=Result("sravs",40)
s.display_marks()
s.check_result()
s1=Result("valli", 45)
s1.display_marks()
s1.check_result()





