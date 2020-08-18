# This page is to design class model.

from db import db_handler


class Base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    def save(self):
        db_handler.save_data(self)


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def create_school(self, school_name, school_address):
        school_obj = School(school_name, school_address)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        course_obj = Course(course_name)
        course_obj.save()
        school_obj.course_list.append(course_name)
        school_obj.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, school_name, school_address):
        self.user = school_name
        self.address = school_address
        self.course_list = []


class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Student(Base):
    def __init__(self, student_name, student_password):
        self.user = student_name
        self.pwd = student_password
        self.school = None
        self.course_list = []
        self.score_dic = {}

    def choose_school(self, school_name):
        self.school = school_name
        self.save()

    def choose_course(self, course_name):
        self.course_list.append(course_name)
        self.score_dic[course_name] = 80  # Set default score:80
        self.save()

        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()


class Teacher(Base):
    def __init__(self, teacher_name, teacher_password):
        self.user = teacher_name
        self.pwd = teacher_password
        self.course_list = []

    def show_course(self):
        return self.course_list

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def show_student(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def change_score(self, course_name, student_name, score):
        student_obj = Student.select(student_name)
        student_obj.score_dic[course_name] = score
        student_obj.save()
