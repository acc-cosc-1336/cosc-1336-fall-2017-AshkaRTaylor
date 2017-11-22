from person import Person


class Student(Person):

    def __init__(self, sid, fn, ln, ed):

        super(Student, self).__init__(fn, ln)
        self.student_id = sid
        self.enroll_date = ed
