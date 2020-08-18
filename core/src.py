# This is view page's primary view.

from core import admin
from core import student
from core import teacher

# view dic
func_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


# run function
def run():
    while True:
        print('''
        === Welcome to Course Selection System ===
        |   1.Administrator View
        |   2.Student View
        |   3.Teacher View
        ================= THE END ================
        ''')

        choice = input('Please input your choice:').strip()

        if choice not in func_dic:
            print('Please input correct number')
            continue

        func_dic[choice]()
