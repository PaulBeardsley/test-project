from grader1 import *

score = int(input("Please enter History score "))
historyGrade = scoreToGrade(score)

score = int(input("Please enter Geography score "))
geographyGrade = scoreToGrade(score)

print()
print("History grade:", historyGrade)
print("Geography grade:", geographyGrade)

help(scoreToGrade)