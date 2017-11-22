from enrollment import Enrollment
from student import Student
from course import Course
from professor import Professor
from transcript import Transcript


class GradeBook:

    def __init__(self):
        self.students = {}

        # add to student dictionary
        s = Student(1, "Carson", "Alexander", "09012005")
        self.students[s.student_id] = s
        s = Student(2, "Meredith", "Alonso", "09022002")
        self.students[s.student_id] = s
        s = Student(3, "Arturo", "Anand", "09032003")
        self.students[s.student_id] = s
        s = Student(4, "Gytis", "Barzdukas", "09012001")
        self.students[s.student_id] = s
        s = Student(5, "Peggy", "Justice", "09012001")
        self.students[s.student_id] = s
        s = Student(6, "Laura", "Norman", "09012003")
        self.students[s.student_id] = s
        s = Student(7, "Nino", "Olivetto", "09012005")
        self.students[s.student_id] = s

        self.courses = {}

        # add to course dictionary
        c = Course(1050, "Chemistry", 4, 3, 1)
        self.courses[c.course_id] = c
        c = Course(4022, "Microeconomics", 2, 3, 2)
        self.courses[c.course_id] = c
        c = Course(4041, "Macroeconomics", 3, 3, 3)
        self.courses[c.course_id] = c
        c = Course(1045, "Calculus", 1, 4, 4)
        self.courses[c.course_id] = c
        c = Course(3141, "Trigonometry", 5, 4, 5)
        self.courses[c.course_id] = c
        c = Course(2021, "Composition", 2, 3, 1)
        self.courses[c.course_id] = c
        c = Course(2042, "Literature", 3, 4, 2)
        self.courses[c.course_id] = c

        self.enrollments = {}

        # add enrolled students into courses
        enroll_id = 11050  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[1050], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14022  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4022], 'B')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 14041  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[1], self.courses[4041], 'C')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 21045  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[1045], 'D')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 23141  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[3141], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 22021  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[2], self.courses[4041], 'B')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 31050  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[3], self.courses[1050], 'C')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 41050  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[1050], 'D')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 44022  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[4], self.courses[4022], 'A')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 54041  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[5], self.courses[2021], 'B')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 61045  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[6], self.courses[1045], 'C')
        self.enrollments[enroll_id] = enrollment

        enroll_id = 73141  # combine student id + chemistry id
        enrollment = Enrollment(enroll_id, self.students[7], self.courses[3141], 'D')
        self.enrollments[enroll_id] = enrollment

        self.professors = {}

        # professor_id   first_name   last_name  hire_date
        p = Professor(1, "Kim", "Abercrombie", "1995-03-11")
        self.professors[p.professor_id] = p

        p = Professor(2, "Fadi", "Fakhouri", "2002-07-06")
        self.professors[p.professor_id] = p

        p = Professor(3, "Roger", "Harui", "1998-07-01")
        self.professors[p.professor_id] = p

        p = Professor(4, "Candace", "Kapoor", "2001-01-15")
        self.professors[p.professor_id] = p

        p = Professor(5, "Roger", "Zheng", "2004-02-12")
        self.professors[p.professor_id] = p

    # def add_student(self, id, ermnt):
    #    enrollment = ermnt
    #    self.enrollments[enroll_id] = enrollment

    #    for i in self.enrollments.values():
    #       i.display()


    def update_grade(self, eid):
        enroll_id = eid
        new_enrollment = self.enrollments[enroll_id]
        new_enrollment.grade = str(input("Enter new grade, A B C D F I or W: "))
        del self.enrollments[enroll_id]
        self.enrollments[enroll_id] = new_enrollment


    def display_student_pass(self, s_id):
        sid = s_id
        student = self.students[sid]
        student_name = student.first_name
        pass_student = [sid, student_name]
        t = Transcript(self.enrollments)
        t.print_transcript(pass_student)

    def display_all_enrollments(self):

        for key in self.enrollments:
            e = self.enrollments[key]
            print(key, e.student.student_id, e.student.first_name, e.student.last_name, e.course.title)


    def menu(self):
        x = False

        while x is False:
            choice = 0
            print("1. UPDATE GRADE")
            print("2. PRINT GPA")
            print("3. DISPLAY ALL ENROLLMENTS")
            choice = int(input("ENTER: "))

            if choice == 1:
                self.update_grade(int(input("Enter enroll id: ")))

            elif choice == 2:
                student = int(input("Enter ID of student to display: "))
                self.display_student_pass(student)

            elif choice == 3:
                self.display_all_enrollments()






