# This is common's interface page

import os
from db import models
from conf import settings


# common login interface
def login_interface(user, pwd, user_type):
    if user_type == 'admin':
        obj = models.Admin.select(user)

    elif user_type == 'student':
        obj = models.Student.select(user)

    elif user_type == 'teacher':
        obj = models.Teacher.select(user)

    else:
        return False, 'Login role error, please login again'

    if obj:
        if pwd == obj.pwd:
            return True, f'{user_type}[{user}] login success'
        else:
            return False, 'Password error, please try again'

    else:
        return False, 'This username isn\'t exist'


# get all school interface
def get_all_school_interface():
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )

    if not os.path.exists(school_dir):
        return False, 'There is no any school, please contact Administrator to create school first'

    school_list = os.listdir(school_dir)

    return True, school_list


# get all course interface
def get_all_course_interface(school_name):
    school_obj = models.School.select(school_name)

    course_list = school_obj.course_list

    if course_list:
        return True, course_list

    return False, f'Sorry, {school_name} do\'t have any course'
