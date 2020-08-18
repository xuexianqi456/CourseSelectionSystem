# This is view page's administrator view.

from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {
    'user': None
}


# administrator register
def register():
    while True:
        username = input('Supreme Administrator, please input your username:').strip()
        password = input('Supreme Administrator, please input your password:').strip()
        re_password = input('Supreme Administrator, please confirm your password:').strip()

        # judge twice password is the same
        if password == re_password:
            flag, msg = admin_interface.register_interface(
                username, password
            )

            if flag:
                print(msg)
                break

            else:
                print(msg)

        else:
            print('Twice password is not the same, please input again')


# administrator login
def login():
    while True:
        username = input('Supreme Administrator, please input your username:').strip()
        password = input('Supreme Administrator, please input your password:').strip()

        flag, msg = common_interface.login_interface(
            username, password, user_type='admin'
        )

        if flag:
            print(msg)
            admin_info['user'] = username
            break

        else:
            print(msg)


@common.auth('admin')
# administrator create school
def create_school():
    while True:
        school_name = input('Please input School\'s name:').strip()
        school_address = input('Please input School\'s address:').strip()

        flag, msg = admin_interface.create_school_interface(
            school_name, school_address, admin_info.get('user')
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)


@common.auth('admin')
# administrator create course
def create_course():
    while True:
        flag, school_list_info = common_interface.get_all_school_interface()

        if not flag:
            print(school_list_info)
            break

        for index, school_name in enumerate(school_list_info):
            print(f'ID [{index}]  School [{school_name}]')

        choice = input('Please input School\'s ID(Press q to quit):').strip()

        if choice.lower() == 'q':
            print('Quit success')
            break

        if not choice.isdigit():
            print('Please input number')
            continue

        choice = int(choice)

        if choice not in range(len(school_list_info)):
            print('Please input correct number')
            continue

        school_name = school_list_info[choice]

        course_name = input('Please input Course\'s name you want create:').strip()

        flag, msg = admin_interface.create_course_interface(
            school_name, course_name, admin_info.get('user')
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)


@common.auth('admin')
# administrator create teacher
def create_teacher():
    while True:
        teacher_name = input('Please input Teacher\'s name you want create:').strip()

        flag, msg = admin_interface.create_teacher_interface(
            teacher_name, admin_info.get('user')
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)


# administrator views
func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


# administrator views function
def admin_view():
    while True:
        print('''
        === Welcome to Administrator Panel ===
        |   1.Register           
        |   2.Login              
        |   3.Create School           
        |   4.Create Course          
        |   5.Create Teacher          
        ============== THE END ===============
        ''')

        choice = input('Please input your choice（Press q to quit）:').strip()

        if choice.lower() == 'q':
            admin_info['user'] = None
            print('Quit success')
            break

        if choice not in func_dic:
            print('Please input correct number')
            continue

        func_dic[choice]()
