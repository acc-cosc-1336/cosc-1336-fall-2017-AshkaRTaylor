from GradeBook import GradeBook
from enrollment import Enrollment
from student import Student
from course import Course

g = GradeBook()

x = False
while x == False:
    selection = 0

    while selection <= 0 or selection > 3:
        print("1. ADD STUDENT")
        print("2. SEARCH STUDENT & UPDATE")
        print("3. DISPLAY ALL STUDENTS")
        selection = int(input("Enter selection: "))

        if selection <= 0 and selection > 3:
            print("Invalid selection.")

    if selection == 1:
        s1 = []
        s1.append(int(input("Enter student ID: ")))
        s1.append(str(input("Enter student first name: ")))
        s1.append(str(input("Enter student last name: ")))
        s1.append(str(input("Enter enroll data: ")))
        sa = s1[0]
        sb = s1[1]
        sc = s1[2]
        sd = s1[3]
        s = Student(sa, sb, sc, sd)
        c1 = []
        c1.append(int(input("Enter course ID: ")))
        c1.append(str(input("Enter course name: ")))
        ca = c1[0]
        cb = c1[1]
        c = Course(ca, cb, sa)
        enrollID = str(s1[0],) + str(c1[0])
        enrollment = (enrollID, s, c)
        g.add_student(enrollID, enrollment)
    elif selection == 2:
        
        g.enrollments[11050].grade = 'B'

    elif selection == 3:
        for enroll in g.enrollments.values():
            print(enroll.course.title, enroll.student.first_name, enroll.grade)






