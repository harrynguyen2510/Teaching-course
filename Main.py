from Admin import Admin
from Student import Student
from Instructor import Instructor
from User import User

# 3.7.1
def show_menu(role):
    print('\nPlease enter',role,'command for further service:\n1. EXTRACT_DATA\n2. VIEW_COURSES\n3. VIEW_USERS\n4. VIEW_REVIEWS\n5. REMOVE_DATA')



# 3.7.2
def process_operations(user_object):
    # user is admin
    if type(user_object) == Admin:
        commandopt = input("")
        if commandopt != 'logout':
            if commandopt == '1':
                user_object.extract_info()
                print('s')
            elif '2' in commandopt:
                cmd_list = commandopt.split(' ')
                if len(cmd_list) == 3:
                    cmd = cmd_list[1]
                    value = cmd_list[-1]
                    user_object.view_courses([cmd,value])
                else:
                    user_object.view_courses([])
            elif commandopt == '3':
                user_object.view_users()
            elif '4' in commandopt:
                cmd_list = commandopt.split(' ')
                if len(cmd_list) == 3:
                    cmd = cmd_list[1]
                    value = cmd_list[-1]
                    user_object.view_reviews([cmd,value])
                else:
                    user_object.view_reviews([])
            elif commandopt == '5':
                user_object.remove_data()

            return None
        else:
            return 'logout'
        
    #user id instructor or student
    if type(user_object) == Instructor or Student: 
        commandopt = input("")
        if commandopt != 'logout':
            if commandopt == '1':
                User().extract_info()
            elif '2' in commandopt:
                if len(commandopt) > 1:
                    print('No other arguments are allowed.')
                else:
                    user_object.view_courses([])
            if commandopt == '3':
                User().view_users()
            elif '2' in commandopt:
                if len(commandopt) > 1:
                    print('No other arguments are allowed.')
                else:
                    user_object.view_reviews([])
            if commandopt == '5':
                User().remove_data()
            
            return None
        else:
            return 'logout'



# 3.7.2
def main():
    while True:
        inputlogin = input('Please input username and password to login:(format username password)\n')
        if inputlogin != 'exit':
            if ' ' in inputlogin:
                username = inputlogin.split(' ')[0]
                password = inputlogin.split(' ')[-1]
                temp_user = User(None,username,password)
                login_result = temp_user.login()
                user_object = None

                if login_result[0] == True:
                    # login successfully

                    role = login_result[1]
                    
                    print('\n'+role,'login successfully\n')
                    print('Welcome',role+'. Your role is',role)
                    
                    userinfo = login_result[-1]

                    # index of userinfo: 0-id; 1-username; 2-password
                    if role == 'Admin':
                        user_object = Admin(userinfo[0],userinfo[1],userinfo[2])
                    elif role == 'Student':
                        user_object = Student(userinfo[0],userinfo[1],userinfo[2])
                    elif role == 'Instructor':
                        user_object = Instructor(userinfo[0],userinfo[1],userinfo[2])
                    
                    while True:
                        show_menu(role) 
                        aftermethod = process_operations(user_object)

                        if aftermethod == 'logout\n':
                            print('\nThank you for using our system\n')
                            break
                        else:
                            continue
                else:
                    print('\nAuthentication failed: incorrect username or password\n')
            else:
                print('\nWrong format! Format should be: username password\n')
        else:
            break


if __name__ == "__main__":
    # print a welcome message
    print('\nWelcome to our system')

    # manually register admin
    new_admin = Admin(123456,'hieu_nguyen','hieung12345')
    new_admin.register_admin()

    main()






