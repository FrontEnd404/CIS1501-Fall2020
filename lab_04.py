keep_adding_students = "y"
students_and_grades = {}
while keep_adding_students == "y":
    students_and_grades[input("what is the name of the student you want to add")] = 0
    keep_adding_students = input("if you want to add more students type y if you are done adding students type n")

for key in students_and_grades:
    print(key)
    students_and_grades[key] = int(input("what is his grade out of 100"))

print(students_and_grades)
max_grade =max(students_and_grades)
print(students_and_grades[max_grade])

def get_max_student_grade():
    max_grade = max(students_and_grades)
    print(students_and_grades[max_grade])

def get_min_grade():
    min_grade = min(students_and_grades)
    print(students_and_grades[min_grade])

def get_students_grade():
    students_grade_you_want_to_get = input("name the student you want to get the grade for")
    print(students_and_grades[students_grade_you_want_to_get])

def menu_loop():
    keep_in_the_menu = "y"
    while keep_in_the_menu == "y":
        what_to_do = input("if you want to get the max student grade type max if you want to get the minimum student "
                           "garde type min and if you want to get the grade of a particular student type p if you are "
                           "done using the menu type done "
                           "  ")
        if what_to_do == "max":
            get_max_student_grade()
        elif what_to_do == "min":
            get_min_grade()
        elif what_to_do == "p":
            get_students_grade()
        else:
            break



menu_loop()






