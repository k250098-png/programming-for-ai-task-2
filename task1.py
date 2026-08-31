
students_data = {
    "Ali": [85, 90, 88],
    "Sara": [92, 95, 90],
    "Zain": [70, 75, 80],
    "Usman": [60, 65, 70]
}


student_averages = {}
for name, marks in students_data.items():
    student_averages[name] = sum(marks) / len(marks)


print("--- Student Averages ---")
for name, avg in student_averages.items():
    print(f"{name}: {avg:.2f}")


highest_student = max(student_averages, key=student_averages.get)
print(f"\nHighest-performing student: {highest_student} ({student_averages[highest_student]:.2f})")


threshold = 80.0
above_threshold = [name for name, avg in student_averages.items() if avg > threshold]

print(f"Students with average above {threshold}: {above_threshold}")
