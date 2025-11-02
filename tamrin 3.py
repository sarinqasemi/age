def calculate_student_gpa(student):
    grades = student["grades"]
    return sum(grades) / len(grades)

students_list = [
    { "student_id" : 1 , "name" : "Ali" , "grades" : [12 , 16 , 17] },
    { "student_id" : 2 , "name" : "Zahra" , "grades" : [15 , 19 , 10] }
]

for stdnt in students_list:
    avg = calculate_student_gpa(stdnt)
    print(stdnt["name"] , ":")
    print("avarage" , avg , "\n")
