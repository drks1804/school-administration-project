condition = True
student_num = 1

while(condition):
    student_info = input("enter student info for student #{} in the format name age contact_number: ".format(student_num))

    student_info_list = student_info.split(' ')
    print("entered information: " + str(student_info_list))


          

    choice_check = input("is entered data correct? (yes/no): ")

    if choice_check == "yes":
        print("ok proceed")

        condition_check = input("enter (yes/no) if you want to enter information of new student: ")
        if condition_check == "yes":
            condition = True
            student_num = student_num + 1
        elif condition_check == "no":
            condition = False

    elif choice_check == "no":
        print("re-enter information of student: ")
                        
                         
     
                         
        
