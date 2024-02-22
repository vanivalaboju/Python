# Automation Tester Blueprint (Py System
# Class -Students,Courses, Payments - Razorpay, Stipe, Instamojo

# Object
# Student (A/B) - > Vivek, Shreeram, Vani
# Course (A/B) -> PyAtb, MTB, ATBJ, APIAT
# Payments (A/B) - Razorpay, Stipe, Instamojo

class Student:
    name = None
    phone_no =None

    def __repr__(self):
        return f"student name:{self.name} student phone# : {self.phone_no}"

    def watch_recordings(self):
        print("Reco")
        return "I am in watch_recordings"

    def do_assignment(self):
        print("Reco")

    def do_coding_q(self):
        print("Reco")


s1 = Student()
s1.name = "shreeram"
s1.phone_no = 123455789
print(s1)
print(s1.do_coding_q())
print(s1.watch_recordings())
print(s1.do_assignment())
bikas = Student()

vani = Student()


