# This is student's interface page.

from db import models


# student register interface
def register_interface(username, password):
    student_obj = models.Student.select(username)

    if student_obj:
        return False, f'Username [{username}] is exists, please try other username'

    student_obj = models.Student(username, password)
    student_obj.save()

    return True, f'Student [{username}] registered success'


# student choose school interface
def choose_school_interface(school_name, student_name):
    student_obj = models.Student.select(student_name)

    if student_obj.school:
        return False, 'You already have one school'

    student_obj.choose_school(school_name)
    return True, f'Student[{school_name}] choosed School [{school_name}] success'


# student check course interface
def check_course_interface(student_name):
    # get current student object
    student_obj = models.Student.select(student_name)
    school_name = student_obj.school

    if not school_name:
        return False, 'Please choose School first'

    school_obj = models.School.select(school_name)

    course_list = school_obj.course_list

    if not course_list:
        return False, 'There is no course, please contact Administrator to create course first'

    return True, course_list


# student choose course interface
def add_course_interface(course_name, student_name):
    student_obj = models.Student.select(student_name)

    if course_name in student_obj.course_list:
        return False, f'Course [{course_name}] is already in you course_list'

    student_obj.choose_course(course_name)

    return True, f'Student [{student_name}] added Course [{course_name}] success'


# student check course's score interface
def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)

    if student_obj.score_dic:
        return student_obj.score_dic
