# This is teacher's interface page.

from db import models


# teacher check course interface
def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    course_list = teacher_obj.show_course()

    if not course_list:
        return False, f'Teacher [{teacher_name}] have no course'

    return True, course_list


# teacher add course interface
def add_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    course_list = teacher_obj.course_list

    if course_name in course_list:
        return False, f' Course [{course_name}] is exists, please add others'

    teacher_obj.add_course(course_name)

    return True, f'Teacher [{teacher_name}] added Course [{course_name}] success'


# teacher check course's student interface
def show_student_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    student_list = teacher_obj.show_student(course_name)

    if not student_list:
        return False, f'There is no Student choose Course [{course_name}]'

    return True, student_list


# teacher modify course's student's score interface
def change_score_interface(course_name, student_name, score, teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)

    teacher_obj.change_score(course_name, student_name, score)

    return True, f'Teacher [{teacher_name}] modify Course [{course_name}] \'s Student [{student_name}] Score to:[{score}] '
