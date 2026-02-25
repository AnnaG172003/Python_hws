grade1, grade2, grade3 = input("Enter your grades(e.g, A B C D F): ").split()
g1 = 0
g2 = 0
g3 = 0

if grade1 =="A":
    g1 += 4.0
elif grade1 =="B":
    g1 += 3.0
elif grade1 == "C":
    g1 += 2.0
elif grade1 == "D":
    g1 += 1.0
elif grade1 == "F":
    g1 += 0.0
else:
    print("Invalid input")

if grade2 =="A":
    g2 += 4.0
elif grade2 =="B":
    g2 += 3.0
elif grade2 == "C":
    g2 += 2.0
elif grade2 == "D":
    g2 += 1.0
elif grade2 == "F":
    g2 += 0.0
else:
    print("Invalid input")

if grade3 =="A":
    g3 += 4.0
elif grade3 =="B":
    g3 += 3.0
elif grade3 == "C":
    g3 += 2.0
elif grade3 == "D":
    g3 += 1.0
elif grade3 == "F":
    g3 += 0.0
else:
    print("Invalid input")


total_score = g1 + g2 + g3
gpa = total_score/3
print("Your GPA is: ", gpa)