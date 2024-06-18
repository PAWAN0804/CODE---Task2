name = input("Enter the name of the student")
print("Please Enter the Marks Obtained in SSc Examination: ")

English = float(input("Enter the marks obtained in English: "))
Hindi = float(input("Enter the marks obtained in Hindi: "))
Maths= float(input("Enter the marks obtained in Maths: "))
Science = float(input("Enter the marks obtained in Science: "))
History = float(input("Enter the marks obtained in History: "))


total_marks = (English + Hindi + Maths + Science + History)
avg_marks= (total_marks)/5
print(f"dear{name}, you obtained {total_marks}total & {avg_marks} average marks in your SSC Examination.")


if avg_marks>=91 and avg_marks<=100:
    print("Your Grade is A1")
elif avg_marks>=81 and avg_marks<91:
    print("Your Grade is A2")
elif avg_marks>=71 and avg_marks<81:
    print("Your Grade is B1")
elif avg_marks>=61 and avg_marks<71:
    print("Your Grade is B2")
elif avg_marks>=51 and avg_marks<61:
    print("Your Grade is C1")
elif avg_marks>=41 and avg_marks<51:
    print("Your Grade is C2")
else:
    print("Better Luck Next Time! You're Failed")


