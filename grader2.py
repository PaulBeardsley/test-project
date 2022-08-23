def scoreToGrade(score, aGrade = 80, bGrade = 65, cGrade = 50):
    """
    This function converts percentage score into grades: A, B, C or F
    
    Required input: Percentage score; must be a number
    Optional inputs: threshold percentage for each grade if not default; must be numbers
    
    Returns grade as a char"""
    if(score >= aGrade):
        grade = "A"
    elif(score >= bGrade):
        grade = "B"
    elif(score >= cGrade):
        grade = "C"
    else:
        grade = "F"
    return grade
