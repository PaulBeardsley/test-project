def scoreToGrade(score, aGrade = 80, bGrade = 65, cGrade = 50):
    if(score >= aGrade):
        grade = "A"
    elif(score >= bGrade):
        grade = "B"
    elif(score >= cGrade):
        grade = "C"
    else:
        grade = "F"
    return grade
