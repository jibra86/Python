####
##Checking the Grade of the Students using if and elif
####
score = input("Enter the score of the student: ")
fscore = float(score)

def stuScore(x):
    if x > 1.0:
        return "Error"
    elif x >= 0.9:
        return "A"
    elif x >= 0.8:  
        return "B"
    elif x >= 0.7:  
        return "C"
    elif x <= 0.6:  
        return "F"
    elif x < 0.0:
        return "Error"

xp = stuScore(fscore)
if xp == "Error":
    print(xp)
else:
    print("Grade of Student is", xp)
