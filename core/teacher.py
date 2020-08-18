# This is view page's teacher view.

from interface import teacher_interafce
from interface import common_interface
from lib import common

teacher_info = {
    'user': None
}


# teacher login
def login():
    while True:
        username = input('Please input your username:').strip()
        password = input('Please input your password(default:123):').strip()

        flag, msg = common_interface.login_interface(
            username, password, user_type='teacher'
        )

        if flag:
            print(msg)
            teacher_info['user'] = username
            break

        else:
            print(msg)


# teacher check course
@common.auth('teacher')
def check_course():
    flag, course_list = teacher_interafce.check_course_interface(
        teacher_info.get('user')
    )

    if flag:
        print(course_list)

    else:
        print('You have no course')


# teacher choose course
@common.auth('teacher')
def t_choose_course():
    while True:
        flag1, school_list = common_interface.get_all_school_interface()

        if not flag1:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'ID [{index}]  School name[{school_name}]')

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

        flag2, course_list = common_interface.get_all_course_interface(
            school_name
        )

        if not flag2:
            print(course_list)
            break

        for index2, course_name in enumerate(course_list):
            print(f'ID [{index2}]  Course name [{course_name}]')

        choice2 = input('Please input Course\'s ID(Press q to quit):').strip()

        if choice2.lower() == 'q':
            print('Quit success')
            break

        if not choice2.isdigit():
            print('Please input number')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('Please input correct number')
            continue

        course_name = course_list[choice2]

        flag3, msg = teacher_interafce.add_course_interface(
            course_name, teacher_info.get('user')
        )
        if flag3:
            print(msg)
            break
        else:
            print(msg)


# teacher check course's student
@common.auth('teacher')
def check_course_student():
    while True:
        flag1, course_list = teacher_interafce.check_course_interface(
            teacher_info.get('user')
        )

        if not flag1:
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

        flag2, student_list = teacher_interafce.show_student_interface(
            course_name, teacher_info.get('user')
        )
        if flag2:
            print(student_list)
            break
        else:
            print('You nave not choose this Course')
            break


# teacher modify student's course score
@common.auth('teacher')
def change_score():
    while True:
        flag, course_list = teacher_interafce.check_course_interface(
            teacher_info.get('user')
        )

        if not flag:
            print(course_list)
            break

        for index, course_name in enumerate(course_list):
            print(f'ID [{index}]   Course name [{course_name}]')

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

        flag2, student_list = teacher_interafce.show_student_interface(
            course_name, teacher_info.get('user')
        )

        if not flag2:
            print(student_list)
            break

        for index2, student_name in enumerate(student_list):
            print(f'ID {index2}   Student name {student_name}')

        choice2 = input('Please input Student\'s ID(Press q to quit):').strip()

        choice2 = int(choice2)

        if choice2 not in range(len(student_list)):
            print('Please input number')
            continue

        student_name = student_list[choice2]

        score = input('Please input a score you want to modify').strip()
        if not score.isdigit():
            continue

        score = int(score)

        flag3, msg = teacher_interafce.change_score_interface(
            course_name, student_name,
            score, teacher_info.get('user')
        )

        if flag3:
            print(msg)
            break


# teacher view
func_dic = {
    '1': login,
    '2': check_course,
    '3': t_choose_course,
    '4': check_course_student,
    '5': change_score,
}


# teacher view function
def teacher_view():
    while True:
        print('''
        === Welcome to Teacher Panel ===
        |   1.Login
        |   2.Check Course
        |   3.Choose Course
        |   4.Check Student
        |   5.Modify Score
        ============THE END ============
        ''')

        choice = input('Please input you choice(Press q to quit):').strip()

        if choice.lower() == 'q':
            teacher_info['user'] = None
            print('Quit success')
            break

        if choice not in func_dic:
            print('Please input correct number')
            continue

        func_dic[choice]()
