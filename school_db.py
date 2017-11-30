from school_initializer import SchoolInitializer
from os.path import isfile
import pickle

class SchoolDB:

    def __init__(self, school_initializer):

        self.school_initializer = school_initializer
        self.file_name = r".\enroll.dat"
        self.data = {}

        self.data = self.school_initializer.enrollments
        self.school_initializer.enrollments = self.data

        self.load_data()


    def load_data(self):

        if isfile(self.file_name):
            self.data_file = open(self.file_name, 'rb')
            self.data = pickle.load(self.data_file)
            self.data_file.close()

    def save_data(self):
        self.data_file = open(self.file_name, 'wb')
        pickle.dump(self.data, self.data_file)
        self.data_file.close()
