
class Transcript:

    def __init__(self, ed):

        self.enrollment_dictionary = ed


    def print_transcript(self, stdnt):

        s = stdnt
        compare = int(s[0])
        # s = [id, first_name]
        totalcp = 0
        totalgp = 0

        print(s[1])
        print(format("Class", '15'), format("Credit Hours", '15'), format("Credit Points", '15'),
              format("Grade Points", '15'), format("Grade", '15'))
        for key in self.enrollment_dictionary.data:
            k = str(key)
            l = list(k)
            confirm = int(l[0])

            if confirm == compare:

                e = self.enrollment_dictionary.data[key]


                # (enroll_id, self.students[1], self.courses[1050], 4, 'A')
                # (1050, "Chemistry", 3, 1)


                creditPoints = e.course.credit_hours
                gradePoints = 0
                gradeNum = 0
                grade = str(e.grade)

                if grade == 'A':
                    gradeNum = 4

                elif grade == 'B':
                    gradeNum = 3

                elif grade == 'C':
                    gradeNum = 2

                elif grade == 'D':
                    gradeNum = 1

                elif grade == 'F' or grade == 'I' or grade == 'W':
                    gradeNum = 0
                    creditPoints = 0

                if creditPoints != 0:
                    gradePoints = gradeNum * creditPoints

                totalgp += gradePoints
                totalcp += creditPoints



                #                   class                     credit hours                  credit points                       grade points                   grade
                print(format(e.course.title, '15'), format(str(e.course.credit_hours), '15'), format(str(creditPoints), '15'), format(str(gradePoints), '15'), format(e.grade, '15'))

        print('___________________________________________________________')
        print(format(str(totalcp), '>15'), format(str(totalgp), '>30'))

        GPA = str(totalgp / (totalcp * 1.0))
        print("GPA: " + GPA)









