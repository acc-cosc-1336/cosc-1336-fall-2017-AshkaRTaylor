from enrollment import Enrollment
from student import Student
from course import Course
from professor import Professor
from transcript import Transcript
from school_initializer import SchoolInitializer
from school_db import SchoolDB


class GradeBook:

    def __init__(self, schdb):

        self.schdb = schdb
        self.schinit = SchoolInitializer()

        self.students = {}
        self.students = self.schinit.students

        self.courses = {}
        self.courses = self.schinit.courses

        self.enrollments = {}
        self.enrollments = self.schdb

        self.professors = {}
        self.professors = self.schinit.professors


    # def add_student(self, id, ermnt):
    #    enrollment = ermnt
    #    self.enrollments[enroll_id] = enrollment

    #    for i in self.enrollments.values():
    #       i.display()

    def update_grade(self, eid):
        enroll_id = eid
        new_enrollment = self.enrollments.data[enroll_id]
        new_enrollment.grade = raw_input("Enter new grade, A B C D F I or W: ")
        del self.enrollments.data[enroll_id]
        self.enrollments.data[enroll_id] = new_enrollment


    def display_student_pass(self, s_id):
        sid = s_id
        student = self.students[sid]
        student_name = student.first_name
        pass_student = [sid, student_name]
        t = Transcript(self.enrollments)
        t.print_transcript(pass_student)

    def display_all_enrollments(self):

        for key in self.enrollments.data:
            e = self.enrollments.data[key]
            print(key, e.student.student_id, e.student.first_name, e.student.last_name, e.course.title)


    def menu(self):
        x = False

        while x is False:
            choice = 0
            print("1. UPDATE GRADE")
            print("2. PRINT GPA")
            print("3. DISPLAY ALL ENROLLMENTS")
            print("4. SAVE ENROLLMENTS")
            choice = int(input("ENTER: "))

            if choice == 1:
                self.update_grade(int(input("Enter enroll id: ")))

            elif choice == 2:
                student = int(input("Enter ID of student to display: "))
                self.display_student_pass(student)

            elif choice == 3:
                self.display_all_enrollments()

            elif choice == 4:
                self.schdb.save_data()
