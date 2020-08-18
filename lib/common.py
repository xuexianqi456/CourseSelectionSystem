# This page is to design login-authentication decorator for many users.

def auth(role):
    from core import admin
    from core import student
    from core import teacher

    def login_auth(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('Oh~ Supreme Administrator, please follow me to login first')
                    admin.login()

            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('Hey~ Small Student, login first')
                    student.login()

            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('Hello~ Dear Teacher, why not login first')
                    teacher.login()

            else:
                print('Sorry, you have no permission in this view')

        return inner

    return login_auth
