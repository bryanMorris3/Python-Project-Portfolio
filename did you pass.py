#Bryan Morris
#9/23/19
#Did I pass?
#User inputs the grade
myGrade = input("What score did you get?")
myGrade = int(myGrade)
#Assign starting grade
myLetterGrade = "Not Assigned"
#Show letter grade for scores
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
#print out the grade
print("My grade is:", myLetterGrade)
