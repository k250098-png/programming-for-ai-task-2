
course_a = {"S101", "S102", "S103", "S104", "S105"}
course_b = {"S103", "S104", "S106", "S107"}

both_courses = course_a.intersection(course_b)

only_a = course_a.difference(course_b)


only_b = course_b.difference(course_a)


all_students = course_a.union(course_b)

print("--- Enrollment Analysis ---")
print("Enrolled in both courses:", both_courses)
print("Enrolled only in Course A:", only_a)
print("Enrolled only in Course B:", only_b)
print("All unique students:", all_students)
