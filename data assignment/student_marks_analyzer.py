student_marks = [78, 85, 90, 65, 88, 92, 80]

print("---Student Assignment Report---")

print(f"Full Marks List: {student_marks}")
print(f"First Three Marks: {student_marks[:3]}")
print(f"Last Three Marks: {student_marks [-3:]}")

print("-" * 35)

higest_marks = max(student_marks)
lowest_marks = min(student_marks)
total_sum = sum(student_marks)
number_of_students = len(student_marks)
average_marks = total_sum / number_of_students

print(f"Higest Mark: {higest_marks}")
print(f"Lowest Mark: {lowest_marks}")
print(f"Average Mark: {average_marks}")

print("-" * 35)