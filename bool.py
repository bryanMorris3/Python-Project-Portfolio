myGrade = input("What score did you get?")
myGrade = int(myGrade)
myLetterGrade = "Not Assigned"
if myGrade >= 90:
    myLetterGrade = "A"
elif myGrade >=80:
    myLetterGrade = "B"
elif myGrade >=70:
    myLetterGrade = "C"
elif myGrade >=60:
    myLetterGrade = "D"
elif myGrade >=50:
    myLetterGrade = "F"    
print("My grade is:", myLetterGrade)
