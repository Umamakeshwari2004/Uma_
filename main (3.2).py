def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x['CGPA'], reverse=True)
    return sorted_students

# Example usage:
students = [
    {'name': 'Alice', 'roll_number': 'A001', 'CGPA': 3.9},
    {'name': 'Bob', 'roll_number': 'B002', 'CGPA': 3.7},
    {'name': 'Charlie', 'roll_number': 'C003', 'CGPA': 3.8}
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, CGPA: {student['CGPA']}")