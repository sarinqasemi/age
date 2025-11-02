def avarage(num):
    return sum(num) / len(num)


numbers = int(input("enter number of lessons:"))
grades = []
for i in range(numbers):
    grade = int(input(f"enter lessons {i+1}:"))
    grades.append(grade)

avg = avarage(grades)
if avg >= 17:
    print("great")
elif avg >= 12:
    print("passed")
else:
    print("conditional")      

    