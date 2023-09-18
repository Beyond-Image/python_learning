student_grades = {'harry': 81, 'Ron': 78,  'hermione': 99, 'draco': 74, "nevile": 62}

grades = {}

for student in student_grades:
    score = student_grades[student]
    if score > 90:
        grades[student] = "Outstanding"

    elif score > 80:
        grades[student] = "Exceeds Expectations"
    
    elif score > 70:
        grades[student] = "Acceptable"
    
    else:
        grades[student] = "Fail"

for student in grades:
    print (f'{student}: {grades[student]}')

    
