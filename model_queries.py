
from student.models import *


# -----------------------------
# 1) Create an advisor
# -----------------------------
advisor1 = Advisor.objects.create(fname="Henry", lname="Sherman")

# -----------------------------
# 2) Create two courses
# -----------------------------
course1 = Course.objects.create(dept="DEM", course_num=200, subject="Demo-Intro to Wagner")
course2 = Course.objects.create(dept="DEM", course_num=301, subject="Demo-Quantum Mechanics")

# -----------------------------
# 3) Create two students
# -----------------------------
student1 = Student.objects.create(fname="Betty", lname="Boop", student_advisor=advisor1)
student2 = Student.objects.create(fname="Annie", lname="Hall", student_advisor=advisor1)

# -----------------------------
# 4) Assign students to courses
# -----------------------------
course1.students.add(student1, student2)  # Both students in course1
student1.courses.add(course2)             # student1 also in course2

# -----------------------------
# 5) Query a student’s courses
# -----------------------------
student1.courses.all()

# -----------------------------
# 6) Query a course’s students
# -----------------------------
course1.students.all()

# -----------------------------
# 7) Query an advisor’s advisees
# -----------------------------
advisor1.advisees.all()

# -----------------------------
# 8) Add another course to a student
# -----------------------------
course3 = Course.objects.create(dept="DEM", course_num=210, subject="World History")
student2.courses.add(course3)

# -----------------------------
# 9) Query updated student courses
# -----------------------------
student2.courses.all()

# -----------------------------
# 10) Simple filter: students in course1
# -----------------------------
students_in_course1 = Student.objects.filter(courses=course1)
students_in_course1





