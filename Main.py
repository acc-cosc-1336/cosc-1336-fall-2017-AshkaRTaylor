from GradeBook import GradeBook
from school_db import SchoolDB
from school_initializer import SchoolInitializer

schoolInit = SchoolInitializer()
schoolDB = SchoolDB(schoolInit)

g = GradeBook(schoolDB)

g.menu()










