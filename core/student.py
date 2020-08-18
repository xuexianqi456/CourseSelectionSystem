# This is view page's student view.

from interface import student_interface
from interface import common_interface
from lib import common

student_info = {
    'user': None
}


# student register
def register():
    while True:
        username = input('Rookie, input your username:').strip()
        password = input('Rookie, input your password:').strip()
        re_password = input('Rookie, confirm your password:').strip()

        # judge twice password is the same
        if password == re_password:
            flag, msg = student_interface.register_interface(
                username, password
            )

            if flag:
                print(msg)
                break

            else:
                print(msg)

        else:
            print('Twice password is not the same, please input again')


# student login
def login():
    while True:
        username = input('Rookie, input your username:').strip()
        password = input('Rookie, input your password:').strip()

        flag, msg = common_interface.login_interface(
            username, password, user_type='student'
        )

        if flag:
            print(msg)
            student_info['user'] = username
            break

        else:
            print(msg)


# student choose school
@common.auth('student')
def choose_school():
    while True:
        flag, school_list = common_interface.get_all_school_interface()

        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'ID [{index}]  School name [{school_name}]')

        choice = input('Please input School\'s ID(Press q to quit):').strip()

        if choice.lower() == 'q':
            print('Quit success')
            break

        if not choice.isdigit():
            print('Please input number')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('Please input correct number')
            continue

        school_name = school_list[choice]

        flag, msg = student_interface.choose_school_interface(
            school_name, student_info.get('user')
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)
            break


# student choose course
@common.auth('student')
def choose_course():
    while True:
        flag, course_list = student_interface.check_course_interface(
            student_info.get('user')
        )

        if not flag:
            print(course_list)
            break

        for index, course_name in enumerate(course_list):
            print(f'ID [{index}]  Course name [{course_name}]')

        choice = input('Please input Course\'s ID(Press q to quit):').strip()

        if choice.lower() == 'q':
            print('Quit success')
            break

        if not choice.isdigit():
            print('Please input number')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('Please input correct number')
            continue

        course_name = course_list[choice]

        flag, msg = student_interface.add_course_interface(
            course_name, student_info.get('user')
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)


# student check course's score
@common.auth('student')
def check_score():
    score_dic = student_interface.check_score_interface(
        student_info.get('user')
    )

    if not score_dic:
        print('You have not choose course')

    print(score_dic)


# student view
func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
}


# student view function
def student_view():
    while True:
        print('''
        === Welcome to Student Panel ===
        |   1.Register
        |   2.Login
        |   3.Choose School
        |   4.Choose Course
        |   5.Check course
        ============THE END ============
        ''')

        choice = input('Please input you choice(Press q to quit):').strip()

        if choice.lower() == 'q':
            student_info['user'] = None
            print('Quit success')
            break

        if choice not in func_dic:
            print('Please input correct number')
            continue

        func_dic[choice]()
