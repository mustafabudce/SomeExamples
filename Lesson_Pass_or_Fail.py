print("""
condition 1) %30 midterm_exam + % 70 final_exam = 50
condition 2) final_exam >= 50 
Note:Both conditions must be successful in order to pass the lesson.
""")

final_exam_score = int(input("Enter the final_exam_score:"))
midterm_exam_score = int(input("Enter the midterm_exam_score:"))
if final_exam_score >= 50:
    average = ((midterm_exam_score * 0.30) + (final_exam_score * 0.70))
    if average >= 50:
        print("You passed.")
    else:
        print("You did not pass!")
else:
    print("You did not pass!")






