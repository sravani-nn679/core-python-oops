#multilevel
class Course:
    def fee(self, course):
        if course=="java":
            return 30000
        elif course=="python":
            return 27000
        else:
            return 0
class Academy(Course):
    def courses(self):
        print("java-30000")
        print("python-27000")
    def billing(self,total):
        if total==0:
            print("Invalid course")
        else:
            final=total+100#registration fee
            print(final)
    def enroll(self):
        self.courses()
        total=0
        n=int(input("enter no of courses:"))
        i=0
        while i<n:
            course=input("enter name of the course:")
            courseprize=self.fee(course)
            if courseprize==0:
                print("invalid course")
            else:
                total=total+courseprize
                i+=1
        self.billing(total)
class Student(Academy):
    pass
s=Student()
s.enroll()
