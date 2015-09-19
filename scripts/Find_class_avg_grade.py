

#Find avergae grade of a class
#based on - 
#1. Grade of students
#2. students grade are based on the weighted average of 	quizzes,tests and homework.



lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def sum(num):
    total=0
    for item in num:        
        total=item+total    
    return total
    
def average(num):
    return float(sum(num))/len(num)
    
def get_average(student):
    homework = average(student['homework'])
    tests = average(student['tests'])
    quizzes= average(student['quizzes'])
    return homework*0.1+tests*0.6+quizzes*0.3
    
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif  score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else :
        return "F"
    
get_letter_grade(get_average(lloyd))

def get_class_average(students):
    results=[]
    for student in students:
        results.append(get_average(student))
    return average(results)
        
students=[lloyd,alice,tyler]    
print get_class_average(students)
print get_letter_grade(get_class_average(students))