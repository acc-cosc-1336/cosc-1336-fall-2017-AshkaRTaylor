from person import Person


class Professor(Person):

    def __init__(self, pid, fn, ln, hd):

        super(Professor, self).__init__(fn, ln)
        self.professor_id = pid
        self.hire_date = hd
