# This is administrator's interface page.

from db import models


# administrator register interface
def register_interface(username, password):
    admin_obj = models.Admin.select(username)

    if admin_obj:
        return False, f'Username [{username}] is exist, please use others'

    admin_obj = models.Admin(username, password)
    admin_obj.save()

    return True, f'Administrator [{username}] login success'


# administrator create school interface
def create_school_interface(school_name, school_address, admin_name):
    school_obj = models.School.select(school_name)

    if school_obj:
        return False, f'School [{school_name}] is exists, please create other school'

    admin_obj = models.Admin.select(admin_name)

    admin_obj.create_school(school_name, school_address)

    return True, f'School [{school_name}] create success'


# administrator create course interface
def create_course_interface(school_name, course_name, admin_name):
    school_obj = models.School.select(school_name)

    if course_name in school_obj.course_list:
        return False, f'Course [{course_name}] is exist, please create other course'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj, course_name)

    return True, f'Administrator [{admin_name}] created Course [{course_name}] in School [{school_name}]'


# administrator create teacher interface
def create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
    teacher_obj = models.Teacher.select(teacher_name)

    if teacher_obj:
        return False, f'Teacher [{teacher_name}] is exist, please create other teacher name'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)

    return True, f'Administrator [{admin_name}] created Teacher [{teacher_name}] success'
