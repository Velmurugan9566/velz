n = int(input("Enter the number of students: "))

# Create a list to store student information
student_info = []

# Input student names and grades
for _ in range(n):
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    student_info.append([name, score])

# Sort the student_info list based on scores
student_info.sort(key=lambda x: (x[1], x[0]))

# Find the second lowest score
second_lowest_score = None
for i in range(1, n):
    if student_info[i][1] > student_info[i - 1][1]:
        second_lowest_score = student_info[i][1]
        break

# Print names with the second lowest score
second_lowest_names = [name for name, score in student_info if score == second_lowest_score]
second_lowest_names.sort()  # Sort names alphabetically
for name in second_lowest_names:
    print(name)
