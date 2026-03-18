<<<<<<< HEAD
def s_marks(m1,m2,m3):
    return m1+m2+m3

def s_percentage(total):
    return total/3

def s_grade(per):
    if per>=90:
        return "A"
    elif per>=75:
        return "B"
    elif per>=60:
        return "C"
    elif per>=40:
        return "D"
    else:
        return "Fail"

while True:
    print("Grade Managent System")

    name=input("Enter the Student name:")
    mark1=int(input("Enter makrs of sub1:"))
    mark2=int(input("Enter makrs of sub2:"))
    mark3=int(input("Enter makrs of sub3:"))

    total = s_marks(mark1,mark2,mark3)
    per = s_percentage(total)
    grade = s_grade(per)

    print("\n Student Report ")
    print("Name:",name)
    print("Total marks",total)
    print("Percentage:",per)
    print("Grade:",grade)

    choice = input("Do you want to add another student? (yes/no)")
    if choice.lower() != "yes":
        print("Program Ended. Tahnk you")
        break
=======
def s_marks(m1,m2,m3):
    return m1+m2+m3

def s_percentage(total):
    return total/3

def s_grade(per):
    if per>=90:
        return "A"
    elif per>=75:
        return "B"
    elif per>=60:
        return "C"
    elif per>=40:
        return "D"
    else:
        return "Fail"

while True:
    print("Grade Managent System")

    name=input("Enter the Student name:")
    mark1=int(input("Enter makrs of sub1:"))
    mark2=int(input("Enter makrs of sub2:"))
    mark3=int(input("Enter makrs of sub3:"))

    total = s_marks(mark1,mark2,mark3)
    per = s_percentage(total)
    grade = s_grade(per)

    print("\n Student Report ")
    print("Name:",name)
    print("Total marks",total)
    print("Percentage:",per)
    print("Grade:",grade)

    choice = input("Do you want to add another student? (yes/no)")
    if choice.lower() != "yes":
        print("Program Ended. Tahnk you")
        break
>>>>>>> 1a7c192261d8cb08888d1c0830130fba219b7b99
    