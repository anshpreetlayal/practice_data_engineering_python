students = {
    1: {
        'id': 1,
        'name': 'riya',
        'age': 20,
        'school_name': 'XYZ School',
        'completed_courses': {
            'Math': 90,
            'Science': 88,
            'History': 75,
        },
        'ongoing_courses': {
            'English': 'In Progress',
            'Art': 'In Progress',
        }
    },
     2: {
        'id': 2,
        'name': ' john',
        'age': 21,
        'school_name': 'ABC School',
        'completed_courses': {
            'Math': 85,
            'Science': 92,
            'History': 78,
        },
        'ongoing_courses': {
            'English': 'In Progress',
            'Gym': 'In Progress',
        }
    },
    3: {
        'id': 3,
        'name': ' miko',
        'age': 23,
        'school_name': 'ABC School',
        'completed_courses': {
            'Math': 65,
            'Science': 56,
            'History': 78,
        },
        'ongoing_courses': {
            'English': 'In Progress',
            'Art': 'In Progress',
        }
    },
    4: {
        'id': 4,
        'name': ' mia',
        'age': 20,
        'school_name': 'ABC School',
        'completed_courses': {
            'Math': 90,
            'Science': 92,
            'History': 77,
            'English' : 89,
        },
        'ongoing_courses': {
            'Gym': 'In Progress',
        }
    },
}
def view_all_students():
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"School Name: {student_info['school_name']}")
        print()
        
def view_student_info(student_id):
    student_info = students.get(student_id)
    if student_info:
        print(f"Student ID: {student_info['id']}")
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"School Name: {student_info['school_name']}")
        print()
    else:
        print("Student not found.")

def view_ongoing_grades(student_id):
    student_info = students.get(student_id)
    if student_info:
        print(f"Ongoing Grades for {student_info['name']}:")
        for course, status in student_info['ongoing_courses'].items():
            print(f"{course}: {status}")
    else:
        print("Student not found.")
        
def view_completed_grades(student_id):
    student_info = students.get(student_id)
    if student_info:
        print(f"Completed Grades for {student_info['name']}:")
        for course, grade in student_info['completed_courses'].items():
            print(f"{course}: {grade}")
    else:
        print("Student not found.")
        
def view_average_completed_grades(student_id):
    student_info = students.get(student_id)
    if student_info:
        completed_grades = list(student_info['completed_courses'].values())
        if completed_grades:
            average = sum(completed_grades) / len(completed_grades)
            print(f"Average Completed Grades for {student_info['name']}: {average}")
        else:
            print("No completed grades available.")
    else:
        print("Student not found.")

def view_specific_grade(student_id, course_name):
    student_info = students.get(student_id)
    if student_info:
        completed_courses = student_info['completed_courses']
        if course_name in completed_courses:
            print(f"{student_info['name']}'s grade in {course_name}: {completed_courses[course_name]}")
        else:
            print(f"{course_name} not found in completed courses.")
    else:
        print("Student not found.")
